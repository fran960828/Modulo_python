Esta es la guía definitiva para integrar **Swagger (OpenAPI)** en tu proyecto Django REST Framework, estructurada paso a paso y con todos los comandos necesarios para mantener tu flujo de CI/CD impecable.

---

## 📖 Documentando con Swagger

[cite_start]Swagger (ahora **OpenAPI Specification**) permite describir, producir y visualizar APIs RESTful[cite: 1]. [cite_start]Utilizaremos **drf-yasg** para generar automáticamente la documentación y **Swagger UI** para que puedas probar los endpoints directamente desde el navegador[cite: 1].

---

## 🛠️ 1. Configuración Inicial (Setup)

### Actualizar dependencias

Añade `drf-yasg` a tu archivo de requerimientos principal.

**`app/requirements.txt`**:

```text
Django==6.0
dj-database-url==3.0.1
djangorestframework==3.16.1
[cite_start]drf-yasg==1.21.11  # <--- Nueva dependencia [cite: 1]
gunicorn==22.0.0
psycopg2-binary==2.9.11
whitenoise==6.11.0
```

### Registrar la aplicación

Añade la librería a la lista de aplicaciones instaladas de Django.

**`app/drf_project/settings.py`**:

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    [cite_start]"drf_yasg",  # <--- Añadir [cite: 1]
    "movies",
]
```

---

## 🔗 2. Configuración de Rutas (URLs)

Para habilitar la interfaz, debemos definir la vista del esquema en el archivo de URLs principal.

**`app/drf_project/urls.py`**:

```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
  openapi.Info(
      [cite_start]title="Movies API",       # Título de tu API [cite: 1]
      [cite_start]default_version="v1",     # Versión [cite: 1]
  ),
  public=True,
  [cite_start]permission_classes=(permissions.AllowAny,), # Acceso público para documentación [cite: 1]
)

urlpatterns = [
    ...
    # [cite_start]Ruta para visualizar la documentación [cite: 1]
    path("swagger-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    ...
]
```

---

## 🚀 3. Comandos de Construcción y Prueba

Para aplicar los cambios, reconstruye tus contenedores:

- **Construir e iniciar contenedores:**
  `$ docker compose up -d --build`
  [cite_start]_Sirve para instalar la nueva dependencia `drf-yasg` en la imagen y levantar los servicios[cite: 1]._

- **Acceso a la documentación:**
  [cite_start]Navega a `http://localhost:8009/swagger-docs/` para ver y probar tus métodos CRUD[cite: 1].

---

## 🎨 4. Personalización del Esquema (Custom Schema)

[cite_start]Si notas que Swagger no muestra los parámetros para `POST` o `PUT`, debes usar decoradores en tus vistas para definir el cuerpo de la petición[cite: 1].

**`app/movies/views.py`**:

```python
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Ejemplo en el método POST
@swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING),
            "genre": openapi.Schema(type=openapi.TYPE_STRING),
            "year": openapi.Schema(type=openapi.TYPE_STRING),
        },
    ))
def post(self, request, format=None):
    ...
```

### Limpieza de la Interfaz (UI)

[cite_start]Si tu API no requiere autenticación de sesión, puedes eliminar el botón "Django Login" para que la UI sea más limpia[cite: 1].

**`app/drf_project/settings.py`**:

```python
SWAGGER_SETTINGS = {
    [cite_start]"USE_SESSION_AUTH": False  # Desactiva el botón de login de sesión en Swagger [cite: 1]
}
```

---

## 🧹 5. Comandos de Calidad antes de Producción (CI)

Antes de hacer el push final, ejecuta los linters localmente para asegurar que el pipeline no falle.

- **Flake8 (Estilo PEP8):**
  `$ docker compose exec movies flake8 .`
  [cite_start]_Revisa que el código cumpla con las reglas de estilo de Python[cite: 1]._

- **Black (Formateador):**
  `$ docker compose exec movies black --exclude=migrations .`
  [cite_start]_Formatea automáticamente el código, ignorando las migraciones[cite: 1]._

- **isort (Orden de Imports):**
  `$ docker compose exec movies isort .`
  [cite_start]_Ordena alfabéticamente los imports y los separa por secciones[cite: 1]._

---

## 🌍 6. Despliegue Final

1. [cite_start]**Commit y Push**: Sube tus cambios a GitHub/GitLab[cite: 1].
2. [cite_start]**Verificación CI/CD**: El pipeline construirá la imagen de producción con `Dockerfile.prod`, instalará `drf-yasg` y ejecutará los tests[cite: 1].
3. [cite_start]**Producción**: Una vez desplegado, verifica que Swagger funcione en tu instancia de Render/Heroku navegando a `/swagger-docs/`[cite: 1].
