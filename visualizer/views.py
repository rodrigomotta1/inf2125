
import json
from itertools import chain

from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

from .models import Place, ThirdPartyInformation, ImageInformation, VideoInformation, UserProfile

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


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
