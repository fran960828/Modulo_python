## 1. Explicación e Instalación

> **Explicación:** `django-modeltranslation` registra los modelos que queremos traducir y "duplica" los campos seleccionados para cada idioma configurado en el proyecto. Por ejemplo, si tienes un campo `titulo` y los idiomas español e inglés, la librería creará en la base de datos `titulo_es` y `titulo_en`.

**Instalación con Pipenv:**

```bash
pipenv install django-modeltranslation

```

---

## 2. Configuración en `settings.py`

> **Explicación:** Para que la librería funcione correctamente, debe cargarse **antes** que la propia aplicación de administración de Django. Además, requiere que la configuración de idiomas (`LANGUAGES`) esté bien definida.

```python
# settings.py

INSTALLED_APPS = [
    # ¡IMPORTANTE! Debe ir ANTES de 'django.contrib.admin'
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    # ... tus otras apps ...
]

# Configuración de idiomas (indispensable para la librería)
from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('es', _('Español')),
    ('en', _('Inglés')),
]

# Idioma por defecto del sitio
LANGUAGE_CODE = 'es'

# Si quieres que los campos originales se rellenen automáticamente
# con el idioma por defecto si la traducción está vacía
MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'
MODELTRANSLATION_LANGUAGES=('es', 'en')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('es', 'en')
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'

```

---

## 3. Uso de django-modeltranslation Paso a Paso

Para traducir un modelo, seguiremos un flujo de tres pasos: Definir el modelo, crear el archivo de traducción y registrarlo en el admin.

### Paso A: El Modelo Original (`models.py`)

Creamos un modelo normal. No hace falta añadir nada especial aquí.

```python
from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

```

### Paso B: El Archivo de Traducción (`translation.py`)

Debes crear un archivo llamado **exactamente** `translation.py` dentro de la carpeta de tu aplicación. Aquí indicas qué campos quieres duplicar por idioma.

```python
from modeltranslation.translator import register, TranslationOptions
from .models import Curso

# Registramos el modelo Curso con sus opciones de traducción
@register(Curso)
class CursoTranslationOptions(TranslationOptions):
    # Definimos los campos que tendrán versiones en varios idiomas
    fields = ('nombre', 'descripcion')

```

### Paso C: Migraciones de Base de Datos

Al haber registrado los campos en `translation.py`, la base de datos necesita nuevas columnas.

```bash
# Django detectará los nuevos campos como nombre_es, nombre_en, etc.
python manage.py makemigrations
python manage.py migrate

```

### Paso D: Configuración en el Admin (`admin.py`)

Para que el panel de administración sea cómodo y muestre los campos de idiomas agrupados, usamos `TranslationAdmin`.

```python
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Curso

# En lugar de admin.ModelAdmin, heredamos de TranslationAdmin
@admin.register(Curso)
class CursoAdmin(TranslationAdmin):
    # Podemos configurar pestañas o grupos para los idiomas
    group_fieldsets = True

    class Media:
        # Esto carga JS necesario para que la interfaz sea más fluida
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

```

---

## 4. Funcionamiento en el Template

Lo mejor de esta librería es que es **transparente**. No tienes que escribir `curso.nombre_es`. Si el usuario tiene el idioma en inglés, Django automáticamente hará que `curso.nombre` devuelva el valor de `nombre_en`.

```html
{% load i18n %}

<h2>{{ curso.nombre }}</h2>
<p>{{ curso.descripcion }}</p>
```

### Resumen del flujo profesional:

1. **Instalar** y añadir en `INSTALLED_APPS` (antes del admin).
2. Definir **`LANGUAGES`** en `settings.py`.
3. Crear **`translation.py`** en tu app y registrar los campos.
4. **Migrar** la base de datos.
5. Usar **`TranslationAdmin`** para una gestión visual de las traducciones.

¿Te gustaría que viéramos cómo forzar la visualización de un idioma específico en un template independientemente del idioma del usuario?
