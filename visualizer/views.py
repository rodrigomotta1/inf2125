import json
from itertools import chain

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

from .models import Place, ThirdPartyInformation, ImageInformation, VideoInformation, UserProfile, Estimate
from .forms import UserSettingsForm


def index(request):
    places = Place.objects.all()

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
        
        if estimates.exists():  # 🔹 Garante que o local tem estimativas
            current_estimate = estimates.first()
            future_estimate = estimates.filter(datetime__gt=current_estimate.datetime).first()

            trend_icon = "ti ti-minus"
            if future_estimate:
                if future_estimate.amount > current_estimate.amount:
                    trend_icon = "ti ti-trending-up"
                elif future_estimate.amount < current_estimate.amount:
                    trend_icon = "ti ti-trending-down"

            activity_data.append({
                "id": place.pk,
                "name": place.name,
                "status": place.status,
                "trend_icon": trend_icon
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
        "heatmap_data": json.dumps(heatmap_data),
        "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
        "activity_data": activity_data,
        "notifications": notifications,
        "saved_places": saved_places,
        "user_authenticated": request.user.is_authenticated
    }

    return render(request, "visualizer/heatmap.html", context)


# def get_latest_estimates(request):
#     """
#     Retorna as últimas estimativas para todos os locais
#     Envia ao frontend via AJAX
#     """
#     places = Place.objects.all()

#     data = [
#         {
#             "lat": place.latitude,
#             "lng": place.longitude,
#             "amount": place.estimates.order_by('-datetime').first().amount if place.estimates.exists() else 0 # type: ignore
#         }
#         for place in places
#     ]

#     return JsonResponse(data, safe=False)

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
