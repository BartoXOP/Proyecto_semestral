from django.db import models
from django.utils import timezone
from distutils.command.upload import upload

# Create your models here.

class RazaGato(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Gatito(models.Model):
    nombre              = models.CharField(max_length=50)
    raza                = models.ForeignKey(RazaGato, on_delete=models.PROTECT)
    edad                = models.IntegerField(default=1)
    descripcion         = models.TextField()
    imagen              = models.ImageField(upload_to="", null=True)
    fecha_publicacion   = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre