from django.db import models
from django.utils import timezone

class Contacto(models.Model):
    OPCIONES_SERVICIO = [
        ('hardware', 'Desarrollo de Hardware (PCB)'),
        ('software', 'Software Industrial / Nube'),
        ('domotica', 'Domótica y Control de Accesos'),
        ('3d', 'Diseño e Impresión 3D'),
        ('soporte', 'Mantenimiento o Soporte'),
        ('otro', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True)
    servicio = models.CharField(max_length=20, choices=OPCIONES_SERVICIO, default='otro')
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    leido = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-fecha']
        
    def __str__(self):
        return f"{self.nombre} - {self.get_servicio_display()}"
