from django.db import models

class InfoEmpresa(models.Model):
    """Información general de la empresa (Singleton)"""
    hero_titulo = models.CharField(max_length=200, default="Ingeniería real para problemas reales.")
    hero_descripcion = models.TextField(help_text="Texto principal bajo el título")
    historia_titulo = models.CharField(max_length=200, default="Nuestra misión en la planta")
    historia_cuerpo = models.TextField(help_text="Relato cercano sobre cómo nació Control Modular MX")
    historia_imagen = models.ImageField(upload_to='empresa/', blank=True, null=True, help_text="Imagen lateral de la sección historia")
    
    # Metadatos para SEO
    meta_titulo = models.CharField(max_length=70, blank=True)
    meta_descripcion = models.CharField(max_length=160, blank=True)

    class Meta:
        verbose_name = "Información de la Empresa"
        verbose_name_plural = "Información de la Empresa"

    def __str__(self):
        return "Configuración de Nosotros"

class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, help_text="Pequeña descripción humana")
    foto = models.ImageField(upload_to='equipo/', blank=True, null=True)
    orden = models.PositiveIntegerField(default=0, help_text="Para decidir quién sale primero")

    class Meta:
        verbose_name = "Miembro del Equipo"
        verbose_name_plural = "Miembros del Equipo"
        ordering = ['orden']

    def __str__(self):
        return f"{self.nombre} - {self.rol}"

class Valor(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Valor de la Empresa"
        verbose_name_plural = "Valores de la Empresa"
        ordering = ['orden']

    def __str__(self):
        return self.titulo

class Estadistica(models.Model):
    etiqueta = models.CharField(max_length=100, help_text="Ej: Proyectos Industriales")
    valor = models.CharField(max_length=50, help_text="Ej: +50")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.etiqueta}: {self.valor}"
