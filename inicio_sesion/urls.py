from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'inicio_sesion'

urlpatterns = [
    #rutas de login, logout, registro, perfil y recuperacion de contraseña
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('delete_account/', views.delete_profile, name='delete_account'),
    #rutas para el cambio de contraseña   
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(
             template_name='registration/password_change.html',
         ), 
         name='password_change'),

    #ruta para confirmar el cambio de contraseña
    path('password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(
             template_name='registration/password_change_done.html'
         ), 
         name='password_change_done'),
## rutas para el restablecimiento de contraseña
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html'
         ), 
         name='password_reset'),

    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
                template_name='registration/password_reset_done.html'
            ),
         name='password_reset_done'),
]