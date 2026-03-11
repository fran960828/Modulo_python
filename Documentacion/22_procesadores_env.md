Esta documentación técnica está diseñada para enseñarte a gestionar datos globales y configuraciones sensibles en Django. En el desarrollo profesional, no queremos pasar la misma variable (como el nombre de la web o el año actual) en cada una de nuestras vistas manualmente. Para eso usamos los **Procesadores de Contexto**. Además, aprenderás a proteger tus "secretos" (como contraseñas de bases de datos) mediante **Variables de Entorno**.

---

## 1. Procesadores de Contexto (Context Processors)

> **Explicación:** Un Procesador de Contexto es una función que toma el objeto `request` y devuelve un diccionario. Los datos de este diccionario se inyectan automáticamente en **todos** los templates de tu proyecto sin que tengas que escribirlos en cada vista.
> **Ámbito Laboral:** Se usan para mostrar información global: redes sociales, datos de contacto de la empresa, el carrito de compras del usuario, o el año actual para el copyright del footer.

**Ejemplo de creación (`context_processors.py`):**

```python
# Creamos un archivo llamado context_processors.py en nuestra app
def info_empresa(request):
    # Definimos datos que queremos en toda la web
    return {
        'nombre_web': 'Conquer Blocks',
        'email_contacto': 'soporte@conquerblocks.com',
        'redes': {'twitter': '@conquer', 'insta': '@conquerblocks'}
    }

```

---

## 2. Adición al archivo `settings.py`

> **Explicación:** Para que Django sepa que debe usar esa función, debemos registrarla en la lista `context_processors` dentro de la configuración `TEMPLATES`.

```python
# settings.py
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

                # AÑADIMOS EL NUESTRO: ruta.del.archivo.funcion
                'miapp.context_processors.info_empresa',
            ],
        },
    },
]

```

---

## 3. Uso de `django.conf` en Procesadores de Contexto

> **Explicación:** A veces queremos que el Procesador de Contexto lea una variable definida en `settings.py`. Para ello usamos `django.conf.settings`. Esto es muy útil para activar/desactivar funciones globales (como un modo mantenimiento o un banner de ofertas).

**Ejemplo Práctico:**

```python
from django.conf import settings # Importación profesional

def configuracion_global(request):
    # Accedemos a una variable que hayamos creado en settings.py
    # Por ejemplo: MODO_NOCHE = True
    return {
        'modo_noche_activo': settings.MODO_NOCHE
    }

```

---

## 4. Variables de Entorno y Seguridad

> **Explicación:** En el ámbito laboral, **nunca** subimos contraseñas, claves de API o la `SECRET_KEY` de Django a GitHub. Las variables de entorno son valores que residen en el sistema operativo o en un archivo oculto (`.env`) y no en el código fuente.

---

## 5. Instalación y uso de `django-environ`

> **Explicación:** Es la librería estándar en la industria para manejar archivos `.env`. Nos permite leer variables y, lo más importante, **convertirlas al tipo de dato correcto** (Booleano, Entero, Lista).

**Instalación:**

```bash
pip install django-environ

```

**Configuración en `settings.py`:**

```python
import environ
import os

# 1. Inicializamos environ
env = environ.Env(
    # Establecemos valores por defecto si la variable no existe
    DEBUG=(bool, False)
)

# 2. Leemos el archivo .env (buscándolo desde la base del proyecto)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# 3. Usamos las variables
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

```

---

## 6. La librería `os` y `getenv`

> **Explicación:** Antes de `django-environ`, se usaba la librería nativa de Python `os`. El método `os.getenv('NOMBRE')` busca la variable directamente en el sistema. Es útil pero menos potente que `django-environ` porque siempre devuelve el valor como **texto (string)**.

**Ejemplo:**

```python
import os

# Buscamos la variable 'DB_PASSWORD'. Si no existe, devuelve el segundo parámetro.
db_pass = os.getenv('DB_PASSWORD', 'password_por_defecto')

```

---

## 7. Concepto de `loadenv` (python-dotenv)

> **Explicación:** Aunque `django-environ` es preferido en Django, puede que veas `load_dotenv`. Es una función de la librería `python-dotenv` que carga las variables del archivo `.env` directamente al diccionario `os.environ` del sistema.

```python
from dotenv import load_dotenv
import os

# Carga las variables del archivo .env al entorno de Python
load_dotenv()

# Ahora se pueden leer con os.getenv
api_key = os.getenv('API_KEY')

```

---

### Resumen de Flujo Profesional

1. Creas un archivo **`.env`** (y lo añades a `.gitignore`).
2. Defines tus secretos: `SECRET_KEY=super-secreto-123`.
3. Usas **`django-environ`** en `settings.py` para leerlos.
4. Si necesitas que un dato de esos secretos llegue a los HTML, creas un **Procesador de Contexto** que use `django.conf.settings`.

¿Te gustaría que configuráramos ahora la **conexión a una base de datos PostgreSQL** usando variables de entorno y el método `env.db_url()` que es el estándar en servidores de producción?
