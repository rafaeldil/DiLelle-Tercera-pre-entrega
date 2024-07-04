from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Paleta
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Paletas(ListView):
    model = Paleta
    template_name = 'paletas/listado_paletas.html'
    context_object_name = 'paletas'
    
class CrearPaleta(CreateView):
    model = Paleta
    template_name = 'paletas/crear_paleta.html'
    success_url = reverse_lazy('paletas')
    fields = ['marca', 'descripcion', 'fecha']
   
class EditarPaleta(LoginRequiredMixin, UpdateView):
    model = Paleta
    template_name = 'paletas/editar_paleta.html'
    success_url = reverse_lazy('paletas')
    fields = ['marca', 'descripcion', 'fecha']
    
class EliminarPaleta(DeleteView):
    model = Paleta
    template_name = "paletas/eliminar_paleta.html"
    success_url = reverse_lazy('paletas')
    
class VerPaleta(DetailView):
    model = Paleta
    template_name = 'paletas/ver_paleta.html'
