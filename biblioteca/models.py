from django.db import models

# Create your models here.

#Modelo para representar un libro en la bliblioteca
class Libro(models.Model):
    titulo=models.CharField(max_length=200)
    autor=models.CharField(max_length=100)
    fecha_publicacion=models.DateField()
    isbn=models.CharField(max_length=13, unique=True)
    disponible=models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
