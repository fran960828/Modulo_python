

## 1. Ejecución de Scripts en la Shell de Django

> **Explicación:** Aunque `python manage.py shell` abre una consola interactiva, a veces queremos ejecutar un archivo `.py` completo que use la configuración de Django (modelos, settings, etc.). La forma estándar de "inyectar" un script es redirigiendo la entrada o usando herramientas como `django-extensions`.

```python
# Para ejecutar un script llamado 'mi_script.py' desde la terminal:
# Opción A (Standard): python manage.py shell < mi_script.py
# Opción B (Recomendada): Usar el comando 'shell_plus' de django-extensions si está instalado.
# Opción C (Profesional): Crear un "Custom Management Command" si es una tarea recurrente.

# Ejemplo de contenido en script.py:
from myapp.models import Producto
print(f"Total de productos: {Producto.objects.count()}")

```

---

## 2. Consultas entre Modelos Relacionados (ForeignKey)

> **Explicación:** Django permite navegar entre tablas relacionadas usando el "doble guion bajo" (`__`). Podemos filtrar un objeto basado en los atributos de su padre o de su hijo.

```python
# Imagina estos modelos: Autor -> Libro (ForeignKey a Autor)

# 1. Buscar libros cuyo autor se llame "Cervantes" (Hacia "adelante")
libros = Libro.objects.filter(autor__nombre="Cervantes")

# 2. Buscar autores que hayan escrito un libro con el título "Quijote" (Hacia "atrás")
autores = Autor.objects.filter(libro__titulo="Quijote")

```

---

## 3. Uso de `related_name`

> **Explicación:** Por defecto, para acceder desde un Autor a sus Libros, Django crea un atributo llamado `libro_set`. El `related_name` redefine ese nombre para que el código sea más legible y semántico.

```python
# En models.py:
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="mis_libros")

# Uso en la shell:
autor = Autor.objects.get(id=1)
# En lugar de autor.libro_set.all(), usamos el nombre que definimos:
libros_del_autor = autor.mis_libros.all()

```

---

## 4 y 5. Agregaciones y Anotaciones (`annotate` vs `aggregate`)

> **Explicación:** > - **`aggregate`**: Devuelve un **diccionario** con un cálculo sobre todo el QuerySet (resumen final).
> * **`annotate`**: Devuelve un **QuerySet** donde cada objeto tiene un "campo extra" con el cálculo (resumen por cada fila).
> 
> 

```python
from django.db.models import Count, Avg, Sum, Max, Min

# AGGREGATE: ¿Cuál es el precio medio de TODOS los libros?
resultado = Libro.objects.aggregate(precio_medio=Avg('precio'))
# Devuelve: {'precio_medio': 25.5}

# ANNOTATE: Queremos una lista de autores y cuántos libros tiene cada uno
autores_con_conteo = Autor.objects.annotate(total_libros=Count('mis_libros'))
for a in autores_con_conteo:
    print(f"{a.nombre} tiene {a.total_libros} libros.")

```

---

## 6. Custom Managers (Heredando de `models.Manager`)

> **Explicación:** Los Managers son la interfaz por la que Django interactúa con la DB. Crear uno propio permite encapsular lógica de filtrado común para no repetir código (`DRY - Don't Repeat Yourself`).

```python
class LibroPublicadoManager(models.Manager):
    def libros_baratos(self):
        # Filtro reutilizable: libros de menos de 10€
        return self.filter(precio__lt=10)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    
    # Asignamos el manager personalizado
    objects = models.Manager() # El manager por defecto
    tienda = LibroPublicadoManager() # Nuestro manager custom

# Uso:
ofertas = Libro.tienda.libros_baratos()

```

---

## 7. Objetos Q (Operadores OR y AND complejos)

> **Explicación:** Los filtros normales de Django hacen un `AND` lógico. Si necesitas un `OR` (ej: libros que cuesten menos de 10€ **O** que sean de "Ficción"), necesitas objetos `Q`.

```python
from django.db.models import Q

# Buscar libros que: (Título contiene 'Python') O (Precio < 20)
libros = Libro.objects.filter(
    Q(titulo__icontains="Python") | Q(precio__lt=20)
)

# También permiten negación (NOT) con el símbolo ~
# Libros que NO sean de 'Ficción'
no_ficcion = Libro.objects.filter(~Q(categoria="Ficción"))

```

---

## 8 y 9. Optimización: `select_related` y `prefetch_related`

> **Explicación:** Estos métodos evitan el problema de las "consultas N+1" (hacer una consulta a la DB por cada elemento de una lista), lo cual mata el rendimiento.
> * **`select_related`**: Usa un **SQL JOIN**. Ideal para relaciones 1-1 o ForeignKey (lado "muchos a uno").
> * **`prefetch_related`**: Hace una **segunda consulta** y une los datos en Python. Ideal para ManyToMany o ForeignKey inversa (lado "uno a muchos").
> 
> 

```python
# 1. select_related (Optimiza el acceso al Autor desde el Libro)
# SQL: SELECT * FROM libro INNER JOIN autor ON ...
libros = Libro.objects.select_related('autor').all()
for l in libros:
    print(l.autor.nombre) # No hace una consulta extra a la DB aquí.

# 2. prefetch_related (Optimiza el acceso a los Libros desde el Autor)
# SQL: 1. SELECT * FROM autor; 2. SELECT * FROM libro WHERE autor_id IN (...)
autores = Autor.objects.prefetch_related('mis_libros').all()
for a in autores:
    print(a.mis_libros.count()) # Usa los datos ya cargados en memoria.

```

