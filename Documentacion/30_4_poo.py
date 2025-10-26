
# ==============================================================================
# DOCUMENTACIÓN DE EJEMPLOS DE PYTHON OOP
# Parte 1: Métodos Especiales (Dunder/Magic Methods)
# ==============================================================================

# Los métodos especiales, también llamados métodos mágicos o "dunder" (por doble guion bajo),
# permiten emular ciertos comportamientos incorporados en Python y son la base para
# implementar la sobrecarga de operadores. Estos métodos siempre están rodeados
# por doble guion bajo, como en `__init__`.

class Employee:
    """Clase de ejemplo que demuestra el uso de métodos Dunder comunes."""
    
    # El método especial __init__ es el más común y se llama implícitamente cuando
    # se crea un objeto. Se utiliza para establecer todos los atributos de la instancia.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # Asumimos la existencia de un método para obtener el nombre completo que usaremos más adelante
        self.full_name = f"{self.first} {self.last}"
        self.email = f"{self.first}.{self.last}@email.com"

    # --------------------------------------------------------------------------
    # 1. Métodos de Representación: __repr__ y __str__
    # --------------------------------------------------------------------------

    # Estos métodos se utilizan para cambiar el comportamiento predeterminado cuando
    # se imprime o se solicita la representación de un objeto, evitando la salida
    # vaga de "Employee object".

    # __repr__ (Representación Inequívoca):
    # Está destinado a la depuración y el registro (logging), y debe ser una
    # representación inequívoca del objeto. Una buena práctica es devolver
    # una cadena que pueda copiarse y pegarse en código Python para recrear el
    # objeto original.
    def __repr__(self):
        # Ejemplo de retorno que permite recrear el objeto.
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    # __str__ (Representación Legible):
    # Está destinado a ser una representación legible para el usuario final.
    def __str__(self):
        # Ejemplo de retorno que muestra información relevante para el usuario.
        return f"{self.full_name} - {self.email}"

    # --------------------------------------------------------------------------
    # 2. Sobrecarga de Operadores: __add__
    # --------------------------------------------------------------------------

    # Python utiliza un método especial en segundo plano llamado `__add__` para la
    # operación de suma (`+`). Al definir este método, podemos personalizar
    # cómo funciona la adición para nuestros objetos.
    
    # Aquí definimos que al sumar dos objetos Employee, el resultado sea la
    # suma de sus salarios (`pay`).
    def __add__(self, other):
        # 'self' es el objeto a la izquierda de la suma, 'other' es el objeto a la derecha.
        # Se asume que 'other' también es un objeto Employee en este ejemplo.
        return self.pay + other.pay

    # --------------------------------------------------------------------------
    # 3. Función `len()`: __len__
    # --------------------------------------------------------------------------

    # La función `len()` también utiliza un método dunder especial en segundo plano
    # llamado `__len__`. Si queremos que `len()` funcione en nuestros objetos,
    # debemos implementarlo.
    
    # En este ejemplo, `len()` devolverá el número total de caracteres en el
    # nombre completo del empleado.
    def __len__(self):
        return len(self.full_name)


# --- Demostración Ejecutable de Métodos Dunder ---
print("#" * 40)
print("# DEMOSTRACIÓN DE MÉTODOS DUNDER")
print("#" * 40)

# Creación de instancias
emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Jane', 'Doe', 60000)

# 1. Demostración de __str__ (implícita en print())
# Si no existiera __str__, print() usaría el resultado de __repr__ como alternativa.
# Output para el usuario final: nombre y email.
print(f"1. Print (usa __str__): {emp_1}") 

# 2. Demostración de __repr__
# Representación para desarrolladores, mostrando la sintaxis de recreación.
print(f"2. Representación (usa __repr__): {repr(emp_1)}") 

# También se puede llamar a los métodos dunder directamente.
print(f"3. Llamada directa a __repr__: {emp_1.__repr__()}")

# 4. Demostración de Sobrecarga de Operador (+) usando __add__
# Si no tuviéramos __add__, intentaría sumar los objetos y daría un error.
# Retorna la suma de los salarios combinados.
salario_combinado = emp_1 + emp_2
print(f"4. Suma de empleados (emp_1 + emp_2) usando __add__: {salario_combinado}")

