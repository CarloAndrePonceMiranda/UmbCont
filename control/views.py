# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Playera
from .forms import UmbrellaForm
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.template.response import TemplateResponse
import os
from io import BytesIO
from django.db.models import Q, Sum
import time

def Umbrella(request):
    if request.method == 'POST':
        form = UmbrellaForm(request.POST, request.FILES)
        if form.is_valid():
            umbrella = form.save()
            umbrella.save()
            return HttpResponseRedirect('/List/Umbrellas/')
    else:
        form = UmbrellaForm()
    template = loader.get_template('umbrellas/new_umbrella.html')
    context = {
        'form': form
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/login')

def UmbrellaList(request):
    	playera = Playera.objects.order_by('name')
        template = loader.get_template('umbrellas/umbrellas_list.html')
        context = {
        'playera':playera
        }
        if request.user.is_authenticated():
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect('/login')

def UmbrellaDetail(request,pk):
	playera = get_object_or_404(Playera, pk=pk)
	template = loader.get_template('umbrellas/umbrella_detail.html')
	context = {
	'playera': playera
	}
	if request.user.is_authenticated():
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect('/login')

class UmbrellaCreation(CreateView):
    model = Playera
    success_url = reverse_lazy('umbrellas:umbrellalist')
    fields = ['id', 'name', 'ip', 'state']
class UmbrellaUpdate(UpdateView):
    model = Playera
    success_url = reverse_lazy('umbrellas:umbrellalist')
    fields = ['id', 'name', 'ip', 'state']
class UmbrellaDelete(DeleteView):
    model = Playera
    success_url = reverse_lazy('umbrellas:umbrellalist')
    fields = ['id', 'name', 'ip', 'state']

def Control(request):
    control = Playera.objects.order_by('name')
    template = loader.get_template('control.html')
    #print control
    context = {
    'control' : control,
        }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/login')


def SU(request):
    control = Playera.objects.order_by('name')
    template = loader.get_template('smartumbrellas.html')
    #print control
    context = {
    'control' : control,
        }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/login')
