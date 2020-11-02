from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import *
from django.contrib.admin.views.decorators import *
# Create your views here.

#@login_required
#def index(request):
#    return render(request,'appersona/index.html')


def lista_personas(request):
    lista = User.objects.all()  # Todas las personas
    return render(request, 'apppersona/lista_personas.html', {'lista': lista})


def lista_tarjetas(request):
    tarjetas = TarjetaJunaeb.objects.all()
    return render(request, 'apppersona/lista_tarjetas.html', {'listaTarjetas': tarjetas})


def tarjetas_con_plata(request):
    tarjetas = TarjetaJunaeb.objects.filter(montoDisponible__gte=1)
    return render(request, 'apppersona/lista_tarjetas.html', {'listaTarjetas': tarjetas})


def index(request):
    return render(request, 'apppersona/index.html')


def contacto(request):
    return render(request, 'apppersona/contacto.html')


def nosotros(request):
    return render(request, 'apppersona/nosotros.html')

@user_passes_test(lambda u: u.is_superuser)
def adminpage():
    return render(request, 'accounts/admin.html')
    
def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = FormularioPersona(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = ExtendedUserCreationForm()
        profile_form = FormularioPersona()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, "apppersona/registro.html", context)
