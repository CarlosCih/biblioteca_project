#Aqui van las rutas utilizadas en la aplicacion de biblioteca
from django.urls import path
from . import views

app_name='biblioteca'

#definicion de las rutas
urlpatterns = [
    path('', views.index, name='index'),
    #-------------------------------------------------------------------------#
    #rutas de libros
    path('libros/', views.ListaLibrosView.as_view(), name='lista_libros'),
    path('libros/<int:libro_id>/', views.DetalleLibroView.as_view(), name='detalle_libro'),
    path('libros/agregar/', views.AgregarLibroView.as_view(), name='agregar_libro'),
    path('libros/<int:libro_id>/editar/', views.EditarLibroView.as_view(), name='editar_libro'),
    path('libros/<int:libro_id>/eliminar/', views.EliminarLibroView.as_view(), name='eliminar_libro'),
    path('libros/<int:libro_id>/desactivar/', views.DesactivarLibroView.as_view(), name='desactivar_libro'),

    #-------------------------------------------------------------------------#
    #rutas de autores
    path('autores/', views.ListAutorView.as_view(), name='lista_autores'),
    path('autores/agregar/', views.AgregarAutorView.as_view(), name='agregar_autor'),
    path('autores/<int:autor_id>/', views.DetailAutorView.as_view(), name='detalle_autor'),
    path('autores/<int:autor_id>/editar/', views.EditAutorView.as_view(), name='editar_autor'),
    path('autores/<int:autor_id>/eliminar/', views.EliminarAutorView.as_view(), name='eliminar_autor'),
    #-------------------------------------------------------------------------#
    #rutas de categorias
    path("categorias/", views.CategoriaListView.as_view(), name="lista_categorias"),
    path("categorias/<int:pk>/", views.CategoriaDetailView.as_view(), name="detalle_categoria"),
    path('categorias/agregar/', views.AgregarCategoriaView.as_view(), name='agregar_categoria'),
    path('categorias/<int:categoria_id>/editar/', views.EditarCategoriaView.as_view(), name='editar_categoria'),
    path('categorias/<int:categoria_id>/eliminar/', views.EliminarCategoriaView.as_view(), name='eliminar_categoria'),


    #futuras rutas para el modelo Usuario
]
