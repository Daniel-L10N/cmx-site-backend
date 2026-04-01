from django.contrib import admin
from .models import Categoria, Producto, Especificacion, ImagenProducto

class EspecificacionInline(admin.TabularInline):
    model = Especificacion
    extra = 1

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'categoria', 'precio', 'estado_stock', 'disponible')
    list_filter = ('categoria', 'estado_stock', 'disponible')
    search_fields = ('nombre', 'sku', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}
    inlines = [EspecificacionInline, ImagenProductoInline]
    
    fieldsets = (
        ('Identificación', {
            'fields': ('categoria', 'nombre', 'slug', 'sku')
        }),
        ('Precio y Stock', {
            'fields': ('precio', 'moneda', 'estado_stock', 'disponible')
        }),
        ('Contenido SEO', {
            'fields': ('meta_titulo', 'meta_descripcion', 'descripcion_corta', 'descripcion_detallada')
        }),
        ('Datos Técnicos', {
            'fields': ('modelos_compatibles', 'numeros_parte_oem'),
            'description': "Ingresa listas en formato JSON, ej: ['GSP H', 'H33']"
        }),
    )
