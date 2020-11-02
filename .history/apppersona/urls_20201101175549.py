from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.lista_personas, name ='lista_personas'),
    path('tarjetas', views.lista_tarjetas, name ='lista_tarjetas'),
    path('tarjetas_con_plata', views.tarjetas_con_plata, name ='tarjetas_con_plata'),
    path('registro', views.register, name ='registro'),
    path('index', views.index, name = 'index'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('contacto', views.contacto, name = 'contacto'),
    path("register/", views.register, name="register"),
    path('passwordreset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'), 
    path("password_reset", views.password_reset_request, name="password_reset")
    

   
    


]

urlpatterns+= [

    path('accounts/', include ('django.contrib.auth.urls')),
    

]