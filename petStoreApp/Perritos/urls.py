from django.urls import path, include
from .views import PerritoCreate, PerritoList, PerritoUpdate, PerritoDelete, \
    perrito_collection, perrito_element, carrusel_perros
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('carrusel-perros/', carrusel_perros, name="carrusel_perros"),
    
    path('add_perrito', PerritoCreate.as_view(), name="add_perrito"),
    path('list_perritos/', PerritoList.as_view(), name='list_perritos'),
    path('edit_perrito/<int:pk>', PerritoUpdate.as_view(), name='edit_perrito'),
    path('del_perrito/<int:pk>', PerritoDelete.as_view(), name='del_perrito'),
    #path('api/', API_objects.as_view()),
    #path('api/<int:pk>/', API_objects_details.as_view()),
    path('perritos/',  perrito_collection , name='perrito_collection'),
    path('perritos/<int:pk>/', perrito_element ,name='perrito_element'),
]

urlpatterns = format_suffix_patterns(urlpatterns)