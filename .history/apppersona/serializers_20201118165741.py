from django.contrib.auth.models import User
from django.db.models.base import Model
from rest_framework import serializers
from .models import Contactos, Persona, Image


class UserSerializer(serializers.HyperlinkedModelSerializer) :
    
    class Meta : 
        model = Persona, Contactos, Image
        fields = ['url', 'username', 'email', 'edad']
