from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'servicio', 'fecha', 'leido']
    list_filter = ['servicio', 'leido', 'fecha']
    search_fields = ['nombre', 'email', 'empresa', 'mensaje']
    readonly_fields = ['fecha']
    ordering = ['-fecha']
    
    actions = ['marcar_como_leido']
    
    @admin.action(description='Marcar como leído')
    def marcar_como_leido(self, request, queryset):
        queryset.update(leido=True)
