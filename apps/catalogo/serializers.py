from rest_framework import serializers
from .models import Categoria, Producto, Especificacion, ImagenProducto

BASE_URL = 'https://cmxserver.curlew-vector.ts.net/cmx/media/'

def build_media_url(relative_url):
    """Construye URL absoluta con HTTPS"""
    if not relative_url:
        return None
    if relative_url.startswith('http'):
        return relative_url
    return BASE_URL + relative_url

class CategoriaSerializer(serializers.ModelSerializer):
    imagen_portada = serializers.SerializerMethodField()
    
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'slug', 'descripcion_seo', 'imagen_portada']
    
    def get_imagen_portada(self, obj):
        return build_media_url(str(obj.imagen_portada)) if obj.imagen_portada else None

class EspecificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especificacion
        fields = ['clave', 'valor']

class ImagenProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()
    
    class Meta:
        model = ImagenProducto
        fields = ['imagen', 'alt_text', 'es_principal']
    
    def get_imagen(self, obj):
        return build_media_url(str(obj.imagen)) if obj.imagen else None

class ProductoListSerializer(serializers.ModelSerializer):
    """Serializer ligero para listados de productos"""
    imagen_principal = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'slug', 'sku', 'precio', 'moneda', 'estado_stock', 'imagen_principal', 'descripcion_corta']

    def get_imagen_principal(self, obj):
        img = obj.imagenes.filter(es_principal=True).first()
        if not img:
            img = obj.imagenes.first()
        if img:
            return build_media_url(str(img.imagen))
        return None

class ProductoDetalleSerializer(serializers.ModelSerializer):
    """Serializer robusto para la página de detalle (SEO Agresivo)"""
    categoria = CategoriaSerializer(read_only=True)
    especificaciones = EspecificacionSerializer(many=True, read_only=True)
    imagenes = ImagenProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id', 'categoria', 'nombre', 'slug', 'sku', 'precio', 'moneda', 
            'estado_stock', 'meta_titulo', 'meta_descripcion', 
            'descripcion_corta', 'descripcion_detallada', 
            'modelos_compatibles', 'numeros_parte_oem',
            'especificaciones', 'imagenes', 'fecha_actualizacion'
        ]
