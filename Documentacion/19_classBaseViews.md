¡Hola! Como experto en Django, te doy la bienvenida al potente mundo de las **Class-Based Views (CBV)**.

Las vistas basadas en clases no son solo una alternativa a las funciones; son una forma de aplicar el principio **DRY (Don't Repeat Yourself)** al máximo, aprovechando la herencia de Python para reutilizar lógica común (como renderizar un formulario o borrar un objeto).

Aquí tienes la guía definitiva para dominarlas.

---

## 1. Introducción a las Class-Based Views (CBV)

/_
Las CBV permiten organizar la lógica de tu aplicación en clases en lugar de funciones.
Su principal ventaja es la **extensibilidad**: puedes heredar de clases existentes de Django
que ya tienen programada la lógica para tareas comunes (listar, crear, ver detalles),
reduciendo drásticamente la cantidad de código que escribes.
_/

---

## 2. La clase base: `View`

/_
Es la madre de todas las vistas. Se usa cuando necesitas un control total sobre la petición
y la respuesta, pero quieres separar la lógica según el método HTTP (GET, POST, etc.).
En `urls.py`, se usa `.as_view()` para que Django la trate como una función.
_/

```python
# views.py
from django.views import View
from django.http import HttpResponse

class MiVistaBasica(View):
    # El método 'get' maneja peticiones GET automáticamente
    def get(self, request):
        return HttpResponse("Hola desde una CBV básica")

# urls.py
from django.urls import path
from .views import MiVistaBasica

urlpatterns = [
    # .as_view() convierte la clase en una función ejecutable por el servidor
    path('basica/', MiVistaBasica.as_view(), name='basica'),
]

```

---

## 3. Renderizando plantillas: `TemplateView`

/_
Se utiliza cuando solo quieres mostrar un archivo HTML estático o con poca lógica.
Es mucho más limpia que usar `render()` en una función.
_/

```python
# views.py
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html" # Solo definimos la ruta del template

# urls.py
path('home/', HomeView.as_view(), name='home'),

```

---

## 4. `TemplateView` con contexto personalizado

/_
A menudo necesitamos pasar datos (variables) al HTML. Para ello, sobrescribimos
el método `get_context_data`.
_/

```python
class SaludoView(TemplateView):
    template_name = "saludo.html"

    def get_context_data(self, **kwargs):
        # Llamamos al contexto original para no perder datos existentes
        context = super().get_context_data(**kwargs)
        # Añadimos nuestra información extra
        context['mensaje'] = "Bienvenido a mi plataforma"
        context['hora'] = "12:00 PM"
        return context

```

---

## 5. Redirecciones rápidas: `RedirectView`

/_
Sirve para redirigir al usuario a otra URL de forma interna o externa.
_/

```python
from django.views.generic import RedirectView

class GoogleRedirectView(RedirectView):
    url = 'https://www.google.com' # URL externa o absoluta

class LocalRedirectView(RedirectView):
    pattern_name = 'home' # Redirige usando el 'name' definido en urls.py

```

---

## 6. Ver un objeto específico: `DetailView`

/_
Busca automáticamente un objeto en la base de datos usando un identificador (normalmente `pk` o `slug`)
proporcionado en la URL y lo envía al template.
_/

```python
#
from django.views.generic import DetailView
from .models import Articulo

class ArticuloDetalle(DetailView):
    model = Articulo # Especificamos el modelo
    template_name = "articulo_ver.html"
    # Por defecto, en el HTML el objeto se llama 'object' o 'articulo'

```

---

## 7. Listar elementos: `ListView`

/_
Ideal para mostrar tablas o listas de objetos. Permite renombrar la variable
que recibe el template y añadir contexto extra de forma sencilla.
_/

```python
from django.views.generic import ListView
from .models import Producto

class ListaProductos(ListView):
    model = Producto
    template_name = "productos.html"

    # Por defecto se llama 'object_list'. Aquí lo cambiamos a 'mis_productos':
    context_object_name = "mis_productos"

    # Pasar información extra (ej. un título)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = "Catálogo de Temporada"
        return context

# En el template (productos.html) llamaríamos a:
# {% for p in mis_productos %} ... {% endfor %}

```

---

## 8. Procesar formularios: `FormView`

/_
Se encarga de mostrar un formulario y procesarlo si es válido. No está atada
necesariamente a un modelo de base de datos.
_/

```python
from django.views.generic import FormView
from .forms import ContactoForm
from django.urls import reverse_lazy

class ContactoView(FormView):
    template_name = "contacto.html"
    form_class = ContactoForm
    success_url = reverse_lazy('gracias') # Donde ir si el formulario es correcto

    def form_valid(self, form):
        # Aquí ejecutamos lógica (ej. enviar email) antes de redirigir
        form.send_email()
        return super().form_valid(form)

```

---

## 9. Crear registros: `CreateView` y `reverse_lazy`

/_
Crea un nuevo registro en la base de datos. Usamos `reverse_lazy` porque las URLs
pueden no estar cargadas cuando el archivo de vistas se procesa; `reverse_lazy`
espera hasta que se necesite la redirección.
_/

```python
from django.views.generic import CreateView
from .models import Tarea
from django.urls import reverse_lazy

class TareaCreate(CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion'] # Campos que saldrán en el form
    success_url = reverse_lazy('lista_tareas') # Redirección tras éxito

```

---

## 10. Editar registros: `UpdateView`

/_
Es casi idéntica a `CreateView`, pero requiere que la URL incluya la clave primaria (`pk`)
del objeto que queremos editar.
_/

```python
# views.py
from django.views.generic import UpdateView

class TareaUpdate(UpdateView):
    model = Tarea
    fields = ['titulo', 'completada']
    template_name_suffix = "_update_form" # Busca: tarea_update_form.html
    success_url = reverse_lazy('lista_tareas')

# urls.py
# Es OBLIGATORIO pasar el <int:pk>
path('editar/<int:pk>/', TareaUpdate.as_view(), name='editar_tarea'),

```

---

## 11. Eliminar registros: `DeleteView`

/_
Muestra una página de confirmación (vía GET) y borra el objeto (vía POST).
También requiere el `pk` en la URL.
_/

```python
from django.views.generic import DeleteView

class TareaDelete(DeleteView):
    model = Tarea
    template_name = "tarea_confirm_delete.html"
    success_url = reverse_lazy('lista_tareas')

```

---

### Resumen de conceptos clave

| Clase            | Propósito                     | Requisito en URL |
| ---------------- | ----------------------------- | ---------------- |
| **View**         | Control total / Lógica manual | Cualquiera       |
| **TemplateView** | Mostrar HTML estático/simple  | Cualquiera       |
| **ListView**     | Listar muchos objetos         | Cualquiera       |
| **DetailView**   | Ver un objeto único           | `pk` o `slug`    |
| **CreateView**   | Formulario para crear         | Cualquiera       |
| **UpdateView**   | Formulario para editar        | `pk` o `slug`    |
| **DeleteView**   | Confirmar y borrar            | `pk` o `slug`    |

¿Te gustaría que profundicemos en cómo personalizar el comportamiento de los formularios dentro de `CreateView` o cómo aplicar permisos de usuario a estas vistas?
