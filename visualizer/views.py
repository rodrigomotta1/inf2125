import json
from itertools import chain

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect

from .models import Place, ThirdPartyInformation, ImageInformation, VideoInformation, UserProfile, Estimate
from .forms import UserSettingsForm, InformationUploadForm
from movrio.utils import DatabaseQueryManager

query_manager = DatabaseQueryManager()

def index(request):
    form = InformationUploadForm()

    places = Place.objects.all().order_by("name")

    # Gerar os pontos de calor a partir das estimativas
    heatmap_data = []
    for place in places:
        latest_estimate = place.estimates.order_by('-datetime').first()  # type: ignore # Pegando a estimativa mais recente

        if latest_estimate:  # 🔹 Verifica se existe pelo menos uma estimativa
            heatmap_data.append({
                "lat": place.latitude,
                "lng": place.longitude,
                "weight": latest_estimate.amount  # Usa a quantidade de pessoas como peso do mapa de calor
            })

    # Criar lista de atividade com status e tendência
    activity_data = []
    for place in places:
        estimates = place.estimates.order_by('datetime') # type: ignore

        activity_data.append({
            "id": place.pk,
            "name": place.name,
            "status": place.status,
            "trend_icon": place.get_trend_icon(),
        })

    # Obter notificações gerais sobre o Rio
    notifications = list(chain(
        ThirdPartyInformation.objects.order_by('-created_at')[:5],
        ImageInformation.objects.order_by('-created_at')[:5],
        VideoInformation.objects.order_by('-created_at')[:5]
    ))

    # Obter locais salvos se o usuário estiver logado
    saved_places = []
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        saved_places = [place.pk for place in user_profile.saved_places.all()]  # type: ignore

    context = {
        "form": form,
        "heatmap_data": json.dumps(heatmap_data),
        "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
        "activity_data": activity_data,
        "notifications": notifications,
        "saved_places": saved_places,
        "user_authenticated": request.user.is_authenticated
    }

    return render(request, "visualizer/heatmap.html", context)

class CustomLoginView(LoginView):
    """
    Sobrescreve o LoginView para exibir erros na index.html e abrir automaticamente o modal de login em caso de erro.
    """
    template_name = "visualizer/heatmap.html"

    def form_invalid(self, form):
        """
        Se o login falhar, renderiza index.html passando os erros do formulário.
        """
        return render(self.request, self.template_name, {
            "form": form,
            "show_login_modal": True  # 🔹 Adiciona um flag para abrir o modal
        })

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

@login_required
def update_user_settings(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserSettingsForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        return JsonResponse({"success": False, "errors": form.errors}, status=400)
    
    return JsonResponse({"success": False}, status=400)

@login_required
def toggle_saved_place(request):
    """
    Adiciona ou remove um local salvo para o usuário logado.
    """
    if request.method == "POST":
        place_id = request.POST.get("place_id")
        place = get_object_or_404(Place, id=place_id)
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

        if place in user_profile.saved_places.all():
            user_profile.saved_places.remove(place)
            return JsonResponse({"success": True, "saved": False})
        else:
            user_profile.saved_places.add(place)
            return JsonResponse({"success": True, "saved": True})

    return JsonResponse({"success": False}, status=400)

def get_place_details(request, place_id):
    """
    Retorna detalhes de um local, incluindo estimativas e informações.
    """
    place = get_object_or_404(Place, id=place_id)

    # Última estimativa
    last_estimate = place.estimates.order_by("-datetime").first()
    current_estimate = last_estimate.amount if last_estimate else 0

    # Histórico de estimativas (últimos 10 registros)
    history = place.estimates.order_by("-datetime")
    history_data = [{"time": e.datetime.strftime("%H:%M"), "amount": e.amount} for e in history][:10]

    # Buscar todas as informações do local usando DatabaseQueryManager
    info_data = query_manager.get_all_info_for_place(place)

    # Verifica se o local está salvo pelo usuário logado
    is_saved = False
    if request.user.is_authenticated:
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        is_saved = place in user_profile.saved_places.all()

    return JsonResponse({
        "name": place.name,
        "trend_icon": place.get_trend_icon(),
        "current_estimate": current_estimate,
        "history": history_data,
        "information": info_data,
        "is_saved": is_saved
    })

@login_required
def upload_information(request):
    """
    Processa o envio do formulário e redireciona para index com um toast de feedback.
    """
    if request.method == "POST":
        form = InformationUploadForm(request.POST, request.FILES)
        if form.is_valid():
            place = form.cleaned_data["place"]  # Pega o local selecionado
            info_type = form.cleaned_data["info_type"]
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]

            if info_type == "third_party":
                ThirdPartyInformation.objects.create(
                    place=place,
                    title=title,
                    description=description,
                    source_name=form.cleaned_data["source_name"],
                    source_url=form.cleaned_data["source_url"],
                )
            elif info_type == "video":
                VideoInformation.objects.create(
                    place=place,
                    title=title,
                    description=description,
                    video_url=form.cleaned_data["video_url"],
                    author=request.user
                )
            elif info_type == "image":
                ImageInformation.objects.create(
                    place=place,
                    title=title,
                    description=description,
                    image=form.cleaned_data["image"],
                    author=request.user
                )

            messages.success(request, "Informação enviada com sucesso!")
        else:
            messages.error(request, "Erro ao enviar a informação. Verifique os campos.")

    return redirect("index")  # Redireciona para index.html após o envio