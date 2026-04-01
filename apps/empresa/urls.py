from django.urls import path
from .views import InfoEmpresaDetailView

urlpatterns = [
    path('info/', InfoEmpresaDetailView.as_view(), name='empresa-info'),
]
