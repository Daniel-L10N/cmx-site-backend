# CMX-SITE-BACKEND - Configuración de Despliegue

Este documento describe la configuración necesaria para desplegar el backend en producción con el prefijo de URL `/cmx/`.

---

## Requisitos

```bash
pip install Django djangorestframework django-cors-headers gunicorn Pillow python-dotenv
```

---

## Cambios en el Código

### 1. `config/settings.py`

Agregar al final del archivo:

```python
CSRF_TRUSTED_ORIGINS = [
    'https://cmxserver.curlew-vector.ts.net',
    'http://cmxserver.curlew-vector.ts.net',
    'https://controlmodularmx.com',
    'https://www.controlmodularmx.com',
    'https://api.controlmodularmx.com',
]

FORCE_SCRIPT_NAME = '/cmx'
```

**Nota:** Agregar los dominios de producción correspondientes.

### 2. `config/urls.py`

Agregar imports y la función de login:

```python
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
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            error = 'Usuario o contraseña incorrectos'
    return render(request, 'cmx_login.html', {'next': next_url, 'error': error})
```

Agregar las rutas prefixed en `urlpatterns`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/catalogo/', include('apps.catalogo.urls')),
    path('cmx/admin/login/', cmx_admin_login),
    path('cmx/admin/', admin.site.urls),
    path('cmx/api/catalogo/', include('apps.catalogo.urls')),
]
```

### 3. `templates/cmx_login.html`

Crear este archivo con el formulario de login custom:

```html
<!DOCTYPE html>
<html lang="es-mx">
<head>
    <meta charset="UTF-8">
    <title>Login - CMX Admin</title>
    <style>
        body { font-family: sans-serif; background: #f5f5f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 100%; max-width: 400px; }
        h1 { text-align: center; color: #333; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 5px; color: #555; font-weight: 500; }
        input { width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; font-size: 14px; }
        button { width: 100%; padding: 12px; background: #1a73e8; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        button:hover { background: #1557b0; }
        .error { color: #d32f2f; margin-bottom: 15px; text-align: center; }
    </style>
</head>
<body>
    <div class="login-box">
        <h1>CMX Admin</h1>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
        <form action="/cmx/admin/login/" method="post">
            {% csrf_token %}
            <input type="hidden" name="next" value="{{ next|default:'/cmx/admin/' }}">
            <div class="form-group">
                <label>Usuario</label>
                <input type="text" name="username" required autofocus>
            </div>
            <div class="form-group">
                <label>Contraseña</label>
                <input type="password" name="password" required>
            </div>
            <button type="submit">Ingresar</button>
        </form>
    </div>
</body>
</html>
```

### 4. `apps/core/middleware.py`

Crear el directorio `apps/core/` y el archivo:

```python
class DisableCSRFForAdmin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response
```

En `config/settings.py`, agregar a `MIDDLEWARE`:

```python
MIDDLEWARE = [
    # ... middleware existente ...
    'apps.core.middleware.DisableCSRFForAdmin',
]
```

---

## Pasos de Despliegue

```bash
# 1. Clonar y entrar al proyecto
cd /var/www/cmx
git pull origin main

# 2. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
pip install gunicorn

# 4. Migrar base de datos
python manage.py migrate

# 5. Recolectar archivos estáticos
python manage.py collectstatic --noinput

# 6. Reiniciar servicio
sudo systemctl restart cmx-backend
```

---

## URLs de Acceso

| Servicio | URL |
|----------|-----|
| Admin | `https://dominio.com/cmx/admin/` |
| Login | `https://dominio.com/cmx/admin/login/` |
| API | `https://dominio.com/cmx/api/catalogo/` |

---

## Credenciales (Desarrollo)

- **Usuario:** `cmx`
- **Contraseña:** `cmx*123`

**IMPORTANTE:** Cambiar estas credenciales en producción.
