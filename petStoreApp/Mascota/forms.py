from dataclasses import fields
from django import forms
from .models import Perrito

# Create your forms here.

class PerritoForm(forms.ModelForm):
    fecha_publicacion = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'])
    class Meta:
        model = Perrito
        fields = '__all__'