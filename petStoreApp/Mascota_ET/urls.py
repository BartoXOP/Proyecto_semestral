from django.urls import path, include
from .views import GatitoCreate, GatitoList, GatitoUpdate, GatitoDelete, carrusel_gatitos, \
    gatito_collection, gatito_element
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
        path('carrusel-gatos/', carrusel_gatitos, name="carrusel_gatos"),
    
    path('add_gatito', GatitoCreate.as_view(), name="add_gatito"),
    path('list_gatitos/', GatitoList.as_view(), name='list_gatitos'),
    path('edit_gatito/<int:pk>', GatitoUpdate.as_view(), name='edit_gatito'),
    path('del_gatito/<int:pk>', GatitoDelete.as_view(), name='del_gatito'),
    #path('api/', API_objects.as_view()),
    #path('api/<int:pk>/', API_objects_details.as_view()),
    path('gatitos/',  gatito_collection , name='gatito_collection'),
    path('gatitos/<int:pk>/', gatito_element ,name='gatito_element'),
]

urlpatterns = format_suffix_patterns(urlpatterns)