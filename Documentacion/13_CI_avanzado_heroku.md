Esta es la guía definitiva de **CI/CD Avanzado**, estructurada específicamente para el flujo de trabajo con **GitLab** y **Heroku**. Esta versión incluye la optimización de imágenes multietapa, gestión de secretos y el cumplimiento de los estándares de seguridad de Django.

---

## 1. Organización de Dependencias (Requirements)

Separamos las dependencias para evitar instalar herramientas de desarrollo en el entorno de producción, reduciendo el tamaño de la imagen y la superficie de ataque.

**`app/requirements.txt` (Producción):**

```text
Django==6.0
dj-database-url==3.0.1
djangorestframework==3.16.1
gunicorn==22.0.0
psycopg2-binary==2.9.11
whitenoise==6.11.0
```

**`app/requirements-dev.txt` (Desarrollo y CI):**
Contiene las herramientas de testing y formateo de código.

```text
-r requirements.txt
black==25.12.0
flake8==7.3.0
isort==7.0.0
pytest==9.0.2
pytest-cov==7.0.0
pytest-django==4.11.1
pytest-xdist==3.8.0
```

---

## 2. Dockerfile de Producción (Multistage)

Actualizamos `app/Dockerfile.prod` para usar una construcción multietapa. La imagen `builder` compila las dependencias y la imagen final las consume, eliminando herramientas de compilación innecesarias.

```dockerfile
############ BUILDER ############
FROM python:3.14.2-slim-bookworm as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalamos gcc para compilar dependencias de python
RUN apt-get update && apt-get -y install gcc postgresql && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt .
# Creamos "wheels" (binarios) para evitar compilar en la etapa final
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# Ejecución de Linters: si fallan, la construcción se detiene
COPY . .
RUN pip install black==25.12.0 flake8==7.3.0 isort==7.0.0
RUN flake8 .
RUN black . --check --exclude=migrations
RUN isort . --check-only

############ FINAL ############
FROM python:3.14.2-slim-bookworm

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# Argumento para pasar la SECRET_KEY durante la construcción
ARG SECRET_KEY
ENV SECRET_KEY $SECRET_KEY
ENV DJANGO_ALLOWED_HOSTS .herokuapp.com

RUN apt-get update && apt-get -y install gcc postgresql && apt-get clean

# Copiamos las wheels e instalamos
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

COPY . .

# Recopilamos archivos estáticos para WhiteNoise
RUN python manage.py collectstatic --noinput

# Seguridad: ejecutamos como usuario no-root
RUN adduser --disabled-password myuser
USER myuser

CMD gunicorn drf_project.wsgi:application --bind 0.0.0.0:$PORT
```

---

## 3. Comandos de Verificación Local

Comandos esenciales para asegurar que el entorno local y las pruebas son consistentes antes de subir a GitLab.

- **Reinicio total del entorno:**
  `docker compose down -v`
  _Sirve para detener contenedores y borrar volúmenes (incluyendo la base de datos)._
- **Construcción y arranque:**
  `docker compose up -d --build`
  _Reconstruye las imágenes con los nuevos requerimientos y levanta los servicios en segundo plano._
- **Ejecución de Pruebas (Pytest):**
  `docker compose exec movies pytest -p no:warnings --cov=.`
  _Ejecuta los tests silenciando avisos y genera el reporte de cobertura._
- **Comprobación de Estilo:**
  `docker compose exec movies flake8 .` (Errores PEP8)
  `docker compose exec movies black --exclude=migrations .` (Formato automático)
  `docker compose exec movies isort .` (Orden de importaciones)

---

## 4. Configuración de Seguridad en `settings.py`

Para cumplir con el despliegue en Heroku, añadimos lógica condicional para activar las protecciones SSL solo cuando `DEBUG` sea `False`.

```python
if not DEBUG:
    SECURE_HSTS_SECONDS = 3600
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_REFERRER_POLICY = "same-origin"
```

