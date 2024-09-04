from django.shortcuts import render, redirect
from .models import Registro
from vehiculos.models import Vehiculo
from django.utils import timezone
from django.db.models import Q

def index(request):
    registros_entrada = Registro.objects.filter(fecha_hora_salida__isnull=False)
    registros_salida = Registro.objects.filter(fecha_hora_salida__isnull=True)
    return render(request, 'registros/index.html', {
        'registros_entrada': registros_entrada,
        'registros_salida': registros_salida
    })

def registrar_entrada(request):
    # conseguir los vehiculos que no tienen el registro y los que tienen fecha de salida
    vehiculos_entrantes = Vehiculo.objects.filter(
        Q(registro__isnull=True) | ~Q(registro__fecha_hora_salida__isnull=True)
    ).distinct()

    if request.method == 'POST':
        vehiculo_id = request.POST['vehiculo']
        vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        
        # se crea el nuevo registro
        Registro.objects.create(vehiculo=vehiculo)
        
        return redirect('registros:index')

    return render(request, 'registros/registrar_entrada.html', {'vehiculos': vehiculos_entrantes})

def registrar_salida(request):
    # conseguir los registros sin fecha de salida y que tengan registros
    vehiculos_salida = Vehiculo.objects.filter(
        Q(registro__fecha_hora_salida__isnull=True) &
        ~Q(registro__isnull=True)
    ).distinct()

    if request.method == 'POST':
        matricula = request.POST['matricula']
        
        # buscar la matricula del vehiculo
        vehiculo = Vehiculo.objects.filter(matricula=matricula).first()
        
        # encontrar registro donde falta fecha de salida
        registro = Registro.objects.filter(vehiculo=vehiculo, fecha_hora_salida__isnull=True).first()
        
        # actualizar la hora de salida
        registro.fecha_hora_salida = timezone.now()
        registro.save()
        
        return redirect('registros:index')

    return render(request, 'registros/registrar_salida.html', {'vehiculos': vehiculos_salida})
