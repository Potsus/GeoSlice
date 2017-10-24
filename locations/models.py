# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Location(Base):
    name  = models.CharField(max_length=200)
    north = DecimalField(max_digits=9, decimal_places=6)
    south = DecimalField(max_digits=9, decimal_places=6)
    east  = DecimalField(max_digits=9, decimal_places=6)
    west  = DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name