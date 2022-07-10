from telnetlib import GA
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Gatito, RazaGato
from .forms import GatitoForm
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework import generics
from .serializers import GatitoSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

#Create your views here.

def carrusel_gatitos(request):
    gatitos = Gatito.objects.all()
    data = {
        'gatitos' : gatitos
    }
    return render(request, 'paginas/carrusel_gatos.html', data)

#------------------------------Vistas clases genéricas
class GatitoCreate(CreateView):
    model           = Gatito
    form_class      = GatitoForm
    template_name   = 'Mascotas/gatito_form.html'
    success_url     = reverse_lazy("list_gatitos")

class GatitoList(ListView):
    model           = Gatito
    template_name   = 'Mascotas/list_gatitos.html'
    # paginate_by = 4

class GatitoUpdate(UpdateView):
    model           = Gatito
    form_class      = GatitoForm
    template_name   = 'Mascotas/gatito_form.html'
    success_url     = reverse_lazy('list_gatitos')

class GatitoDelete(DeleteView):
    model           = Gatito
    template_name   = 'Mascotas/gatito_delete.html'
    success_url     = reverse_lazy('list_gatitos')

#------------------------------Vistas clases API
class API_objects(generics.ListCreateAPIView):
    queryset = Gatito.objects.all()
    serializer_class = GatitoSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gatito.objects.all()
    serializer_class = GatitoSerializer

#todos los perritos
@api_view(['GET', 'POST'])
def gatito_collection(request):
    if request.method == 'GET':
        gatito = Gatito.objects.all()
        serializer = GatitoSerializer(gatito, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GatitoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#un solo perrito
@api_view(['GET', 'PUT', 'DELETE'])
def gatito_element(request, pk):
    gatito = get_object_or_404(Gatito, id=pk)
    #si es pa ver que lo vea
    if request.method == 'GET':
        serializer = GatitoSerializer(gatito)
        return Response(serializer.data)
    #si es pa borra que lo borre
    elif request.method == 'DELETE':
        gatito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #y si es pa meter que lo meta
    elif request.method == 'PUT': 
        gatito_new = JSONParser().parse(request) 
        serializer = GatitoSerializer(gatito, data=gatito_new)
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)