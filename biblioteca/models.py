from django.db import models

#creacion de modelos relacionados los otros modelos de la aplicacion biblioteca
class Autor(models.Model):
    nombre=models.CharField(max_length=100)
    year=models.IntegerField()
    nacionalidad=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()

    def __str__(self):
        return self.nombre

#Modelo para representar un libro en la bliblioteca
class Libro(models.Model):
    titulo=models.CharField(max_length=200)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE) #Relacion muchos a uno con el modelo Autor
    fecha_publicacion=models.DateField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) #Relacion muchos a uno con el modelo Categoria
    isbn=models.CharField(max_length=13, unique=True)
    paginas=models.IntegerField(default=0)
    precio=models.DecimalField(max_digits=6, decimal_places=2, default=0.00) #max_digits incluye los decimales, decimal_places es la cantidad de decimales. Es decir, 9999.99 es un max_digits de 6 y decimal_places de 2 
    disponible=models.BooleanField(default=True)


    def __str__(self):
        return self.titulo

class Review(models.Model):
    libro=models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    user_review=models.CharField(max_length=100) #En un futuro esto puede ser una relacion con un modelo Usuario
    comentario=models.TextField()
    calificacion = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 estrellas
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.user_review} para {self.libro.titulo}"
    class Meta:
        ordering = ['-fecha']  # Ordenar por fecha descendente
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'

#futuro modelo para representar un usuario de la biblioteca
#class Usuario(models.Model):
#    nombre=models.CharField(max_length=100)
#    email=models.EmailField(unique=True)
#
#    def __str__(self):
#        return self.nombre

