#Aqui van todos los formularios de la aplicacion biblioteca
from django import forms
from .models import Libro, Autor, Categoria

#formulario para los autores
class AutorForm(forms.ModelForm):

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year and (year < 0 or year > 2100):
            raise forms.ValidationError('Por favor ingrese un año válido.')
        return year
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and Autor.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError('Ya existe un autor con este nombre.')
        return nombre
    class Meta:
        model=Autor
        fields=['nombre','year','nacionalidad']
        widgets={
            'nacionalidad': forms.TextInput(attrs={'placeholder':'Ejemplo: Peruano, Mexicano, Español'}),
        }

#formulario para las categorias
class CategoriaForm(forms.ModelForm):
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion and len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres.')
        return descripcion
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and Categoria.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError('Ya existe una categoría con este nombre.')
        return nombre
    class Meta:
        model=Categoria
        fields=['nombre','descripcion']
        widgets={
            'descripcion': forms.Textarea(attrs={'rows': 3, 'cols': 40}), # Ajusta el número de filas según sea necesario
        }

#Formulario para agregatr un nuevo libro
class LibroForm(forms.ModelForm):
    #Esta función valida que el ISBN tenga el formato correcto
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if isbn and not isbn.isdigit():
            raise forms.ValidationError('El ISBN debe contener solo dígitos.')
        if isbn and len(isbn) not in [10, 13]:
            raise forms.ValidationError('El ISBN debe tener 10 o 13 dígitos.')
        return isbn
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo.')
        return precio
    def clean_paginas(self):
        paginas = self.cleaned_data.get('paginas')
        if paginas is not None and paginas < 0:
            raise forms.ValidationError('El número de páginas no puede ser negativo.')
        return paginas
    def clean(self):
        cleaned_data = super().clean()
        fecha_publicacion = cleaned_data.get('fecha_publicacion')
        if fecha_publicacion and fecha_publicacion > datetime.date.today():
            self.add_error('fecha_publicacion', 'La fecha de publicación no puede ser en el futuro.')
        return cleaned_data
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
