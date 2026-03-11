Esta documentación técnica está diseñada para enseñarte a comunicarte con el usuario de forma profesional. En el desarrollo web, cuando un usuario realiza una acción (como registrarse o borrar un curso), necesita una confirmación visual. El **Messages Framework** de Django permite "encolar" mensajes en una página y mostrarlos en la siguiente (tras una redirección), gestionando todo el ciclo de vida del aviso de forma automática.

---

## 1. Configuración del Framework en `settings.py`

> **Explicación:** Para que el sistema de mensajes funcione, Django necesita tres componentes trabajando en equipo: una aplicación que gestione la lógica, un middleware que guarde los mensajes en la sesión y un procesador de contexto que los haga disponibles en el HTML. Por defecto, Django ya trae esto configurado, pero es vital saber dónde están por si alguna vez heredas un proyecto que los ha eliminado.

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'django.contrib.messages', # 1. La aplicación que contiene el motor de mensajes
    # ...
]

MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware', # Necesario para guardar mensajes entre páginas
    'django.contrib.messages.middleware.MessageMiddleware', # 2. Procesa los mensajes en cada petición
    # ...
]

TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                # ...
                'django.contrib.messages.context_processors.messages', # 3. Inyecta la variable 'messages' en los HTML
            ],
        },
    },
]

```

---

## 2. Los 5 Niveles de Mensajes y sus Valores Numéricos

> **Explicación:** Django categoriza los mensajes por niveles. Cada nivel tiene un nombre (que se suele usar como clase CSS) y un valor numérico. El valor numérico es clave: Django permite configurar un **nivel mínimo** (vía `MESSAGE_LEVEL` en settings). Si el nivel del mensaje es inferior al mínimo configurado, el mensaje se ignora.

| Nivel (Tag) | Valor | Propósito Profesional                                        |
| ----------- | ----- | ------------------------------------------------------------ |
| **DEBUG**   | 10    | Notas de desarrollo (se suelen ocultar en producción).       |
| **INFO**    | 20    | Información informativa general para el usuario.             |
| **SUCCESS** | 25    | Confirmación de que una acción (póster, edición) salió bien. |
| **WARNING** | 30    | Avisos de que algo no fue del todo bien o requiere atención. |
| **ERROR**   | 40    | El nivel más alto. Notifica fallos críticos o denegaciones.  |

---

## 3. Uso en las Vistas (`views.py`)

> **Explicación:** Para enviar un mensaje, importamos el módulo `messages` y usamos el método correspondiente al nivel que deseamos.

**Ejemplo Práctico:**

```python
from django.contrib import messages
from django.shortcuts import render, redirect

def gestion_curso(request):
    # Ejemplo de un mensaje de éxito (SUCCESS - 25)
    messages.success(request, "¡El curso se ha creado correctamente!")

    # Ejemplo de un mensaje informativo (INFO - 20)
    messages.info(request, "Recuerda completar todos los campos del perfil.")

    # Ejemplo de un error (ERROR - 40)
    if not request.user.is_staff:
        messages.error(request, "No tienes permisos para realizar esta acción.")
        return redirect('home')

    return render(request, 'cursos.html')

```

---

## 4. Renderizado en los Templates (`base.html`)

> **Explicación:** Gracias al procesador de contexto, la variable `messages` está disponible en todos tus HTML. Como puede haber más de un mensaje en la cola, siempre debemos iterar sobre ellos usando un bucle `for`.

**Ejemplo Práctico:**

```html
{% if messages %}
<ul class="messages">
  {% for message in messages %} {# message.tags devuelve el nivel (success,
  error, etc.) para usarlo como clase CSS #}
  <li class="alert alert-{{ message.tags }}">{{ message }}</li>
  {% endfor %}
</ul>
{% endif %}
```

---

## 5. Prioridad y Acumulación

> **Explicación:** ¿Qué pasa si añades un `success` y un `error` a la vez? Django los mostrará en el orden en que fueron creados. Sin embargo, el valor numérico determina qué mensajes "sobreviven" según el filtro global.
> Si en `settings.py` pones `MESSAGE_LEVEL = 30`, los mensajes de tipo `SUCCESS` (25) o `INFO` (20) **no se mostrarán**, solo verás `WARNING` (30) y `ERROR` (40). Esto es muy útil para limpiar el ruido visual en entornos de producción.

**Ejemplo de cambio de nivel mínimo en `settings.py`:**

```python
from django.contrib.messages import constants as message_constants

# Solo mostraremos avisos importantes y errores de aquí en adelante
MESSAGE_LEVEL = message_constants.WARNING

```

---

### Resumen para el éxito:

1. **Vistas:** Usas `messages.success(request, "Texto")`.
2. **Redirección:** El mensaje viaja en la sesión hasta la siguiente página.
3. **Template:** Usas `{% for message in messages %}` para pintarlo.
4. **CSS:** Aprovechas `message.tags` para darle color (verde para success, rojo para error).

¿Te gustaría que personalizáramos los **Tags de los mensajes** para que coincidan exactamente con las clases de **Bootstrap** o de tu propio framework de **Sass**?
