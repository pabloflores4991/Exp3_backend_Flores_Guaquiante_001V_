from django.urls import path
from .views import index, contactanos, quienessomos, signin, parejas, crearMascota, Ver, form_mod_mascota,form_del_Mascota,index2

urlpatterns=  [
    path('', index,name="index"),
    path('contactanos', contactanos, name="contactanos"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('signin', signin, name="signin"),
    path('index', index, name="index"),
    path('parejas', parejas, name="parejas"),
    path('crearMascota',crearMascota, name="crearMascota"),
    path('ver',Ver, name="ver"),
    path('form_mod_mascota/<id>',form_mod_mascota, name="form_mod_mascota"),
    path('form_del_Mascota/<id>', form_del_Mascota, name="form_del_Mascota"),
    path('index2', index2, name="index2")
]
