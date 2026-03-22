Esta es la **Guía Maestra de Integración Continua (CI) con GitHub Actions**. Con este paso, cerramos el círculo: tu código se prueba, se limpia y se valida automáticamente en la nube antes de llegar a producción.

---

## 1. Conceptos de Integración Continua (CI)

La CI es un vigilante automático. Cada vez que subes código a GitHub, un servidor independiente descarga tu proyecto, construye la imagen Docker y ejecuta todos los tests. Si algo falla, el despliegue se detiene, protegiendo tu aplicación en producción.

---

## 2. Preparación del Dockerfile de Producción (`Dockerfile.prod`)

Para que los tests funcionen correctamente en GitHub Actions, necesitamos ajustar los permisos de escritura para el usuario no-root.

### Modificación de Permisos

Asegúrate de que tu `app/Dockerfile.prod` incluya la línea `chown` para evitar errores de base de datos en los tests de cobertura:

```dockerfile
# ... (instalar dependencias y copiar código)

# Crear usuario de seguridad (non-root)
RUN adduser --disabled-password myuser

# ASIGNAR PROPIEDAD: Vital para que 'myuser' pueda escribir reportes de tests (.coverage)
RUN chown -R myuser:myuser /usr/src/app

USER myuser

# Comando de inicio
CMD ["sh", "-c", "python manage.py migrate && gunicorn drf_project.wsgi:application --bind 0.0.0.0:$PORT"]
```

---

## 3. Configuración del Workflow de GitHub (`main.yml`)

Creamos el archivo en la ruta: `.github/workflows/main.yml`. Este archivo le dice a GitHub qué "receta" debe seguir.

### El archivo definitivo con Postgres:

```yaml
name: Continuous Integration

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    name: Build and Test
    runs-on: ubuntu-latest

    # Forzar Node 24 para evitar warnings de deprecación
    env:
      FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

    # LEVANTAR BASE DE DATOS REAL PARA TESTS
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: movies_test
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build Docker Image
        # Importante: El punto '.' al final indica la raíz como contexto
        run: |
          docker build \
            -f app/Dockerfile.prod \
            -t django-tdd-image \
            .

      - name: Run Tests and Linters
        # Ejecutamos el contenedor conectándolo al Postgres de GitHub
        run: |
          docker run \
            --network host \
            -e SECRET_KEY="key-secreta-de-test" \
            -e DATABASE_URL="postgres://postgres:postgres@localhost:5432/movies_test" \
            -e DEBUG=0 \
            django-tdd-image \
            sh -c "pytest --cov=. && flake8 . && black --check --exclude=migrations . && isort . --check-only"
```

---

## 4. Diccionario de Comandos y Parámetros

Para entender qué hace cada pieza de esta "maquinaria":

| Comando / Parámetro             | ¿Para qué sirve?                                                         |
| :------------------------------ | :----------------------------------------------------------------------- |
| **`on: push`**                  | Dispara el proceso automáticamente al subir cambios.                     |
| **`services: postgres`**        | Crea un contenedor temporal de base de datos real para los tests.        |
| **`--health-cmd pg_isready`**   | Asegura que la DB esté encendida antes de que Django intente conectar.   |
| **`actions/checkout@v4`**       | Copia tu código de GitHub al servidor de tests.                          |
| **`docker build -f ...`**       | Construye la imagen. Verifica que el Dockerfile no tenga errores.        |
| **`docker run --network host`** | Permite que el contenedor vea la base de datos de GitHub en `localhost`. |
| **`pytest --cov=.`**            | Ejecuta las pruebas y mide qué porcentaje de código está cubierto.       |
| **`flake8 .`**                  | Revisa que no haya errores de estilo (PEP 8).                            |
| **`black --check`**             | Verifica si el código está bien formateado sin cambiarlo.                |
| **`isort --check-only`**        | Verifica si los imports están ordenados alfabéticamente.                 |

---

## 5. El Paso a Paso del Despliegue Profesional

1.  **Limpieza Local:** Antes de subir nada, pasa los formateadores en tu PC:
    - `docker compose exec movies black .`
    - `docker compose exec movies isort .`
2.  **Subida a GitHub:** ```bash
    git add .
    git commit -m "feat: mi nueva funcionalidad"
    git push origin main
    ```

    ```
3.  **Vigilancia en GitHub Actions:** Entra en la pestaña **Actions** de tu repositorio.
    - Si ves un **Check Verde (✅)**: Tu código es seguro y Render lo desplegará automáticamente.
    - Si ves una **X Roja (❌)**: Entra en el log, corrige el error (un test fallido o un espacio de más) y vuelve a subir.

---

## 6. Bonus: Badge de Estado en el README

Para lucir tu éxito, añade esta línea al principio de tu archivo `README.md`:

```markdown
![CI Status](https://github.com/TU_USUARIO/TU_REPO/actions/workflows/main.yml/badge.svg)
```
