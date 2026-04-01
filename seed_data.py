from apps.catalogo.models import Categoria, Producto, Especificacion

def run():
    # 1. Crear Categoría
    cat, _ = Categoria.objects.get_or_create(
        nombre="Tarjetas Electrónicas",
        slug="tarjetas-electronicas",
        defaults={
            "descripcion_seo": "Refacciones electrónicas y tarjetas de control industrial de alta precisión."
        }
    )

    # 2. Crear Producto (Tarjeta Bizerba)
    prod, created = Producto.objects.get_or_create(
        categoria=cat,
        sku="CMX-BIZ-603",
        defaults={
            "nombre": "Tarjeta de Control Maestro para Rebanadora Bizerba (Serie GSP)",
            "slug": "tarjeta-rebanadora-bizerba",
            "precio": 7499.00,
            "meta_titulo": "Tarjeta de Control para Rebanadora Bizerba | Reemplazo Premium | Control Modular MX",
            "meta_descripcion": "Tarjeta electrónica industrial compatible con Bizerba GSP H, H33. Reemplazo de alto rendimiento (P/N: 603 85 07 51 02).",
            "descripcion_corta": "Nuestra solución estrella para rebanadoras industriales Bizerba. Elimina el tiempo de espera por refacciones de importación.",
            "descripcion_detallada": "Diseño de ingeniería avanzada que supera las especificaciones del fabricante original. Nuestra tarjeta está protegida contra picos de voltaje y humedad.",
            "modelos_compatibles": ["GSP H", "GSP H33", "GSP V", "VS12"],
            "numeros_parte_oem": ["603 85 07 51 02", "603.85.075.102"]
        }
    )

    # 3. Añadir Especificaciones
    if created:
        Especificacion.objects.create(producto=prod, clave="Voltaje", valor="110V / 220V Auto-switch")
        Especificacion.objects.create(producto=prod, clave="Garantía", valor="12 meses")
        Especificacion.objects.create(producto=prod, clave="Protección", valor="Capa Conformal Coating")
        print(f"Producto '{prod.nombre}' creado exitosamente.")
    else:
        print(f"El producto '{prod.nombre}' ya existe.")

if __name__ == "__main__":
    run()
