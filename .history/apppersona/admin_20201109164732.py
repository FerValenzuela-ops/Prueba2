from django.contrib import admin
from .models import Persona, TarjetaJunaeb, Image, Contactos
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.
admin.site.register(Persona) #Permite la visualizacion del model Persona en el panel de admin
admin.site.register(TarjetaJunaeb) #Permite la visualizacion del model TarjetaJunaeb en el panel de admin
admin.site.register(Image) #Permite la visualizacion del model Image en el panel de admin
admin.site.register(Contactos) #Permite la visualizacion del model Contactos en el panel de admin


