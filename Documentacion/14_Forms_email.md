Esta documentación técnica aborda uno de los pilares de la interacción con el usuario en Django: la **comunicación vía e-mail**. Aprenderás no solo a enviar correos, sino a configurar un servidor real (Gmail) y a persistir esa información en tu base de datos para llevar un control profesional de tus contactos.

---

## 1. Configuración del Servidor de Correo en `settings.py`

> **Explicación:** Para que Django pueda enviar correos, necesita conectarse a un servidor SMTP (como el de Gmail). Debemos definir las credenciales y el comportamiento de seguridad en nuestro archivo de configuración.

- **`EMAIL_HOST`**: La dirección del servidor de correo (ej: `smtp.gmail.com`).
- **`EMAIL_PORT`**: El puerto de conexión (generalmente `587` para TLS).
- **`EMAIL_HOST_USER`**: Tu dirección de correo electrónico completa.
- **`EMAIL_HOST_PASSWORD`**: Tu **Contraseña de Aplicación** (no la de tu cuenta personal).
- **`EMAIL_USE_TLS`**: Booleano que activa la seguridad de la conexión.

**Ejemplo en `settings.py`:**

```python
# settings.py

# Servidor de salida de Gmail
EMAIL_HOST = 'smtp.gmail.com'
# Puerto estándar para conexiones seguras
EMAIL_PORT = 587
# Tu correo de Conquer Blocks
EMAIL_HOST_USER = 'tu-usuario@gmail.com'
# La clave de 16 caracteres generada en Google
EMAIL_HOST_PASSWORD = 'abcd efgh ijkl mnop'
# Activamos el cifrado de seguridad
EMAIL_USE_TLS = True
# Dirección por defecto que aparecerá como remitente
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

```

---

## 2. Configuración de Gmail (Seguridad y Clave de Aplicación)

> **Explicación:** Por seguridad, Google bloquea aplicaciones externas que intentan usar tu contraseña normal. Para permitir que Django envíe correos, debes seguir este flujo profesional:

1. **Verificación en dos pasos:** Actívala en tu cuenta de Google.
2. **Google Authenticator:** Instala la App en tu móvil para verificar tu identidad.
3. **Contraseña de Aplicación:** \* Ve a "Seguridad" en tu cuenta de Google.

- Busca "Contraseñas de aplicaciones".
- Dale un nombre (ej: "Django Conquer Blocks").
- Copia la clave de **16 caracteres** que te darán. **Esta es la que va en `EMAIL_HOST_PASSWORD**`.

---

## 3. La Función `send_mail`: Los 5 Parámetros

> **Explicación:** Django simplifica el envío con la función `send_mail`. Esta función requiere 5 argumentos clave para ejecutarse correctamente.

```python
from django.core.mail import send_mail

send_mail(
    'Asunto del correo',        # 1. Subject (Asunto)
    'Cuerpo del mensaje',      # 2. Message (Texto plano)
    'remitente@gmail.com',     # 3. From Email (De quién viene)
    ['destino@gmail.com'],     # 4. Recipient List (Lista de destinos)
    fail_silently=False,       # 5. Error handling (¿Explota si falla?)
)

```

1. **Subject:** El título del correo que verá el usuario.
2. **Message:** El contenido principal en texto.
3. **From Email:** El correo configurado en tu servidor.
4. **Recipient List:** Una **lista** de correos (debe ir entre corchetes `[]`).
5. **Fail Silently:** Si es `False`, Django lanzará un error si el correo no sale (ideal para desarrollo). Si es `True`, ignorará el error.

---

## 4. Ejemplo Práctico: Registro en BD + Envío de Email

> **Explicación:** En un flujo profesional, cuando un usuario rellena un formulario de contacto, primero **guardamos el contacto en el modelo** (para tener un registro histórico) y luego **enviamos el aviso por e-mail**.

**Paso A: El Modelo (`models.py`)**

```python
from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

```

**Paso B: La Vista (`views.py`)**

```python
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Contacto

def contacto_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        email_cliente = request.POST.get('email')
        mensaje = request.POST.get('message')

        # 1. Registro en la Base de Datos
        nuevo_contacto = Contacto.objects.create(
            nombre=nombre,
            email=email_cliente,
            mensaje=mensaje
        )

        # 2. Configuración del Email
        asunto = f"Nuevo contacto de {nombre} - Conquer Blocks"
        cuerpo_mensaje = f"Has recibido un mensaje de {nombre} ({email_cliente}):\n\n{mensaje}"
        email_desde = settings.EMAIL_HOST_USER
        email_para = ['tu-propio-correo@gmail.com'] # A dónde te llega el aviso

        # 3. Envío del Email
        send_mail(asunto, cuerpo_mensaje, email_desde, email_para, fail_silently=False)

        return render(request, 'contacto_exito.html', {'nombre': nombre})

    return render(request, 'contacto.html')

```

---

### Verificación Profesional:

- **Seguridad:** Nunca subas tu `EMAIL_HOST_PASSWORD` a GitHub. Usa variables de entorno (`.env`).
- **Validación:** Siempre usa `is_valid()` si estás empleando clases de formularios (`forms.Form`) antes de guardar el modelo o enviar el mail.
- **Asincronía:** En proyectos muy grandes, enviar correos puede ralentizar la web. Los profesionales usan herramientas como **Celery** para que el envío se haga "en segundo plano", pero para tu práctica actual, `send_mail` es perfecto.

¿Te gustaría que probáramos a crear un **Email en formato HTML** (con negritas, imágenes y el logo de Conquer Blocks) en lugar de solo texto plano?
