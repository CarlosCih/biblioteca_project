#Aqui van todos los formularios de la aplicacion biblioteca
from django import forms
from .models import Libro, Autor, Categoria

#formulario para los autores
class AutorForm(forms.ModelForm):
    class Meta:
        model=Autor
        fields=['nombre','year','nacionalidad']

#formulario para las categorias
class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['nombre','descripcion']

#Formulario para agregatr un nuevo libro
class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=['titulo','autor','categoria','fecha_publicacion','isbn','paginas','precio','disponible']
        widgets={
            'disponible': forms.CheckboxInput(attrs={'class':'filled-in'}),
        }
        
#futuro formulario para el modelo Usuario
#class UsuarioForm(forms.ModelForm):
#    class Meta:
#        model=Usuario
#        fields=['nombre','email']
