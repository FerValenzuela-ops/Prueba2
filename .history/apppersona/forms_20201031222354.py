from django import forms
from django.db import models
from django.db.models.fields import CharField
from django.forms import ModelForm, Textarea
from django.forms.widgets import EmailInput, PasswordInput, Select, TextInput

from .models import Persona
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm



class FormularioPersona(forms.ModelForm) :
    
    class Meta:
        model =  Persona
        fields = ('nombre' ,'apellido', 'email' ,'celular', 'usuario', 'region' , 'contraseña', 'contraseñaconfirmar')
        widgets = {
          'nombre': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;', 'id': 'nombre', 'class':'form-control', 'required onfocus':"setVisibility('100','inline')", 'onBlur':"setVisibility('100','none')" }),
          'apellido': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;', 'id': 'apellido', 'class':"form-control", 'required onfocus':"setVisibility('101','inline')", 'onBlur':"setVisibility('101','none')"}),
          'email': EmailInput(attrs={'rows':1, 'cols':30, 'style':'resize:none;', 'id': 'email', 'class':"form-control", 'required onfocus':"setVisibility('102','inline')", 'onBlur':"setVisibility('102','none')", 'type':'email'}),
          'celular': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;', 'id': 'celular', 'class':"form-control", 'required onfocus':"setVisibility('103','inline')", 'onBlur':"setVisibility('103','none')"}),
          'usuario': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;', 'id': 'usuario', 'class':"form-control", 'required onfocus':"setVisibility('104','inline')", 'onBlur':"setVisibility('104','none')"}),
          'region' : Select(attrs={'class':"form-control", 'onfocus':"setVisibility('105','inline')", 'onBlur':"setVisibility('105','none')", 'default': "rm"}),
          'contraseña':  PasswordInput(attrs={'rows':1, 'cols':30, 'style':'resize:none;', 'id': 'pass', 'class':"form-control inputPass", 'required onfocus':"setVisibility('106','inline')", 'onBlur':"setVisibility('106','none')"}),
          'contraseñaconfirmar': PasswordInput(attrs={'rows':1, 'cols':30, 'style':'resize:none;', 'id': 'passconfirm', 'class':"form-control", 'required onfocus':"setVisibility('107','inline')", 'onBlur':"setVisibility('107','none')"}),
        }

									
        
									
        labels = {
            'nombre': _('Nombre'),
            'apellido': _('Apellido'),
            'email': _('Correo Electronico'),
            'celular': _('Numero Telefonico'),
            'usuario': _('Usuario'),
            'region': _('Region'),
            'contraseña': _('Contraseña'),
            'contraseñaconfirmar': _('Confirmar Contraseña'),
        }

        
               

        """help_texts = {
            'nombre': _('Ingrese su nombre.'),
        }
        error_messages = {
            'nombre': {
                'max_length': _("El nombre excede el limite de caracteres."),
            },
        }"""


									
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('region', 'celular')
        
		
class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user         

        

       