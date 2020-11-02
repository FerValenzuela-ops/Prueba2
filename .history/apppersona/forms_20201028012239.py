from django import forms

from .models import Persona

class FormularioPersona(forms.ModelForm) :
    class Meta:
        model =  Persona
        fields = ('nombre', 'asunto', 'telefono', 'email', 'mensaje')