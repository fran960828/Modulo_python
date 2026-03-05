

## 1. Introducción al uso de Formularios

> **Explicación:** Un formulario es el puente de comunicación entre el usuario y el servidor. Permite al usuario enviar datos (texto, archivos, opciones) que Django procesará. En la web existen dos métodos principales:
> * **GET:** Los datos viajan en la URL (visibles). Se usa para **consultas o búsquedas**.
> * **POST:** Los datos viajan en el cuerpo de la petición (ocultos). Se usa para **crear o modificar datos**.
> 
> 

---

## 2. Formularios GET Manuales (Manejo de "Bajo Nivel")

> **Explicación:** Podemos manejar formularios escribiendo el HTML a mano y extrayendo los datos directamente del objeto `request.GET`.
> **Por qué es una mala práctica:** No hay validación automática. Si el usuario envía datos maliciosos o vacíos, el servidor podría fallar. Además, obliga a escribir mucho código repetitivo y es propenso a errores de seguridad como la inyección de código.

**Ejemplo en `views.py`:**

```python
def buscar_noticia_manual(request):
    # Extraemos el valor directamente del diccionario GET usando la 'name' del input
    criterio = request.GET.get('titulo_buscado', '') 
    
    # Realizamos la query basándonos en ese dato crudo
    resultados = Noticia.objects.filter(titulo__icontains=criterio)
    
    # Pasamos los resultados al context
    return render(request, 'busqueda.html', {'resultados': resultados, 'query': criterio})

```

**Ejemplo en `template.html`:**

```html
<form method="GET">
    <input type="text" name="titulo_buscado" placeholder="Escribe el título...">
    <button type="submit">Buscar</button>
</form>

{% if resultados %}
    <p>Resultados para: {{ query }}</p>
    <ul>
    {% for noticia in resultados %}
        <li>{{ noticia.titulo }}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>No se encontraron noticias que coincidan.</p>
{% endif %}

```

---

## 3. Clases `Form` para Peticiones GET

> **Explicación:** Django permite definir formularios como clases. Esto automatiza la creación del HTML y la lectura de datos.
> **Ventajas:** Reutilización de código, generación automática de HTML, y una estructura más limpia.

**Definición en `forms.py`:**

```python
from django import forms

class BusquedaForm(forms.Form):
    # Definimos el campo y sus reglas
    query = forms.CharField(label="Buscar", max_length=100, required=False)

```

**Uso en `views.py`:**

```python
def buscar_con_clase(request):
    # Instanciamos el formulario pasándole los datos del GET
    form = BusquedaForm(request.GET)
    
    # Accedemos a los datos crudos a través de .data (No recomendado para POST, pero útil en GET simple)
    # Buscamos la clave 'query' que definimos en la clase
    termino = form.data.get('query', '')
    
    noticias = Noticia.objects.filter(titulo__icontains=termino)
    
    return render(request, 'busqueda_pro.html', {
        'form': form, 
        'noticias': noticias
    })

```

---

## 4. El método `as_p`

> **Explicación:** Cuando pasas una instancia de formulario al template, Django puede renderizarlo automáticamente. `as_p` envuelve cada campo en una etiqueta `<p>`, ahorrándote escribir los `<label>` e `<input>` uno por uno.

**Uso en Template:**

```html
<form method="GET">
    {{ form.as_p }}
    <button type="submit">Enviar</button>
</form>

```

---

## 5. Seguridad POST: CSRF Token

> **Explicación:** Las peticiones POST son sensibles (cambian datos). Django requiere obligatoriamente la etiqueta `{% csrf_token %}` dentro del formulario. Esto genera un código único que evita ataques de tipo "Cross-Site Request Forgery", asegurando que los datos vienen de tu propia web y no de un sitio malicioso.

---

## 6. Manejo Profesional de Formularios POST

> **Explicación:** El flujo profesional implica:
> 1. Instanciar con `request.POST`.
> 2. Validar con `is_valid()` (esto ejecuta validadores del modelo y del formulario).
> 3. Usar `cleaned_data` para obtener datos ya limpios y convertidos a tipos de Python (ej: un string de fecha convertido a objeto `datetime`).
> 
> 

**Ejemplo en `views.py`:**

```python
from .forms import ContactoForm

def contacto_view(request):
    exito = False
    
    if request.method == 'POST':
        # Pasamos los datos enviados por el usuario a la clase
        form = ContactoForm(request.POST)
        
        # is_valid() comprueba longitud, tipos de datos y validadores personalizados
        if form.is_valid():
            # Los datos en cleaned_data son seguros y ya están validados
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            
            # Aquí iría la lógica (ej: enviar email o guardar en BD)
            print(f"Mensaje de {nombre}: {mensaje}")
            
            exito = True
            # Limpiamos el formulario para que no se reenvíe
            form = ContactoForm() 
    else:
        # Si es GET, enviamos el formulario vacío
        form = ContactoForm()

    return render(request, 'contacto.html', {
        'form': form,
        'exito': exito
    })

```

**Ejemplo en Template (`contacto.html`):**

```html
<h1>Contáctanos</h1>

{% if exito %}
    <div style="color: green;">¡El formulario se envió con éxito!</div>
{% endif %}

<form method="POST">
    {% csrf_token %}
    
    {{ form.as_p }}
    
    <button type="submit">Enviar Mensaje</button>
</form>

```

---

### Resumen Profesional:

* **GET** para buscar, **POST** para guardar.
* Usa siempre **clases de formularios**; el manejo manual es para prototipos rápidos pero inseguros.
* `is_valid()` es tu mejor amigo: nunca confíes en los datos del usuario hasta que esta función devuelva `True`.
* `cleaned_data` te entrega los datos listos para operar en Python sin errores de formato.

