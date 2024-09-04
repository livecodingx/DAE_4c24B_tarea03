from django.shortcuts import render, redirect
from .models import Vehiculo
from propietarios.models import Propietario
# Create your views here.

# index de vehiculos

def index(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/index.html', {'vehiculos': vehiculos})

# Rgistrar nuevos vehiculos

def registrar_vehiculo(request):
    if request.method == 'POST':
        matricula = request.POST['matricula']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        color = request.POST['color']
        propietario_id = request.POST['propietario']
        errors = []
        
        # verificar errores posibles
        if Vehiculo.objects.filter(matricula=matricula).exists():
            errors.append = ["El vehículo con esta matrícula ya está registrado."]
        if len(matricula) != 7:
            errors.append("La matricula no es valida.")
        if errors:
            propietarios = Propietario.objects.all()
            return render(request, 'vehiculos/registrar.html', {'errors': errors, 'propietarios': propietarios})
        
        propietario = Propietario.objects.get(id=propietario_id)
        
        Vehiculo.objects.create(
            matricula=matricula,
            marca=marca,
            modelo=modelo,
            color=color,
            propietario=propietario
        )
        
        return redirect('vehiculos:index')

    propietarios = Propietario.objects.all()
    return render(request, 'vehiculos/registrar.html', {'propietarios': propietarios})


