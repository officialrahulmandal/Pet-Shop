# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p> Welcome to the Homepage </p>')

def pet_detail(request, id):
    return HttpResponse("<p>showing the details of id {}</p>".format(id))
