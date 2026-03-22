Aquí tienes la **Guía Maestra de Testing con Pytest**. He estructurado este paso a paso integrando las herramientas de Docker, la lógica de Django y las mejores prácticas de arquitectura (GWT/AAA) para que te sirva de plantilla en cualquier proyecto profesional.

---

## Fase 13: Configuración de Pytest y Entorno de Pruebas

En esta fase abandonamos el sistema de pruebas por defecto de Django para implementar **Pytest**, el estándar de la industria, debido a su potencia y legibilidad.

### 1. Instalación de Dependencias

Añadimos Pytest y su conector para Django al proyecto.

1. **Actualizar `app/requirements.txt`:**

   ```text
   Django==6.0
   djangorestframework==3.16.1
   psycopg2-binary==2.9.11
   pytest==9.0.2
   pytest-django==4.11.1
   ```

2. **Reconstruir la imagen de Docker** (necesario siempre que cambien los requirements):
   ```bash
   docker compose up -d --build
   ```

### 2. Estructura de Directorios de Tests

Adoptamos un enfoque centralizado para los tests, separándolos del código de la aplicación.

1. **Crear carpetas y archivos init:**
   ```bash
   mkdir -p app/tests/movies
   touch app/tests/__init__.py
   touch app/tests/movies/__init__.py
   ```

### 3. Configuración del Motor de Pytest (`pytest.ini`)

Creamos el archivo `app/pytest.ini` para que Pytest sepa cómo interactuar con Django.

> **IMPORTANTE:** Asegúrate de que `[pytest]` esté solo en su propia línea.

```ini
[pytest]
DJANGO_SETTINGS_MODULE = drf_project.settings
python_files = tests.py test_*.py *_tests.py
```

---

## Fase 14: Desarrollo del Primer Endpoint (TDD)

### 1. Crear el Test de Sanidad

Creamos un test simple para verificar que Pytest está "escuchando".

1. **Crear `app/tests/test_foo.py`:**

   ```python
   def test_hello_world():
       assert "hello_world" == "hello_world"
       assert "foo" != "bar"
   ```

2. **Ejecutar el test en el contenedor:**
   ```bash
   docker compose exec movies pytest
   ```

### 2. Crear la lógica de la API (Endpoint "Ping")

Implementamos una vista sencilla que responda en formato JSON.

1. **Crear `app/drf_project/views.py`:**

   ```python
   from django.http import JsonResponse

   def ping(request):
       data = {"ping": "pong!"}
       return JsonResponse(data)
   ```

2. **Registrar la URL en `app/drf_project/urls.py`:**

   ```python
   from django.contrib import admin
   from django.urls import path
   from .views import ping

   urlpatterns = [
       path("admin/", admin.site.urls),
       path("ping/", ping, name="ping"),
   ]
   ```

### 3. Test de Integración (Usando Fixtures)

Actualizamos nuestro test para que verifique el comportamiento real de la URL usando la arquitectura **Given-When-Then** (o AAA).

1. **Actualizar `app/tests/test_foo.py`:**

   ```python
   import json
   from django.urls import reverse

   def test_ping(client):
       # Given (Arrange) - El fixture 'client' es inyectado automáticamente
       url = reverse("ping")

       # When (Act)
       response = client.get(url)
       content = json.loads(response.content)

       # Then (Assert)
       assert response.status_code == 200
       assert content["ping"] == "pong!"
   ```

---

## Fase 15: Conceptos Avanzados de Testing

### 1. El Sistema de Fixtures

Las fixtures son objetos reutilizables que gestionan el **Setup** (preparación) y el **Teardown** (limpieza) de recursos.

**Scopes (Alcances):**

- `function`: Se ejecuta una vez por cada test (por defecto).
- `class`: Una vez por clase de tests.
- `module`: Una vez por archivo `.py`.
- `session`: Una vez en toda la ejecución (ideal para configurar la DB).

### 2. El archivo `conftest.py` (Opcional/Configuración Pro)

Si necesitas personalizar la base de datos de tests o compartir fixtures globalmente, crea `app/conftest.py`.

```python
import pytest

@pytest.fixture(scope="session")
def django_db_setup():
    # Lógica para configurar una base de datos de test personalizada
    pass
```

### 3. Metodología Given-When-Then (GWT)

Para tests mantenibles, estructura siempre tu código así:

- **Given:** Estado inicial del sistema (Datos, Fixtures).
- **When:** La acción específica que se está probando.
- **Then:** El resultado esperado (Asserts).

---

## Comandos de Verificación Final

1. **Ejecutar todos los tests:**

   ```bash
   docker compose exec movies pytest
   ```

2. **Ejecutar tests y ver la salida detallada (verbose):**

   ```bash
   docker compose exec movies pytest -v
   ```

3. **Verificar el endpoint en el navegador:**
   Accede a `http://localhost:8009/ping/`.

---
