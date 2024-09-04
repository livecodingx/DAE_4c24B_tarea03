from django.urls import path
from . import views
app_name = 'vehiculos'

urlpatterns = [
    path('', views.index, name="index"),
    path('registrar/', views.registrar_vehiculo, name='registrar_vehiculo'),
]
