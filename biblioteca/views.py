from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy

from biblioteca.form import AutorForm, CategoriaForm, LibroForm
from biblioteca.models import Libro, Autor, Categoria
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

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

#Vista de autores en CBV
class ListAutorView(ListView):
    model = Autor
    template_name = 'autores/lista_autores.html'
    context_object_name = 'autores'
    ordering = ['nombre']
    paginate_by = 10  # Numero de autores por pagina
    # Esta clase genera una vista para listar los autores con paginacion
class DetailAutorView(DetailView): #esta clase genera una vista para ver los detalles de un autor y sus libros disponibles
    model = Autor
    template_name = 'autores/detalle_autor.html' 
    context_object_name = 'autor'

    #Esta funcion agrega al contexto los libros disponibles del autor
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_libros = Libro.objects.filter(autor=self.object, disponible=True).order_by('titulo')
        context['libros'] = contexto_libros
        return context
    
class EditAutorView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autores/editar_autor.html'
    success_url = reverse_lazy('autores:lista_autores') 
    pk_url_kwarg = 'autor_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Autor'
        return context

class AgregarAutorView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autores/agregar_autor.html'
    success_url = reverse_lazy('autores:lista_autores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Autor'
        return context
    
class EliminarAutorView(DeleteView):
    model = Autor
    template_name = 'autores/eliminar_autor.html'
    success_url = reverse_lazy('autores:lista_autores')
    pk_url_kwarg = 'autor_id'
    context_object_name = 'autor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Autor'
        return context

#Vista de categorias en CBV
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias/lista_categorias.html'
    context_object_name = 'categorias'
    ordering = ['nombre']
    paginate_by = 10  # Numero de categorias por pagina

class AgregarCategoriaView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/agregar_categoria.html'
    success_url = reverse_lazy('categorias:lista_categorias')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Categoria'
        return context
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categorias/detalle_categoria.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_libros = Libro.objects.filter(categoria=self.object, disponible=True).order_by('titulo')
        context['libros'] = contexto_libros
        return context
    
class EditarCategoriaView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/editar_categoria.html'
    success_url = reverse_lazy('categorias:lista_categorias')
    pk_url_kwarg = 'categoria_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Categoria'
        return context
    
class EliminarCategoriaView(DeleteView):
    model = Categoria
    template_name = 'categorias/eliminar_categoria.html'
    success_url = reverse_lazy('categorias:lista_categorias')
    pk_url_kwarg = 'categoria_id'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Categoria'
        return context
#Vista de categorias en CBV

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