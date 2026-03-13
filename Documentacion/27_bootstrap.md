Esta documentación técnica está diseñada para enseñarte a transformar los formularios nativos de Django (que por defecto son bastante feos) en componentes profesionales, modernos y estilizados. En el desarrollo profesional, no perdemos tiempo escribiendo HTML para cada campo del formulario; utilizamos **Django Crispy Forms**. Esta herramienta actúa como un "filtro" que inyecta automáticamente las clases y la estructura de **Bootstrap 5** en tus formularios de Django de forma elegante y mantenible.

---

## 1. Instalación de Crispy Forms y Bootstrap 5

> **Explicación:** Django Crispy Forms es el motor principal, pero para que funcione con la última versión de Bootstrap, necesitamos un "paquete de plantillas" (template pack) específico llamado `crispy-bootstrap5`. Instalamos ambos para asegurar la compatibilidad total.

**Instalación con Pipenv:**

```bash
pipenv install django-crispy-forms
pipenv install crispy-bootstrap5

```

---

## 2. Configuración en `settings.py`

> **Explicación:** Debemos registrar las aplicaciones instaladas y decirle a Django que use específicamente el motor de Bootstrap 5 para renderizar los formularios. Es un paso crítico; si no se configura, Crispy intentará usar versiones antiguas de Bootstrap.

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'crispy_forms',          # El motor principal de Crispy
    'crispy_bootstrap5',     # El paquete de plantillas para Bootstrap 5
    # ...
]

# Definimos que Bootstrap 5 será nuestro pack de diseño por defecto
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

```

---

## 3. Uso en Templates: `crispy` y `load`

> **Explicación:** Para usar Crispy en tus archivos HTML, primero debes cargar su librería de etiquetas con `{% load crispy_forms_tags %}`. Luego, en lugar de usar `{{ form.as_p }}`, usas el filtro `| crispy`. Esto hará que Django genere el HTML siguiendo las reglas exactas de Bootstrap 5 (divs con clase `mb-3`, etiquetas `label` correctas y clases `form-control` en los inputs).

**Ejemplo en `registro.html`:**

```html
{% load crispy_forms_tags %} {% block content %}
<div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-6 card p-4 shadow">
      <h2 class="text-center mb-4">Registro de Usuario</h2>

      <form method="post">
        {% csrf_token %} {{ form|crispy }}

        <div class="d-grid gap-2 mt-3">
          <button type="submit" class="btn btn-primary">Registrarse</button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```

---

## 4. Personalización con Clases de Bootstrap en `forms.py`

> **Explicación:** Aunque Crispy hace el 90% del trabajo, a veces queremos añadir clases específicas de Bootstrap a un campo concreto (como cambiar el tamaño del input o añadir un placeholder). Para ello, usamos el atributo `widget` dentro de la definición del formulario.

**Ejemplo en `forms.py`:**

```python
from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={
            # Añadimos clases de Bootstrap manualmente si fuera necesario
            'class': 'form-control-lg',
            'placeholder': 'Ej: juan_perez'
        })
    )

    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'placeholder': 'correo@ejemplo.com'
        })
    )

    # Nota: Crispy detectará automáticamente el tipo de campo y aplicará
    # las clases .form-control (para texto) o .form-check-input (para checkboxes)

```

---

## 5. El "FormHelper": Control Total (Nivel Pro)

> **Explicación:** Si quieres ir un paso más allá, puedes usar la clase `FormHelper`. Esto te permite definir la estructura del formulario (botones, filas, columnas) directamente desde el código Python de tu formulario, manteniendo el HTML del template totalmente limpio.

**Ejemplo avanzado en `forms.py`:**

```python
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class RegistroFormProfesional(forms.Form):
    # ... campos del formulario ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # Creamos una fila con dos columnas usando Bootstrap
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            'password',
            Submit('submit', 'Crear Cuenta', css_class='btn-success w-100')
        )

```

### Resumen del flujo de trabajo:

1. **Instalar** Crispy y el pack de Bootstrap 5.
2. Configurar **`CRISPY_TEMPLATE_PACK`** en settings.
3. En el HTML: **`{% load crispy_forms_tags %}`**.
4. Renderizar con **`{{ form|crispy }}`**.

¿Te gustaría que viéramos cómo aplicar estilos específicos de **Bootstrap** para que los mensajes de error de los formularios aparezcan con el estilo de "invalid-feedback" de color rojo automáticamente?
