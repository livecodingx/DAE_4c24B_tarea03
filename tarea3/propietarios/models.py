from django.db import models

# Create your models here.
class Propietario(models.Model):
    nombre_completo = models.CharField(max_length=50)
    numero_apartamento = models.CharField(max_length=3)
    numero_telefono = models.CharField(max_length=9)
    email = models.EmailField(unique=True)