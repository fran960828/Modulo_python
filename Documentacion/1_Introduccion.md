## Fase 1: Estructura de Directorios y Entorno Inicial

Comenzamos creando la jerarquía de carpetas necesaria para separar la configuración de despliegue (raíz) del código fuente (`app`).

1. **Crear directorios y entrar en la carpeta de código:**

   ```bash
   mkdir django-tdd-docker && cd django-tdd-docker
   mkdir app && cd app
   ```

2. **Configurar el entorno virtual (Local):**

   ```bash
   python3.14 -m venv env
   source env/bin/activate
   ```

3. **Instalar dependencias base:**

   ```bash
   (env)$ pip install django==6.0 djangorestframework==3.16.1
   ```

4. **Inicializar Proyecto y App:**
   _Nota: El punto `.` al final de startproject es crítico para evitar carpetas anidadas innecesarias._
   ```bash
   (env)$ django-admin startproject drf_project .
   (env)$ python manage.py startapp movies
   ```

---

## Fase 2: Configuración del Custom User Model

Es una práctica recomendada definir un modelo de usuario propio antes de realizar la primera migración para evitar problemas de base de datos en el futuro.

1. **Registrar Apps en `settings.py`:**
   Modifica `app/drf_project/settings.py` añadiendo las librerías y la app local:

   ```python
   # app/drf_project/settings.py

   INSTALLED_APPS = [
       "django.contrib.admin",
       "django.contrib.auth",
       "django.contrib.contenttypes",
       "django.contrib.sessions",
       "django.contrib.messages",
       "django.contrib.staticfiles",
       "rest_framework",  # nuevo
       "movies",          # nuevo
   ]
   ```

2. **Apuntar al nuevo modelo de usuario:**
   Al final de `app/drf_project/settings.py`, añade:

   ```python
   AUTH_USER_MODEL = "movies.CustomUser"
   ```

3. **Definir el modelo en `models.py`:**

   ```python
   # app/movies/models.py
   from django.contrib.auth.models import AbstractUser

   class CustomUser(AbstractUser):
       pass
   ```

---

## Fase 3: Persistencia y Verificación de Integridad

Ejecutamos las migraciones iniciales y verificamos que la base de datos SQLite refleje nuestros cambios.

1. **Generar y aplicar migraciones:**

   ```bash
   (env)$ python manage.py makemigrations
   (env)$ python manage.py migrate
   ```

2. **Verificación manual en la base de datos:**

   ```bash
   $ sqlite3 db.sqlite3
   ```

   Dentro del prompt de `sqlite>`:

   ```sqlite
   sqlite> .tables
   -- Deberías ver: movies_customuser, django_migrations, etc.

   sqlite> .schema movies_customuser
   -- Verifica que los campos (id, password, email...) coincidan.

   sqlite> .exit
   ```

---

## Fase 4: Prueba de Funcionamiento y Limpieza Local

Validamos que el servidor y el panel de administración funcionen antes de pasar al flujo de Docker.

1. **Crear Superusuario y lanzar servidor:**

   ```bash
   (env)$ python manage.py createsuperuser
   (env)$ python manage.py runserver
   ```

   - Accede a `http://localhost:8000/admin` para probar tus credenciales.
   - Detén el servidor con `Ctrl + C`.

2. **Limpieza del entorno local:**
   Desactivamos y borramos el entorno virtual, ya que Docker se encargará de esto a partir de ahora.
   ```bash
   (env)$ deactivate
   (env)$ cd ..
   rm -rf app/env
   ```

---

## Fase 5: Preparación para Docker y Git

Configuramos los archivos de requerimientos y el control de versiones.

1. **Crear `requirements.txt`:**

   ```bash
   cd app
   echo "Django==6.0" > requirements.txt
   echo "djangorestframework==3.16.1" >> requirements.txt
   cd ..
   ```

2. **Configurar `.gitignore` en la raíz del proyecto:**

   ```bash
   nano .gitignore
   ```

   Contenido del archivo:

   ```text
   __pycache__
   env
   *.sqlite3
   .DS_Store
   ```

3. **Inicializar Repositorio Git:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Django project with CustomUser"
   ```

---

### Estado actual de la estructura:

```text
django-tdd-docker/  <-- Raíz (Aquí vive Git y próximamente Dockerfile)
├── .gitignore
└── app/            <-- Código fuente
    ├── db.sqlite3
    ├── requirements.txt
    ├── manage.py
    ├── drf_project/
    └── movies/
```
