from django.shortcuts import render
from .models import  Vehiculo

# Create your views here.

def index(request):
    return render(request, 'index.html' )


def contactanos(request):
    return render(request, 'contactanos.html')

def quienessomos(request):
    return render(request, 'quienessomos.html')

def signin(request):
    return render(request, 'signin.html')

def parejas(request):
    
    vehiculos = Vehiculo.objects.all()
    return render(request, 'parejas.html', context={'datos': vehiculos})


