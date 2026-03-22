## Fase 16: Arquitectura y Modelado con TDD

En esta fase implementamos el corazón de la aplicación siguiendo el ciclo **Red-Green-Refactor**.

### 1. El modelo de datos (Movie)

Antes de crear el código, definimos qué queremos probar.

**Paso 1: Crear el test de modelo**
Crea `app/tests/movies/test_models.py`:

```python
import pytest
from movies.models import Movie

@pytest.mark.django_db
def test_movie_model():
    # Given / Arrange
    movie = Movie(title="Raising Arizona", genre="comedy", year="1987")
    movie.save()
    # Then / Assert
    assert movie.title == "Raising Arizona"
    assert movie.genre == "comedy"
    assert movie.year == "1987"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title
```

**Paso 2: Ejecutar el test (Fallo esperado - ROJO)**
Desde la terminal de tu **Dev Container**:

```bash
pytest tests/movies/test_models.py
```

_Error esperado:_ `ImportError: cannot import name 'Movie'`.

**Paso 3: Implementar el modelo**
Edita `app/movies/models.py`:

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
```

### 2. Persistencia en Base de Datos

Para que los tests y la app funcionen, debemos informar a Postgres sobre el nuevo modelo.

1. **Crear archivos de migración:**
   ```bash
   python manage.py makemigrations
   ```
2. **Ejecutar tests de nuevo (VERDE):**
   ```bash
   pytest tests/movies/test_models.py
   ```
3. **Aplicar a la base de datos real:**
   ```bash
   python manage.py migrate
   ```

---

## Fase 17: Interfaz de Administración y Datos Manuales

Django nos regala un panel de control. Vamos a configurarlo para que sea útil.

1. **Configurar `app/movies/admin.py`:**

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Movie, CustomUser

@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ("title", "genre", "year", "created_date", "updated_date",)
    list_display = ("title", "genre", "year", "created_date", "updated_date",)
    readonly_fields = ("created_date", "updated_date",)
```

2. **Crear acceso de Superusuario:**

   ```bash
   python manage.py createsuperuser
   ```

   _(Sigue las instrucciones en la terminal: admin / admin@email.com / password)_

3. **Verificación Visual:**
   Navega a `http://localhost:8009/admin/` y añade 2 o 3 películas para tener datos de prueba.

---

## Fase 18: Serializadores (El Traductor JSON)

El serializador convierte modelos complejos en JSON para React y viceversa.

### 1. Test de Serialización

Crea `app/tests/movies/test_serializers.py`:

```python
from movies.serializers import MovieSerializer

def test_valid_movie_serializer():
    valid_serializer_data = {"title": "Raising Arizona", "genre": "comedy", "year": "1987"}
    serializer = MovieSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.data == valid_serializer_data

def test_invalid_movie_serializer():
    invalid_serializer_data = {"title": "Raising Arizona", "genre": "comedy"} # Falta 'year'
    serializer = MovieSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.errors == {"year": ["This field is required."]}
```

### 2. Implementar el Serializador

Crea `app/movies/serializers.py`:

```python
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ("id", "created_date", "updated_date",)
```

---

## Fase 19: Gestión y Filtrado de Tests

A medida que el proyecto crece, necesitamos eficiencia al ejecutar pruebas.

### Comandos de ejecución selectiva:

- **Ejecutar todo:** `pytest`
- **Filtrar por nombre:** `pytest -k <nombre_parcial>`
  - Ejemplo: `pytest -k models` (Ejecuta solo `test_models.py`).
  - Ejemplo: `pytest -k hello_world` (Ejecuta el test de ping/sanity check).
- **Modo detallado:** `pytest -v`
- **Ver logs del servidor (Desde terminal Mac):** `docker compose logs -f movies`

---

### Resumen de comandos imprescindibles (Cheat Sheet)

| Acción                      | Comando (Dentro del Dev Container) |
| :-------------------------- | :--------------------------------- |
| **Pasar tests**             | `pytest`                           |
| **Nuevo cambio en modelos** | `python manage.py makemigrations`  |
| **Actualizar DB**           | `python manage.py migrate`         |
| **Crear Admin**             | `python manage.py createsuperuser` |
| **Ayuda de comandos**       | `python manage.py help`            |
