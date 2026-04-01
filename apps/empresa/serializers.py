from rest_framework import serializers
from django.conf import settings
from .models import InfoEmpresa, MiembroEquipo, Valor, Estadistica

BASE_URL = 'https://cmxserver.curlew-vector.ts.net/cmx/media/'

class MiembroEquipoSerializer(serializers.ModelSerializer):
    foto = serializers.SerializerMethodField()
    
    class Meta:
        model = MiembroEquipo
        fields = ['id', 'nombre', 'rol', 'biografia', 'foto']
    
    def get_foto(self, obj):
        if obj.foto:
            if obj.foto.url.startswith('http'):
                return obj.foto.url
            return BASE_URL + str(obj.foto)
        return None

class ValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valor
        fields = ['id', 'titulo', 'descripcion']

class EstadisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadistica
        fields = ['id', 'etiqueta', 'valor']

class InfoEmpresaSerializer(serializers.ModelSerializer):
    historia_imagen = serializers.SerializerMethodField()
    equipo = serializers.SerializerMethodField()
    valores = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()

    class Meta:
        model = InfoEmpresa
        fields = [
            'hero_titulo', 'hero_descripcion', 
            'historia_titulo', 'historia_cuerpo', 'historia_imagen',
            'meta_titulo', 'meta_descripcion',
            'equipo', 'valores', 'stats'
        ]
    
    def get_historia_imagen(self, obj):
        if obj.historia_imagen:
            if obj.historia_imagen.url.startswith('http'):
                return obj.historia_imagen.url
            return BASE_URL + str(obj.historia_imagen)
        return None

    def get_equipo(self, obj):
        members = MiembroEquipo.objects.all()
        return MiembroEquipoSerializer(members, many=True).data

    def get_valores(self, obj):
        vals = Valor.objects.all()
        return ValorSerializer(vals, many=True).data

    def get_stats(self, obj):
        st = Estadistica.objects.all()
        return EstadisticaSerializer(st, many=True).data
