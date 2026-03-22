Esta es la **Guía Maestra de Monkeypatching y Pruebas Unitarias**. Con este módulo, aprenderás a desacoplar tus tests de la base de datos y de servicios externos, lo que te permitirá tener una suite de pruebas extremadamente rápida y confiable.

---

## 1. ¿Qué es el Monkeypatching?

El **Monkeypatching** es la técnica de cambiar dinámicamente una pieza de código en tiempo de ejecución. Te permite sobrescribir el comportamiento por defecto de un módulo, objeto o método sin modificar el código fuente original.

**¿Para qué sirve en el mundo real?**

- **Velocidad:** Evitas llamadas lentas a la base de datos.
- **Aislamiento:** No dependes de si una API externa (como Twitter o Stripe) está caída.
- **Predictibilidad:** Tú controlas exactamente qué devuelve la función "engañada".

---

## 2. Preparación de Unit Tests (Vistas)

A diferencia de los tests de integración, aquí crearemos una suite que **no toca la base de datos**.

### Creación del archivo de tests unitarios

Crea `app/tests/movies/test_views_unit.py` y define los esqueletos de los tests. Usaremos el fixture `monkeypatch` proporcionado por pytest.

```python
import pytest
from django.http import Http404
from movies.views import MovieSerializer, MovieDetail, Movie

# Ejemplo de estructura base
def test_add_movie(client, monkeypatch):
    pass
```

---

## 3. Implementación del Monkeypatching (Paso a Paso)

Para que la vista funcione sin base de datos, debemos hacer una "cirugía" en dos puntos clave: la **escritura** (create/update) y la **lectura** (data).

### A. Test: Añadir Película (POST)

```python
def test_add_movie(client, monkeypatch):
    payload = {"title": "The Big Lebowski", "genre": "comedy", "year": "1998"}

    # 1. Mockeamos el método create para que no vaya a la DB
    def mock_create(self, payload):
        return "The Big Lebowski"

    # 2. Aplicamos el cambiazo
    monkeypatch.setattr(MovieSerializer, "create", mock_create)
    monkeypatch.setattr(MovieSerializer, "data", payload)

    resp = client.post("/api/movies/", payload, content_type="application/json")
    assert resp.status_code == 201
    assert resp.data["title"] == "The Big Lebowski"
```

### B. Test: Eliminar Película (DELETE)

Aquí simulamos un objeto que tiene un método `.delete()` para que la vista no explote al intentar llamarlo.

```python
def test_remove_movie(client, monkeypatch):
    def mock_get_object(self, pk):
        class FakeMovie:
            def delete(self): # Método ficticio
                pass
        return FakeMovie

    monkeypatch.setattr(MovieDetail, "get_object", mock_get_object)

    resp = client.delete("/api/movies/1/")
    assert resp.status_code == 204
```

---

## 4. Ejecución en Paralelo con `pytest-xdist`

Como los unit tests no comparten la base de datos, podemos ejecutarlos simultáneamente en todos los núcleos de tu CPU para ahorrar tiempo.

### Paso 1: Actualizar dependencias

Añade `pytest-xdist==3.8.0` a tu `requirements.txt`.

### Paso 2: Reconstruir el entorno

Ejecuta el comando para instalar la nueva librería en el contenedor:

```bash
docker compose up -d --build
```

- **`--build`**: Obliga a Docker a leer el `requirements.txt` y reinstalar las librerías.

### Paso 3: Ejecutar tests en paralelo

```bash
docker compose exec movies pytest -k "unit" -n auto
```

- **`-k "unit"`**: Filtra y ejecuta solo los tests que contienen la palabra "unit" en su nombre.
- **`-n auto`**: Distribuye los tests automáticamente entre todos los núcleos disponibles de tu procesador.

---

## 5. Diccionario de Comandos y Fixtures

| Comando / Fixture              | Definición                        | Uso en esta guía                                          |
| :----------------------------- | :-------------------------------- | :-------------------------------------------------------- |
| **`monkeypatch`**              | Fixture de pytest para "mockear". | Se pasa como argumento a la función del test.             |
| **`setattr(obj, name, mock)`** | "Set Attribute".                  | Reemplaza el método real por tu versión `mock`.           |
| **`indirect=["fixture"]`**     | Argumento de `parametrize`.       | Indica que el dato de la tabla es en realidad un fixture. |
| **`-n auto`**                  | Bandera de `xdist`.               | Lanza los tests en paralelo para máxima velocidad.        |
| **`raise Http404`**            | Lanzar excepción.                 | Se usa en los mocks para simular que un objeto no existe. |

---

## 6. Conclusión y Siguiente Paso

Has transformado tu suite de pruebas de una "lenta y pesada" a una de "grado de ingeniería", capaz de ejecutarse en paralelo y sin dependencias externas. Esta es la base para escalar proyectos con miles de tests.

**¿Te gustaría que ahora preparemos la Guía de Swagger para que toda esta lógica que hemos testeado sea visible y usable desde una interfaz web profesional?** Es el siguiente paso lógico para tu portfolio.
