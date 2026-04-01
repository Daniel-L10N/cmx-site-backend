from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
    slug = models.SlugField(unique=True, help_text="URL amigable para SEO")
    descripcion_seo = models.TextField(blank=True, help_text="Meta descripción para buscadores")
    imagen_portada = models.ImageField(upload_to='categorias/', blank=True, null=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    STOCK_STATUS = [
        ('disponible', 'Disponible'),
        ('bajo_pedido', 'Bajo Pedido'),
        ('agotado', 'Agotado'),
    ]

    # Relaciones y Identificación
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    slug = models.SlugField(unique=True, help_text="URL amigable para SEO (ej: tarjeta-rebanadora-bizerba)")
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU / Código Interno")
    
    # Precios y Stock
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio (MXN)")
    moneda = models.CharField(max_length=3, default='MXN')
    estado_stock = models.CharField(max_length=20, choices=STOCK_STATUS, default='disponible')
    disponible = models.BooleanField(default=True, verbose_name="Activo en el sitio")
    
    # SEO y Contenido
    meta_titulo = models.CharField(max_length=70, blank=True, help_text="Título SEO (Máx 70 caracteres)")
    meta_descripcion = models.CharField(max_length=160, blank=True, help_text="Meta descripción SEO (Máx 160 caracteres)")
    descripcion_corta = models.TextField(max_length=500, help_text="Extracto para listados")
    descripcion_detallada = models.TextField(help_text="Descripción técnica enriquecida")
    
    # Datos Técnicos (JSON para flexibilidad en modelos y números de parte)
    modelos_compatibles = models.JSONField(default=list, help_text="Ej: ['GSP H', 'H33']")
    numeros_parte_oem = models.JSONField(default=list, help_text="Ej: ['603 85 07 51 02']")
    
    # Auditoría
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.sku} - {self.nombre}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

class Especificacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='especificaciones')
    clave = models.CharField(max_length=50, help_text="Ej: Voltaje, Material, Protección")
    valor = models.CharField(max_length=100, help_text="Ej: 110V, FR4 Militar, IP65")

    class Meta:
        verbose_name = "Especificación Técnica"
        verbose_name_plural = "Especificaciones Técnicas"

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/')
    alt_text = models.CharField(max_length=200, help_text="Texto descriptivo para Google Images (SEO)")
    es_principal = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Imagen de Producto"
        verbose_name_plural = "Imágenes de Productos"
