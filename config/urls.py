from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cmx_admin_login(request):
    next_url = request.GET.get('next', '/cmx/admin/')
    error = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '/cmx/admin/')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            error = 'Usuario o contraseña incorrectos'
    
    return render(request, 'cmx_login.html', {'next': next_url, 'error': error})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/catalogo/', include('apps.catalogo.urls')),
    path('api/empresa/', include('apps.empresa.urls')),
    path('api/contacto/', include('apps.contacto.urls')),
    
    # CMX prefixed routes
    path('cmx/admin/login/', cmx_admin_login, name='cmx_admin_login'),
    path('cmx/admin/', admin.site.urls),
    path('cmx/api/catalogo/', include('apps.catalogo.urls')),
    path('cmx/api/empresa/', include('apps.empresa.urls')),
    path('cmx/api/contacto/', include('apps.contacto.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
