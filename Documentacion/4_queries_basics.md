## 1. Introducción a las Queries (Consultas)

/_ Las queries en Django son la forma de extraer datos de la base de datos utilizando el Manager de tus modelos (usualmente llamado `objects`). La unidad básica de retorno es un **QuerySet**, que es una colección de objetos que puede ser filtrada, ordenada o iterada. Una característica clave es que son **lazy** (perezosas): no tocan la base de datos hasta que realmente necesitas el dato (al iterar o imprimir).
_/

```python
# Ejemplo: Obtener el gestor de objetos de un modelo llamado 'Producto'
# Producto.objects es el punto de entrada para todas las consultas.

```

## 2. El método `all()`

/_
El método `all()` devuelve un QuerySet que contiene **todos** los registros de la tabla correspondiente al modelo. Es el equivalente a un `SELECT _ FROM tabla;` en SQL.
\*/

```python
# Obtenemos todos los libros de nuestra base de datos
todos_los_libros = Libro.objects.all()

# Al ser un QuerySet, podemos iterar sobre él
for libro in todos_los_libros:
    print(libro.titulo)

```

## 3. El método `get()`

/_
`get()` se usa para recuperar un **único objeto** que coincida con los parámetros.
**Regla de oro:** Solo úsalo con campos únicos (como el ID o un slug). Si no encuentra nada, lanza una excepción `DoesNotExist`; si encuentra más de uno, lanza `MultipleObjectsReturned`.
_/

```python
# Buscamos un usuario por su clave primaria (ID único)
try:
    usuario = Usuario.objects.get(id=1)
    print(usuario.nombre)
except Usuario.DoesNotExist:
    print("No se encontró el usuario")

```

## 4. El método `filter()`

/_
`filter()` devuelve un QuerySet que contiene los objetos que coinciden con los parámetros de búsqueda. Si no hay coincidencias, devuelve un QuerySet vacío (no da error). Es ideal para búsquedas múltiples.
_/

```python
# Buscamos todos los productos que tengan un precio de 10
productos_baratos = Producto.objects.filter(precio=10)

```

## 5. El método `exclude()`

/_
Funciona de forma opuesta a `filter()`. Devuelve un QuerySet con los objetos que **no** coinciden con los parámetros indicados.
_/

```python
# Obtenemos todos los empleados, excepto los que están en el departamento de 'RRHH'
empleados_campo = Empleado.objects.exclude(departamento='RRHH')

```

## 6. Concatenación de consultas (Chaining)

/_
Dado que la mayoría de los métodos de búsqueda devuelven un QuerySet, podemos encadenarlos uno tras otro. Esto permite crear consultas complejas de forma muy legible.
_/

```python
# Filtramos productos activos Y que NO sean de la marca 'MarcaX'
resultado = Producto.objects.filter(activo=True).exclude(marca='MarcaX')

```

## 7. Actualización: `save()` vs `update()`

/\*

- `save()`: Se usa sobre una **instancia individual** (un objeto). Actualiza todos los campos del objeto en la BD.
- `update()`: Se usa sobre un **QuerySet**. Es mucho más eficiente para cambios masivos ya que se traduce en una sola sentencia SQL.
  \*/

```python
# Caso 1: save() - Modificar un solo objeto
autor = Autor.objects.get(id=5)
autor.nombre = "Nuevo Nombre"
autor.save() # Guarda los cambios en la BD

# Caso 2: update() - Modificar muchos a la vez
# Cambiamos el estado a 'descatalogado' para todos los libros de 2010
Libro.objects.filter(anio=2010).update(estado='descatalogado')

```

## 8. Eliminación: `delete()`

/_
El método `delete()` elimina los registros de la base de datos. Se puede aplicar tanto a un objeto único como a un QuerySet completo. Ten cuidado: por defecto, Django simula el comportamiento de SQL `ON DELETE CASCADE`.
_/

```python
# Eliminar un comentario específico
comentario = Comentario.objects.get(id=10)
comentario.delete()

# Eliminar todos los registros de log antiguos (borrado masivo)
Log.objects.filter(fecha__lt='2023-01-01').delete()

```

## 9. Operadores de comparación (Field Lookups)

/\*
Django utiliza una sintaxis de doble guion bajo `__` para aplicar filtros más complejos que la igualdad simple.

- `lt` (Less Than): menor que.
- `gt` (Greater Than): mayor que.
- `lte` / `gte`: menor/mayor o igual que.
- `contains`: contiene (distingue mayúsculas).
- `icontains`: contiene (ignora mayúsculas).
  \*/

```python
# Productos con stock mayor a 50 (Greater Than)
stock_alto = Producto.objects.filter(stock__gt=50)

# Usuarios cuyo nombre contiene "Ana" (Case Insensitive)
usuarios_ana = Usuario.objects.filter(nombre__icontains="ana")

# Precios menores o iguales a 100
asequibles = Producto.objects.filter(precio__lte=100)

```

## 10. Ordenación y Recorte (Slicing)

/\*

- `order_by()`: Ordena los resultados por uno o más campos (usa `-` para orden descendente).
- `[:n]`: Slicing de Python para limitar resultados (como `LIMIT` en SQL).
- `first()` / `last()`: Atajos para obtener el primer o último elemento de un QuerySet.
  \*/

```python
# 1. Ordenar por precio de menor a mayor
libros_ordenados = Libro.objects.all().order_by('precio')

# 2. Ordenar por fecha de creación (del más reciente al más antiguo)
recientes = Libro.objects.all().order_by('-fecha_creacion')

# 3. Obtener los 5 productos más caros (Slicing)
top_5_caros = Producto.objects.all().order_by('-precio')[:5]

# 4. Obtener directamente el primer o último registro
el_primero = Producto.objects.all().order_by('nombre').first()
el_ultimo = Producto.objects.all().order_by('nombre').last()

```

---

¿Te gustaría que profundizáramos en cómo realizar consultas que involucren relaciones entre dos tablas distintas (Foreign Keys)?
