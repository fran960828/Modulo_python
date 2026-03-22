Esta es la **Guía Maestra de Calidad de Código y Cobertura**. Aquí recopilamos todas las herramientas que transforman un código que "simplemente funciona" en un proyecto profesional, limpio y testeado.

---

## 1. Cobertura de Código (Code Coverage)

La cobertura mide qué porcentaje de tus líneas de código ejecutan tus tests. Sirve para encontrar "puntos ciegos" en tu lógica.

### A. Instalación y Requisitos

Añadimos `pytest-cov` a nuestro archivo `app/requirements.txt`:

- `pytest-cov`: Extensión que integra la herramienta Coverage.py con Pytest.

### B. Configuración de Exclusiones

Creamos el archivo `app/.coveragerc`. Esto sirve para no medir archivos que no tienen lógica de negocio (como configuraciones o archivos generados por Django).

```ini
[run]
omit =
    *apps.py
    *settings.py
    *urls.py
    *wsgi.py
    *asgi.py
    manage.py
    */migrations/*
    */tests/*
branch = True
```

- **branch = True**: Mide no solo líneas, sino caminos (si probaste el `True` y el `False` de cada `if`).

### C. Comandos de Ejecución

1.  **Actualizar contenedor:** `docker compose up -d --build` (Instala la nueva librería).
2.  **Correr tests con cobertura:**
    ```bash
    docker compose exec movies pytest -p no:warnings --cov=.
    ```
    - `--cov=.`: Ejecuta la cobertura en el directorio actual.
3.  **Generar reporte visual (HTML):**

    ```bash
    docker compose exec movies pytest -p no:warnings --cov=. --cov-report html
    ```

    - Crea una carpeta `htmlcov`. Puedes abrir el `index.html` para ver línea por línea qué falta por testear.

    - Uso del siguiente comando en la terminal pero no la del dev container:

    ```bash
    open app/htmlcov/index.html
    ```

---

## 2. Calidad de Estilo (Linting con Flake8)

El **Linting** analiza tu código en busca de errores de estilo (PEP 8) y errores de programación obvios (como variables no usadas).

### A. Instalación y Configuración

Añadimos `flake8` a `requirements.txt` y configuramos `app/setup.cfg`:

```ini
[flake8]
max-line-length = 119
exclude = migrations,env
```

- **max-line-length**: Permite líneas un poco más largas (estándar moderno).
- **exclude**: Evita que Flake8 pierda el tiempo revisando archivos automáticos de Django (migraciones).

### B. Ejecución

- **Comando:** `docker compose exec movies flake8 .`
  - Si hay errores, te dirá la línea y el código de error (ej: `E302`). Si no dice nada, ¡tu código está perfecto!

---

## 3. Formateo Automático (Black)

Black es "el formateador de código sin compromisos". Se encarga de que todo el código se vea idéntico, sin importar quién lo escribió.

### A. Instalación

Añadimos `black` a `requirements.txt`.

### B. Comandos Clave

1.  **Verificar sin cambiar (Check):**
    ```bash
    docker compose exec movies black --check --exclude=migrations .
    ```
2.  **Ver diferencias (Diff):**
    ```bash
    docker compose exec movies black --diff --exclude=migrations .
    ```
3.  **Aplicar cambios (¡El que usas siempre!):**
    ```bash
    docker compose exec movies black --exclude=migrations .
    ```
    - Este comando reescribe tus archivos para que luzcan perfectos.

---

## 4. Orden de Importaciones (isort)

isort organiza los `import` al principio de tus archivos alfabéticamente y por secciones (Librerías de Python, Django, y tu propio código).

### A. Comandos Clave

1.  **Verificar orden:** `docker compose exec movies isort . --check-only`
2.  **Ver cambios sugeridos:** `docker compose exec movies isort . --diff`
3.  **Aplicar orden automático:**
    ```bash
    docker compose exec movies isort .
    ```

---

## 5. El Flujo de Trabajo Profesional (Resumen)

Cuando termines una funcionalidad, antes de hacer `git push`, ejecuta este "combo" de comandos para asegurar que tu código es de 10/10:

1.  **Limpiar:**
    ```bash
    docker compose exec movies black --exclude=migrations .
    docker compose exec movies isort .
    ```
2.  **Validar:**
    ```bash
    docker compose exec movies flake8 .
    ```
3.  **Testear:**
    ```bash
    docker compose exec movies pytest --cov=.
    ```
4.  **Subir:**
    ```bash
    git add .
    git commit -m "feat: add new movie logic and clean code"
    git push origin main
    ```

---

### Recordatorio Final: `.dockerignore` y `.gitignore`

No olvides añadir estos archivos a tus listas de ignorados para no subirlos a la nube:

- `.coverage`
- `htmlcov/`
- `.pytest_cache/`

**¿Damos el paso final y configuramos GitHub Actions para que haga todo esto automáticamente cada vez que hagas un push?**
