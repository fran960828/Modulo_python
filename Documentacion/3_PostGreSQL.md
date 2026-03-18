Aquí tienes la guía definitiva de la **Fase de Base de Datos (PostgreSQL)**. He integrado todos los comandos ejecutados, las correcciones de sintaxis modernas y las comprobaciones de "Sanity Check" para que tengas un flujo de trabajo profesional.

---

## Fase 10: Configuración de PostgreSQL en Docker

En esta fase, sustituimos SQLite por una base de datos relacional robusta, configurando la persistencia de datos y la sincronización entre servicios.

### 1. Actualizar Dependencias y Entorno

Añadimos el driver de Postgres para Python y las variables de conexión.

1. **Actualizar `app/requirements.txt`:**

   ```text
   Django==6.0
   djangorestframework==3.16.1
   psycopg2-binary==2.9.11
   ```

2. **Actualizar `app/.env.dev`:**
   ```text
   DEBUG=1
   SECRET_KEY=foo
   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
   SQL_ENGINE=django.db.backends.postgresql
   SQL_DATABASE=movies_dev
   SQL_USER=movies
   SQL_PASSWORD=movies
   SQL_HOST=movies-db
   SQL_PORT=5432
   DATABASE=postgres
   ```

### 2. Configuración de Django (`settings.py`)

Modificamos la conexión a base de datos para que sea dinámica.

```python
# app/drf_project/settings.py
import os

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
```

### 3. El Script de Control (`entrypoint.sh`)

Creamos el script que garantiza que Django no arranque hasta que Postgres esté listo.

1. **Crear `app/entrypoint.sh`:**

   ```bash
   #!/bin/sh
   if [ "$DATABASE" = "postgres" ]
   then
       echo "Waiting for postgres..."
       while ! nc -z $SQL_HOST $SQL_PORT; do
         sleep 0.1
       done
       echo "PostgreSQL started"
   fi
    <!-- La siguiente linea solo debe estar en desarrollo pues su papel es borrar el contenido de la base de datos -->
   python manage.py flush --no-input
   python manage.py migrate
   exec "$@"
   ```

2. **Dar permisos en el host (macOS):**
   ```bash
   chmod +x app/entrypoint.sh
   ```

### 4. Dockerfile Optimizado (Postgres + Entrypoint)

Actualizamos la imagen para incluir herramientas de compilación y red.

```dockerfile
# app/Dockerfile
FROM python:3.14.2-slim-bookworm

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
  && apt-get -y install netcat-traditional gcc postgresql \
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
```

### 5. Orquestación Global (`docker-compose.yml`)

Definimos el servicio de base de datos y la persistencia en la raíz del proyecto.

```yaml
services:
  movies:
    build: ./app
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./app/:/usr/src/app/
    ports:
      - 8009:8000
    env_file:
      - ./app/.env.dev
    depends_on:
      - movies-db

  movies-db:
    image: postgres:18
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=movies
      - POSTGRES_PASSWORD=movies
      - POSTGRES_DB=movies_dev

volumes:
  postgres_data:
```

---

## Fase 11: Ejecución y Verificación Técnica

1. **Construir y levantar el ecosistema:**

   ```bash
   docker compose up -d --build
   ```

2. **Verificar logs de sincronización:**

   ```bash
   docker compose logs -f movies
   ```

   _Debes ver: "Waiting for postgres..." -> "PostgreSQL started" -> "Apply all migrations: OK"._

3. **Inspección de base de datos (psql):**

   ```bash
   docker compose exec movies-db psql --username=movies --dbname=movies_dev
   ```

   Dentro de psql:

   - `\l` (ver base de datos `movies_dev`)
   - `\dt` (ver las 10 tablas de Django creadas)
   - `\q` (salir)

4. **Inspección del Volumen (Persistencia):**
   ```bash
   docker volume inspect django-tdd-docker_postgres_data
   ```

---

## Fase 12: Prueba de Portabilidad (Sanity Check)

Verificamos que nuestra imagen de Django sigue siendo independiente y puede funcionar fuera de Compose (con SQLite por defecto).

1. **Construir imagen independiente:**

   ```bash
   docker build -f ./app/Dockerfile -t hello_django:latest ./app
   ```

2. **Ejecutar contenedor "Lobo Solitario" en puerto 8001:**

   ```bash
   docker run -p 8001:8000 \
     -e "SECRET_KEY=please_change_me" \
     -e "DEBUG=1" \
     -e "DJANGO_ALLOWED_HOSTS=*" \
     hello_django python /usr/src/app/manage.py runserver 0.0.0.0:8000
   ```

   - Verifica en `http://localhost:8001`.

3. **Limpieza Final:**
   ```bash
   # Detener el contenedor del puerto 8001 con Ctrl+C
   docker compose down -v
   ```

---

**Estado del proyecto:** Tienes una infraestructura profesional, autogestionada y con persistencia de datos. ¿Qué quieres que hagamos ahora? ¿Te gustaría que configuremos **Pytest** para empezar con los tests o pasamos a definir los **Modelos y Serializers** de la API? Pásame el siguiente bloque de tu curso.
