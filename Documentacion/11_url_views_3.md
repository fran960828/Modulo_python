Esta documentación se centra en la **reutilización de código** y la **manipulación de datos** directamente en la capa de presentación (Templates). En un entorno profesional, el objetivo es mantener el código "DRY" (*Don't Repeat Yourself*), asegurando que si cambias el menú de navegación, se actualice en las 100 páginas de tu sitio automáticamente.

---

## 1. Herencia de Plantillas: `extends` y `block`

> **Explicación:** La herencia es la joya de la corona de Django.
> * **`extends`**: Se usa al principio de un archivo hijo para decirle a Django: "Copia toda la estructura de este archivo padre".
> * **`block`**: Son "huecos" o "ventanas" que definimos en el padre para que el hijo pueda rellenarlos con su propio contenido.
> 
> 

**Ejemplo - El Padre (`base.html`):**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mi Sitio{% endblock %}</title>
</head>
<body>
    <nav>Menú de Navegación Global</nav>

    <main>
        {% block content %}
        {% endblock %}
    </main>

    <footer>Copyright 2024</footer>
</body>
</html>

```

**Ejemplo - El Hijo (`home.html`):**

```html
{% extends "base.html" %}

{% block title %}Inicio | Mi Sitio{% endblock %}

{% block content %}
    <h1>Bienvenido a la Home</h1>
    <p>Este texto se inyectará en el hueco del padre.</p>
{% endblock %}

```

---

## 2. Herramientas de Desarrollo: Extensiones de VSCode

> **Explicación:** Para programar en Django de forma profesional, necesitas autocompletado y resaltado de sintaxis. Sin estas extensiones, VSCode tratará tus archivos como HTML simple y no entenderá las etiquetas `{% %}`.

* **Django (Baptiste Darthenay):** Es la extensión "estándar". Ofrece el mejor resaltado de sintaxis y fragmentos de código (snippets).
* **Django (Robert Solis):** Excelente para el autocompletado de etiquetas de plantillas y navegación rápida entre vistas y templates.

---

## 3. Variables y Filtros (Modificación de datos)

> **Explicación:** Las **Variables** (`{{ variable }}`) muestran datos del contexto. Los **Filtros** se usan con el símbolo de tubería (`|`) para transformar ese dato antes de mostrarlo (formatear fechas, pasar a mayúsculas, etc.).

**Ejemplo - Formatear una fecha:**

```html
<p>Registrado el: {{ fecha_registro|date:"d/m/Y" }}</p>
<p>Mes de publicación: {{ fecha_registro|date:"F" }}</p>

```

### Filtros profesionales más empleados:

| Filtro | Función | Ejemplo |
| --- | --- | --- |
| `default` | Muestra un valor si la variable está vacía | `{{ user |
| `upper/lower` | Cambia a mayúsculas o minúsculas | `{{ nombre |
| `length` | Devuelve el tamaño de una lista o string | `Tienes {{ tareas |
| `truncatechars` | Corta un texto y pone "..." | `{{ bio |
| `safe` | Renderiza HTML sin escaparlo (usar con cuidado) | `{{ contenido_html |

---

## 4. Tags Personalizados: `simple_tag` e `inclusion_tag`

> **Explicación:** A veces los filtros no son suficientes. Django permite crear tus propias etiquetas de lógica.
> * **`simple_tag`**: Procesa datos y devuelve un string o valor.
> * **`inclusion_tag`**: Procesa datos y **renderiza otro pequeño template** (útil para componentes repetitivos como barras laterales o widgets).
> 
> 

**Ejemplo - Creación (`templatetags/mi_logica.py`):**

```python
from django import template
register = template.Library()

@register.simple_tag
def saludar(nombre):
    return f"Hola, {nombre}, bienvenido de nuevo."

@register.inclusion_tag('componentes/alerta.html')
def mostrar_alerta(mensaje, tipo="info"):
    # Devuelve un mini-contexto para el template 'alerta.html'
    return {'msg': mensaje, 'clase': tipo}

```

---

## 5. Estructuras de Control de Flujo

> **Explicación:** Permiten decidir qué se muestra y cómo se repite la información en el HTML.

### `if` / `elif` / `else` (Condicionales)

```html
{% if usuario.is_authenticated %}
    <p>Bienvenido, {{ usuario.username }}</p>
{% else %}
    <a href="/login">Inicia sesión</a>
{% endif %}

```

### `for` (Bucles)

```html
<ul>
    {% for tarea in lista_tareas %}
        <li>{{ forloop.counter }}. {{ tarea.titulo }}</li>
    {% empty %}
        <li>No hay tareas pendientes.</li>
    {% endfor %}
</ul>

```

### `with` (Alias de variables)

> **Explicación:** Se usa para guardar un resultado complejo en una variable corta dentro de un bloque, mejorando el rendimiento y la lectura.

```html
{% with total=carrito.productos.all.count %}
    <p>Tienes {{ total }} productos en tu cesta.</p>
{% endwith %}

```

### `include` (Fragmentación)

> **Explicación:** A diferencia de `extends`, `include` trae un trozo de HTML dentro de otro. Ideal para componentes como el `navbar.html` o `footer.html`.

```html
<body>
    {% include "includes/navbar.html" %}
    
    <h1>Contenido Principal</h1>
    
    {% include "includes/footer.html" %}
</body>

```

---

### Verificación de Calidad Profesional:

* **Modularidad:** El uso de `include` y `inclusion_tag` permite que tu código sea como piezas de LEGO.
* **Orden:** Siempre coloca tus archivos base en una carpeta `templates/` raíz y los componentes específicos en `templates/includes/` o `templates/components/`.
* **Rendimiento:** Usa `with` cuando accedas a propiedades de base de datos que se repiten mucho en el mismo template.

