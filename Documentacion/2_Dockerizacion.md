Esta es la continuación lógica de tu guía anterior. He estructurado esta "Fase de Dockerización" manteniendo el rigor técnico y añadiendo esos comandos "obvios" (como abrir Docker Desktop o verificar versiones) que son los que suelen causar fricción al principio.

---

## Fase 6: Containerización con Docker

En esta etapa, dejamos de depender de la configuración local de tu macOS para crear un entorno idéntico al de producción usando contenedores.

### 1. Verificación del Motor de Docker

Antes de ejecutar cualquier comando, asegúrate de que **Docker Desktop** está abierto y funcionando.

```bash
# Verificar versiones instaladas
docker --version
docker compose version

# Comprobar que el demonio de Docker está activo
docker ps
```

### 2. Configuración del Dockerfile (El "Plano")

Crea el archivo `Dockerfile` dentro de la carpeta `app/`. Este archivo define cómo se construye la imagen de Python.

```dockerfile
# app/Dockerfile

# 1. Imagen base oficial
FROM python:3.14.2-slim-bookworm

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# 3. Variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. Instalación de dependencias (Aprovechando la caché de Docker)
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# 5. Copiar el resto del código del proyecto
COPY . .
```

### 3. Limpieza de Construcción (.dockerignore)

Crea el archivo `.dockerignore` en `app/` para evitar copiar archivos innecesarios al contenedor.

```bash
nano app/.dockerignore
```

**Contenido:**

```text
env
.dockerignore
Dockerfile
Dockerfile.prod
```

### 4. Orquestación con Docker Compose

Crea el archivo `docker-compose.yml` en la **raíz** del proyecto (`django-tdd-docker/`). Este archivo gestiona los servicios (contenedores).

```yaml
# docker-compose.yml (en la raíz)

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
```

---

## Fase 7: Configuración de Variables de Entorno

Para que Django sea flexible y seguro, extraemos la configuración sensible a un archivo externo.

1. **Crear archivo de entorno local:**

   ```bash
   nano app/.env.dev
   ```

   **Contenido:**

   ```text
   DEBUG=1
   SECRET_KEY=foo
   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
   ```

2. **Actualizar `app/drf_project/settings.py`:**
   Añade `import os` y modifica las siguientes variables para que lean del sistema:

   ```python
   import os

   SECRET_KEY = os.environ.get("SECRET_KEY")
   DEBUG = int(os.environ.get("DEBUG", default=0))
   ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
   ```

---

## Fase 8: Construcción y Ejecución

1. **Construir la imagen (Build):**
   _(Este comando lee el Dockerfile e instala todo)_.

   ```bash
   docker compose build
   ```

2. **Levantar contenedores (Up):**
   _(El flag -d lo corre en segundo plano)_.

   ```bash
   docker compose up -d
   ```

3. **Verificación y Logs:**
   Accede a `http://localhost:8009/`. Si no carga, revisa qué está pasando dentro del contenedor:
   ```bash
   docker compose logs -f
   ```

---

## Fase 9: Reset para Base de Datos Profesional

Como el curso va a introducir **PostgreSQL**, debemos limpiar el rastro de SQLite y los contenedores actuales.

1. **Detener y eliminar contenedores/volúmenes:**

   ```bash
   docker compose down -v
   ```

2. **Eliminar la base de datos local:**

   ```bash
   rm app/db.sqlite3
   ```

3. **Commit de progreso en Git:**
   ```bash
   git add .
   git commit -m "Dockerized Django app and configured environment variables"
   ```

---

### Estado actual de la estructura:

```text
django-tdd-docker/
├── .gitignore
├── docker-compose.yml  <-- El orquestador
└── app/
    ├── .dockerignore
    ├── .env.dev        <-- Configuración sensible
    ├── Dockerfile      <-- Plano de la imagen
    ├── requirements.txt
    ├── manage.py
    └── ...
```
