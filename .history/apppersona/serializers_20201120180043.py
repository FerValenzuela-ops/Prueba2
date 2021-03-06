from django.contrib.auth.models import User
from django.db.models.base import Model
from rest_framework import serializers
from .models import Contactos, Persona, Image


class UserSerializer(serializers.HyperlinkedModelSerializer) :
    
    persona = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='persona-url'
    )
    class Meta : 
        model = User
        fields = ['url','persona','username','first_name','last_name', 'email']

class PersonaSerializer(serializers.HyperlinkedModelSerializer) :
    
    class Meta : 
        model = Persona
        fields = ['url','user','nombre', 'apellido', 'email', 'celular', 'rut', 'region', 'edad']        


   
