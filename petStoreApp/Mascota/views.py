from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Perrito, Raza
from .forms import PerritoForm
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework import generics
from .serializers import PerritoSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

# Create your views here.

def carrusel_perros(request):
    perritos = Perrito.objects.all()
    data = {
        'perritos' : perritos
    }
    return render(request, 'paginas/carrusel_perros.html', data)

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

#------------------------------Vistas clases API
class API_objects(generics.ListCreateAPIView):
    queryset = Perrito.objects.all()
    serializer_class = PerritoSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perrito.objects.all()
    serializer_class = PerritoSerializer

#todos los perritos
@api_view(['GET', 'POST'])
def perrito_collection(request):
    if request.method == 'GET':
        perritos = Perrito.objects.all()
        serializer = PerritoSerializer(perritos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PerritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#un solo perrito
@api_view(['GET', 'PUT', 'DELETE'])
def perrito_element(request, pk):
    perrito = get_object_or_404(Perrito, id=pk)
    #si es pa ver que lo vea
    if request.method == 'GET':
        serializer = PerritoSerializer(perrito)
        return Response(serializer.data)
    #si es pa borra que lo borre
    elif request.method == 'DELETE':
        perrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #y si es pa meter que lo meta
    elif request.method == 'PUT': 
        perrito_new = JSONParser().parse(request) 
        serializer = PerritoSerializer(perrito, data=perrito_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)