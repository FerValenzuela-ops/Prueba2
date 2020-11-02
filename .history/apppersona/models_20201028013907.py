from django.db import models
from django.db.models.fields import EmailField
from django.db.models.manager import ManagerDescriptor

# Create your models here.

class Persona(models.Model):
    nombre = models.TextField(max_length=30)
    asunto = models.TextField(max_length=30)
    telefono = models.TextField(max_length=15)
    email = models.TextField(max_length=50)
    mensaje = models.TextField(max_length=300)
    
    def __str__(self):
        return self.nombre + " " + self.email 

class TarjetaJunaeb(models.Model):
    numeroTarjeta = models.TextField(max_length=12) # es un identificador
    montoDisponible = models.IntegerField()
    rut = models.TextField(max_length=9)
    clave = models.TextField(max_length=8)

    def __str__(self):
        return self.rut + " " + self.numeroTarjeta 


    
