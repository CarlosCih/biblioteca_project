from django.shortcuts import get_object_or_404, render

from biblioteca.form import LibroForm
from biblioteca.models import Libro

#-- Vista para la pagina de inicio de la aplicacion biblioteca con un FBV(Function Based View) ---#
def index(request):
    return render(request, 'biblioteca/index.html')
#Nota: La ruta establecida dice que en la carpeta templates debe haber una carpeta llamada biblioteca que contenga el archivo index.html

# Vista para listar todos los libros
def lista_libros(request):
    libros = Libro.objects.filter(disponible=True).order_by('titulo')
    context = {'libros': libros} #el contexto es un diccionario que se pasa a la plantilla a renderizar
    return render(request, 'biblioteca/lista_libros.html', context)

# Vista para ver los detalles de un libro
def detalle_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    context = {'libro': libro}
    return render(request, 'biblioteca/detalle_libro.html', context)

# Vista para agregar un nuevo libro
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return lista_libros(request) #redirecciona a la lista de libros despues de agregar uno nuevo
    else:
        form = LibroForm()
    return render(request, 'biblioteca/libro_form.html', {'form': form, 'titulo': 'Agregar Libro', 'libro': None})
    
# Vista para editar un libro existente
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method=='POST':
        form=LibroForm(request.POST, instance=libro) #instance indica que se esta editando un libro existente
        if form.is_valid():
            form.save()
            return lista_libros(request) #redirecciona a la lista de libros despues de editar uno
    else:
        form=LibroForm(instance=libro)
    return render(request, 'biblioteca/libro_form.html', {'form': form, 'titulo': 'Editar Libro', 'libro': libro})


# Vista para eliminar un libro existente
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.delete()
        return lista_libros(request)
    return render(request, 'biblioteca/eliminar_libro.html', {'libro': libro, 'titulo': 'Eliminar Libro'}) 
## Esta vista muestra una confirmacion antes de eliminar el libro, el borrado es definitivo.

#Vista para un soft delete de un libro (marcar como no disponible en lugar de eliminar)
def desactivar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.disponible = False
        libro.save()
        return lista_libros(request)
    return render(request, 'biblioteca/desactivar_libro.html', {'libro': libro, 'titulo': 'Desactivar Libro'})

#-- Fin de la vista basadas en funciones (FBV) ---#

#-- Inicio de vistas basadas en clases (CBV) - futuro ---#

#-- Fin de vistas basadas en clases (CBV) - futuro ---#

#los archivos html que se deben crear son:
# biblioteca/index.html
# biblioteca/lista_libros.html
# biblioteca/detalle_libro.html
# biblioteca/agregar_libro.html
# biblioteca/editar_libro.html
# biblioteca/eliminar_libro.html
# biblioteca/desactivar_libro.html
#Estos archivos contendran el codigo HTML para renderizar las vistas correspondientes.
#Se recomienda crear una plantilla master.html para heredar en las demas plantillas y mantener un diseño consistente.
#La plantilla master.html puede incluir el encabezado, pie de pagina y estilos comunes.