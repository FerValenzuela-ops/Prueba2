from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields import EmailField



# Modelos

# Regiones del combo box en el formulario
REGIONES = (

    ('primera' ,'I Región de Tarapacá'),
    ('segunda','II Región de Antofagasta'),
    ('tercera','III Región de Atacama'),
    ('cuarta','IV Región de Coquimbo'),
    ('quinta','V Región de Valparaíso'),
    ('sexta','VI Región del Libertador General Bernardo O’Higgins'),
    ('septima','VII Región del Maule'),
    ('octava','VIII Región del Biobío'),
    ('novena','IX Región de La Araucanía'),
    ('decima','X Región de Los Lagos'),
    ('decimoprimera','XI Región Aysén del General Carlos Ibáñez del Campo'),
    ('decimosegunda','XII Región de Magallanes y Antártica Chilena'),
    ('rm','Región Metropolitana de Santiago'),
    ('decimocuarta','XIV Región de Los Ríos'),
    ('decimoquinta','XV Región de Arica y Parinacota'),
    ('decimosexta','XVI Región de Ñuble')
)

#Clase Image para las imagenes de la galeria
class Image(models.Model):
    #Atributos de Image
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    #Metodo que devuelve el titulo de la imagen
    def __str__(self):
        return self.title

#Clase Persona
class Persona(models.Model): 
    #Atributos de Persona
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    email = models.TextField(max_length=50)
    celular = models.IntegerField(max_length=50)
    rut = models.TextField(max_length=12)
    region = models.CharField(max_length=6, choices=REGIONES, default='rm')
    edad = models.IntegerField(max_length=30)
    
    #Metodo que devuelve el nombre de la persona
    def __str__(self):
        return self.nombre

#Clase Contactos
class Contactos(models.Model):
    #Atributos de Contactos
    nombre = models.TextField(max_length=50)
    asunto = models.TextField(max_length=50)
    telefono = models.IntegerField(max_length=12)
    email = models.EmailField(max_length=50)
    mensaje = models.TextField(max_length=50)

    #Metodo que devuelve el nombre del contacto
    def __str__(self):
        return self.nombre


class TarjetaJunaeb(models.Model):
    numeroTarjeta = models.TextField(max_length=12) # es un identificador
    montoDisponible = models.IntegerField()
    rut = models.TextField(max_length=9)
    clave = models.TextField(max_length=8)

    def __str__(self):
        return self.rut + " " + self.numeroTarjeta 


    
