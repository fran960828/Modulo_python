

### Tutorial 1: Clases e Instancias

# Tutorial 1: Clases e Instancias

# Introducción a la POO en Python
# El objetivo de las clases es agrupar lógicamente datos y funciones de una manera
# que sea fácil de reutilizar y construir.
# Los datos asociados a una clase se conocen como atributos, y las funciones como métodos.
# Un buen caso de uso para una clase sería representar a los empleados de una compañía.

# Paso 1: Creación de una clase simple
# Una clase actúa como un plano (blueprint) para crear instancias.
class Employee:
    # Si desea dejar una clase o función vacía temporalmente, se usa 'pass' para evitar errores.
    pass

# Paso 2: Creación de instancias
# Una instancia es un objeto único creado a partir de la clase (el plano).
emp_1 = Employee()
emp_2 = Employee()

# Cada una de estas es una instancia única (tienen diferentes ubicaciones en memoria).
print("# Demostración de instancias únicas (objetos Employee con ubicaciones de memoria distintas):")
print(emp_1)
print(emp_2)
print("-" * 50)


# Paso 3: Asignación manual de variables de instancia (Método no recomendado)
# Las variables de instancia contienen datos que son únicos para cada instancia.
# Se pueden crear manualmente, pero esto es propenso a errores y genera mucho código repetitivo.
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

# Imprimir un atributo único de cada instancia creada manualmente:
print("# Atributos de instancia asignados manualmente (Email):")
print(emp_1.email)
print(emp_2.email)
print("-" * 50)


# Paso 4: Uso del método especial '__init__' (El Constructor)
# El método '__init__' se usa para inicializar automáticamente las variables
# de instancia cuando se crea un nuevo objeto.
class Employee:
    # Cuando se crean métodos dentro de una clase, el primer argumento
    # siempre es la instancia de manera automática. Por convención, se llama 'self'.
    def __init__(self, first, last, pay):
        # 'self' aquí es la instancia que se está creando (ej: emp_1).
        # Los argumentos que siguen a 'self' son los valores que se pasan al crear la instancia.
        self.first = first  # Variable de instancia
        self.last = last    # Variable de instancia
        self.pay = pay      # Variable de instancia
        # También se pueden crear atributos basados en otros atributos pasados.
        self.email = first + '.' + last + '@company.com'

# Re-creación de instancias usando __init__
# Al crear el objeto, la instancia ('self') se pasa automáticamente, por lo que
# solo proporcionamos los valores para 'first', 'last' y 'pay'.
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Verificamos que los emails se crearon automáticamente.
print("# Atributos de instancia creados automáticamente con __init__ (Email):")
print(emp_1.email)
print(emp_2.email)
print("-" * 50)


# Paso 5: Adición de Métodos
# Los métodos permiten a la clase realizar algún tipo de acción.
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        # Este método devuelve el nombre completo del empleado.
        # Requiere 'self' para acceder a las variables de instancia (self.first, self.last).
        return '{} {}'.format(self.first, self.last)

# Re-creación de instancias con el nuevo método
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Llamada al método desde la instancia (self se pasa automáticamente).
# Notar que se requieren los paréntesis '()' porque es un método (función) y no un atributo.
print("# Llamada estándar al método 'full_name' desde la instancia:")
print(emp_1.full_name())
print(emp_2.full_name())
print("-" * 50)


# Paso 6: Llamada al método a través de la Clase
# Esto demuestra lo que ocurre en segundo plano.
# Al llamar al método directamente desde la clase, se debe pasar manualmente la instancia
# como argumento (que se convierte en 'self' dentro del método).
print("# Llamada al método 'full_name' a través de la Clase (Pasando la instancia manualmente):")
print(Employee.full_name(emp_1))
# Ambas formas de llamar al método (emp_1.full_name() y Employee.full_name(emp_1))
# hacen la misma cosa.
print("-" * 50)

```

***

### Tutorial 2: Variables de Clase
**(Python OOP Tutorial 2: Class Variables)**

```python
# Tutorial 2: Variables de Clase

# Las variables de clase son compartidas entre todas las instancias de una clase.
# Mientras que las variables de instancia son únicas (nombres, salario),
# las variables de clase deberían ser las mismas para cada instancia (ej: un porcentaje de aumento anual).

class Employee:
    # Ejemplo 1: raise_amount (Cantidad de aumento)
    # Esta variable se define a nivel de clase.
    raise_amount = 1.04 # 4% de aumento

    # Ejemplo 2: num_of_employees (Contador de empleados)
    # Variable de clase para rastrear cuántos empleados existen.
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Incrementamos el contador. Usamos el nombre de la Clase (Employee.num_of_employees).
        # Esto asegura que todas las instancias compartan el mismo contador y que
        # una instancia individual no pueda accidentalmente sobrescribir el total.
        Employee.num_of_employees += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # Utilizamos self.raise_amount para acceder a la variable de clase.
        # Acceder mediante 'self' (en lugar de Employee.raise_amount) permite que
        # una instancia específica pueda sobrescribir el valor si es necesario.
        self.pay = int(self.pay * self.raise_amount)

# Creación de instancias (Esto incrementa num_of_employees a 2)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


# --- Demostración de raise_amount: Acceso y Sobreescritura ---

# Se puede acceder a la variable de clase tanto por la Clase como por la Instancia.
print("# 1. Acceso a la variable de clase (raise_amount):")
print(f"Clase: {Employee.raise_amount}")
print(f"Instancia 1: {emp_1.raise_amount}")
print(f"Instancia 2: {emp_2.raise_amount}")
print("-" * 50)

# ¿Por qué las instancias pueden acceder a la variable?
# Cuando se accede a un atributo en una instancia, Python primero verifica si la instancia
# tiene ese atributo en su propio namespace. Si no lo tiene, busca en el namespace de la clase.
print("# 2. Namespace de la Instancia (emp_1.__dict__):")
# Inicialmente, el diccionario de la instancia NO contiene 'raise_amount'.
print(emp_1.__dict__)
print("-" * 50)

# Sobreescritura de la variable SOLO para la instancia 1:
# Esta asignación crea el atributo 'raise_amount' en el namespace de 'emp_1'.
emp_1.raise_amount = 1.05 # 5% de aumento solo para emp_1

print("# 3. Namespace de la Instancia 1 después de la sobreescritura:")
# Ahora 'raise_amount' aparece en el diccionario de emp_1, lo que sobrescribe
# el valor de la clase para esta instancia.
print(emp_1.__dict__)
print("-" * 50)

print("# 4. Valores después de la sobreescritura de emp_1:")
print(f"Instancia 1: {emp_1.raise_amount}") # Utiliza 1.05 (su valor de instancia)
print(f"Instancia 2: {emp_2.raise_amount}") # Utiliza 1.04 (el valor de la clase)
print("-" * 50)

# Aplicación de aumentos:
print("# 5. Aplicando el método apply_raise:")
print(f"Pago inicial emp_1: {emp_1.pay}")
print(f"Pago inicial emp_2: {emp_2.pay}")

emp_1.apply_raise() # Usará 1.05
emp_2.apply_raise() # Usará 1.04

print(f"Pago con aumento emp_1: {emp_1.pay}") # 50000 * 1.05 = 52500
print(f"Pago con aumento emp_2: {emp_2.pay}") # 60000 * 1.04 = 62400
print("-" * 50)


# --- Demostración de num_of_employees: Contador Global ---

# El contador se incrementó en __init__ usando el nombre de la clase.
# Muestra el número total de instancias creadas (2).
print("# 6. Contador global (num_of_employees):")
print(f"Número total de empleados creados: {Employee.num_of_employees}")

