Esta documentación técnica aborda la **gestión de identidad y acceso**, uno de los sistemas más potentes de Django. En el desarrollo profesional, no reinventamos la rueda: utilizamos el sistema integrado de autenticación de Django para manejar usuarios, permisos y seguridad, garantizando que solo las personas autorizadas accedan a ciertas partes de **Conquer Blocks**.

---

## 1. Gestión de Usuarios y Seguridad

> **Explicación:** Django utiliza un modelo de usuario robusto. Para crear usuarios desde el código, nunca usamos `create()` (porque guardaría la contraseña como texto plano), sino `create_user()`, que la **encripta** automáticamente mediante un hash seguro.

**Ejemplo de creación y modificación:**

```python
from django.contrib.auth.models import User

# 1. Creación profesional: La contraseña se encripta automáticamente
nuevo_user = User.objects.create_user(
    username='alumno_conquer',
    email='alumno@conquer.com',
    password='password_seguro_123',
    first_name='Juan',
    last_name='Pérez'
)

# 2. Modificación de datos:
nuevo_user.first_name = 'Juan Ignacio'
# Para cambiar la contraseña, usamos este método para re-encriptarla
nuevo_user.set_password('nueva_clave_456') 
nuevo_user.save() # Siempre guardar tras modificar

```

---

## 2. Grupos y Permisos

> **Explicación:** Los permisos controlan qué puede hacer un usuario. Los grupos permiten organizar esos permisos por roles (ej: "Profesores", "Alumnos"). Django ofrece métodos específicos para gestionar estas relaciones de muchos a muchos.

* **`add()`**: Añade un permiso o grupo sin borrar los anteriores.
* **`remove()`**: Quita uno específico.
* **`set()`**: Reemplaza toda la lista actual por una nueva.
* **`clear()`**: Elimina todas las relaciones (lo deja "limpio").

```python
from django.contrib.auth.models import Group, Permission

user = User.objects.get(username='alumno_conquer')
grupo_alumnos = Group.objects.get(name='Alumnos')

# Añadir al grupo
user.groups.add(grupo_alumnos)

# Quitar todos los grupos y dejar solo uno específico
user.groups.set([grupo_alumnos])

# Borrar todos los permisos individuales
user.user_permissions.clear()

```

---

## 3. Autenticación y Sesiones (`authenticate` y `login`)

> **Explicación:** > - **`authenticate()`**: Verifica si las credenciales son correctas. Devuelve el objeto `User` si es válido o `None` si no lo es. **No inicia sesión**, solo comprueba.
> * **`login()`**: Toma el objeto `User` y crea la sesión en el navegador (la "llave" para que el usuario navegue identificado).
> 
> 

---

## 4. Implementación Profesional: Formulario y Vista de Login

> **Explicación:** Usamos una clase `Form` para capturar datos y una vista que orqueste la validación y el inicio de sesión.

**El Formulario (`forms.py`):**

```python
from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

```

**La Vista (`views.py`):**

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Obtenemos los datos limpios
            u = form.cleaned_data.get('username')
            p = form.cleaned_data.get('password')
            
            # 1. Comprobamos si el usuario existe y la clave coincide
            user = authenticate(username=u, password=p)
            
            if user is not None:
                # 2. Iniciamos la sesión
                login(request, user)
                return redirect('home') # Redirigimos a la página principal
            else:
                # Si falla, podemos añadir un error al formulario
                form.add_error(None, "Usuario o contraseña incorrectos")
                
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    # Cierra la sesión y borra las cookies
    logout(request)
    return redirect('home')

```

---

## 5. Limitadores de Acceso y Decoradores

> **Explicación:** Para proteger tus vistas (ej: que solo alumnos logueados vean el temario), usamos el decorador `@login_required`. Además, debemos configurar en `settings.py` a dónde enviar al usuario si intenta entrar sin estar logueado.

**Configuración en `settings.py`:**

```python
# Rutas a las que Django redirigirá automáticamente
LOGIN_URL = '/login/'         # A donde va si no está logueado
LOGIN_REDIRECT_URL = 'home'   # A donde va tras loguearse con éxito
LOGOUT_REDIRECT_URL = 'home'  # A donde va tras cerrar sesión

