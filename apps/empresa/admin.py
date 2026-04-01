from django.contrib import admin
from .models import InfoEmpresa, MiembroEquipo, Valor, Estadistica

@admin.register(InfoEmpresa)
class InfoEmpresaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_titulo', 'hero_descripcion')
        }),
        ('Nuestra Historia', {
            'fields': ('historia_titulo', 'historia_cuerpo', 'historia_imagen')
        }),
        ('SEO', {
            'fields': ('meta_titulo', 'meta_descripcion')
        }),
    )
    def has_add_permission(self, request):
        # Evita crear más de una configuración global
        return not InfoEmpresa.objects.exists()

@admin.register(MiembroEquipo)
class MiembroEquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol', 'orden')
    list_editable = ('orden',)

@admin.register(Valor)
class ValorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden')
    list_editable = ('orden',)

@admin.register(Estadistica)
class EstadisticaAdmin(admin.ModelAdmin):
    list_display = ('etiqueta', 'valor', 'orden')
    list_editable = ('orden',)
