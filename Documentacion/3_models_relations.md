

## 1. Relaciones One-to-Many (ForeignKey) y `on_delete`

> **Explicación:** Una `ForeignKey` define una relación "uno a muchos". Por ejemplo, una Empresa tiene muchos Empleados, pero un empleado pertenece a una sola empresa. El parámetro `on_delete` es obligatorio y define qué sucede con el "hijo" cuando el "padre" se elimina.
> * `CASCADE`: Si se borra el padre, se borran todos los hijos (peligroso en producción).
> * `PROTECT`: Impide borrar al padre si tiene hijos asociados (lanza un error `ProtectedError`).
> * `SET_NULL`: Pone el campo en `NULL` (requiere `null=True`).
> 
> 

```python
from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    # Relación ForeignKey: Un empleado pertenece a una empresa.
    # Si la empresa se borra, PROTECT evita que perdamos rastro del empleado accidentalmente.
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

```

---

## 2. Relaciones ManyToMany (Muchos a Muchos)

> **Explicación:** Se usa cuando múltiples registros de una tabla pueden estar asociados a múltiples registros de otra. Django crea automáticamente una **tabla intermedia** (invisible en tus modelos) para gestionar estas uniones.

```python
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    # Un proyecto tiene muchos empleados y un empleado puede estar en varios proyectos.
    empleados = models.ManyToManyField(Empleado)

```

---

## 3. Uso de `add`, `remove`, `clear` y `_set` en la Shell

> **Explicación:** Una vez definidas las relaciones, necesitamos manipularlas.
> * `add()`: Crea el vínculo en la tabla intermedia.
> * `remove()`: Rompe el vínculo específico sin borrar los objetos.
> * `clear()`: Rompe todos los vínculos de un objeto.
> * `_set`: Es el "acceso inverso". Si `Empleado` tiene la FK, `Empresa` usa `empleado_set` para ver a sus empleados.
> 
> 

```python
# Ejemplo en la Shell (python manage.py shell)

e1 = Empresa.objects.create(nombre="TechCorp")
emp1 = Empleado.objects.create(nombre="Ana", empresa=e1)
proy1 = Proyecto.objects.create(titulo="App Móvil")

# --- USO DE ADD ---
# Añadimos al empleado al proyecto (tabla ManyToMany)
proy1.empleados.add(emp1)

# --- USO DE _SET (Acceso Inverso) ---
# Obtenemos todos los empleados de la empresa 'TechCorp'
empleados_de_tech = e1.empleado_set.all()

# --- USO DE REMOVE ---
# Quitamos a Ana del proyecto, pero Ana sigue existiendo en la DB
proy1.empleados.remove(emp1)

# --- USO DE CLEAR ---
# Quitamos a TODOS los empleados de ese proyecto de un solo golpe
proy1.empleados.clear()

```

---

## 4. ManyToMany con `through` (Tablas Intermedias Personalizadas)

> **Explicación:** A veces necesitas guardar datos extra sobre la relación (ej: ¿qué rol tiene el empleado en ese proyecto?). Para eso usamos el argumento `through`.

```python
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    colaboradores = models.ManyToManyField(Empleado, through='Asignacion')

class Asignacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_inicio = models.DateField() # Dato extra en la relación
    rol = models.CharField(max_length=50) # Ejemplo: 'Líder', 'Developer'

```

---

## 5. El método `__str__`

> **Explicación:** Por defecto, Django muestra los objetos como `<QuerySet [Empleado object (1)]>`. El método `__str__` permite que el objeto se represente como una cadena de texto legible, ideal para el panel de administración y depuración.

```python
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        # Ahora en lugar de "Empleado object", veremos "Empleado: Ana"
        return f"Empleado: {self.nombre}"

```

---

## 6. Clase Meta: Comportamiento y Orden

> **Explicación:** La `class Meta` dentro de un modelo sirve para configurar opciones que no son campos de la base de datos, sino metadatos sobre cómo debe comportarse el modelo.

### Atributos más importantes de Meta:

1. `ordering`: Define el orden por defecto al consultar (ej: `['nombre']` ascendente, `['-nombre']` descendente).
2. `verbose_name`: Nombre legible para el modelo en singular.
3. `db_table`: Para renombrar la tabla en la base de datos.
4. `unique_together`: Asegura que la combinación de dos campos sea única.

```python
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    salario = models.IntegerField()

    class Meta:
        # Ordenar siempre por nombre alfabéticamente
        ordering = ['nombre']
        # Cómo se verá en el panel de administración
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

```

---

## 7. Constraints (Restricciones a nivel de DB)

> **Explicación:** Aunque puedes validar datos en formularios, las `Constraints` aseguran la integridad de los datos directamente en el motor de la base de datos (PostgreSQL, SQLite, etc.). El `CheckConstraint` es ideal para reglas lógicas.

```python
from django.db.models import CheckConstraint, Q

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()

    class Meta:
        constraints = [
            # Solo permite guardar si la edad es mayor o igual a 18
            CheckConstraint(
                check=Q(edad__gte=18), 
                name='persona_mayor_de_edad'
            ),
        ]

```

