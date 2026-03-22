Esta es la **Guía Maestra para la Finalización del CRUD (Update & Delete)**. Con este módulo, tu API de películas alcanza su funcionalidad completa. Siguiendo la metodología **TDD (Test-Driven Development)**, nos aseguraremos de que cada nueva funcionalidad esté blindada antes de escribir el código final.

---

## 1. El Mapa de Rutas de la API (Endpoints)

Tras completar esta parte, tu API tendrá la siguiente estructura profesional:

| Endpoint           | Método HTTP | Acción CRUD | Resultado                         |
| :----------------- | :---------- | :---------- | :-------------------------------- |
| `/api/movies/`     | **GET**     | READ        | Obtener todas las películas       |
| `/api/movies/:id/` | **GET**     | READ        | Obtener una sola película         |
| `/api/movies/`     | **POST**    | CREATE      | Añadir una nueva película         |
| `/api/movies/:id/` | **PUT**     | UPDATE      | Actualizar una película existente |
| `/api/movies/:id/` | **DELETE**  | DELETE      | Eliminar una película             |

---

## 2. Fase 1: Eliminar una Película (DELETE)

### A. Los Tests (Rojo 🔴)

Añadimos las pruebas en `app/tests/movies/test_views.py`. Probamos tanto el borrado exitoso como el intento de borrar algo que no existe.

```python
@pytest.mark.django_db
def test_remove_movie(client, add_movie):
    # Creamos una película para borrarla
    movie = add_movie(title="The Big Lebowski", genre="comedy", year="1998")

    # 1. Verificamos que existe
    resp = client.get(f"/api/movies/{movie.id}/")
    assert resp.status_code == 200

    # 2. La borramos (Esperamos un 204 No Content)
    resp_two = client.delete(f"/api/movies/{movie.id}/")
    assert resp_two.status_code == 204

    # 3. Verificamos que ya no está en la lista general
    resp_three = client.get("/api/movies/")
    assert len(resp_three.data) == 0

@pytest.mark.django_db
def test_remove_movie_incorrect_id(client):
    # Intentamos borrar un ID que no existe
    resp = client.delete(f"/api/movies/99/")
    assert resp.status_code == 404
```

### B. La Vista (Verde 🟢)

Modificamos `app/movies/views.py` para incluir el método `delete` en la clase `MovieDetail`.

```python
class MovieDetail(APIView):
    # ... (get_object y get anteriores)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

---

## 3. Fase 2: Actualizar una Película (PUT)

### A. Los Tests (Rojo 🔴)

Probamos la actualización completa y los casos de error. Aquí es donde aplicamos la **Parametrización** para limpiar el código.

```python
@pytest.mark.django_db
def test_update_movie(client, add_movie):
    movie = add_movie(title="The Big Lebowski", genre="comedy", year="1998")

    # Cambiamos el año de 1998 a 1997
    resp = client.put(
        f"/api/movies/{movie.id}/",
        {"title": "The Big Lebowski", "genre": "comedy", "year": "1997"},
        content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["year"] == "1997"

@pytest.mark.django_db
@pytest.mark.parametrize("add_movie, payload, status_code", [
    ["add_movie", {}, 400],
    ["add_movie", {"title": "The Big Lebowski", "genre": "comedy"}, 400],
], indirect=["add_movie"])
def test_update_movie_invalid_json(client, add_movie, payload, status_code):
    movie = add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    resp = client.put(f"/api/movies/{movie.id}/", payload, content_type="application/json")
    assert resp.status_code == status_code
```

### B. La Vista (Verde 🟢)

Añadimos el método `put` en `MovieDetail`. Fíjate que al serializador le pasamos la `movie` (instancia actual) y los `data` (nuevos datos).

```python
    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

## 4. Diccionario de Comandos (Tu Base de Proyectos)

Ejecuta estos comandos en orden para asegurar la calidad total antes de subir a producción:

| Comando                                 | Explicación                                                                      |
| :-------------------------------------- | :------------------------------------------------------------------------------- |
| **`docker compose exec movies pytest`** | Ejecuta todos los tests. Es tu primer filtro.                                    |
| **`--cov=.`**                           | Bandera de pytest para medir cuánto código cubren tus tests (buscamos el 100%).  |
| **`flake8 .`**                          | Revisa que el código cumpla las normas de estilo PEP8 (espacios, líneas largas). |
| **`black .`**                           | Formatea automáticamente tu código para que sea estéticamente perfecto.          |
| **`isort .`**                           | Ordena alfabéticamente todos tus `imports` al principio de los archivos.         |

---

## 5. El Paso a Paso Final para el Despliegue

Una vez que los 17 tests (o los que tengas) pasen en local:

1.  **Limpieza Final:** Pasa `black` e `isort`.
2.  **Commit:** `git add .` y `git commit -m "feat: complete crud and test coverage"`.
3.  **Push:** `git push origin main`.
4.  **Verificación CI/CD:** Entra en GitHub Actions y espera al check verde ✅.
5.  **Prueba Real (Consumo de API):** Como no tenemos shell en Render, usa **Postman** o **Swagger** (en el siguiente paso) para verificar que la URL `https://tu-app.onrender.com/api/movies/` responde correctamente.

---
