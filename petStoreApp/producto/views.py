from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Producto, Tipo_producto, Marca
from .forms import ProductoForm
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'producto' : productos
    }
    return render(request, 'home.html', data)

#-----------------------------CRUD PRODUCTOS
def listar(request):
    productos = Producto.objects.all()
    data = {
        'producto' : productos
    }
    return render(request, 'crud/listar.html', data)

def agregar(request):
    data = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario
    
    return render(request, 'crud/agregar.html', data)

def modificar(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto),
        'producto' : producto
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar')
        data['form'] = formulario
    
    return render(request, 'crud/modificar.html', data)

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to='listar')

#-----------------------------Mantener de momento, actualizar a futuro
def carrusel_perros(request):
    return render(request, 'paginas/carrusel_perros.html')
def perros_rescatados(request):
    return render(request, 'paginas/perros_rescatados.html')
def perro_zeus(request):
    return render(request, 'paginas/perro_zeus.html')
def perro_pelusa(request):
    return render(request, 'paginas/perro_pelusa.html')
def perro_duque(request):
    return render(request, 'paginas/perro_duque.html')
def web_service(request):
    return render(request, 'paginas/web_service.html')
def login(request):
    return render(request, 'paginas/login.html')
def login_registro(request):
    return render(request, 'paginas/login_registro.html')
def contacto(request):
    return render(request, 'paginas/contacto.html')