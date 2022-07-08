from django.db import models

class Clientes(models.Model):

    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    trabajo= models.CharField(max_length=50)
    nacimiento=models.DateField(max_length=30)
    dni= models.IntegerField()