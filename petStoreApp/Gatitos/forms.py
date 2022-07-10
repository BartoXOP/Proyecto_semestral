from dataclasses import fields
from django import forms
from .models import Gatito

# Create your forms here.

class GatitoForm(forms.ModelForm):
    fecha_publicacion = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'])
    class Meta:
        model = Gatito
        fields = '__all__'