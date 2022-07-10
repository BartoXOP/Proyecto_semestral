from django.contrib import admin
from .models import Gatito, RazaGato

# Register your models here.
class GatitoAdmin(admin.ModelAdmin):
    list_display = ["nombre","edad","raza"]
    list_editable = ["raza","edad"]
    search_fields = ["nombre"]
    list_filter = ["raza", "edad"]
    list_per_page = 12

class RazaGatoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    list_per_page = 12


admin.site.register(Gatito, GatitoAdmin)
admin.site.register(RazaGato, RazaGatoAdmin)