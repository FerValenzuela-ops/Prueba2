from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_personas, name ='lista_personas'),
    path('tarjetas', views.lista_tarjetas, name ='lista_tarjetas'),
    path('tarjetas_con_plata', views.tarjetas_con_plata, name ='tarjetas_con_plata'),
    path('persona/nueva', views.persona_nueva, name ='persona_nueva')


]

urlpatterns+= [
    path('accounts/', include ('django.contrib.auth.url'))

]