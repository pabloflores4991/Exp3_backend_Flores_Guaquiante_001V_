from django.contrib import admin
from .models import TipoMascota, Mascota, Producto

# Register your models here.
admin.site.register(TipoMascota)
admin.site.register(Mascota)
admin.site.register(Producto)
