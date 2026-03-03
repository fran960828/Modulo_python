## 1. El ciclo de Vida de una Request en Django

> **Explicación:** Cuando un usuario escribe una dirección en su navegador, Django recibe una **HttpRequest**.
>
> 1. Primero, consulta el archivo `urls.py` principal.
> 2. Intenta hacer "match" (coincidir) el texto de la URL con sus rutas definidas.
> 3. Si coincide, salta a la función de la **Vista (View)** asociada.
> 4. La vista procesa la lógica y devuelve un `render()`. Este método combina la `request` original con un archivo HTML para generar una **HttpResponse** (lo que el usuario finalmente ve).

```python
# views.py sencillo
from django.shortcuts import render

def home(request):
    # 'request': El objeto con la info del usuario
    # 'index.html': El nombre del archivo que queremos mostrar
    return render(request, 'index.html')

```

---

## 2. Configuración de la ruta de Templates en `settings.py`

> **Explicación:** Django necesita saber dónde buscar los archivos HTML. Usamos `BASE_DIR` (que apunta a la carpeta raíz de tu proyecto) para crear una ruta absoluta hacia una carpeta llamada `templates`. Esto asegura que tu proyecto funcione igual en tu PC que en un servidor profesional.

```python
# settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Definimos la ruta uniendo la base con el nombre de la carpeta
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR], # <--- ¡Aquí inyectamos nuestra ruta!
        'APP_DIRS': True, # Permite que Django también busque dentro de cada app
        # ... resto de la config
    },
]

```

---

## 3. Estructura de Carpetas: Templates y HTML

> **Explicación:** Para mantener el orden profesional, creamos una carpeta raíz `templates/`. Dentro de ella, es una excelente práctica crear subcarpetas con el nombre de cada aplicación. Así, si tienes dos archivos `index.html` en apps distintas, Django no se confundirá.

```text
mi_proyecto/
├── templates/          # Carpeta global
│   ├── base.html       # Estructura común (Navbar, Footer)
│   └── todos/          # Subcarpeta para la app 'todos'
│       ├── lista.html
│       └── detalle.html

```

---

## 4. Vistas Generales vs. Vistas de App (Modelos)

> **Explicación:** > - **Vistas Generales:** Manejan páginas estáticas que no dependen de la base de datos (Ej: Inicio, Contacto, Acerca de).
>
> - **Vistas de App:** Son el corazón del proyecto. Consultan los **Modelos** para obtener datos (Ej: lista de tareas, perfiles de usuario) y pasarlos al template.

```python
# todos/views/task_views.py
from django.shortcuts import render
from ..models import Task # Importamos el modelo para usar sus datos

def list_tasks(request):
    # Obtenemos todos los objetos de la base de datos
    tareas = Task.objects.all()
    # Pasamos los datos en un diccionario llamado 'context'
    return render(request, 'todos/lista.html', {'lista_tareas': tareas})

```

---

## 5. Modularización de Vistas (Carpeta `views/`)

> **Explicación:** Cuando una app crece, el archivo `views.py` se vuelve gigante. La técnica profesional es borrar `views.py` y crear un **paquete** (una carpeta llamada `views/` con un archivo `__init__.py`). Dentro, separamos las vistas por funcionalidad.

```text
todos/
├── views/
│   ├── __init__.py    # Permite importar desde la carpeta
│   ├── task_views.py  # Lógica de tareas
│   └── user_views.py  # Lógica de perfil

```

---

## 6. Organización de Templates por Modelo

> **Explicación:** Al igual que con las vistas, los templates deben estar categorizados. Dentro de `templates/nombre_app/`, creamos carpetas por cada modelo o sección importante.

```python
# Ejemplo de llamada en la vista:
# Indicamos la ruta interna: carpeta_app/carpeta_modelo/archivo.html
return render(request, 'todos/tasks/task_list.html', context)

```

---

## 7. Desacoplamiento de URLs (`include`)

> **Explicación:** El archivo `urls.py` principal del proyecto no debería conocer cada ruta de cada app. Usamos `include()` para delegar la responsabilidad. El archivo principal solo dice: "Si la URL empieza por /todos/, pregúntale a la app 'todos' qué hacer".

### Paso A: El archivo principal (`mi_proyecto/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include # Importamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Cualquier ruta que empiece con 'todos/' se va a la app
    path('todos/', include('todos.urls')),
]

```

### Paso B: El archivo de la App (`todos/urls.py`)

```python
from django.urls import path
from .views.task_views import list_tasks # Importamos la función de la vista

urlpatterns = [
    # Esta ruta es realmente 'todos/list/'
    path('list/', list_tasks, name='task_list'),
]

```

---

## Resumen de flujo para el alumno:

1. El usuario entra en `/todos/list/`.
2. El **URL principal** ve que empieza por `todos/` y lo manda al `urls.py` de la app.
3. El **URL de la app** ve que termina en `list/` y llama a la función `list_tasks`.
4. La **Vista** `list_tasks` busca las tareas en el **Modelo**.
5. La **Vista** hace un `render` uniendo la información con el archivo `templates/todos/tasks/task_list.html`.
6. El usuario recibe su HTML con los datos.
