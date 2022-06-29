from django.urls import path, include
from .views import home,listar,agregar,modificar,eliminar \
    ,carrusel_perros,perros_rescatados,perro_zeus,perro_pelusa,perro_duque \
    ,web_service,login,login_registro,contacto

urlpatterns = [
    path('', home, name="home"),
    
    path('listar/', listar, name="listar"),
    path('agregar/', agregar, name="agregar"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    
    #path('carrusel-perros/', carrusel_perros, name="carrusel_perros"),
    path('perros-rescatados/', perros_rescatados, name="perros_rescatados"),
    path('perro-zeus/', perro_zeus, name="perro_zeus"),
    path('perro-pelusa/', perro_pelusa, name="perro_pelusa"),
    path('perro-duque/', perro_duque, name="perro_duque"),
    path('web-service/', web_service, name="web_service"),
    #path('login-registro/', login_registro, name="login_registro"),
    path('contacto/', contacto, name="contacto"),
]
