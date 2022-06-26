from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Perrito, Raza
from .forms import PerritoForm
from datetime import datetime, timedelta
from django.utils import timezone

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

#------------------------------Vistas clases genéricas
class PerritoCreate(CreateView):
    model           = Perrito
    form_class      = PerritoForm
    template_name   = 'Mascotas/perrito_form.html'
    success_url     = reverse_lazy("list_perritos")

class PerritoList(ListView):
    model           = Perrito
    template_name   = 'Mascotas/list_perritos.html'
    # paginate_by = 4

class PerritoUpdate(UpdateView):
    model           = Perrito
    form_class      = PerritoForm
    template_name   = 'Mascotas/perrito_form.html'
    success_url     = reverse_lazy('list_perritos')

class PerritoDelete(DeleteView):
    model           = Perrito
    template_name   = 'Mascotas/perrito_delete.html'
    success_url     = reverse_lazy('list_perritos')