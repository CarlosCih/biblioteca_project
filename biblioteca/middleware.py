import time
import logging

logger = logging.getLogger(__name__)# Configura el logger para este módulo

class RequestLoggingMiddleware:
    """
    Middleware que registra el tiempo de procesamiento de cada solicitud.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time() # Tiempo de inicio de la solicitud
        response = self.get_response(request) # Procesa la solicitud
        duration = time.time() - start_time # Calcula la duración de la solicitud

        logger.info(f"Request: {request.method} {request.path} completed in {duration:.4f} seconds.") # Registra la información de la solicitud

        response['x-Request-Duration'] = f"{duration:.4f}s" # Agrega la duración al encabezado de la respuesta

        return response