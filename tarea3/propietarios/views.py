from django.shortcuts import render,redirect
from .models import Propietario

# Create your views here.

#vista para la lista de propietarios

def index(request):
    propietarios = Propietario.objects.all()
    return render(request, 'propietarios/index.html', {'propietarios': propietarios})

def registrar_propietario(request):
    errors = []
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre_completo')
        numero_apartamento = request.POST.get('numero_apartamento')
        numero_telefono = request.POST.get('numero_telefono')
        email = request.POST.get('email')

        # Validaciones
        if not nombre_completo:
            errors.append('nombre no valido.')
        if not numero_apartamento:
            errors.append('numero de apartamento no valido.')
        if len(numero_telefono) != 9 or not numero_telefono.isdigit():
            errors.append('numero de telefono de 9 digitos.')
        if Propietario.objects.filter(email=email).exists():
            errors.append('Ya existe el correo electronico.')
        if not errors:
            # Se crea un nuevo propietario
            Propietario.objects.create(
                nombre_completo=nombre_completo,
                numero_apartamento=numero_apartamento,
                numero_telefono=numero_telefono,
                email=email
            )
            return redirect('propietarios:index')
        

    return render(request, 'propietarios/registro.html', {'errors': errors})