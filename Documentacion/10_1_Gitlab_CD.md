Esta es la **Guía Maestra de Despliegue Continuo (CD) con GitLab y Heroku**. A diferencia de la integración nativa de Render, GitLab requiere un proceso manual de "push & release" hacia el registro de Heroku, lo cual es excelente para entender qué ocurre "bajo el capó" en un despliegue profesional.

---

## 1. Concepto de CD (Continuous Delivery) en GitLab

El objetivo de esta fase es que, tras superar los tests en GitLab, la imagen Docker de producción se envíe al **Heroku Container Registry** y se active automáticamente. Esto elimina la necesidad de usar comandos manuales de Heroku desde tu PC.

---

## 2. Configuración de Credenciales (Secrets)

Para que GitLab tenga permiso de "entrar" en tu cuenta de Heroku, necesitamos configurar variables de entorno seguras.

### Obtención del Token

En tu terminal local, ejecuta el comando para obtener tu llave maestra:

```bash
heroku auth:token
```

- **¿Para qué sirve?** Es una contraseña técnica que permite a GitLab identificarse como tú ante Heroku sin usar tu email/password real.

### Configuración en GitLab

1. Ve a tu proyecto en GitLab.
2. Navega a **Settings > CI / CD > Variables**.
3. Añade una nueva variable:
   - **Key:** `HEROKU_AUTH_TOKEN`
   - **Value:** (El token que copiaste arriba).
   - **Masked:** Sí (para que no aparezca en los logs del servidor).

---

## 3. Script de Liberación (`release.sh`)

Heroku requiere un paso extra: no basta con subir la imagen, hay que decirle a la API de Heroku "usa esta imagen específica que acabo de subir".

Crea el archivo `release.sh` en la raíz de tu proyecto:

```bash
#!/bin/sh
# 1. Obtenemos el ID interno de la imagen Docker que acabamos de construir
IMAGE_ID=$(docker inspect ${HEROKU_REGISTRY_IMAGE} --format={{.Id}})

# 2. Creamos el mensaje (payload) para la API de Heroku
PAYLOAD='{"updates": [{"type": "web", "docker_image": "'"$IMAGE_ID"'"}]}'

# 3. Llamada a la API de Heroku usando cURL para activar la nueva versión
curl -n -X PATCH https://api.heroku.com/apps/$HEROKU_APP_NAME/formation \
  -d "${PAYLOAD}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/vnd.heroku+json; version=3.docker-releases" \
  -H "Authorization: Bearer ${HEROKU_AUTH_TOKEN}"
```

---

## 4. Configuración de GitLab CI (`.gitlab-ci.yml`)

Añadimos la tercera etapa (**deploy**) al archivo de configuración.

```yaml
stages:
  - build
  - test
  - deploy

# ... (etapas de build y test anteriores)

deploy:
  stage: deploy
  services:
    - docker:28.5.0-dind
  variables:
    DOCKER_DRIVER: overlay2
    HEROKU_APP_NAME: <TU_APP_NAME> # Cambia esto por el nombre en Heroku
    HEROKU_REGISTRY_IMAGE: registry.heroku.com/${HEROKU_APP_NAME}/web
  script:
    # 1. Instalamos herramientas necesarias (curl)
    - apk add --no-cache curl
    - cd app
    # 2. Construimos la imagen con el tag de Heroku
    - docker build
      --tag $HEROKU_REGISTRY_IMAGE
      --file ./Dockerfile.prod
      "."
    # 3. Login en el registro de Heroku (usuario es '_' por estándar de Heroku)
    - docker login -u _ -p $HEROKU_AUTH_TOKEN registry.heroku.com
    # 4. Subimos la imagen al registro de Heroku
    - docker push $HEROKU_REGISTRY_IMAGE
    - cd ..
    # 5. Damos permisos de ejecución al script y lanzamos el despliegue
    - chmod +x ./release.sh
    - ./release.sh
```

---

## 5. Diccionario de Comandos y Herramientas

| Comando / Herramienta   | Explicación Simple                                                                    |
| :---------------------- | :------------------------------------------------------------------------------------ |
| **`apk add curl`**      | Instala `curl` en el servidor de GitLab (necesario para hablar con la API de Heroku). |
| **`docker login -u _`** | Heroku usa el guion bajo `_` como nombre de usuario cuando usas un Token.             |
| **`docker inspect`**    | Extrae información técnica de una imagen Docker (en este caso, su ID único).          |
| **`chmod +x`**          | "Change Mode + Execute". Da permiso al sistema para ejecutar el archivo `.sh`.        |
| **`PATCH` (en curl)**   | Un tipo de petición HTTP que dice: "Actualiza solo esta parte de la configuración".   |

---

## 6. Verificación y Flujo de Trabajo

Una vez configurado, el flujo profesional es:

1.  **Push:** Subes cambios a GitLab.
2.  **Build/Test:** GitLab verifica que todo funcione.
3.  **Deploy:** Si los tests pasan, GitLab construye la imagen final, la sube a Heroku y ejecuta el `release.sh`.
4.  **Live:** Tu app está actualizada.

### Debugging Pro

Si el despliegue falla y quieres ver qué está haciendo `curl` o el script paso a paso, recuerda añadir esta variable a tu trabajo de deploy en el `.yml`:

```yaml
variables:
  CI_DEBUG_TRACE: "true"
```

**¿Ves la diferencia?** En Render, la plataforma hace el `release.sh` y el `docker login` por ti. En GitLab/Heroku, tú tienes el control total de cada paso del envío.

¿Te gustaría que ahora consolidemos todo este conocimiento en un **Cheatsheet definitivo** con todos los comandos de Docker, Git y CI/CD que hemos usado hasta ahora para que lo tengas siempre a mano?
