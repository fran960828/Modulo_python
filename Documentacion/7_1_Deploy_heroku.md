Esta es la comparativa definitiva. Aunque ya hemos desplegado en Render, entender cómo lo hace Heroku te ayudará a comprender los conceptos estándar de la industria (registros de contenedores, variables de entorno dinámicas y servidores WSGI).

Aquí tienes la guía de Heroku desglosada paso a paso con explicaciones para principiantes.

---

## 1. El Servidor de Producción (Gunicorn)

En desarrollo usas `python manage.py runserver`, pero ese servidor es solo para pruebas y no soporta muchas visitas.

- **Gunicorn:** Es un servidor de grado profesional que puede manejar múltiples peticiones a la vez.
- **Acción:** Añadirlo a `requirements.txt`.
  - `gunicorn==22.0.0`: El motor que moverá tu app en la nube.
  - `psycopg2-binary`: El conector necesario para que Python hable con bases de datos PostgreSQL.

---

## 2. Dockerfile de Producción (`Dockerfile.prod`)

Este archivo es la "receta" para construir el contenedor que Heroku ejecutará.

### Explicación de las líneas clave:

- `FROM python:3.14.2-slim-bookworm`: Una versión de Python "ligera" (slim) para ahorrar espacio.
- `ENV DEBUG 0`: **Crítico.** Apaga el modo de depuración para que los usuarios no vean errores internos de tu código.
- `RUN adduser --disabled-password myuser`: Crea un usuario que no tiene permisos de administrador (root). Por seguridad, nunca debes correr aplicaciones en la nube con el usuario root.
- `CMD gunicorn drf_project.wsgi:application --bind 0.0.0.0:$PORT`:
  - **¿Qué es $PORT?** Heroku asigna un puerto aleatorio cada vez que el contenedor arranca. Esta variable le dice a Gunicorn: "Escucha en el puerto que Heroku te asigne".

---

## 3. Configuración de Base de Datos Dinámica

En local usas SQLite, pero Heroku te da una URL de base de datos Postgres que cambia con frecuencia.

### El paquete `dj-database-url`:

Permite que Django configure la base de datos automáticamente leyendo una URL (ej: `postgres://usuario:password@host:puerto/nombre`).

**Acción en `settings.py`:**

```python
import dj_database_url
DATABASE_URL = os.environ.get('DATABASE_URL')
# Esta línea traduce la URL de Heroku al formato que Django entiende
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500)
DATABASES['default'].update(db_from_env)
```

---

## 4. Despliegue con Heroku CLI

Heroku usa su propio "almacén" de imágenes (Container Registry).

### Los comandos paso a paso:

1.  `heroku create`: Crea un espacio en los servidores de Heroku para tu app. Te da una URL pública.
2.  `heroku container:login`: Abre la "puerta" para que puedas subir archivos (imágenes Docker) desde tu ordenador a Heroku.
3.  `heroku addons:create heroku-postgresql:essential-0`: Crea una base de datos Postgres real y la conecta a tu app.
4.  `docker build -f Dockerfile.prod -t registry.heroku.com/<app>/web .`:
    - Construye la imagen en tu PC y le pone una "etiqueta" (tag) con el nombre de tu app de Heroku.
5.  `docker push registry.heroku.com/<app>/web`:
    - Sube (como un "upload") esa imagen a Heroku.
6.  `heroku container:release web`:
    - Le dice a Heroku: "¡Listo! Ya tienes la imagen, ahora enciende el servidor".

---

## 5. WhiteNoise y Archivos Estáticos

Django no sabe servir archivos CSS o JS por sí solo en producción.

- **WhiteNoise:** Permite que Django sirva sus propios archivos estáticos sin necesidad de un servidor extra como Nginx.
- `python manage.py collectstatic`: Este comando busca todos los CSS/JS del proyecto y los junta en una sola carpeta (`staticfiles`) para que WhiteNoise los encuentre.

---

## 6. Migraciones y Datos (El paso final)

Igual que hicimos en Render, una vez que la app está "viva", hay que crear las tablas.

- `heroku run python manage.py migrate`: Ejecuta el comando **dentro** de los servidores de Heroku.
- `heroku run python manage.py loaddata movies.json`: Carga tus películas iniciales en la base de datos de la nube.

---

### Resumen de comandos para tu base de proyectos:

| Acción           | Comando Heroku                        | Equivalente en Render           |
| :--------------- | :------------------------------------ | :------------------------------ |
| **Crear App**    | `heroku create`                       | "New Web Service" (Panel)       |
| **Subir Código** | `docker push`                         | `git push origin main`          |
| **Migrar DB**    | `heroku run python manage.py migrate` | Pestaña "Shell" o CMD en Docker |
| **Ver Logs**     | `heroku logs --tail`                  | Pestaña "Logs"                  |
| **Abrir App**    | `heroku open`                         | Botón con URL de la app         |

**¿Qué te parece esta comparativa?** Ahora que tienes el mapa completo de ambos mundos, **¿te gustaría que configuremos los tests automáticos en GitHub para cerrar el círculo del proyecto?**
