# CMX-SITE-BACKEND | Control Modular MX

Este proyecto es el núcleo administrativo y la API REST para la plataforma industrial de **Control Modular MX**. Construido con **Django 5.0** y **Django REST Framework**, siguiendo una arquitectura modular y escalable para servicios de ingeniería.

---

## 🛠 Arquitectura del Proyecto

El backend está diseñado de forma modular para separar la configuración del núcleo de la lógica de negocio:

*   **`config/`**: Ajustes globales del sistema, URLs maestras y configuración de seguridad.
*   **`apps/`**: Directorio raíz para todas las aplicaciones funcionales.
    *   **`catalogo/`**: Gestión de productos, SEO técnico, especificaciones y compatibilidad industrial.
*   **`media/`**: Almacenamiento local de imágenes de productos y catálogos (configurado para desarrollo).

---

## 🔑 Credenciales de Desarrollo (ACCESO TOTAL)

> **NOTA:** Estas credenciales son únicamente para el entorno de desarrollo y serán revocadas al pasar a producción.

*   **Panel Administrativo:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
*   **Usuario:** `cmx`
*   **Contraseña:** `cmx*123`

---

## 🏗 Modelo de Datos (Enfoque SEO Industrial)

El catálogo de productos está optimizado para capturar tráfico técnico mediante:

1.  **Tablas de Producto:** Slugs automáticos para URLs amigables y metadatos específicos (Title, Description) por ítem.
2.  **Tabla de Compatibilidad:** Almacenamiento de modelos de maquinaria (ej: Bizerba GSP H) y Números de Parte OEM (ej: 603 85 07 51 02) para aparecer en búsquedas específicas de refacciones.
3.  **Especificaciones Dinámicas:** Permite añadir cualquier dato técnico sin cambiar la base de datos.
4.  **Galería SEO:** Cada imagen cuenta con `alt_text` para indexar correctamente en Google Images.

---

## 🚀 Comandos Rápidos

**Correr el servidor:**
```bash
python manage.py runserver
```

**Aplicar cambios en la DB:**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🌐 Configuración de Red y CORS

Para facilitar el desarrollo con el frontend en **Next.js**, se ha configurado:
*   `CORS_ALLOW_ALL_ORIGINS = True`: Permite peticiones desde cualquier origen (local o externo).
*   `ALLOWED_HOSTS = ['*']`: Permite que el servidor responda en cualquier IP pública del servidor Ubuntu.

---

## 📝 Próximos Pasos (Roadmap)
1.  **API Serializers:** Crear los serializadores para convertir los modelos de productos en JSON.
2.  **Endpoints Públicos:** Exponer los productos para que el Frontend en Next.js los consuma.
3.  **CRM de Leads:** Crear la app para gestionar formularios de contacto y cotizaciones.
