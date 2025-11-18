#Aqui van todos los formularios de la aplicacion biblioteca
from django import forms
from .models import Libro, Autor, Categoria

#formulario para los autores
class AutorForm(forms.ModelForm):
    class Meta:
        model=Autor
        fields=['nombre','year','nacionalidad']
        widgets={
            'nacionalidad': forms.TextInput(attrs={'placeholder':'Ejemplo: Peruano, Mexicano, Español'}),
        }

#formulario para las categorias
class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['nombre','descripcion']
        widgets={
            'descripcion': forms.Textarea(attrs={'rows': 3, 'cols': 40}), # Ajusta el número de filas según sea necesario
        }

#Formulario para agregatr un nuevo libro
class LibroForm(forms.ModelForm):
    # Asegura que el campo fecha se renderice y procese en formato ISO (YYYY-MM-DD)
    fecha_publicacion = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    )
    class Meta:
        model=Libro
        fields=['titulo','autor','categoria','fecha_publicacion','isbn','paginas','precio','disponible']
        widgets={
            'autor': forms.Select(attrs={'class':'browser-default'}),
            'categoria': forms.Select(attrs={'class':'browser-default'}),
            'disponible': forms.CheckboxInput(attrs={'class':'filled-in'}),
        }
        
#futuro formulario para el modelo Usuario
#class UsuarioForm(forms.ModelForm):
#    class Meta:
#        model=Usuario
#        fields=['nombre','email']
