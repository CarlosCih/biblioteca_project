from django.contrib import admin
from .models import Autor, Categoria ,Libro

# Register your models here.

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

#futuro registro para el modelo Usuario
#from .models import Usuario
#@admin.register(Usuario)
#class UsuarioAdmin(admin.ModelAdmin):
#    list_display = ('nombre','email')
#    search_fields = ('nombre','email')
