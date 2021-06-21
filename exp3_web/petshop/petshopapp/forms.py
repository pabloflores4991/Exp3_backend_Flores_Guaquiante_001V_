from django import forms 
from django.forms import ModelForm, widgets
from .models import Mascota, TipoMascota
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget



class MascotaForm(ModelForm): 

    class Meta: 
        model = Mascota 
        fields = ['nombreMascota', 'nombreDueño', 'raza', 'sexo', 'edad', 'TipoMascota','imagen' ]


        labels={
            'nombreMascota': 'Nombre Mascota',
            'nombreDueño': 'Nombre Dueño', 
            'morazadelo': 'raza o especie', 
            'sexo': 'Sexo Mascota',
            'edad': 'edad Mascota',
            'TipoMascota': 'Seleccione tipo de mascota',
            
        }


        widgets={

            'nombreMascota': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'nombreMascota', 
                    'id': 'nombreMascota',
                
                }
            ),
            'nombreDueño': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'nombreDueño', 
                    'id': 'nombreDueño'
                }
            ),
            'raza': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'raza', 
                    'id': 'raza'
                }
            ), 
            'sexo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'sexo', 
                    'id': 'sexo'
                }
            ), 
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'edad', 
                    'id': 'edad'
                }
            ), 

            'TipoMascota': forms.Select(
                attrs={
                    'class': 'form-control', 
                    'id':'TipoMascota'
                }
            ),
        }


