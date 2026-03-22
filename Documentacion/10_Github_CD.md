Esta es la **Guía Maestra de Despliegue Continuo (CD) con Render y GitHub Actions**. Aunque Render simplifica enormemente este proceso, configurarlo de forma profesional requiere sincronizar los "Checks" de calidad para evitar que un error llegue a tus usuarios.

---

## 1. Concepto de CD (Continuous Delivery) en Render

El Despliegue Continuo es la fase final donde el código, tras haber superado todas las pruebas de la fase de **CI** (Integración Continua), se publica automáticamente en el servidor. En Render, esto se gestiona mediante una conexión nativa con los estados de GitHub.

---

## 2. Configuración en el Panel de Render

Para que tu flujo sea seguro y profesional, no basta con que Render detecte el `push`; debe esperar a que los tests den el visto bueno.

### Paso a paso:

1. Entra en tu **Dashboard de Render** y selecciona tu **Web Service**.
2. Ve a la pestaña **Settings**.
3. Busca la sección **Auto Deploy**.
4. Selecciona la opción: **"After CI test checks pass"**.
5. Haz clic en **Save Changes**.

> **¿Qué sucede ahora?** Render recibirá la notificación de que has subido código, pero se quedará en estado "congelado" (_Waiting for CI_). Solo iniciará la construcción de la imagen Docker si el Job de GitHub Actions termina en verde.

---

## 3. Sincronización con `main.yml`

Para que Render sepa qué debe esperar, el archivo de configuración de GitHub debe estar correctamente estructurado. No necesitas añadir comandos de "deploy" (como `curl` o `scripts`), solo asegurar que tus tests tengan un nombre claro.

### Estructura de referencia:

```yaml
jobs:
  build: # <--- Este es el identificador que Render monitoriza
    name: Build and Test # <--- Este es el nombre visual que verás en GitHub
    runs-on: ubuntu-latest
    # ... resto de la configuración de tests y linters
```

---

## 4. El Flujo de Trabajo "Zero Downtime"

Una de las grandes ventajas de este sistema es que Render utiliza **Blue-Green Deployment** (o despliegue sin tiempo de inactividad):

1. **Construcción:** Render construye la nueva imagen Docker en segundo plano.
2. **Health Check:** Antes de apagar la versión vieja, Render verifica que la nueva versión responde correctamente.
3. **Intercambio:** Si la nueva versión está sana, Render redirige el tráfico de los usuarios a ella y apaga la antigua.

---

## 5. Cuadro de mando: ¿Qué mirar cuando algo falla?

Si haces un `push` y tu web no se actualiza, sigue este orden de diagnóstico:

| Lugar              | Qué buscar                              | Significado                                                                                    |
| :----------------- | :-------------------------------------- | :--------------------------------------------------------------------------------------------- |
| **GitHub Actions** | Una **X roja** en el commit.            | Los tests, el linter o el formato fallaron. El CD se detuvo por seguridad.                     |
| **Render Events**  | Estado **"Cancelled"** o **"Waiting"**. | Render está cumpliendo su orden de no desplegar código sin validar.                            |
| **Render Logs**    | Errores durante el `docker build`.      | El código es válido pero hay un error en el `Dockerfile.prod` o falta una variable de entorno. |

---

## 6. Comandos de Verificación (Base de Proyectos)

Para confirmar que tu CD está funcionando, puedes usar estos comandos simples en tu terminal local:

- **Ver el estado de la API:** `curl https://tu-app.onrender.com/ping/`
- **Ver los últimos cambios:** Mira el **"Latest Deploy"** en el dashboard de Render; debería coincidir con el ID de tu último commit en GitHub que tenga el check verde.

---

### Resumen de tu Hoja de Ruta Profesional

Con esto, has pasado de un despliegue manual y arriesgado a un sistema **blindado**:

- **Local:** Limpias con Black/Isort.
- **GitHub:** Validas con Pytest/Flake8.
- **Render:** Despliegas automáticamente **solo si todo lo anterior es perfecto**.

**¿Te gustaría que pasemos ahora a la parte de documentación con Swagger (drf-spectacular) para que tu API tenga una interfaz visual profesional donde probar los endpoints?**
