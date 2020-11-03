from django import forms
from django.db import models
from django.db.models.fields import CharField, EmailField
from django.forms import ModelForm, Textarea
from django.forms.widgets import EmailInput, HiddenInput, PasswordInput, Select, TextInput

from .models import Persona, Image
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class FormularioPersona(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'email', 'celular',
                  'region', 'rut', 'edad')
        widgets = {
            'nombre': Textarea(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'nombre', 'class': 'form-control', 'required onfocus': "setVisibility('100','inline')", 'onBlur': "setVisibility('100','none')",  'onkeyup':"sync()"}),
            'apellido': Textarea(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'apellido', 'class': "form-control", 'required onfocus': "setVisibility('101','inline')", 'onBlur': "setVisibility('101','none')",  'onkeyup':"sync()"}),
            'email': EmailInput(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'email', 'class': "form-control", 'required onfocus': "setVisibility('102','inline')", 'onBlur': "setVisibility('102','none')", 'type': 'email',  'onkeyup':"sync()"}),
            'celular': Textarea(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'celular', 'class': "form-control", 'required onfocus': "setVisibility('103','inline')", 'onBlur': "setVisibility('103','none')"}),
            'region': Select(attrs={'class': "form-control", 'onfocus': "setVisibility('105','inline')", 'onBlur': "setVisibility('105','none')", 'default': "rm"}),
            'rut' : Textarea(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'rut', 'class': 'form-control', 'required onfocus': "setVisibility('106','inline')", 'onBlur': "setVisibility('106','none')", }),
            'edad' : Textarea(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'edad', 'class': 'form-control', 'required onfocus': "setVisibility('109','inline')", 'onBlur': "setVisibility('109','none')", })
          }

        labels = {
            'nombre': _('Nombre'),
            'apellido': _('Apellido'),
            'email': _('Correo Electronico'),
            'celular': _('Numero Telefonico'),
            'region': _('Region'),

        }

        #help_texts = {
       #     'nombre': _('Ingrese su nombre.'),
        #}
        #error_messages = {
        #    'nombre': {
        #        'max_length': _("El nombre excede el limite de caracteres."),
        #    },
        #}



 



class ExtendedUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(ExtendedUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = TextInput(attrs = {'class': 'form-control', 'id':'first_name', 'type':'hidden'})
        self.fields['last_name'].widget = TextInput(attrs = {'class': 'form-control', 'id':'last_name', 'type':'hidden'})
        self.fields['username'].widget = TextInput(attrs = {'class': 'form-control', 'id':'username', 'required onfocus': "setVisibility('104','inline')", 'onBlur': "setVisibility('104','none')"})
        self.fields['password1'].widget = PasswordInput(attrs = {'class': 'form-control', 'id':'password1', 'required onfocus': "setVisibility('107','inline')", 'onBlur': "setVisibility('107','none')"})
        self.fields['password2'].widget = PasswordInput(attrs = {'class': 'form-control', 'id':'password2','required onfocus': "setVisibility('108','inline')", 'onBlur': "setVisibility('108','none')"})
        self.fields['email'].widget = EmailInput(attrs = {'class': 'form-control', 'id':'useremail', 'type':'hidden'})

    class Meta:
        model = User
        fields =  ('first_name', 'last_name', 'username', 'email', 'password1', 'password2') 

   

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')

class FormularioContacto(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('nombre', 'asunto', 'email', 'telefono',
                  'mensaje')
        widgets = {
            'nombre': Textarea(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'nombre', 'class': 'form-control', 'required onfocus': "setVisibility('100','inline')", 'onBlur': "setVisibility('100','none')",  'onkeyup':"sync()"}),
            'asunto': Textarea(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'apellido', 'class': "form-control", 'required onfocus': "setVisibility('101','inline')", 'onBlur': "setVisibility('101','none')",  'onkeyup':"sync()"}),
            'email': EmailInput(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'email', 'class': "form-control", 'required onfocus': "setVisibility('102','inline')", 'onBlur': "setVisibility('102','none')", 'type': 'email',  'onkeyup':"sync()"}),
            'telefono': Textarea(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'celular', 'class': "form-control", 'required onfocus': "setVisibility('103','inline')", 'onBlur': "setVisibility('103','none')"}),
            'mensaje' : Textarea(attrs={'rows': 1, 'cols': 30, 'style': 'resize:none;', 'id': 'rut', 'class': 'form-control', 'required onfocus': "setVisibility('106','inline')", 'onBlur': "setVisibility('106','none')", }),
           }        