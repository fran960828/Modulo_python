

## 1. Gestión de Imágenes con `ImageField` y Pillow

> **Explicación:** `ImageField` es un campo especializado que hereda de `FileField` pero añade validaciones específicas para asegurar que el archivo subido sea realmente una imagen. Para que Django pueda procesar los metadatos de las imágenes (ancho, alto, formato), es obligatorio instalar la librería **Pillow**.

**Instalación:**

```bash
pip install Pillow

```

**Ejemplo en `models.py`:**

```python
from django.db import models

class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    # upload_to crea subcarpetas dentro de MEDIA_ROOT
    foto = models.ImageField(upload_to='perfiles/', null=True, blank=True)

```

---

## 2. Optimización con `django-thumbnails`

> **Explicación:** Cargar una imagen de 5MB para mostrar un icono de 50px es un error grave de rendimiento. `django-thumbnails` permite definir "tamaños preestablecidos" en la configuración. Cuando subes una imagen, la librería genera versiones pequeñas (miniaturas) optimizadas.

**Instalación:**

```bash
pip install django-thumbnails

```

**Configuración en `settings.py`:**

```python
INSTALLED_APPS = [
    # ...
    'thumbnails',
]

# Definimos los tamaños que usaremos en toda la web
THUMBNAILS = {
    'METADATA': {
        'PREFIX': 'thumb_',
    },
    'SIZES': {
        'pequeno': {
            'PROCESSORS': [
                {'name': 'resize', 'width': 100, 'height': 100, 'method': 'fit'},
                {'name': 'crop', 'width': 100, 'height': 100},
            ],
        },
        'tarjeta': {
            'PROCESSORS': [
                {'name': 'resize', 'width': 400, 'height': 300, 'method': 'fill'},
            ],
        },
    }
}

```

**Uso del campo especializado en el Modelo:**

```python
from thumbnails.fields import ImageField # Importamos el campo de la librería

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    # Este campo se encarga de gestionar las miniaturas automáticamente
    imagen_portada = ImageField(upload_to='articulos/')

```

**Limpieza de Caché:**
Si cambias los tamaños en `settings.py`, las imágenes viejas no se actualizarán solas. Debes borrar las miniaturas generadas para que se vuelvan a crear con el nuevo tamaño:

```bash
python manage.py delete_thumbnails

```

---

## 3. La evolución: `django-pictures`

> **Explicación:** Mientras que las miniaturas tradicionales crean un archivo estático, `django-pictures` permite implementar imágenes **responsive** modernas (etiquetas `<picture>`) y formatos de última generación como **WebP** y **AVIF**, que pesan un 30% menos que el JPG.

**Instalación y Configuración:**

```bash
pip install django-pictures

```

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'pictures',
]

PICTURES = {
    'BREAKPOINTS': {
        'mob': 576,
        'desktop': 1200,
    },
    'GRID_COLUMNS': 12,
    'CONTAINER_WIDTH': 1200,
    'FILE_TYPES': ['WEBP', 'AVIF'], # Formatos de alta compresión
}

```

---

## 4. Contenido Enriquecido con `django-ckeditor`

> **Explicación:** Un `TextField` normal es aburrido. `django-ckeditor` transforma ese cuadro de texto en un editor tipo Word (negritas, listas, enlaces, imágenes) dentro del panel de administrador.

**Instalación:**

```bash
pip install django-ckeditor

```

**Configuración en `settings.py`:**

```python
INSTALLED_APPS = [
    # ...
    'ckeditor',
    'ckeditor_uploader', # Opcional: para subir imágenes dentro del editor
]

# Configuración básica del editor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': '100%',
    },
}

```

**Cambio en `models.py`:**

```python
from django.db import models
from ckeditor.fields import RichTextField # Importamos el campo enriquecido

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    # Sustituimos models.TextField por RichTextField
    cuerpo = RichTextField(verbose_name="Contenido de la noticia")

```

---

## 5. El filtro `safe` y Renderizado de HTML

> **Explicación:** Por seguridad, Django "escapa" el HTML (muestra las etiquetas `<p>` como texto plano). Como CKEditor guarda código HTML real en la base de datos, debemos decirle a la plantilla que ese código es seguro para ser ejecutado por el navegador.

**Uso en el Template:**

```html
<article>
    <h1>{{ noticia.titulo }}</h1>
    
    <div class="noticia-body">
        {{ noticia.cuerpo|safe }}
    </div>
</article>

```

---

## 6. Preparación para Producción: `collectstatic`

> **Explicación:** En desarrollo, Django busca los archivos estáticos de las librerías (como el CSS de CKEditor o del Admin) en muchas carpetas diferentes. En producción, esto es ineficiente. El comando `collectstatic` busca todos esos archivos y los copia en una sola carpeta centralizada llamada `STATIC_ROOT`.

**Configuración previa en `settings.py`:**

```python
# Carpeta donde se reunirá todo para el servidor real (Nginx/Apache)
STATIC_ROOT = BASE_DIR / 'staticfiles'

```

**Ejecución en la terminal:**

```bash
python manage.py collectstatic

```

*Django te dirá: "¿Deseas sobreescribir los archivos?". Escribes `yes`. Ahora verás una carpeta nueva llamada `staticfiles` con todo el CSS/JS del Admin y los plugins.*

---

### Resumen de flujo profesional:

1. Instalas **Pillow** para manejar imágenes.
2. Usas **Thumbnails** o **Pictures** para no destruir el ancho de banda del usuario.
3. Implementas **CKEditor** para que los editores de contenido puedan dar formato.
4. En el HTML usas **`|safe`** para que el diseño del editor se respete.
5. Antes de subir a internet, ejecutas **`collectstatic`** para que el servidor encuentre los estilos del editor.

