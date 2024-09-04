from django.urls import path, include
from . import views
app_name = 'propietarios'


urlpatterns = [
    path('', views.index, name="index"),
    path('registrar_propietario', views.registrar_propietario, name="registrar_propietario"),
]
