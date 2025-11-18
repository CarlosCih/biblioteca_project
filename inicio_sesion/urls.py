from django.urls import path
from . import views

app_name = 'inicio_sesion'

urlpatterns = [
    #rutas de login, logout, registro, perfil y recuperacion de contraseña
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    #rutas para el cambio de contraseña

    
]