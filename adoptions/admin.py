# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Pet

from django.contrib import admin
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display=['name','species','breed', 'age', 'sex']
