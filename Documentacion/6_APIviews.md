Aquí tienes la **Guía Maestra de TDD: Views, URLs y Comandos Avanzados**. He consolidado toda la lógica de los endpoints, las refactorizaciones con fixtures y los comandos de limpieza de base de datos en un paso a paso estructurado.

---

## Fase 21: Implementación de Endpoints RESTful con TDD

Siguiendo las mejores prácticas, definimos tres rutas principales para nuestro recurso `Movie`.

| Endpoint           | Método HTTP | Acción CRUD | Resultado                       |
| :----------------- | :---------- | :---------- | :------------------------------ |
| `/api/movies/`     | **GET**     | READ        | Listar todas las películas      |
| `/api/movies/:id/` | **GET**     | READ        | Obtener detalle de una película |
| `/api/movies/`     | **POST**    | CREATE      | Añadir una nueva película       |

---

### 1. Crear Recurso (POST)

**Paso 1: Test de Creación**
Crea `app/tests/movies/test_views.py`. Usamos el cliente de pruebas de Django para simular peticiones.

```python
import json
import pytest
from django.urls import reverse
from movies.models import Movie

@pytest.mark.django_db
def test_add_movie(client):
    url = reverse("movies:movie-list")
    payload = {"title": "The Big Lebowski", "genre": "comedy", "year": "1998"}

    resp = client.post(url, payload, content_type="application/json")

    assert resp.status_code == 201
    assert resp.data["title"] == "The Big Lebowski"
```

**Paso 2: Implementar Vista y URLs**
En `app/movies/views.py`, usamos `APIView` para manejar el POST:

```python
class MovieList(APIView):
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Configura `app/movies/urls.py` y asegúrate de incluirlo en el `urls.py` principal del proyecto.

---

### 2. Obtener Detalle (GET Individual)

**Paso 1: Test de Detalle**
Añadimos la lógica para buscar por ID y manejar errores 404.

```python
@pytest.mark.django_db
def test_get_single_movie(client, add_movie): # Usando fixture add_movie
    movie = add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    url = reverse("movies:movie-detail", kwargs={"pk": movie.id})
    resp = client.get(url)
    assert resp.status_code == 200
