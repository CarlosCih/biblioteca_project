from django.contrib import admin
from .models import Autor, Categoria ,Libro, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1 #Esto mostrara un formulario extra para agregar nuevas reseñas directamente desde la pagina de admin del libro
    fields = ('user_review','comentario','calificacion')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','year','nacionalidad')
    list_filter = ('nacionalidad',)
    search_fields = ('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display= ('nombre','descripcion')
    search_fields = ('nombre',)
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','fecha_publicacion','isbn','disponible')
    list_filter = ('disponible','fecha_publicacion') #filtros laterales
    search_fields = ('titulo','autor','isbn') #barra de busqueda
    ordering = ('titulo','-fecha_publicacion') #ordenar por fecha de publicacion descendente
    inlines = [ReviewInline]  # Agrega las reseñas en línea al admin de Autor


#futuro registro para el modelo Usuario
#from .models import Usuario
#@admin.register(Usuario)
#class UsuarioAdmin(admin.ModelAdmin):
#    list_display = ('nombre','email')
#    search_fields = ('nombre','email')
