## 1. Estructura de una App

Antes de definir datos, necesitamos un contenedor lógico llamado "App".

> **Explicación:** En Django, un proyecto se divide en aplicaciones independientes. El comando `startapp` crea una carpeta con la estructura necesaria (`models.py`, `views.py`, etc.).

```bash
# Comando para crear una aplicación llamada 'inventario'
python manage.py startapp inventario

```

---

## 2. Configuración del Motor de Base de Datos

Todo proyecto Django necesita saber dónde guardar la información. Esto se configura en `settings.py`.

> **Explicación:** Por defecto, Django viene con **SQLite**, un archivo local ideal para desarrollo. Sin embargo, para producción se suelen usar motores más robustos como **PostgreSQL** o **MySQL**.

```python
# settings.py

# Ejemplo de configuración por defecto (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Ejemplo conceptual para PostgreSQL (requiere instalar psycopg2)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'nombre_db',
#         'USER': 'usuario',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

```

---

## 3. Definición de Modelos (Models)

El modelo es una clase Python que representa una tabla en la base de datos.

> **Explicación:** > * **Herencia:** Deben heredar de `models.Model` para que Django les otorgue superpoderes de base de datos.
> * **Clave Única (ID):** Django crea automáticamente un campo `id` autoincremental como Primary Key, a menos que definas uno manualmente.
> * **Tipos de Datos:** Cada atributo define el tipo de columna (texto, fecha, etc.).
> 
> 

### Tipos de Campos y Atributos Especiales

* `CharField`: Para textos cortos.
* `DateField`: Para fechas.
* `ForeignKey`: Para crear relaciones (uno a muchos) con otros modelos.
* `IntegerField`: Para números enteros.
* `blank=True`: Permite que el campo esté vacío en formularios.
* `default`: Valor predefinido si no se envía nada.
* `help_text`: Texto de ayuda para el usuario en el admin.
* `unique=True`: No permite valores duplicados en esa columna.
* `verbose_name`: Un nombre legible para humanos.

### Ejemplo: Uso de Choices y TextChoices

Para campos con opciones limitadas, usamos diccionarios o la clase `TextChoices`.

```python
from django.db import models

# Definición de opciones usando TextChoices (forma profesional y moderna)
class EstadoPedido(models.TextChoices):
    PENDIENTE = 'P', 'Pendiente'
    ENVIADO = 'E', 'Enviado'
    ENTREGADO = 'D', 'Entregado'

class Producto(models.Model):
    # primary_key=True se usa si no quieres el ID automático de Django
    codigo_sku = models.CharField(max_length=20, primary_key=True, unique=True)
    
    nombre = models.CharField(
        max_length=100, 
        verbose_name="Nombre del Producto",
        help_text="Introduce el nombre comercial"
    )
    
    precio = models.IntegerField(default=0)
    
    # Uso de blank=True para que pueda no tener descripción
    descripcion = models.TextField(blank=True, null=True)
    
    # Campo con opciones predefinidas mediante TextChoices
    estado = models.CharField(
        max_length=1,
        choices=EstadoPedido.choices,
        default=EstadoPedido.PENDIENTE
    )

    # Relación con otro modelo (ForeignKey)
    # models.CASCADE significa: si se borra la categoría, se borran sus productos
    # categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

```

---

## 4. El Ciclo de las Migraciones

Las migraciones son la forma en que Django propaga los cambios de tus modelos al esquema de la base de datos.

### Paso A: `makigrations`

> **Explicación:** Examina tus archivos `models.py` y genera un archivo de "instrucciones" (en la carpeta `migrations/`) sobre qué ha cambiado. No afecta a la base de datos aún.

```bash
python manage.py makemigrations

```

### Paso B: `migrate`

> **Explicación:** Ejecuta las instrucciones pendientes. Crea las tablas físicamente en SQLite/PostgreSQL. También migra los modelos internos de Django (usuarios, sesiones, etc.).

```bash
python manage.py migrate

```

---

## 5. La Shell de Django e Instancias

La Shell es un entorno interactivo de Python que tiene cargada toda la configuración de tu proyecto. Es vital para pruebas rápidas.

> **Explicación:** Permite manipular la base de datos usando código Python directamente sin necesidad de una interfaz web.

### Creación de una instancia (Objeto)

Para crear un registro en la base de datos, seguimos estos pasos:

1. Entrar a la shell: `python manage.py shell`
2. Importar el modelo.
3. Crear y guardar el objeto.

```python
# Dentro de la shell de Django:

# 1. Importamos el modelo (asumiendo que la app se llama 'inventario')
from inventario.models import Producto, EstadoPedido

# 2. Creamos una instancia del modelo en memoria
nuevo_producto = Producto(
    codigo_sku="LAP-001",
    nombre="Laptop Gaming",
    precio=1500,
    estado=EstadoPedido.PENDIENTE
)

# 3. Guardamos en la base de datos (aquí se ejecuta el SQL INSERT)
nuevo_producto.save()

# 4. Verificación: Consultar todos los productos
todos = Producto.objects.all()
print(todos)

```

