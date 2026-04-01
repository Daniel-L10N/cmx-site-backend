from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InfoEmpresa
from .serializers import InfoEmpresaSerializer

class InfoEmpresaDetailView(APIView):
    """Retorna toda la información necesaria para la página de Nosotros"""
    def get(self, request):
        info = InfoEmpresa.objects.first()
        if not info:
            # Crear uno por defecto si no existe
            info = InfoEmpresa.objects.create(
                hero_descripcion="Ingeniería técnica honesta.",
                historia_cuerpo="Empezamos resolviendo problemas en sitio."
            )
        serializer = InfoEmpresaSerializer(info, context={'request': request})
        return Response(serializer.data)
