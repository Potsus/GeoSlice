# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.shortcuts import render
from django.http import HttpResponse

from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class map_view(TemplateView):
    template_name = 'map.html'

    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger

    def get(self, request, *args, **kwargs):
        from .models import Location
        import random

        locations = list(Location.objects.all())
        #loc = random.choice(locations)
        #lat = (loc.north + loc.south)/2,
        #lon = (loc.east + loc.west)/2,
        lat = 0
        lon = 0
        zoom = 2

        context = {
            'gmaps_key': "AIzaSyCJSs7xAR0pNk_-XUQ9f30Oord-q2950Jc",
            'zoom': zoom,
            'maptype': 'terrain',
            'location_list': locations,
            'latitude': lat,
            'longitude': lon
        }

        return TemplateResponse(
                request,
                self.template_name,
                context
            ) 