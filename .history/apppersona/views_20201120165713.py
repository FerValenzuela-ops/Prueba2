from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth import login
from django.contrib.auth.decorators import *
from django.contrib.admin.views.decorators import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ImageForm
from rest_framework import viewsets
from rest_framework import permissions
from apppersona.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet) : 
    """
        endpoints para acceder a los usuarios
    """

    queryset = Persona.objects.all(), User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
# metodos para las vistas 


def is_valid_queryparam(param):
    return param != '' and param is not None

def filtros(request):
    qs = Persona.objects.all()
    nombre_contains_query = request.GET.get('nombre_contains')
    if nombre_contains_query != '' and nombre_contains_query is not None:
        qs = qs.filter(email__icontains=nombre_contains_query)
    context = {'queryset': qs}
    return render(request, 'apppersona/filtros.html', context)

#metodo de formulario
def bootstrap_form(request):
    qs = Persona.objects.all()
    nombre_contains_query = request.GET.get('nombre_contains')
    correo_contains_query = request.GET.get('correo_exacto')
    min_edad_query = request.GET.get('min_edad_query')
    max_edad_query = request.GET.get('max_edad_query')

    if nombre_contains_query != '' and nombre_contains_query is not None:
        qs = qs.filter(nombre__icontains=nombre_contains_query)

    elif correo_contains_query != '' and correo_contains_query is not None:
        qs = qs.filter(email__icontains=correo_contains_query)

    if is_valid_queryparam(min_edad_query):
        qs = qs.filter(edad__gte=min_edad_query)

    if is_valid_queryparam(max_edad_query):
        qs = qs.filter(edad__lt=max_edad_query)

    context = {'queryset': qs}
    return render(request, 'apppersona/bootstrap_form.html', context)

#filtro de personas
def filterpersonas(request):
    return render(request, 'apppersona/filterpersonas.html')

#metodo para listas  personas
def lista_personas(request):
    lista = User.objects.all()  # Todas las personas
    persona = Persona.objects.get()
    return render(request, 'apppersona/lista_personas.html', {'lista': lista})

#metodoo para listar tarjetas
def lista_tarjetas(request):
    tarjetas = TarjetaJunaeb.objects.all()
    return render(request, 'apppersona/lista_tarjetas.html', {'listaTarjetas': tarjetas})

#metodo para listar tarjetas con dinero
def tarjetas_con_plata(request):
    tarjetas = TarjetaJunaeb.objects.filter(montoDisponible__gte=1)
    return render(request, 'apppersona/lista_tarjetas.html', {'listaTarjetas': tarjetas})

#metodos que devuelven ciertas paginas para redirecciones 
def index(request):
    return render(request, 'apppersona/index.html')


def profile(request):
    return render(request, 'apppersona/profile.html')


def contacto(request):
    return render(request, 'apppersona/contacto.html')


def nosotros(request):
    return render(request, 'apppersona/nosotros.html')

#metodo para registrar personas 
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
#metodo para resetear la contraseña

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form": password_reset_form})

#metodo para subir imagenes 
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return HttpResponseRedirect('image_gallery')

    else:
        form = ImageForm()
    return render(request, 'apppersona/upload.html', {'form': form})

#metodo para mostrar imagenes 
def image_gallery(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'apppersona/image_gallery.html', {'images': images})

#metodo para guardar el formulario 
def contactosPersonas(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            
            return HttpResponseRedirect('index')

    else:
        form = FormularioContacto()
    return render(request, 'apppersona/contacto.html', {'form': form})
          
           
