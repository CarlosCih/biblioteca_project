#Aqui van las rutas utilizadas en la aplicacion de biblioteca
from django.urls import path
from . import views

app_name='biblioteca'

#definicion de las rutas
urlpatterns = [
    path('', views.index, name='index'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/agregar/', views.agregar_libro, name='agregar_libro'),
    path('libros/<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    path('libros/<int:libro_id>/desactivar/', views.desactivar_libro, name='desactivar_libro'),

    #futuras rutas para el modelo Usuario
]
