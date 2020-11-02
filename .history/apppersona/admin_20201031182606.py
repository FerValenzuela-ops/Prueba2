from django.contrib import admin
from .models import Persona, TarjetaJunaeb, UserProfile
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.
admin.site.register(Persona)
admin.site.register(TarjetaJunaeb)
admin.site.register(UserProfile)


