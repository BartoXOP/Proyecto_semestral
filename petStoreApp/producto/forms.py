from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Producto
from crispy_forms.helper import FormHelper
from django.conf import settings

class ProductoForm(forms.ModelForm):
    fecha_publicacion = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'])
    class Meta:
        model = Producto
        fields = '__all__'