```

**Uso en la Vista:**

```python
from django.contrib.auth.decorators import login_required

@login_required # Solo permite el paso si request.user.is_authenticated es True
def zona_privada(request):
    # En el template podemos usar {{ request.user.username }}
    return render(request, 'privado.html')

```

**Uso manual en Template:**

> Si no quieres proteger toda la vista, puedes usar lógica dentro del HTML:

```html
{% if request.user.is_authenticated %}
    <p>Bienvenido, {{ request.user.first_name }} | <a href="{% url 'logout' %}">Salir</a></p>
{% else %}
    <a href="{% url 'login' %}">Iniciar Sesión</a>
{% endif %}

```
Esta es una excelente adición. En el desarrollo profesional con Django, **nunca** debemos escribir las URLs a mano (como `/home/` o `/login/`) dentro de nuestras funciones de Python. Si el día de mañana decides cambiar la URL en el `urls.py`, tendrías que buscar y reemplazar ese texto en todos tus archivos de vistas.

Para solucionar esto, utilizamos la función **`reverse`**, que busca el nombre de la ruta (el `name`) y lo convierte en la URL real.

---

### Nuevo Punto: Uso de `reverse` dentro de `redirect`

> **Explicación:** > - **`reverse()`**: Es una función que recibe el **nombre** de una ruta (o `namespace:name`) y devuelve el string de la URL física. Es el equivalente en Python a la etiqueta `{% url %}` de los templates.
> * **`redirect()`**: Es un "atajo" (*shortcut*) de Django. Si le pasas el nombre de una vista o una URL, envía al usuario allí.
> 
> 
> Al combinar ambos, o simplemente pasar el nombre de la ruta a `redirect`, nos aseguramos de que nuestra navegación sea dinámica y no se rompa si cambiamos los paths en el futuro.

#### Ejemplo Práctico: Login, Logout y Redirección Dinámica

**En tus Vistas (`views.py`):**

```python
from django.shortcuts import redirect
from django.urls import reverse # Importación fundamental
from django.contrib.auth import logout

def logout_view(request):
    # 1. Ejecutamos la lógica de cerrar sesión
    logout(request)
    
    # 2. Uso profesional de redirect con reverse:
    # En lugar de redirect('/home/'), buscamos el nombre de la ruta.
    # Esto es mucho más seguro y mantenible.
    return redirect(reverse('home'))

def login_success_view(request):
    # Ejemplo de redirección a una app con namespace
    # Si tu app de cursos tiene namespace 'courses' y la ruta 'list'
    return redirect(reverse('courses:list'))

def perfil_usuario(request, username):
    # Ejemplo de reverse con argumentos (como un ID o un Username)
    # Si la URL necesita un parámetro, se lo pasamos en 'kwargs'
    url_destino = reverse('perfil_detalle', kwargs={'nombre_usuario': username})
    return redirect(url_destino)

```

---

### Diferencia clave para el alumno:

1. **En el Template:** Usas `{% url 'nombre_ruta' %}`.
2. **En la Vista (Python):** Usas `reverse('nombre_ruta')`.
3. **Atajo de Django:** La función `redirect()` es tan inteligente que, en versiones modernas de Django, si le pasas directamente el nombre de la ruta, ella misma llama a `reverse` internamente:
* `return redirect('home')` **es equivalente a** `return redirect(reverse('home'))`.



> **Consejo Pro:** Aunque `redirect('home')` funcione solo, conocer `reverse()` es vital para otros casos donde necesitas la URL como un string (por ejemplo, para enviarla en el cuerpo de un email de confirmación o para realizar tests unitarios).

---

### Resumen de flujo en Conquer Blocks:

* El usuario hace login $\rightarrow$ `redirect(reverse('courses:all'))`.
* El usuario se equivoca $\rightarrow$ `redirect(reverse('auth:login'))`.
* El usuario hace logout $\rightarrow$ `redirect(reverse('home'))`.


