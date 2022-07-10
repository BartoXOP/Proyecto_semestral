from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from distutils.command.upload import upload

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Tipo_producto(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre              = models.CharField(max_length=50)
    marca               = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipo_producto       = models.ForeignKey(Tipo_producto, on_delete=models.PROTECT)
    precio              = models.IntegerField(default=0)
    descripcion         = models.TextField()
    imagen              = models.ImageField(upload_to="", null=True)
    stock               = models.IntegerField(default=1)
    disponible          = models.BooleanField(default=True)
    fecha_publicacion   = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre
