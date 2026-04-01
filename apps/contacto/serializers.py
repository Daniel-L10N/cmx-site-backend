from rest_framework import serializers
from .models import Contacto

class ContactoSerializer(serializers.ModelSerializer):
    servicio_display = serializers.CharField(source='get_servicio_display', read_only=True)
    
    class Meta:
        model = Contacto
        fields = ['id', 'nombre', 'empresa', 'email', 'telefono', 'servicio', 'servicio_display', 'mensaje', 'fecha', 'leido']
        read_only_fields = ['fecha', 'leido']
    
    def create(self, validated_data):
        contacto = Contacto.objects.create(**validated_data)
        return contacto
