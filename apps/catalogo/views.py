from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_object_or_404
from .models import Categoria, Producto
from .serializers import (
    CategoriaSerializer, 
    ProductoListSerializer, 
    ProductoDetalleSerializer
)

class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    lookup_field = 'slug'

class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.filter(disponible=True)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductoDetalleSerializer
        return ProductoListSerializer

    @action(detail=False, methods=['get'], url_path='por-sku/(?P<sku>[^/.]+)')
    def por_sku(self, request, sku=None):
        """Permite buscar un producto directamente por su SKU (Útil para técnicos)"""
        producto = get_object_or_404(Producto, sku=sku, disponible=True)
        serializer = ProductoDetalleSerializer(producto, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='relacionados/(?P<categoria_slug>[^/.]+)')
    def relacionados(self, request, categoria_slug=None):
        """Retorna productos de la misma categoría para cross-selling"""
        productos = Producto.objects.filter(
            categoria__slug=categoria_slug, 
            disponible=True
        ).exclude(slug=request.query_params.get('exclude', ''))[:4]
        serializer = ProductoListSerializer(productos, many=True, context={'request': request})
        return Response(serializer.data)
