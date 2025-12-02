```py
# DOCUMENTACIÓN DEL TUTORIAL DE SQLITE CON PYTHON PARA PRINCIPIANTES

# Este script documenta los pasos clave para interactuar con bases de datos SQLite utilizando el módulo estándar de Python 'sqlite3'.
# SQLite es útil para aplicaciones pequeñas o medianas, para pruebas o para prototipos, ya que la base de datos reside en un archivo simple en disco o en la memoria.
# No es necesario instalar nada, ya que 'sqlite3' es parte de la biblioteca estándar de Python.

################################################################################
# 1. CONFIGURACIÓN INICIAL Y CONEXIÓN
################################################################################

# Importamos el módulo 'sqlite3'.
import sqlite3

# Explicación: Para comenzar a trabajar con SQLite, necesitamos establecer una conexión.
# El método `connect()` crea un objeto de conexión. Podemos pasarle el nombre de un archivo
# para almacenar la base de datos (si el archivo no existe, lo crea automáticamente).
# Opcionalmente, podemos crear una base de datos en memoria (RAM) usando ':memory:'.
# Si el archivo ya existe, simplemente se conecta a él.
# Usaremos 'employee.db' para el ejemplo inicial en disco.

# Ejemplo en formato ejecutable:
try:
    conn = sqlite3.connect('employee.db')
    print("# Conexión a 'employee.db' establecida.")
except sqlite3.Error as e:
    print(f"Error al conectar: {e}")

# Explicación: Una vez que tenemos la conexión (conn), necesitamos un 'cursor'.
# El cursor es lo que nos permite ejecutar comandos SQL.
c = conn.cursor()
print("# Cursor creado (objeto 'c').")


################################################################################
# 2. CREACIÓN DE UNA TABLA
################################################################################

# Explicación: Usamos el método `execute()` del cursor para correr comandos SQL.
# Vamos a crear una tabla llamada 'employees' con tres columnas: first, last, y pay.
# Los tipos de datos de SQLite son limitados: NULL, INTEGER, REAL, TEXT, y BLOB.
# Usaremos TEXT para los nombres e INTEGER para el salario (pay).

# Ejemplo en formato ejecutable (Definición de la tabla):
# El uso de triples comillas (docstring) permite escribir comandos SQL en múltiples líneas.
try:
    c.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
                )""")
    print("# Tabla 'employees' creada exitosamente.")
except sqlite3.OperationalError as e:
    # Si la tabla ya existe (como ocurre si ejecutamos el script varias veces), este error es normal.
    print(f"# Advertencia: {e}. (La tabla ya existe. Esto es esperado si ya se ejecutó el código).")


# Explicación: Es fundamental "confirmar" (commit) la transacción utilizando el objeto de conexión (`conn.commit()`)
# para que los cambios (como la creación de la tabla) se guarden permanentemente en el archivo de base de datos.
conn.commit()
print("# Transacción confirmada.")

# Explicación: Una buena práctica es cerrar la conexión a la base de datos al finalizar.
conn.close()
print("# Conexión cerrada.")

################################################################################
# 3. INSERCIÓN Y CONSULTA DE DATOS (MÉTODO BÁSICO SIN PLACEHOLDERS)
################################################################################

# Reabrimos la conexión para demostrar inserción y selección
conn = sqlite3.connect('employee.db')
c = conn.cursor()

# Explicación: Para insertar datos, utilizamos el comando SQL 'INSERT INTO'.
# Nota: Aquí se usa un valor codificado (hard-coded) directamente en la cadena SQL.

# Ejemplo en formato ejecutable (Inserción de un empleado):
c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 50000)")
conn.commit()
print("\n# Empleado insertado (Corey Schafer).")

# Explicación: Para consultar datos, usamos el comando SQL 'SELECT'.
# Buscamos todos los empleados donde el apellido (last) sea 'Schafer'.
c.execute("SELECT * FROM employees WHERE last='Schafer'")

# Explicación: Hay tres métodos para obtener resultados del cursor:
# 1. `fetchone()`: Retorna la siguiente fila, o None si no quedan filas.
# 2. `fetchmany(N)`: Retorna una lista con las N próximas filas.
# 3. `fetchall()`: Retorna una lista con todas las filas restantes.

# Usamos `fetchone()` ya que esperamos un solo resultado:
employee_result = c.fetchone()
print(f"# Resultado de fetchone(): {employee_result}") # Debería mostrar (Corey, Schafer, 50000)

# Insertamos un segundo empleado para demostrar `fetchall()`:
c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")
conn.commit()
print("# Segundo empleado insertado (Mary Schafer).")

# Consultamos por el apellido 'Schafer' nuevamente:
c.execute("SELECT * FROM employees WHERE last='Schafer'")

# Usamos `fetchall()` para obtener todos los resultados como una lista.
all_employees = c.fetchall()
print(f"# Resultado de fetchall(): {all_employees}") # Debería mostrar ambas entradas en una lista.

conn.close()


################################################################################
# 4. USO DE PLACEHOLDERS (PREVENCIÓN DE INYECCIÓN SQL)
################################################################################

# Explicación: Insertar valores directamente en la cadena SQL (como en el paso 3) hace que la aplicación sea
# vulnerable a ataques de inyección SQL, especialmente si los valores provienen de un usuario.
# La forma correcta es usar "placeholders" y pasar los valores como un segundo argumento al método `execute()`.

# Reabrimos la conexión para la demostración
conn = sqlite3.connect('employee.db')
c = conn.cursor()

# 4a. Placeholders tipo Tupla (signo de interrogación '?')

# Explicación: Se utiliza '?' como marcador de posición.
# Los valores se pasan como una tupla, en el orden en que aparecen los '?'.
# ¡Importante! Incluso si solo pasamos un valor, debe estar dentro de una tupla (o una lista).

# Simulamos la existencia de la clase Employee que se importa en el video.
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

emp_1 = Employee('John', 'Doe', 80000)
print(f"\n# Insertando empleado 1 (John Doe) usando '?' placeholders.")

# Ejemplo en formato ejecutable (Inserción usando '?'):
c.execute("INSERT INTO employees VALUES (?, ?, ?)",
          (emp_1.first, emp_1.last, emp_1.pay))
conn.commit()

# 4b. Placeholders Nombrados (favorito del video)

# Explicación: Se utiliza ':nombre' (e.g., :first, :last) como marcador de posición.
# Los valores se pasan como un diccionario, donde las claves coinciden con los nombres del placeholder.
# Este método se considera más legible, especialmente en consultas complejas o con pocos valores.

emp_2 = Employee('Jane', 'Doe', 90000)
print(f"# Insertando empleado 2 (Jane Doe) usando placeholders nombrados.")

# Ejemplo en formato ejecutable (Inserción usando ':nombre'):
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
          {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
conn.commit()

# 4c. Consulta usando Placeholders Nombrados

# Explicación: Los placeholders nombrados también se usan en la cláusula WHERE para buscar datos.
print(f"# Consultando empleados con el apellido 'Doe' usando placeholders nombrados.")
c.execute("SELECT * FROM employees WHERE last = :last", {'last': 'Doe'})
doe_employees = c.fetchall()
print(f"# Resultados de búsqueda por 'Doe': {doe_employees}")

conn.close()


################################################################################
# 5. MEJORES PRÁCTICAS: CONTEXT MANAGERS Y FUNCIONES CRUD
################################################################################

# Explicación: Para simplificar el código y asegurar que `commit` o `rollback` se ejecuten,
# se recomienda usar la conexión como un "Context Manager" (`with conn:`).
# Esto automáticamente confirma la transacción si no hay errores (y hace rollback si hay una excepción).
# Usaremos una base de datos en memoria (':memory:') para que cada ejecución comience de cero.

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Definición de la clase Employee (reutilizada del paso 4):
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first.lower()}.{last.lower()}@company.com'

# Creamos la tabla 'employees' en la base de datos en memoria
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")
print("\n# Base de datos en memoria creada y tabla inicializada.")


# Funciones CRUD (Create, Read, Update, Delete) usando Context Managers:

# Explicación: Función para insertar un empleado. Utiliza `with conn:` para el commit automático.
def insert_emp(emp):
    with conn: # El context manager se encarga del conn.commit()
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
    print(f"-> Insertado: {emp.first} {emp.last}")

# Explicación: Función para seleccionar empleados por apellido. No requiere commit.
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    # Retorna todas las filas encontradas con ese apellido.
    return c.fetchall()

# Explicación: Función para actualizar el salario. Utiliza `with conn:`.
def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'pay': pay, 'first': emp.first, 'last': emp.last})
    print(f"-> Pago de {emp.first} actualizado a {pay}")

# Explicación: Función para eliminar un empleado. Utiliza `with conn:`.
def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})
    print(f"-> Eliminado: {emp.first} {emp.last}")


# Ejemplo en formato ejecutable (Uso de las funciones):

# Creamos instancias de empleados:
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

# 1. C (Create / Insertar)
insert_emp(emp_1)
insert_emp(emp_2)

# 2. R (Read / Leer)
employees = get_emps_by_name('Doe')
print(f"\n# Empleados 'Doe' después de la inserción:\n{employees}")

# 3. U (Update / Actualizar)
new_pay = 95000
update_pay(emp_2, new_pay) # Actualizamos el pago de Jane a 95000.

# 4. D (Delete / Eliminar)
remove_emp(emp_1) # Eliminamos a John Doe.

# 5. R (Read / Leer) - Verificamos los cambios
employees_after_update_delete = get_emps_by_name('Doe')
print(f"\n# Empleados 'Doe' después de actualizar y eliminar:\n{employees_after_update_delete}")
# El resultado muestra a Jane Doe con el nuevo salario (95000) y John Doe ha sido eliminado.

# Cerramos la conexión a la base de datos en memoria (que se elimina al cerrar).
conn.close()
```