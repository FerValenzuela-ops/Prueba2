from django.contrib.auth.models import User
from django.db.models.base import Model
from rest_framework import serializers
from .models import Contactos, Persona, Image


class UserSerializer(serializers.HyperlinkedModelSerializer) :
    
    class Meta : 
        model = User
        fields = ['url','first_name','last_name', 'email']

class PersonaSerializer(serializers.HyperlinkedModelSerializer) :
    
    class Meta : 
        model = Persona
        fields = ['url','nombre', 'apellido', 'email', 'celular', 'rut', 'region', 'edad']        


   
