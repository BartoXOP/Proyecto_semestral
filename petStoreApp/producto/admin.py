from django.contrib import admin
from .models import Producto, Tipo_producto, Marca

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","marca","tipo_producto","stock"]
    list_editable = ["precio","stock"]
    search_fields = ["nombre"]
    list_filter = ["marca", "tipo_producto"]
    list_per_page = 12

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    list_per_page = 12

class MarcaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    list_per_page = 12

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Tipo_producto, TipoProductoAdmin)
admin.site.register(Marca, MarcaAdmin)