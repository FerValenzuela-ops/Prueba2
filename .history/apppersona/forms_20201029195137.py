from django import forms
from django.db import models

from .models import Persona
from django.contrib.auth.models import User



class FormularioPersona(forms.ModelForm) :
    
    class Meta:
        model =  Persona, User
        fields = ('nombre' ,'apellido', 'email' ,'celular', 'usuario', 'region' , 'contraseña', 'contraseñaconfirmar')

   

        

       