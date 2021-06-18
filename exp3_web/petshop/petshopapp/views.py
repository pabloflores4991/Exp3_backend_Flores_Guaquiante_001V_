from django.shortcuts import redirect, render
from .models import  TipoMascota, Mascota
from .forms import MascotaForm
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
    
    vehiculos = Mascota.objects.all()
    return render(request, 'parejas.html', context={'datos': vehiculos})


def crearVehiculo(request):
    if request.method=='POST':
        Mascota=MascotaForm(request.POST)
        if Mascota.is_valid():
            Mascota.save() #metodo que crea un neuvo objeto y reemplaza al insert
            return redirect('parejas')

    else:
        Mascota=MascotaForm()
    return render(request,'petshopapp/form_crearvehiculo.html',{'Mascota':Mascota})


def Ver(request):
    mascotas = Mascota.objects.all()
    return render(request,'petshopapp/ver.html', context={'mascotas':mascotas})


def form_mod_mascota(request,id):
    mascota = Mascota.objects.get(nombreMascota=id)

    datos ={
        'form': MascotaForm(instance=mascota)
    }
    if request.method == 'POST': 
        formulario = MascotaForm(data=request.POST, instance = mascota)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('ver')
    return render(request, 'petshopapp/form_mod_mascota.html', datos)


def form_del_Mascota(request,id):
    mascota = Mascota.objects.get(nombreMascota=id)
    mascota.delete()
    return redirect('ver')