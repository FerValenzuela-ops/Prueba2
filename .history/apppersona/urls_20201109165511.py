from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# Urls de cada html en el Templates para su redireccionamiento
urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('lista', views.lista_personas, name ='lista_personas'),
    path('tarjetas', views.lista_tarjetas, name ='lista_tarjetas'),
    path('tarjetas_con_plata', views.tarjetas_con_plata, name ='tarjetas_con_plata'),
    path('registro', views.register, name ='registro'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('contacto', views.contactosPersonas, name = 'contacto'),
    path('profile', views.profile, name = 'profile'),
    path("register/", views.register, name="register"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'), 
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('upload', views.image_upload_view, name="upload"),
    path('image_gallery', views.image_gallery, name="image_gallery"),
    path('bootstrap_form', views.bootstrap_form, name="bootstrap_form"),


    

   
    


]

urlpatterns+= [

    path('accounts/', include ('django.contrib.auth.urls')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