# 5. Demostración de la función len() usando __len__
# Retorna la longitud de la cadena del nombre completo.
longitud_nombre = len(emp_1)
print(f"5. Longitud del nombre (len(emp_1)) usando __len__: {longitud_nombre}")
print("-" * 40 + "\n")


# ==============================================================================
# Parte 2: Decoradores de Propiedad (@property)
# ==============================================================================

# El decorador `@property` permite acceder a métodos como si fueran atributos.
# Esto es útil para implementar funcionalidad de 'getter', 'setter' y 'deleter'.

class EmployeeProperty:
    """Clase que demuestra el uso de decoradores de propiedad."""
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # En el diseño inicial, si 'email' fuera un atributo (como self.email = ...),
        # no se actualizaría si 'first' o 'last' cambiaran directamente.

    # --------------------------------------------------------------------------
    # 6. Getter: @property
    # --------------------------------------------------------------------------

    # Definimos 'email' como un método, pero al usar `@property`, se accede como
    # si fuera un atributo (sin paréntesis). Esto asegura que el valor del email
    # se calcule dinámicamente cada vez que se accede, resolviendo el problema
    # de actualización.
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    # Definimos 'full_name' como un getter para asegurar que siempre refleje
    # los valores actuales de 'first' y 'last'.
    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    # --------------------------------------------------------------------------
    # 7. Setter: @full_name.setter
    # --------------------------------------------------------------------------

    # Para permitir que se asigne un valor al atributo de propiedad (`employee.full_name = 'Jim Halpert'`),
    # utilizamos el decorador setter. Su nombre es el nombre de la propiedad (`@full_name.setter`).
    # El método setter toma el valor que se intenta asignar (llamado 'name' aquí).
    @full_name.setter
    def full_name(self, name):
        # Dividimos la cadena de nombre en el espacio para obtener el primer y último nombre.
        first, last = name.split(' ')
        # Actualizamos los atributos internos de la instancia.
        self.first = first
        self.last = last
        # Nota: Al actualizar 'first' y 'last', el 'email' (que es un getter) se actualizará automáticamente.

    # --------------------------------------------------------------------------
    # 8. Deleter: @full_name.deleter
    # --------------------------------------------------------------------------

    # Se usa para definir el código que se ejecutará cuando se elimine el atributo
    # usando `del`.
    @full_name.deleter
    def full_name(self):
        print('--- Ejecutando código de limpieza (deleter) ---')
        # Limpieza o registro de la acción.
        self.first = None
        self.last = None
        print("Nombre de empleado eliminado y atributos restablecidos a None.")


# --- Demostración Ejecutable de Decoradores de Propiedad ---
print("#" * 40)
print("# DEMOSTRACIÓN DE DECORADORES DE PROPIEDAD")
print("#" * 40)

emp_prop = EmployeeProperty('Jim', 'Carey')

# Accediendo a 'email' y 'full_name' como si fueran atributos, aunque son métodos definidos con @property.
print(f"1. Nombre completo (Getter): {emp_prop.full_name}")
print(f"2. Email inicial (Getter): {emp_prop.email}")

# 3. Demostración del Setter
# Intentar asignar un valor a 'full_name' sin el setter resultaría en un error.
# Con el setter, el valor se analiza y actualiza 'first' y 'last'.
print("\n3. Asignando un nuevo nombre completo (invocando el Setter)...")
emp_prop.full_name = 'Corey Schafer' 

print(f"   Primer nombre actualizado: {emp_prop.first}") 
print(f"   Apellido actualizado: {emp_prop.last}")
# El email se actualiza automáticamente al acceder a la propiedad, ya que depende de 'first' y 'last'.
print(f"   Email actualizado (Getter): {emp_prop.email}") 

# 4. Demostración del Deleter
# Ejecuta el código de limpieza definido en el método `@full_name.deleter`.
print("\n4. Eliminando el nombre completo (invocando el Deleter)...")
del emp_prop.full_name 

print(f"   Estado del primer nombre después del Deleter: {emp_prop.first}")
print("-" * 40 + "\n")
