from django.dispatch import receiver
from biblioteca.models import Libro, Review
from django.db.models.signals import post_save

@receiver(post_save, sender=Libro)
def notify_new_book(sender, instance, created, **kwargs):
    """Cuando se crea un nuevo libro, esta señal puede ser utilizada para notificar a los administradores."""
    if created:
        # Aquí podrías agregar la lógica para enviar un correo electrónico o una notificación
        print(f'Nuevo libro agregado: {instance.titulo} por {instance.autor}')
        # Por ejemplo, enviar un correo electrónico a los administradores
        # send_email_to_admins(f'Nuevo libro agregado: {instance.titulo} por {instance.autor}')

@receiver(post_save, sender=Libro)
def crear_review_inicial(sender, instance, created, **kwargs):
    """Crea una reseña inicial para un libro nuevo."""
    if created:
        Review.objects.create(
            libro=instance,
            user_review='Sistema',
            comentario='Esta es una reseña inicial para el libro.',
            calificacion=3
        )
        print(f'Reseña inicial creada para el libro: {instance.titulo}')