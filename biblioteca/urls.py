#Aqui van las rutas utilizadas en la aplicacion de biblioteca
from django.urls import path
from . import views

app_name='biblioteca'

#definicion de las rutas
urlpatterns = [
    path('', views.index, name='index'),
    #-------------------------------------------------------------------------#
    #rutas de libros
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/agregar/', views.agregar_libro, name='agregar_libro'),
    path('libros/<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    path('libros/<int:libro_id>/desactivar/', views.desactivar_libro, name='desactivar_libro'),
    #-------------------------------------------------------------------------#
    #rutas de autores
    path('autores/', views.AutorListView.as_view(), name='lista_autores'),
    path('autores/agregar/', views.agregar_autor, name='agregar_autor'),
    path('autores/<int:autor_id>/editar/', views.editar_autor, name='editar_autor'),
    path('autores/<int:autor_id>/eliminar/', views.eliminar_autor, name='eliminar_autor'),
    #-------------------------------------------------------------------------#
    #rutas de categorias
    path("categorias/", views.CategoriaListView.as_view(), name="lista_categorias"),
    path('categorias/<int:categoria_id>/', views.ver_categoria, name='ver_categoria'),
    path('categorias/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categorias/<int:categoria_id>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:categoria_id>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),


    #futuras rutas para el modelo Usuario
]
