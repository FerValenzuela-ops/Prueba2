from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    rut = models.TextField(max_length=15)
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.rut

class TarjetaJunaeb(models.Model):
    numeroTarjeta = models.TextField(max_length=12) # es un identificador
    montoDisponible = models.IntegerField()
    rut = models.TextField(max_length=9)
    clave = models.TextField(max_length=8)

    def __str__(self):
        return self.rut + " " + self.numeroTarjeta + " "



    
