from django.urls import path
from .views import index, contactanos, quienessomos, signin, parejas

urlpatterns=  [
    path('', index,name="index"),
    path('contactanos', contactanos, name="contactanos"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('signin', signin, name="signin"),
    path('index', index, name="index"),
    path('parejas', parejas, name="parejas"),
    
]
