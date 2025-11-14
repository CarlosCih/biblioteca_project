#Aqui van todos los formularios de la aplicacion biblioteca
from django import forms
from .models import Libro

#Formulario para agregatr un nuevo libro
class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=['titulo','autor','fecha_publicacion','isbn','disponible']
        widgets={
            'disponible': forms.CheckboxInput(attrs={'class':'filled-in'}),
        }
        
#futuro formulario para el modelo Usuario
#class UsuarioForm(forms.ModelForm):
#    class Meta:
#        model=Usuario
#        fields=['nombre','email']
