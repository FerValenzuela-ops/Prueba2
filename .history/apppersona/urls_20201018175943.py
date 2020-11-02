from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personas, name ='lista_personas')
]