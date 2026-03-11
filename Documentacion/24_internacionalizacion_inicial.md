Esta documentación técnica está diseñada para enseñarte a convertir tu aplicación de Django en un producto global. En el desarrollo profesional, no escribimos textos directamente en el código; los envolvemos en funciones de traducción. El proceso de preparar el código se llama **Internacionalización (i18n)** y el proceso de adaptarlo a un idioma específico se llama **Localización (l10n)**.

---

## 1. Configuración Base en `settings.py`

> **Explicación:** Django necesita saber cuáles son los idiomas disponibles, cuál es el predeterminado y dónde se guardarán los archivos de traducción (archivos `.po` y `.mo`).

```python
# settings.py
from django.utils.translation import gettext_lazy as _
import os

# 1. Habilitar el sistema de traducción
USE_I18N = True

# 2. Idioma por defecto
LANGUAGE_CODE = 'es'

# 3. Lista de idiomas soportados (usamos gettext_lazy para los nombres)
LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English')),
]

# 4. Ruta donde se guardarán las traducciones
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# 5. Middleware necesario para detectar el idioma del usuario
MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # Debe ir después de Session y antes de Common
    'django.middleware.common.CommonMiddleware',
    # ...
]

```

---

## 2. Traducciones en Templates: `trans` y `blocktrans`

> **Explicación:** Para traducir texto en HTML, primero debemos cargar el módulo `i18n`.
> * `{% trans %}`: Se usa para frases simples y estáticas.
> * `{% blocktrans %}`: Se usa cuando el texto contiene variables dinámicas o es muy largo.
> 
> 

**Ejemplo en el HTML:**

```html
{% load i18n %}

<h1>{% trans "Bienvenido a nuestra plataforma" %}</h1>

{% blocktrans with nombre=user.username %}
    Hola {{ nombre }}, gracias por visitarnos.
{% endblocktrans %}

```

---

## 3. Traducciones en Código: `gettext` y `gettext_lazy`

> **Explicación:** > - `gettext` (o `_`): Se usa en vistas donde el texto se traduce en el momento de la ejecución.
> * `gettext_lazy`: Es vital para **Modelos y Formularios**. No traduce el texto inmediatamente, sino cuando se va a mostrar al usuario (evita errores de carga de idioma al arrancar el servidor).
> 
> 

**Ejemplo en `models.py`:**

```python
from django.db import models
from django.utils.translation import gettext_lazy as _

class Producto(models.Model):
    # Usamos _() para que el nombre del campo sea traducible en el Admin
    nombre = models.CharField(_("nombre del producto"), max_length=100)

```

---

## 4. El Proceso de Extracción: `makemessages` y `gettext`

> **Explicación:** Django no traduce por arte de magia; necesita "extraer" los textos que marcaste.
> * **Instalación de gettext:** En macOS usa `brew install gettext`. En Windows, descarga los binarios de gettext. Sin esto, el comando fallará.
> * **Comando:** `python manage.py makemessages -l en` (crea el archivo para inglés).
> 
> 

---

## 5. Edición Profesional: Poedit

> **Explicación:** Poedit es la herramienta estándar para traductores. Permite abrir los archivos `.po` generados por Django y escribir la traducción de forma cómoda.
> 1. **Instalación:** Descárgalo en [poedit.net](https://poedit.net/).
> 2. **Uso:** Abre el archivo `locale/en/LC_MESSAGES/django.po`. Escribe la traducción y dale a **Guardar**. Al guardar, Poedit genera automáticamente un archivo `.mo` (que es el que Django lee realmente).
> 
> 

---

## 6. Flujo de trabajo: De Español a Inglés

1. **Marcar:** Pon `_("Texto")` o `{% trans %}` en tu código.
2. **Extraer:** Ejecuta `python manage.py makemessages -l en`.
3. **Traducir:** Abre el `.po` con Poedit y traduce.
4. **Compilar:** Ejecuta `python manage.py compilemessages` (esto crea los archivos binarios `.mo`).

---

## 7. Django Rosetta: Traducción en el Navegador

> **Explicación:** Rosetta es una interfaz web que te permite traducir sin salir de tu propia página, directamente en el panel de administración.

**Instalación y Configuración:**

1. `pip install django-rosetta`
2. En `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'rosetta',
]

```

3. En `urls.py`:

```python
if 'rosetta' in settings.INSTALLED_APPS:
    path('rosetta/', include('rosetta.urls')),

```

---

## 8. Selector de Idioma Profesional

> **Explicación:** Para permitir al usuario cambiar de idioma y que este se mantenga al refrescar, usamos una vista de Django que guarda la preferencia en la **sesión o en una cookie**.

**Ejemplo de Selector en el Template:**

```html
<form action="{% url 'set_language' %}" method="post">
    {% csrf_token %}
    <input name="next" type="hidden" value="{{ redirect_to }}">
    <select name="language" onchange="this.form.submit()">
        {% get_current_language as LANGUAGE_CODE %}
        {% get_available_languages as LANGUAGES %}
        {% for lang in LANGUAGES %}
            <option value="{{ lang.0 }}" {% if lang.0 == LANGUAGE_CODE %}selected{% endif %}>
                {{ lang.1 }}
            </option>
        {% endfor %}
    </select>
</form>

```

**¿Por qué funciona al refrescar?** El `LocaleMiddleware` de Django busca el idioma en este orden:

1. Prefijo en la URL (ej: `/en/home/`).
2. Idioma en la sesión del usuario.
3. Idioma en una cookie.
4. Preferencia del navegador.

