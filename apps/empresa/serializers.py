from rest_framework import serializers
from .models import InfoEmpresa, MiembroEquipo, Valor, Estadistica

class MiembroEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiembroEquipo
        fields = ['id', 'nombre', 'rol', 'biografia', 'foto']

class ValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valor
        fields = ['id', 'titulo', 'descripcion']

class EstadisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadistica
        fields = ['id', 'etiqueta', 'valor']

class InfoEmpresaSerializer(serializers.ModelSerializer):
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

    def get_equipo(self, obj):
        members = MiembroEquipo.objects.all()
        return MiembroEquipoSerializer(members, many=True, context=self.context).data

    def get_valores(self, obj):
        vals = Valor.objects.all()
        return ValorSerializer(vals, many=True).data

    def get_stats(self, obj):
        st = Estadistica.objects.all()
        return EstadisticaSerializer(st, many=True).data
