# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Place

def index(request):
    places:list = list(Place.objects.all().order_by("name"))
    template = loader.get_template("visualizer/index.html")

    context = {
        "places": places
    }

    return HttpResponse(template.render(context, request))
