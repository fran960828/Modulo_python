Esta documentación técnica se centra en uno de los procesos de seguridad más críticos de cualquier aplicación: el **Registro de Usuarios**. Aprenderás a validar datos complejos (como la comparación de contraseñas) dentro de la propia clase del formulario, manteniendo tu vista limpia y siguiendo el principio de responsabilidad única.

---

## 1. El Formulario de Registro Profesional

> **Explicación:** Cuando creamos un formulario de registro, no basta con capturar los datos; debemos validarlos. Django permite definir métodos que empiezan por la palabra `clean_`.
> * **`clean_<campo>`**: Para validar un campo específico (ej. si el nombre de usuario ya existe).
> * **`clean()`**: Para validaciones cruzadas (ej. comparar si las dos contraseñas introducidas son idénticas).
> 
> 
> Si las contraseñas no coinciden, lanzamos una `ValidationError`, lo que impide que el formulario sea considerado válido (`is_valid() == False`).

**Ejemplo en `forms.py`:**

```python
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistroForm(forms.Form):
    # Definimos los campos necesarios para el registro
    username = forms.CharField(max_length=150, label="Nombre de usuario")
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Repetir contraseña")

    # Validación específica para el nombre de usuario
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Comprobamos si el usuario ya existe en la Base de Datos
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        return username

    # Validación general (limpieza cruzada de campos)
    def clean(self):
        # Primero obtenemos los datos ya limpios de los campos individuales
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Verificamos si las contraseñas coinciden
        if password and confirm_password and password != confirm_password:
            # Si no coinciden, lanzamos el error
            raise ValidationError("Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")
        
        # Siempre debemos retornar los datos limpios
        return cleaned_data

```

---

## 2. La Vista de Registro y Renderizado

> **Explicación:** La vista tiene la misión de orquestar el proceso.
> 1. Si la petición es **GET**, simplemente muestra el formulario vacío.
> 2. Si es **POST**, le pasa los datos al formulario, comprueba `is_valid()` (que ejecutará nuestros métodos `clean`) y, si todo está bien, crea el usuario usando `create_user`.
> 
> 

**Ejemplo en `views.py`:**

```python
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegistroForm

def registro_view(request):
    # Instanciamos el formulario con datos POST o vacío si es GET
    form = RegistroForm(request.POST or None)

    if request.method == 'POST':
        # is_valid() ejecuta internamente clean_username() y clean()
        if form.is_valid():
            # Extraemos los datos ya validados y seguros
            data = form.cleaned_data
            
            # Creamos el usuario en la BD (la contraseña se encriptará sola)
            User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            
            # Redirigimos al login usando reverse para mayor profesionalidad
            return redirect(reverse('login'))

    # Si el formulario no es válido o es GET, volvemos a renderizar con los errores
    return render(request, 'registro.html', {'form': form})

```

---

## 3. El Template con manejo de errores

> **Explicación:** Django adjunta automáticamente los mensajes de error de nuestras validaciones (`ValidationError`) al objeto `form`. Al usar `form.as_p`, los errores aparecerán junto a los campos correspondientes.

**Ejemplo en `registro.html`:**

```html
{% extends "base.html" %}

{% block content %}
<main style="max-width: 400px; margin: 40px auto;">
    <h2>Únete a Conquer Blocks</h2>
    
    <form method="POST">
        {% csrf_token %}
        
        {% if form.non_field_errors %}
            <div style="color: red; margin-bottom: 10px;">
                {{ form.non_field_errors }}
            </div>
        {% endif %}

        {{ form.as_p }}

        <button type="submit" style="width: 100%; padding: 10px;">Crear Cuenta</button>
    </form>

    <p style="margin-top: 20px;">
        ¿Ya tienes cuenta? <a href="{% url 'login' %}">Inicia sesión aquí</a>
    </p>
</main>
{% endblock %}

```

---

### Verificación Profesional:

* **Seguridad de la contraseña:** Aunque en este ejemplo hemos comparado si son iguales, Django profesionalmente incluye validadores más potentes (mínimo de caracteres, no ser numérica, etc.) que se pueden configurar en `AUTH_PASSWORD_VALIDATORS` dentro de `settings.py`.
* **UX (Experiencia de Usuario):** Al pasar el objeto `form` de vuelta al template tras un error, el usuario no pierde los datos que ya escribió (excepto las contraseñas por seguridad), lo cual es fundamental para una buena experiencia.
