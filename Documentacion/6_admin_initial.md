## 1. Organización de Modelos en una Carpeta (Paquete de Modelos)

> **Explicación:** En proyectos grandes, tener 50 modelos en un solo archivo `models.py` es un caos. Django permite convertir ese archivo en una **carpeta** (paquete). Para que Django reconozca los modelos, la carpeta debe contener un archivo `__init__.py` donde importemos cada modelo. **Regla de oro:** El nombre de la carpeta debe ser `models`.

### Estructura de carpetas:

```text
miapp/
├── models/
│   ├── __init__.py
│   ├── producto.py
│   └── categoria.py

```

### Ejemplo de configuración:

```python
# miapp/models/producto.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)

# miapp/models/__init__.py
# IMPORTANTE: Si no importas aquí, Django no creará las migraciones.
from .producto import Producto
from .categoria import Categoria

```

---

## 2. Inserción Masiva con `bulk_create`

> **Explicación:** Si necesitas insertar 1,000 registros, hacer 1,000 veces `.save()` es ineficiente porque cada uno abre una conexión a la base de datos. `bulk_create` realiza **una sola consulta SQL** para insertar todos los objetos a la vez. Es ideal para scripts de carga de datos iniciales o demos.

```python
# Ejemplo de script para cargar datos de prueba
from miapp.models import Producto

# 1. Creamos una lista de OBJETOS en memoria (no se guardan aún)
lista_productos = [
    Producto(nombre=f"Producto de prueba {i}")
    for i in range(100)
]

# 2. Los guardamos todos de un solo golpe en la DB
# Esto es mucho más rápido que un bucle con .save()
Producto.objects.bulk_create(lista_productos)

```

---

## 3. Introducción al Admin de Django

> **Explicación:** Una de las características "estrella" de Django es su interfaz de administración automática. Es un panel web listo para usar que lee tus modelos y genera formularios para gestionar los datos sin que tengas que programar ni una línea de HTML o CSS. Es una herramienta interna para dueños del sitio o administradores.

---

## 4. Creación de un Superuser

> **Explicación:** Para entrar al panel de administración (`/admin`), necesitas un usuario con permisos totales. Este usuario no se crea desde la web, sino desde la terminal usando la herramienta de gestión de Django.

```bash
# Ejecuta este comando en tu terminal (dentro de la carpeta del proyecto)
python manage.py createsuperuser

# El sistema te pedirá:
# 1. Username (ej: admin)
# 2. Email (puedes dejarlo vacío)
# 3. Password (no se verá mientras escribes por seguridad)

```

---

## 5. Registro de Modelos en `admin.py`

> **Explicación:** Por seguridad, Django no muestra tus modelos en el panel de administración por defecto. Debes "registrarlos" explícitamente en el archivo `admin.py` de tu aplicación. Puedes hacerlo de forma simple o personalizada.

```python
# miapp/admin.py
from django.contrib import admin
from .models import Producto  # Importamos nuestro modelo

# Forma básica de registro
admin.site.register(Producto)

# Forma profesional (usando decoradores para personalizar la vista)
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id') # Columnas que se verán en el listado
    search_fields = ('nombre',)    # Añade una barra de búsqueda

```

---

## 6. Gestión de Registros en el Admin

> **Explicación:** Una vez creado el superusuario y registrados los modelos, el flujo de trabajo profesional es el siguiente:

1. **Acceso:** Arranca el servidor (`python manage.py runserver`) y ve a `http://127.0.0.1:8000/admin`.
2. **Añadir:** Verás un botón llamado **"+ Add"** al lado de cada modelo. Al pulsarlo, Django genera un formulario basado en los tipos de campos (si es `DateTimeField` pondrá un calendario, si es `ForeignKey` pondrá un desplegable).
3. **Editar:** En el listado de registros, haz clic en el nombre de cualquier objeto. Se abrirá el formulario con los datos actuales para modificarlos.
4. **Borrar:** \* **Individual:** Dentro del formulario de edición, abajo a la izquierda verás un botón rojo de "Delete".

- **Masivo:** En el listado general, selecciona varios registros mediante los checkboxes de la izquierda, elige la acción **"Delete selected..."** en el desplegable superior y pulsa "Go".

---

> **Tip de experto:** Recuerda que si cambias la estructura de carpetas de tus modelos (Punto 1), siempre debes ejecutar `python manage.py makemigrations` y `python manage.py migrate` para que Django procese la nueva ubicación de las clases.

¿Te gustaría que te enseñara cómo **personalizar visualmente** el formulario del Admin para que unos campos aparezcan al lado de otros?
