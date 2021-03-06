from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import * 
# Create your views here.

def lista_personas(request) :
    lista = Persona.objects.all() # Todas las personas
    return render(request, 'apppersona/lista_personas.html',{'lista' : lista})

def lista_tarjetas(request) :
    tarjetas = TarjetaJunaeb.objects.all()
    return render(request, 'apppersona/lista_tarjetas.html',{'listaTarjetas' : tarjetas})

def tarjetas_con_plata(request) :
    tarjetas = TarjetaJunaeb.objects.filter(montoDisponible__gte=1)
    return render(request, 'apppersona/lista_tarjetas.html',{'listaTarjetas' : tarjetas})

def persona_nueva(request) :
    if request.method == "POST" :
        formulario = FormularioPersona(request.POST)
        if formulario.is_valid() :
            persona = formulario.save(commit=False)
            persona.save()
            return HttpResponse("PERSONA GUARDADA")
    formulario = FormularioPersona()
    return render(request, 'apppersona/registro.html',{'form' : formulario})

