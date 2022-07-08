from django.urls import path
from .views import *

urlpatterns = [
    path('template/', template),
    path('comprador/', Cliente),
    path('comprador2/', Cliente2),
    path('', Inicio),
    path('clientes/', clientes),
    path('cajeros/', cajeros),
]