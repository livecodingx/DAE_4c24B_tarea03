from django.db import models
from propietarios.models import Propietario

# Create your models here.
class Vehiculo(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=7, unique=True)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)