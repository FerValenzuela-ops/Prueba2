from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import *

# Create your views here.


def lista_personas(request):
    lista = User.objects.all()  # Todas las personas
    return render(request, 'apppersona/lista_personas.html', {'lista': lista})


def lista_tarjetas(request):
    tarjetas = TarjetaJunaeb.objects.all()
    return render(request, 'apppersona/lista_tarjetas.html', {'listaTarjetas': tarjetas})


def tarjetas_con_plata(request):
    tarjetas = TarjetaJunaeb.objects.filter(montoDisponible__gte=1)
    return render(request, 'apppersona/lista_tarjetas.html', {'listaTarjetas': tarjetas})


def persona_nueva(request):
    if request.method == "POST":
        formulario = FormularioPersona(request.POST)
        if formulario.is_valid():
            persona = formulario.save(commit=False)
            persona.save()

            return HttpResponse("PERSONA GUARDADA")
    else:
        formulario = FormularioPersona()

    return render(request, 'apppersona/registro.html', {'form': formulario})


def index(request):
    return render(request, 'apppersona/index.html')


def contacto(request):
    return render(request, 'apppersona/contacto.html')


def nosotros(request):
    return render(request, 'apppersona/nosotros.html')


def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}    
    return render(request, "apppersona/register.html", context)


"""def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
        profile_form = UserProfileForm(request.POST)
	    
        if form.is_valid():

	        form.save()

	        return HttpResponse("/home")
    else:
	    form = RegisterForm()
        profile_form = UserProfileForm()

    return render(response, "apppersona/register.html", {"form":form})"""
