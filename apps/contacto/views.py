from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contacto
from .serializers import ContactoSerializer

class ContactoCreateView(APIView):
    """Endpoint para recibir mensajes de contacto"""
    
    def post(self, request):
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            contacto = serializer.save()
            return Response(
                {'mensaje': 'Mensaje recibido correctamente', 'id': contacto.id},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
