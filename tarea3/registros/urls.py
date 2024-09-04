from django.urls import path
from . import views

app_name = 'registros'

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('registrar_salida/', views.registrar_salida, name='registrar_salida'),
]
