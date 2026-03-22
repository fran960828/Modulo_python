Esta es la **Guía Maestra de Integración Continua (CI) con GitLab**. A diferencia de GitHub Actions, GitLab utiliza un enfoque basado en un **Registro de Contenedores propio**, lo que permite construir la imagen una sola vez y reutilizarla en todas las etapas.

---

## 1. Conceptos Clave de GitLab CI

En GitLab, todo se define en un único archivo llamado `.gitlab-ci.yml`. La gran diferencia aquí es que GitLab separa el proceso en **Stages** (Etapas) y utiliza el concepto de **Docker-in-Docker (dind)** para construir imágenes dentro de sus propios servidores.

---

## 2. Configuración del Archivo `.gitlab-ci.yml`

Este archivo debe ir en la **raíz de tu proyecto**. A continuación, el código desglosado y explicado:

```yaml
# Definimos la imagen base que usará GitLab para correr los comandos
image: docker:stable

# Definimos el orden de ejecución
stages:
  - build
  - test

# Variables globales para todo el proceso
variables:
  # Ruta automática de la imagen en el registro de GitLab
  IMAGE: ${CI_REGISTRY}/${CI_PROJECT_NAMESPACE}/${CI_PROJECT_NAME}

# --- ETAPA 1: CONSTRUCCIÓN ---
build:
  stage: build
  services:
    - docker:28.5.0-dind # Docker-in-Docker: permite usar comandos docker dentro de GitLab
  variables:
    DOCKER_DRIVER: overlay2
  script:
    - cd app
    # 1. Login automático en el registro de GitLab
    - docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY
    # 2. Intentar bajar la imagen anterior para usarla como caché (ahorra tiempo)
    - docker pull $IMAGE:latest || true
    # 3. Construir la imagen de producción
    - docker build
      --cache-from $IMAGE:latest
      --tag $IMAGE:latest
      --file ./Dockerfile.prod
      "."
    # 4. Subir la imagen recién creada al registro de GitLab
    - docker push $IMAGE:latest

# --- ETAPA 2: PRUEBAS ---
test:
  stage: test
  # Usamos la imagen que acabamos de subir en la etapa anterior
  image: $IMAGE:latest
  services:
    - postgres:latest # Levanta una DB Postgres vinculada
  variables:
    POSTGRES_DB: users
    POSTGRES_USER: runner
    POSTGRES_PASSWORD: runner
    # URL de conexión (el host es 'postgres' por el nombre del servicio)
    DATABASE_URL: postgresql://runner:runner@postgres:5432/users
  script:
    - cd app
    # Ejecución de todo el combo de calidad
    - pytest -p no:warnings --cov=.
    - flake8 .
    - black --check --exclude=migrations .
    - isort . --check-only
```

---

## 3. Diccionario de Comandos y Acciones (Explicación para Principiantes)

Aquí tienes el porqué de cada línea, para que entiendas la lógica detrás de la automatización:

| Comando / Variable       | Explicación Simple                                                                              |
| :----------------------- | :---------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------- |
| **`docker login`**       | Identifica tu servidor ante GitLab para que te permita guardar la imagen allí.                  |
| **`$CI_JOB_TOKEN`**      | Una contraseña temporal que GitLab genera solo para ese proceso. Es muy segura.                 |
| \*\*`docker pull ...     |                                                                                                 | true`\*\* | "Trae la imagen vieja si existe, si no existe (primera vez), no des error y sigue". |
| **`--cache-from`**       | Le dice a Docker: "No instales todo de cero, usa lo que ya estaba instalado si no ha cambiado". |
| **`docker push`**        | Sube tu "contenedor listo" a la nube de GitLab.                                                 |
| **`services: postgres`** | Crea una base de datos real para que los tests no se hagan en el aire.                          |
| **`DATABASE_URL`**       | La dirección donde Django buscará la base de datos de test.                                     |

---

## 4. Paso a Paso para Implementarlo

1.  **Registro:** Crea una cuenta en GitLab y sube tu repositorio.
2.  **Archivo de Configuración:** Crea `.gitlab-ci.yml` en la raíz.
3.  **Dockerfile:** Asegúrate de que tu `Dockerfile.prod` tenga el `chown` que añadimos antes para evitar errores de permisos en la etapa de `test`.
4.  **Push:** ```bash
    git add .gitlab-ci.yml
    git commit -m "ci: add gitlab pipeline configuration"
    git push origin master
    ```

    ```
5.  **Monitorizar:** Ve a la sección **CI/CD > Pipelines** en GitLab. Verás cómo se ejecutan las dos etapas (Build y Test).

---

## 5. El Badge de GitLab (Estado del Proyecto)

Para mostrar si tu proyecto está pasando los tests en tu `README.md`, añade:

```markdown
# Mi Proyecto Django TDD

[![pipeline status](https://gitlab.com/TU_USUARIO/TU_REPO/badges/master/pipeline.svg)](https://gitlab.com/TU_USUARIO/TU_REPO/commits/master)
```

---

## 6. Depuración (Si algo falla)

Si un trabajo falla y no entiendes por qué, puedes activar el rastreo detallado añadiendo esta variable al trabajo que quieras investigar:

```yaml
variables:
  CI_DEBUG_TRACE: "true"
```

_Esto mostrará cada comando que ejecuta GitLab paso a paso en el log._

---

### Comparativa Rápida: GitHub vs GitLab

- **GitHub Actions:** Más sencillo de configurar si ya usas GitHub. Usa una máquina virtual y suele correr todo en pasos seguidos.
- **GitLab CI:** Más potente para equipos grandes. Su punto fuerte es el **Registry integrado**, donde guardas tus propias imágenes Docker de forma privada y gratuita.

**¿Qué te parece tener ambas opciones?** Ahora tienes una base sólida para cualquier empresa que use una u otra herramienta. ¿Te gustaría que cerremos esta fase de guías con un "Cheatsheet" resumen de todos los comandos de Docker que hemos usado hasta ahora?
