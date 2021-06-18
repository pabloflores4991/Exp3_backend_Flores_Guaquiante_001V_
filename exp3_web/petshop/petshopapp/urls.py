from django.urls import path
from .views import index, contactanos, quienessomos, signin, parejas, crearVehiculo, Ver, form_mod_mascota,form_del_Mascota

urlpatterns=  [
    path('', index,name="index"),
    path('contactanos', contactanos, name="contactanos"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('signin', signin, name="signin"),
    path('index', index, name="index"),
    path('parejas', parejas, name="parejas"),
    path('crearMascota',crearVehiculo, name="crearMascota"),
    path('ver',Ver, name="ver"),
    path('form_mod_mascota/<id>',form_mod_mascota, name="form_mod_mascota"),
    path('form_del_Mascota/<id>', form_del_Mascota, name="form_del_Mascota")
]