```

**Paso 2: Implementar Vista de Detalle**
En `app/movies/views.py`:

```python
class MovieDetail(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
```

---

### 3. Listar Recursos (GET All) y Fixtures Profesionales

Para evitar repetir código en los tests, usamos el patrón **Factory as Fixture**.

**Paso 1: Configurar `app/tests/movies/conftest.py`**

```python
@pytest.fixture(scope='function')
def add_movie():
    def _add_movie(title, genre, year):
        return Movie.objects.create(title=title, genre=genre, year=year)
    return _add_movie
```

**Paso 2: Test de Listado**

```python
@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    add_movie("Movie 1", "genre", "2000")
    add_movie("Movie 2", "genre", "2001")
    url = reverse("movies:movie-list")
    resp = client.get(url)
    assert resp.status_code == 200
    assert len(resp.data) == 2
```

---

## Fase 22: Gestión de Datos y Comandos de Consola

### 1. Sembrado de Base de Datos (Seeding)

Para trabajar con datos reales en desarrollo sin usar el Admin:

1. **Limpiar base de datos:** `python manage.py flush`
2. **Cargar JSON:** `python manage.py loaddata movies.json`
3. **Verificar con HTTPie:** `http GET http://localhost:8009/api/movies/`

### 2. Caja de Herramientas Pytest (Cheat Sheet Avanzada)

Ejecuta estos comandos dentro del **Dev Container** para optimizar tu flujo:

| Comando                 | Utilidad                                                             |
| :---------------------- | :------------------------------------------------------------------- |
| `pytest --lf`           | Ejecuta **solo** los tests que fallaron la última vez.               |
| `pytest -x`             | Se detiene inmediatamente tras el **primer fallo**.                  |
| `pytest -k "expresion"` | Filtra tests por nombre (ej: `-k "movie and not all"`).              |
| `pytest --pdb`          | Abre el **depurador interactivo** en el punto exacto del fallo.      |
| `pytest --durations=2`  | Muestra los 2 tests más **lentos** (ideal para optimizar).           |
| `pytest -l`             | Muestra las **variables locales** en el error (muy útil para debug). |

---

### 1. El Refactor de la Vista (`views.py`)

Vamos a sustituir `MovieList` y `MovieDetail` por una única clase. DRF nos ofrece `ModelViewSet`, que ya trae implementada toda la lógica de lectura, creación, actualización y borrado.

**Edita `app/movies/views.py`:**

```python
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```

> **¿Qué acaba de pasar?** Con estas 3 líneas de código, hemos sustituido unas 30 líneas anteriores. `ModelViewSet` sabe que si llega un GET debe listar, si llega un POST debe crear, y si llega un ID en la URL debe buscar ese objeto.

---

### 2. El Refactor de las URLs (`urls.py`)

Al usar ViewSets, ya no definimos las rutas una a una. Usamos un **Router**, que es un objeto que genera automáticamente el mapa de URLs estándar de una API REST.

**Edita `app/movies/urls.py`:**

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

app_name = "movies"

# Creamos el router y registramos nuestro ViewSet
router = DefaultRouter()
router.register(r"api/movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("", include(router.urls)),
]
```

---

### 3. ¿Cómo afecta esto a tus Tests?

Aquí es donde verás la importancia de haber usado `reverse`. Si usaste `reverse("movies:movie-list")` y `reverse("movies:movie-detail", kwargs={"pk": ...})`, **tus tests seguirán pasando en verde** sin tocar ni una línea de código de test.

El `DefaultRouter` genera automáticamente estos nombres (basados en el `basename` que pusimos):

- `movie-list` -> Para la colección (`/api/movies/`)
- `movie-detail` -> Para el objeto individual (`/api/movies/1/`)

---

### 4. Comparativa de "Junior de Élite"

| Característica | APIView (Lo que tenías)        | ViewSet (Lo nuevo)              |
| :------------- | :----------------------------- | :------------------------------ |
| **Código**     | Explícito y largo.             | Conciso y automático.           |
| **Control**    | Total sobre cada método.       | Basado en configuración.        |
| **URLs**       | Manuales (`path`).             | Automáticas (`Router`).         |
| **Uso ideal**  | Lógica compleja/personalizada. | CRUD estándar de base de datos. |

---

### 5. Comandos de Verificación (Dentro del Dev Container)

1. **Ejecuta los tests:** ```bash
   pytest

   ```
   *Deberían salir los 11 puntos verdes. Si alguno falla, revisa que el `basename` en el router coincida con el nombre que usas en el `reverse`.*

   ```

2. **Prueba la "Browsable API":**
   Ve a `http://localhost:8009/api/movies/`. Verás que el `DefaultRouter` te ha creado una página de inicio de la API muy limpia donde puedes ver todos los endpoints disponibles.

3. **HTTPie:**
   ```bash
   http GET http://localhost:8009/api/movies/
   ```

---

### Tu Guía Maestra (Nueva Sección: Abstracción Pro)

Añade esto a tu base de proyectos:

> **Regla de Oro de ViewSets:** Úsalos siempre que tu endpoint sea un reflejo directo de un Modelo (CRUD). Si necesitas un endpoint que haga algo muy raro (ej: "procesar pago y enviar email"), mejor quédate con una `APIView` para tener el control total.

**¿Te han pasado los tests tras el refactor?** Si es así, acabas de reducir la deuda técnica de tu proyecto a la mitad. ¿Estamos listos para hablar de **Deploy** o quieres que miremos cómo personalizar una acción dentro del ViewSet (por ejemplo, un filtro)?
