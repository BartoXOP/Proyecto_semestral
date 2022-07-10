from django.contrib import admin
from .models import Perrito, Raza

# Register your models here.
class PerritoAdmin(admin.ModelAdmin):
    list_display = ["nombre","edad","raza"]
    list_editable = ["raza","edad"]
    search_fields = ["nombre"]
    list_filter = ["raza", "edad"]
    list_per_page = 12

class RazaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    list_per_page = 12


admin.site.register(Perrito, PerritoAdmin)
admin.site.register(Raza, RazaAdmin)