---

## 5. Pipeline de GitLab (`.gitlab-ci.yml`)

El archivo de CI se divide en tres etapas: construcción de la imagen, pruebas automáticas y despliegue a Heroku.

```yaml
image: docker:stable
stages:
  - build
  - test
  - deploy

variables:
  IMAGE: ${CI_REGISTRY}/${CI_PROJECT_NAMESPACE}/${CI_PROJECT_NAME}

build:
  stage: build
  services:
    - docker:28.5.0-dind
  script:
    - cd app
    - docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY
    - docker build
      --tag $IMAGE:latest
      --file ./Dockerfile.prod
      --build-arg SECRET_KEY=$SECRET_KEY "."
    - docker push $IMAGE:latest

test:
  stage: test
  image: $IMAGE:latest
  services:
    - postgres:latest
  variables:
    POSTGRES_DB: users
    POSTGRES_USER: runner
    POSTGRES_PASSWORD: runner
    DATABASE_URL: postgresql://runner:runner@postgres:5432/users
  script:
    - cd app
    - python3.14 -m venv env
    - source env/bin/activate
    - pip install -r requirements.txt
    - pip install black==25.12.0 flake8==7.3.0 isort==7.0.0 pytest==9.0.2 pytest-django==4.11.1
    # Forzamos DEBUG=1 para evitar redirecciones HTTPS durante el test
    - export DEBUG=1
    - pytest -p no:warnings
    - flake8 .
    - black . --check --exclude="migrations|env"
    - isort . --check-only --skip env
    # Forzamos DEBUG=0 para validar el checklist de despliegue
    - export DEBUG=0
    - python manage.py check --deploy --fail-level=WARNING

deploy:
  stage: deploy
  services:
    - docker:28.5.0-dind
  script:
    - cd app
    - docker build
      --tag registry.heroku.com/$HEROKU_APP_NAME/web
      --file ./Dockerfile.prod
      --build-arg SECRET_KEY=$SECRET_KEY "."
    - docker login -u _ -p $HEROKU_AUTH_TOKEN registry.heroku.com
    - docker push registry.heroku.com/$HEROKU_APP_NAME/web
    - cd ..
    - chmod +x ./release.sh
    - ./release.sh
```

### Comandos Clave del CI:

- **`export DEBUG=1`**: Permite que los tests se comuniquen con Django por HTTP normal; sin esto, los tests fallarían con un error `301` (redirección permanente a HTTPS).
- **`check --deploy --fail-level=WARNING`**: Ejecuta el chequeo de seguridad de Django. Si falta alguna configuración de producción, el pipeline falla.
- **`--build-arg SECRET_KEY=$SECRET_KEY`**: Pasa el secreto guardado en las variables de GitLab al Dockerfile durante la construcción sin dejarlo escrito en el código.

---

## 6. Gestión de Secretos en GitLab

Para que el despliegue sea exitoso y seguro:

1. Ve a **Settings > CI/CD > Variables**.
2. Añade `SECRET_KEY`: Una cadena de más de 50 caracteres (evita el símbolo `$` para que GitLab no lo interprete como variable).
3. Añade `HEROKU_AUTH_TOKEN`: Tu API Key de Heroku.
4. Añade `HEROKU_APP_NAME`: El nombre de tu aplicación en Heroku.

---

## 7. Verificación en Producción

Para confirmar que los secretos se han inyectado correctamente en Heroku, puedes entrar en el contenedor remoto:

```bash
# Entrar a la terminal de Heroku
$ heroku run sh --app tu-app-name

# Abrir el shell de Django
~ $ python manage.py shell

# Verificar la clave
>>> from django.conf import settings
>>> print(settings.SECRET_KEY)
```

Esta estructura garantiza que cada cambio subido sea analizado, probado y verificado antes de llegar al usuario final. ¿Te gustaría que procedamos con el siguiente paso de la guía?
