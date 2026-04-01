from rest_framework import serializers
from .models import Categoria, Producto, Especificacion, ImagenProducto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'slug', 'descripcion_seo', 'imagen_portada']

class EspecificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especificacion
        fields = ['clave', 'valor']

class ImagenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = ['imagen', 'alt_text', 'es_principal']

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
            request = self.context.get('request')
            return request.build_absolute_uri(img.imagen.url) if request else img.imagen.url
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
