from django.contrib import admin
from .models import Persona, TarjetaJunaeb
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.
admin.site.register(Persona)
admin.site.register(TarjetaJunaeb)

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
