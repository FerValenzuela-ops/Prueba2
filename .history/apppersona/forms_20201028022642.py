from django import forms
from django.db import models

from .models import Persona


TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class FormularioPersona(forms.ModelForm) :
    
    class Meta:
        model =  Persona
        fields = ('nombre','apellido', 'email' ,'celular', 'usuario', 'region', 'contraseña', 'contraseñaconfirmar')
       