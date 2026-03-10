Esta documentación técnica está diseñada para transformar tu comprensión sobre la seguridad y el flujo de peticiones en Django. En el ámbito profesional, no escribimos código repetitivo para comprobar permisos; utilizamos **Decoradores** y **Middlewares** para interceptar peticiones y aplicar reglas de negocio de forma global y eficiente.

---

## 1. El Concepto de Decorador en Django

> **Explicación:** Un decorador es una función que envuelve a otra función para extender su comportamiento sin modificar su código fuente. En el desarrollo profesional, se usan principalmente para **Control de Acceso (Auth)**, **Caché** y **Limitación de velocidad (Rate Limiting)**. Imagínalo como un "guardia de seguridad" que intercepta al usuario antes de que entre a la "sala" (la vista).

---

## 2. Restricción de Acceso: `login_required`

> **Explicación:** Sirve para asegurar que solo usuarios autenticados vean una vista.
> * **En Funciones:** Se aplica directamente sobre la función.
> * **En Clases (CBV):** Como las clases no son funciones, usamos `method_decorator` para aplicarlo al método `dispatch`, que es el motor que decide qué método (GET, POST) ejecutar.
> 
> 

**Ejemplo Práctico:**

```python
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render

# 1. USO EN FUNCIONES (FBV)
@login_required(login_url='/login/') # Redirige si no está logueado
def mi_perfil(request):
    return render(request, 'perfil.html')

# 2. USO EN CLASES (CBV)
@method_decorator(login_required, name='dispatch') # Aplicamos al método 'dispatch'
class PanelPrivado(View):
    def get(self, request):
        return render(request, 'panel.html')

```

---

## 3. Control por Permisos: `permission_required`

> **Explicación:** Se usa cuando estar logueado no es suficiente; el usuario debe tener un permiso específico (ej: "puede_editar_cursos"). Django los maneja como `app_label.codename`.

**Ejemplo Práctico:**

```python
from django.contrib.auth.decorators import permission_required

@permission_required('cursos.add_curso', raise_exception=True)
def crear_curso(request):
    # Si el usuario no tiene el permiso 'add_curso', lanza un error 403
    return render(request, 'form_curso.html')

```

---

## 4. Lógica Personalizada: `user_passes_test`

> **Explicación:** Es el decorador más flexible. Recibe una función que devuelve `True` o `False`. Si devuelve `False`, el acceso se deniega. Ideal para comprobar si un usuario es "VIP", "Mayor de edad", etc.

**Ejemplo Práctico:**

```python
from django.contrib.auth.decorators import user_passes_test

def es_miembro_premium(user):
    # Comprobamos un atributo personalizado del modelo User o Perfil
    return user.is_authenticated and user.perfil.es_premium

@user_passes_test(es_miembro_premium)
def contenido_exclusivo(request):
    return render(request, 'premium.html')

```

---

## 5. Creación de un Decorador Custom

> **Explicación:** A veces necesitas lógica que Django no trae. Un decorador recibe la función `view_func`, define una función interna `_wrapped_view` que ejecuta la lógica y luego devuelve la vista original si todo es correcto.

**Ejemplo Práctico:**

```python
from django.http import HttpResponseForbidden

def solo_ajax(view_func):
    """Decorador que solo permite peticiones hechas vía AJAX"""
    def _wrapped_view(request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return view_func(request, *args, **kwargs) # Todo ok, pasa
        return HttpResponseForbidden("Solo se permiten peticiones AJAX") # Bloqueado
    return _wrapped_view

```

---

## 6. Middlewares: El Motor de Intercepción

> **Explicación:** Un Middleware es un sistema de "capas" que envuelve a toda la aplicación. A diferencia de un decorador (que protege una vista específica), el Middleware procesa **todas** las peticiones que entran y todas las respuestas que salen.

### Middlewares por defecto en Django:

* **SecurityMiddleware:** Aplica mejoras de seguridad (XSS, redirección HTTPS).
* **SessionMiddleware:** Gestiona las sesiones (quién es el usuario entre páginas).
* **AuthenticationMiddleware:** Asocia el objeto `request.user` al usuario que inició sesión.
* **CsrfViewMiddleware:** Protege contra ataques de falsificación de peticiones (CSRF) validando tokens en formularios.

---

## 7. Creación de un Middleware Custom

> **Explicación:** Un middleware profesional es una clase con un método `__call__`. Se usa para tareas globales como registrar logs de visitas, mantenimiento del sitio o geolocalización.

**Ejemplo: Middleware para registrar la IP de cada petición**

```python
# En un archivo llamado middlewares.py
class RegistroIpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # --- Lógica ANTES de que la petición llegue a la vista ---
        ip = request.META.get('REMOTE_ADDR')
        print(f"Petición desde la IP: {ip}")

        response = self.get_response(request) # Llama a la vista

        # --- Lógica DESPUÉS de que la vista responda ---
        return response

```

### Cómo activarlo en `settings.py`:

Debes añadir la ruta de tu clase al final de la lista `MIDDLEWARE`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... otros middlewares ...
    'miapp.middlewares.RegistroIpMiddleware', # Tu middleware custom
]

```

---

### Resumen para el éxito:

* Usa **Decoradores** para reglas que cambian de una página a otra.
* Usa **Middlewares** para reglas que deben aplicarse a todo el sitio web sin excepción.

