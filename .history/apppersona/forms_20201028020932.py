from django import forms

from .models import Persona

class FormularioPersona(forms.ModelForm) :
    class Meta:
        model =  Persona
        fields = ('nombre','apellido', 'email' ,'celular', 'usuario', 'region', 'contraseña', 'contraseñaconfirmar')