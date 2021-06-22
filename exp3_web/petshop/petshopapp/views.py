from django.shortcuts import redirect, render
from .models import  TipoMascota, Mascota, Producto
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


def index2(request):
    productos = Producto.objects.all()
    return render(request,'index2.html', context={'productos':productos})

def parejas(request):
    
    mascotas = Mascota.objects.all()
    return render(request, 'parejas.html', context={'datos': mascotas})

def Ver(request):
    mascotas = Mascota.objects.all()
    return render(request,'petshopapp/ver.html', context={'mascotas':mascotas})

def crearMascota(request):
    data={
        'form': MascotaForm()
    }
    if request.method=='POST':
        Mascota=MascotaForm(request.POST, files=request.FILES)
        if Mascota.is_valid():
            Mascota.save()
            return redirect('parejas')

    else:
        Mascota=MascotaForm()
    return render(request,'petshopapp/form_crearmascota.html',{'Mascota':Mascota})



def form_mod_mascota(request,id):
    mascota = Mascota.objects.get(nombreMascota=id )
    datos ={
        'form': MascotaForm(instance=mascota)
    }
    if request.method == 'POST': 
        formulario = MascotaForm(data=request.POST, instance = mascota,files=request.FILES )
        if formulario.is_valid: 
            formulario.save()  
            datos['mensaje'] = "modificado correctamente"
        datos['form'] = MascotaForm          #permite actualizar la info del objeto encontrado
    mascota = Mascota.objects.get(nombreMascota=id )
    datos ={
        'form': MascotaForm(instance=mascota)
    }
    return render(request, 'petshopapp/form_mod_mascota.html', datos)
    


def form_del_Mascota(request,id):
    mascota = Mascota.objects.get(nombreMascota=id)
    mascota.delete()
    return redirect('ver')