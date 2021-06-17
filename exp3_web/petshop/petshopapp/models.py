from django.db import models

# Create your models here.
class TipoMascota(models.Model):
    idTipoMascota = models.IntegerField(primary_key=True, verbose_name='Id de TipoMascota')
    nombreTipoMascota = models.CharField(max_length=50, verbose_name='Nombre TipoMascota')

    def __str__(self):
        return self.nombreTipoMascota


class Mascota(models.Model):
    nombreMascota= models.CharField(max_length=20, primary_key=True, verbose_name='nombre Mascota')
    nombreDueño= models.CharField(max_length=20, verbose_name='nombre Dueño')
    raza = models.CharField(max_length=20, verbose_name='raza')
    sexo = models.CharField(max_length=10, verbose_name='sexo')
    edad = models.IntegerField( verbose_name='edad')
    TipoMascota = models.ForeignKey(TipoMascota, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMascota


