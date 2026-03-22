¡Entendido! Aquí tienes la **Guía Maestra de Despliegue de Django con Docker en Render**. Esta estructura sigue paso a paso lo que hemos vivido, desde la preparación del código hasta que la API está online.

---

## 1. Preparación de Archivos de Producción

Antes de tocar Render, el proyecto debe estar listo para el entorno de producción.

### A. Dependencias (`requirements.txt`)

Asegúrate de incluir las librerías necesarias para bases de datos externas y archivos estáticos:

- `gunicorn`: Servidor web de producción.
- `dj-database-url`: Para configurar la BD mediante una URL.
- `psycopg2-binary`: Driver para PostgreSQL.
- `whitenoise`: Para servir archivos estáticos (CSS/JS).

### B. El `Dockerfile.prod` definitivo

Usa esta estructura optimizada para Render (Contexto raíz):

```dockerfile
FROM python:3.14.2-slim-bookworm

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apt-get update && apt-get -y install gcc postgresql && apt-get clean

RUN pip install --upgrade pip
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt

COPY ./app/ .

# Clave temporal para el build de archivos estáticos
ENV SECRET_KEY "django-insecure-dummy-key"
RUN python manage.py collectstatic --noinput --settings=drf_project.settings

RUN adduser --disabled-password myuser
USER myuser

# Comando combo: Migraciones + Carga de datos + Gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py loaddata movies.json && gunicorn drf_project.wsgi:application --bind 0.0.0.0:$PORT"]
```

---

## 2. Configuración de Django (`settings.py`)

Modifica los siguientes puntos para que Django sea "Nube-Ready":

- **ALLOWED_HOSTS:** `ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1").split(" ")`
- **Base de Datos:**
  ```python
  import dj_database_url
  DATABASES = {
      "default": dj_database_url.config(
          default=os.environ.get("DATABASE_URL"),
          conn_max_age=500
      )
  }
  ```
- **Static Files (WhiteNoise):**
  ```python
  MIDDLEWARE = [
      "django.middleware.security.SecurityMiddleware",
      "whitenoise.middleware.WhiteNoiseMiddleware", # Justo aquí
      # ...
  ]
  STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
  STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
  ```

---

## 3. Preparación de Datos Locales

Para llevarte tus usuarios y pelis a la nube:

1.  **Exportar datos:** `python manage.py dumpdata movies --indent 4 > app/movies.json`
2.  **Subir cambios a GitHub:**
    ```bash
    git add .
    git commit -m "Ready for Render deploy"
    git push origin main
    ```

---

## 4. Configuración en el Dashboard de Render

### Paso 1: Crear la Base de Datos

1.  **New +** -> **PostgreSQL**.
2.  Nombre: `movies-db`.
3.  Copia la **Internal Database URL** (la usaremos ahora).

### Paso 2: Crear el Web Service

1.  **New +** -> **Web Service**.
2.  Conecta tu repositorio de GitHub.
3.  **Runtime:** `Docker`.
4.  **Advanced (Build Customization):**
    - **Root Directory:** _(Vacío)_
    - **Docker Context:** `.` (el punto)
    - **Dockerfile Path:** `app/Dockerfile.prod`

### Paso 3: Variables de Entorno (Environment Variables)

Añade estas una a una en la sección **Environment**:

| Key                      | Value                                  |
| :----------------------- | :------------------------------------- |
| **DATABASE_URL**         | _(Pega aquí la Internal URL de tu BD)_ |
| **SECRET_KEY**           | _(Tu clave de 50 caracteres)_          |
| **DEBUG**                | `0`                                    |
| **DJANGO_ALLOWED_HOSTS** | `0.0.0.0 .onrender.com`                |
| **PORT**                 | `10000`                                |
| **PYTHON_VERSION**       | `3.14.2`                               |

---

## 5. El Despliegue y Verificación

1.  **Build:** Render detectará el `Dockerfile.prod` y empezará a instalar todo.
2.  **Logs:** Busca el mensaje `166 static files copied` y `Installed 4 object(s)`.
3.  **Live:** Cuando el log diga `Listening at: http://0.0.0.0:10000`, tu app ya es pública.

### Comandos de prueba:

- **Ping:** `https://tu-app.onrender.com/ping/`
- **API:** `https://tu-app.onrender.com/api/movies/`
- **Admin:** `https://tu-app.onrender.com/admin/`

---

## 6. Mantenimiento Post-Deploy

Una vez que los datos ya están cargados, es recomendable **quitar el comando `loaddata` del Dockerfile** para evitar que en cada reinicio se sobrescriban cambios que hagas manualmente desde el Admin.

El `CMD` final de mantenimiento sería:
`CMD ["sh", "-c", "python manage.py migrate && gunicorn drf_project.wsgi:application --bind 0.0.0.0:$PORT"]`

---

**¿Te gustaría que ahora preparemos un flujo de GitHub Actions para que los tests se ejecuten automáticamente antes de que Render intente desplegar?**
