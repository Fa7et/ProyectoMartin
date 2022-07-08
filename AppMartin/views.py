from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from AppMartin.models import Clientes
from django.template import Context, Template

def Cliente(self):
        clientes= Clientes(nombre= "Franco",direccion= "1ro de mayo 458", trabajo= "Planero", nacimiento="2001-07-03", dni= "43552346" )
        clientes.save()
        texto= f"{clientes.nombre} {clientes.direccion} {clientes.trabajo} {clientes.nacimiento} {clientes.dni}"
        return HttpResponse(texto)

def Cliente2(self):
        clientes= Clientes(nombre= "Maria",direccion= "1ro de mayo 458", trabajo= "Comerciante", nacimiento="1974-02-03", dni= "23732658" )
        clientes.save()
        texto= f"{clientes.nombre} {clientes.direccion} {clientes.trabajo} {clientes.nacimiento} {clientes.dni}"
        return HttpResponse(texto)




def template(self):
    mihtml = open("C:/Users/Franco/Desktop/ProyectoMartin/Plantillas/template.html")

    plantilla = Template(mihtml.read())

    mihtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
