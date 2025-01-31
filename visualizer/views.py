# from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from .models import Estimate, Place, ThirdPartyInformation, ImageInformation, VideoInformation, UserProfile

import json
from itertools import chain

def index(request):
    template = loader.get_template("visualizer/heatmap.html")

    places = Place.objects.all()

    # Gerar os pontos de calor a partir das estimativas
    heatmap_data = []
    for place in places:
        latest_estimate = place.estimates.order_by('-datetime').first()  # Pegando a estimativa mais recente

        if latest_estimate:  # 🔹 Verifica se existe pelo menos uma estimativa
            heatmap_data.append({
                "lat": place.latitude,
                "lng": place.longitude,
                "weight": latest_estimate.amount  # Usa a quantidade de pessoas como peso do mapa de calor
            })

    # Criar lista de atividade com status e tendência
    activity_data = []
    for place in places:
        estimates = place.estimates.order_by('datetime')
        
        if estimates.exists():  # 🔹 Garante que o local tem estimativas
            current_estimate = estimates.first()
            future_estimate = estimates.filter(datetime__gt=current_estimate.datetime).first()

            trend_icon = "ti ti-line-dashed"
            if future_estimate:
                if future_estimate.amount > current_estimate.amount:
                    trend_icon = "ti ti-trending-up"
                elif future_estimate.amount < current_estimate.amount:
                    trend_icon = "ti ti-trending-down"

            activity_data.append({
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
        saved_places = user_profile.saved_places.all()

    context = {
        "heatmap_data": json.dumps(heatmap_data),
        "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
        "activity_data": activity_data,
        "notifications": notifications,
        "saved_places": saved_places,
        "user_authenticated": request.user.is_authenticated
    }

    return HttpResponse(template.render(context, request))
