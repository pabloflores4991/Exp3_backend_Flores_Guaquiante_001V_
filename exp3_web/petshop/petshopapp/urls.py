from django.urls import path
from .views import index, contactanos, quienessomos, signin

urlpatterns=  [
    path('', index,name="index"),
    path('contactanos.html', contactanos, name="contactanos"),
    path('quienessomos.html', quienessomos, name="quienessomos"),
    path('signin.html', signin, name="signin"),
    path('index.html', index, name="index"),
]
