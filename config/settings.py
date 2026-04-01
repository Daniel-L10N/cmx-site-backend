import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- CONFIGURACIÓN DE SEGURIDAD DINÁMICA ---
# Cambia PRODUCTION a True en tu servidor de la nube
PRODUCTION = os.getenv('PRODUCTION', 'False') == 'True'

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-cmx-site-backend-key-change-this')

DEBUG = not PRODUCTION

CSRF_TRUSTED_ORIGINS = [
    'https://cmxserver.curlew-vector.ts.net',
    'http://cmxserver.curlew-vector.ts.net',
    'https://controlmodularmx.com',
    'https://www.controlmodularmx.com',
    'https://api.controlmodularmx.com',
]

FORCE_SCRIPT_NAME = '/cmx'

if PRODUCTION:
    ALLOWED_HOSTS = ['cmxserver.curlew-vector.ts.net', 'api.controlmodularmx.com', 'controlmodularmx.com', 'localhost']
    # Seguridad de Cookies y SSL
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000 # 1 año
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
else:
    ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Terceros
    'rest_framework',
    'corsheaders',
    
    # Propias
    'apps.catalogo',
    'apps.empresa',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Debe ir arriba
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.core.middleware.DisableCSRFForAdmin',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },
]

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- CONFIGURACIÓN CORS (MODO PRODUCCIÓN VS DESARROLLO) ---
if PRODUCTION:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = [
        "https://controlmodularmx.com",
        "https://www.controlmodularmx.com",
        "https://controlmodularmx.vercel.app",
    ]
else:
    CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

FORCE_SCRIPT_NAME = '/cmx'
