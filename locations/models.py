# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Location(models.Model):
    name  = models.CharField(max_length=100)
    north = models.DecimalField(max_digits=9, decimal_places=6)
    south = models.DecimalField(max_digits=9, decimal_places=6)
    east  = models.DecimalField(max_digits=9, decimal_places=6)
    west  = models.DecimalField(max_digits=9, decimal_places=6)

    #center as part of the model or computed?
    #latitude  = (north + south)/2 
    #longitude = (east + west)/2

    #zoom level computed or saved?
    #zoom = models.IntegerField(min=0, max=21)

    def __str__(self):
        return self.name