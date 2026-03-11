¡Excelente iniciativa! Tener una hoja de ruta clara es la diferencia entre un proyecto que se traduce en 5 minutos y uno que da errores de compilación constantes.

Aquí tienes la **Guía Definitiva de Internacionalización (i18n) en Django**, organizada por orden de ejecución profesional.

---

### 1. Configuración del "Cerebro" (`settings.py`)

Antes de traducir, Django debe saber qué idiomas soportar y dónde guardar las traducciones.

* **Variables de Idioma:**
```python
USE_I18N = True  # Activa el sistema de traducción
LANGUAGE_CODE = 'es' # Idioma por defecto

from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('es', _('Español')),
    ('en', _('Inglés')),
]

```


* **Middleware:** Es vital para detectar el idioma del usuario (vía URL, cookies o navegador). **Debe ir después de SessionMiddleware y antes de CommonMiddleware**.
```python
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # <--- AQUÍ
    'django.middleware.common.CommonMiddleware',
]

```


* **Procesador de Contexto:** Normalmente Django lo trae por defecto, pero asegúrate de que esté en la sección `TEMPLATES`:
```python
'django.template.context_processors.i18n',

```


* **Ruta de carpetas:** Indica dónde se crearán los archivos `.po`.
```python
LOCALE_PATHS = [BASE_DIR / 'locale']

```



---

### 2. Configuración de URLs y Prefijos (`urls.py`)

Para que Google indexe tu web en varios idiomas, las URLs deben cambiar (ej: `/es/inicio/` y `/en/home/`).

* **Uso de `i18n_patterns`:**
```python
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

# URLs que NO se traducen (estáticos, media, etc.)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')), # Necesario para set_language
]

# URLs que SÍ llevan prefijo /es/ o /en/
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')), # Si usas Rosetta
    path('', include('apps.core.urls')), 
)

```



---

### 3. Marcado de contenido en Templates

Ahora avisamos a Django qué textos debe "extraer" para traducir.

* **Cargar el módulo:** Siempre al principio del HTML: `{% load i18n %}`.
* **`{% trans "Texto" %}`**: Para frases cortas y simples.
* **`{% blocktrans %}`**: Para textos largos o que incluyen variables:
```html
{% blocktrans with nombre=user.username %}
    Hola {{ nombre }}, bienvenido a Conquer Blocks.
{% endblocktrans %}

```



---

### 4. Implementación del Selector de Idioma

El usuario necesita un botón para cambiar el idioma.

* **Formulario `set_language`:**
```html
<form action="{% url 'set_language' %}" method="post">
    {% csrf_token %}
    <input name="next" type="hidden" value="{{ request.get_full_path }}">
    <select name="language" onchange="this.form.submit()">
        {% get_current_language as CURRENT_LANG %}
        {% get_available_languages as ALL_LANGS %}
        {% for lang_code, lang_name in ALL_LANGS %}
            <option value="{{ lang_code }}" {% if lang_code == CURRENT_LANG %}selected{% endif %}>
                {{ lang_name }}
            </option>
        {% endfor %}
    </select>
</form>

```



---

### 5. Gestión de traducciones con Rosetta

* **Instalación:** `pipenv install django-rosetta`.
* **Uso:** Una vez configurado en `INSTALLED_APPS` y `urls.py`, Rosetta te permite traducir desde una interfaz web amigable en `/rosetta/`.

---

### 6. ¿Te dejas algún paso importante? **SÍ, tres fundamentales:**

Para que la guía sea 100% profesional, añade estos pasos:

1. **Creación de la carpeta física:** Django no crea la carpeta `locale` por ti. Debes crearla en la raíz: `mkdir locale`.
2. **Uso de `gettext_lazy` en Modelos:** No olvides traducir los nombres de los campos en tus `models.py`.
```python
from django.utils.translation import gettext_lazy as _
class Curso(models.Model):
    titulo = models.CharField(_("Título del curso"), max_length=200)

```


3. **El flujo de comandos (Ciclo de Vida):** Este es el paso donde la gente suele fallar:
* **Paso A:** Marcar textos en código/templates.
* **Paso B (Extraer):** `python manage.py makemessages -l en` (crea el archivo `.po`).
* **Paso C (Traducir):** Usas Rosetta o Poedit.
* **Paso D (Compilar):** `python manage.py compilemessages`. **Sin este paso, las traducciones no se verán en la web.**



---

### Resumen del flujo de trabajo diario:

> **Programar** -> **`makemessages`** -> **Traducir en Rosetta** -> **`compilemessages`**.

¿Quieres que profundicemos en cómo configurar **Poedit** si prefieres traducir fuera del navegador o prefieres que veamos cómo traducir los **mensajes de error** de los formularios?