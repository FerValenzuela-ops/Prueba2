from django import forms
from django.db import models

from .models import Persona
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class FormularioPersona(forms.ModelForm) :
    
    class Meta:
        model =  Persona
        fields = ('nombre' ,'apellido', 'email' ,'celular', 'usuario', 'region' , 'contraseña', 'contraseñaconfirmar')

        
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    region = forms.CharField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]
     

        

       