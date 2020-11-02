from django import forms
from django.db import models

from .models import Persona


FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class FormularioPersona(forms.ModelForm) :
    
    class Meta:
        model =  Persona
        nombre = forms.CharField(max_length=100)
        fields = ('nombre' ,'apellido', 'email' ,'celular', 'usuario', 'region', 'contraseña', 'contraseñaconfirmar')
       