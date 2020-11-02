from django import forms
from django.db import models
from django.forms import ModelForm, Textarea

from .models import Persona
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm



class FormularioPersona(forms.ModelForm) :
    
    class Meta:
        model =  Persona
        fields = ('nombre' ,'apellido', 'email' ,'celular', 'usuario', 'region' , 'contraseña', 'contraseñaconfirmar')
        widgets = {
          'nombre': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;'}),
        }
        labels = {
            'nombre': _('Nombres'),
        }
        help_texts = {
            'nombre': _('Some useful help text.'),
        }
        error_messages = {
            'nombre': {
                'max_length': _("This writer's name is too long."),
            },
        }

        
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    region = forms.CharField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]
     

        

       