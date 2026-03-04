## 1. Diferencia entre Static y Media

> **Explicación:** > - **Static Files:** Son los archivos que tú, como programador, incluyes para que la web funcione y se vea bien (CSS, JavaScript, el logo de la empresa, fuentes). Se despliegan junto con el código.
> * **Media Files:** Son archivos que suben los usuarios a través de formularios (la foto de perfil de un usuario, un PDF con un currículum, una imagen de una serie). Django no sabe qué archivos habrá aquí hasta que la web está funcionando.
> 
> 

---

## 2. Configuración de Archivos Estáticos (Static)

> **Explicación:** Para usar CSS o imágenes fijas, necesitamos decirle a Django dos cosas:
> 1. `STATIC_URL`: La dirección pública en el navegador (ej. `/static/`).
> 2. `STATICFILES_DIRS`: La carpeta física en tu ordenador donde guardas esos archivos durante el desarrollo.
> 
> 

**Configuración en `settings.py`:**

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# La URL que se verá en el navegador
STATIC_URL = 'static/'

# Carpeta física en la raíz del proyecto donde pones tus CSS/JS/Logos
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

```

**Uso en el Template:**

```html
{% load static %} <link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'img/logo_empresa.png' %}" alt="Logo">

```

---

## 3. Configuración de Archivos de Usuario (Media)

> **Explicación:** Al igual que con static, necesitamos configurar el acceso.
> 1. `MEDIA_URL`: URL pública para acceder a los archivos subidos (ej. `/media/`).
> 2. `MEDIA_ROOT`: La ruta absoluta en el sistema donde Django guardará físicamente los archivos.
> 
> 

**Configuración en `settings.py`:**

```python
# URL pública para acceder a los archivos
MEDIA_URL = '/media/'

# Ruta física donde se guardarán los archivos subidos
# Se creará una carpeta llamada 'media' en la raíz de tu proyecto
MEDIA_ROOT = BASE_DIR / 'media'

```

---

## 4. Uso de `FileField` e `ImageField` en Modelos

> **Explicación:** Para que un usuario pueda subir un archivo, usamos `FileField` (para cualquier archivo) o `ImageField` (específico para imágenes, requiere instalar la librería `Pillow`). El parámetro `upload_to` crea subcarpetas automáticamente dentro de `MEDIA_ROOT`.

**Ejemplo en `models.py`:**

```python
from django.db import models

class Capitulo(models.Model):
    nombre = models.CharField(max_length=100)
    # El archivo se guardará en: media/capitulos/pdf/archivo.pdf
    documento_guion = models.FileField(upload_to='capitulos/pdf/', null=True, blank=True)
    # La imagen se guardará en: media/capitulos/portadas/imagen.jpg
    portada = models.ImageField(upload_to='capitulos/portadas/', null=True, blank=True)

```

---

## 5. Habilitar el acceso en desarrollo (`urls.py`)

> **Explicación:** Por seguridad, Django no sirve archivos de imagen o documentos automáticamente. Durante el desarrollo (cuando `DEBUG = True`), debemos indicarle manualmente que "conecte" la URL de media con la carpeta física.

**Configuración en `urls.py` principal:**

```python
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
]

# Solo añadimos esto si estamos en modo desarrollo
if settings.DEBUG:
    # Conectamos la URL (/media/) con la carpeta física (MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

---

## 6. Descarga de Ficheros para el Usuario

> **Explicación:** Para que un usuario pueda descargar o ver un archivo subido, accedemos al atributo `.url` del campo en el modelo. Si queremos forzar la descarga en lugar de abrirlo en el navegador, usamos el atributo HTML `download`.

**Uso en el Template:**

```html
<h2>Detalle del Capítulo: {{ capitulo.nombre }}</h2>

{% if capitulo.documento_guion %}
    <p>
        <a href="{{ capitulo.documento_guion.url }}" download>
            Descargar Guion PDF
        </a>
    </p>
{% else %}
    <p>Este capítulo no tiene guion disponible.</p>
{% endif %}

{% if capitulo.portada %}
    <img src="{{ capitulo.portada.url }}" alt="Portada" style="width: 200px;">
{% endif %}

```

---

### Resumen Profesional:

1. **Static** es para TI (el programador).
2. **Media** es para ELLOS (los usuarios).
3. Nunca olvides el `if settings.DEBUG` en las URLs, de lo contrario, al pasar a producción con `DEBUG = False`, tu código intentaría servir archivos de forma insegura y fallaría.
4. Para usar `ImageField` recuerda ejecutar en tu terminal: `pipenv install Pillow`.

