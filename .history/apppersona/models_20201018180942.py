from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    rut = models.TextField(max_length=30)
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.rut



    
