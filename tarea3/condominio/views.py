from django.shortcuts import render
# Create your views here.


# vista principal

def index(request):
    return render(request, 'condominio/index.html')

