from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def lista_personas(request) :
    lista = Persona.objects.all() # Todas las personas
    return render(request, 'apppersona/lista_personas.html',{'lista' : lista})

def lista_tarjetas(request) :
    tarjetas = TarjetaJunaeb.objects.all()
    return render(request, 'apppersona/lista_tarjetas.html',{'listaTarjetas' : tarjetas})

def tarjetas_con_plata(request) :
    tarjetas = TarjetaJunaeb.objects.filter(montoDispobible__gte=1)
    return render(request, 'apppersona/lista_tarjetas.html',{'listaTarjetas' : tarjetas})

