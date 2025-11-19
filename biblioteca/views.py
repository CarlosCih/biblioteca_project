from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from biblioteca.form import AutorForm, CategoriaForm, LibroForm
from biblioteca.models import Libro, Autor, Categoria
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url=reverse_lazy('inicio_sesion:login'))
#-- Vista para la pagina de inicio de la aplicacion biblioteca con un FBV(Function Based View) ---#
def index(request):
    return render(request, 'biblioteca/index.html')
#Nota: La ruta establecida dice que en la carpeta templates debe haber una carpeta llamada biblioteca que contenga el archivo index.html


class ListaLibrosView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Libro
    template_name = 'biblioteca/lista_libros.html'
    context_object_name = 'libros'
    ordering = ['titulo']
    paginate_by = 10  # Numero de libros por pagina

    #select_related para optimizar consultas a la base de datos, evitando consultas adicionales para autor y categoria
    def get_queryset(self):
        return Libro.objects.select_related('autor', 'categoria').exclude(categoria__nombre="Descontinuados").filter(disponible=True).order_by('titulo')

# Vista para ver los detalles de un libro
class DetalleLibroView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Libro
    template_name = 'biblioteca/detalle_libro.html'
    context_object_name = 'libro'
    pk_url_kwarg = 'libro_id'

# Vista para agregar un nuevo libro
class AgregarLibroView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('biblioteca:lista_libros')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Libro'
        return context

# Vista para editar un libro existente
class EditarLibroView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('biblioteca:lista_libros')
    pk_url_kwarg = 'libro_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Libro'
        return context

# Vista para eliminar un libro existente
class EliminarLibroView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Libro
    template_name = 'biblioteca/eliminar_libro.html'
    success_url = reverse_lazy('lista_libros')
    pk_url_kwarg = 'libro_id'
    context_object_name = 'libro'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Libro'
        return context

# Vista para un soft delete de un libro (marcar como no disponible)
class DesactivarLibroView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Libro
    template_name = 'biblioteca/desactivar_libro.html'
    success_url = reverse_lazy('biblioteca:lista_libros')
    pk_url_kwarg = 'libro_id'
    context_object_name = 'libro'
    fields = []  # No necesitamos campos porque solo cambiamos disponible
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Desactivar Libro'
        return context
    
    def form_valid(self, form):
        self.object.disponible = False
        self.object.save()
        return redirect(self.success_url)

#Vista de autores en CBV
class ListAutorView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Autor
    template_name = 'autores/lista_autores.html'
    context_object_name = 'autores'
    ordering = ['nombre']
    paginate_by = 10  # Numero de autores por pagina
    # Esta clase genera una vista para listar los autores con paginacion
class DetailAutorView(LoginRequiredMixin, DetailView): #esta clase genera una vista para ver los detalles de un autor y sus libros disponibles
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Autor
    template_name = 'autores/detalle_autor.html' 
    context_object_name = 'autor'

    #Esta funcion agrega al contexto los libros disponibles del autor
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        autor = self.get_object()
        contexto_libros = autor.libro_set.prefetch_related('categoria').filter(disponible=True).order_by('titulo')
        context['libros'] = contexto_libros
        return context
    
class EditAutorView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Autor
    form_class = AutorForm
    template_name = 'autores/autor_form.html'
    success_url = reverse_lazy('biblioteca:lista_autores') #se usa el namespace definido en urls.py
    pk_url_kwarg = 'autor_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Autor'
        return context

class AgregarAutorView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Autor
    form_class = AutorForm
    template_name = 'autores/autor_form.html'
    success_url = reverse_lazy('biblioteca:lista_autores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Autor'
        return context
    
class EliminarAutorView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Autor
    template_name = 'autores/eliminar_autor.html'
    success_url = reverse_lazy('biblioteca:lista_autores')
    pk_url_kwarg = 'autor_id'
    context_object_name = 'autor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Autor'
        return context

#Vista de categorias en CBV
class CategoriaListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Categoria
    template_name = 'categorias/lista_categorias.html'
    context_object_name = 'categorias'
    ordering = ['nombre']
    paginate_by = 3  # Numero de categorias por pagina

class AgregarCategoriaView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('biblioteca:lista_categorias')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Categoria'
        return context
class CategoriaDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Categoria
    template_name = 'categorias/detalle_categoria.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_libros = Libro.objects.filter(categoria=self.object, disponible=True).order_by('titulo')
        context['libros'] = contexto_libros
        return context
    
class EditarCategoriaView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('biblioteca:lista_categorias')
    pk_url_kwarg = 'categoria_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Categoria'
        return context
    
class EliminarCategoriaView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('inicio_sesion:login')
    redirect_field_name = 'next'
    model = Categoria
    template_name = 'categorias/eliminar_categoria.html'
    success_url = reverse_lazy('biblioteca:lista_categorias')
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

##
# Para denegar el acceso de usuarios no autentificados a las vistas, se utiliza diferentes metodos dependiendo si la estructura es FBV o CBV.
# En una funcion FBV se debe utilizar el decorador @login_required
# En cambio en una clase CBV se utiliza el mixin LoginRequiredMixin, que debe ser el primer mixin en la lista de herencia de la clase. 