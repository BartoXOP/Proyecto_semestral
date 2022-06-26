from django.urls import path, include
from .views import PerritoCreate, PerritoList, PerritoUpdate, PerritoDelete

urlpatterns = [
    path('add_perrito', PerritoCreate.as_view(), name="add_perrito"),
    path('list_perritos/', PerritoList.as_view(), name='list_perritos'),
    path('edit_perrito/<int:pk>', PerritoUpdate.as_view(), name='edit_perrito'),
    path('del_perrito/<int:pk>', PerritoDelete.as_view(), name='del_perrito'),
]
