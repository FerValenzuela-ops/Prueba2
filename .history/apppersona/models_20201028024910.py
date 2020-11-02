from django.db import models
from django.db.models.fields import EmailField
from django.db.models.manager import ManagerDescriptor

# Create your models here.

REGIONES = (

    ('I' ,'I Región de Tarapacá'),
    ('II','II Región de Antofagasta'),
    ('III','III Región de Atacama'),
    ('IV','IV Región de Coquimbo'),
    ('V','V Región de Valparaíso'),
    ('VI','VI Región del Libertador General Bernardo O’Higgins'),
    ('VII','VII Región del Maule'),
    ('VIII','VIII Región del Biobío'),
    ('IX','IX Región de La Araucanía'),
    ('X','X Región de Los Lagos'),
    ('XI','XI Región Aysén del General Carlos Ibáñez del Campo'),
    ('XII','XII Región de Magallanes y Antártica Chilena'),
    ('RM','Región Metropolitana de Santiago'),
    ('XIV','XIV Región de Los Ríos'),
    ('XV','XV Región de Arica y Parinacota'),
    ('XVI','XVI Región de Ñuble'),
)





class Persona(models.Model): 
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    email = models.TextField(max_length=15)
    celular = models.TextField(max_length=50)
    usuario = models.TextField(max_length=300)
    region = models.CharField(max_length=6, choices=REGIONES, default='green')
    contraseña = models.TextField(max_length=30)
    contraseñaconfirmar = models.TextField(max_length=30)
    
    def __str__(self):
        return self.nombre + " " + self.email 

class TarjetaJunaeb(models.Model):
    numeroTarjeta = models.TextField(max_length=12) # es un identificador
    montoDisponible = models.IntegerField()
    rut = models.TextField(max_length=9)
    clave = models.TextField(max_length=8)

    def __str__(self):
        return self.rut + " " + self.numeroTarjeta 


    
