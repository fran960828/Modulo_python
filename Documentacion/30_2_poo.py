
### Tutorial 3: Métodos de Instancia, Métodos de Clase y Métodos Estáticos

# Importamos la librería necesaria para el ejemplo de staticmethod.
import datetime

# CLASE BASE (Continuación de Tutorial 2)
# Recreamos la clase Employee con la variable de clase 'raise_amount' y el contador.
class Employee:
    # Variables de clase compartidas por todas las instancias.
    raise_amount = 1.04 # 4%
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_employees += 1

    # 1. MÉTODO REGULAR (Método de Instancia)
    # Toman automáticamente la INSTANCIA ('self') como primer argumento.
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # Utiliza la variable de instancia (self.pay) y la variable de clase (self.raise_amount).
        self.pay = int(self.pay * self.raise_amount)

    # 2. MÉTODO DE CLASE (Class Method)
    # Se define usando el decorador '@classmethod'.
    # Toman automáticamente la CLASE ('cls') como primer argumento, en lugar de la instancia ('self').
    # Por convención, se usa 'cls' en lugar de 'class' porque 'class' es una palabra clave reservada de Python.

    # CASO DE USO A: Modificar variables de clase
    @classmethod
    def set_raise_amount(cls, amount):
        # Este método trabaja con la CLASE (cls).
        # Al usar cls.raise_amount, se modifica la variable para TODAS las instancias y la clase misma.
        cls.raise_amount = amount

    # CASO DE USO B: Constructores Alternativos
    # Los Class Methods pueden utilizarse para proveer múltiples maneras de crear objetos.
    # Esto es útil cuando la información de entrada viene en un formato diferente al esperado por __init__ (ej: una cadena).
    @classmethod
    def from_string(cls, employee_string):
        # La convención es que estos constructores alternativos comiencen con 'from' (ej: from_string).

        # Paso 1: Parsear la cadena de entrada (ej: 'John-Doe-70000').
        first, last, pay = employee_string.split('-')
        pay = int(pay) # Aseguramos que el pago sea un entero.

        # Paso 2: Crear y devolver la nueva instancia.
        # En lugar de usar 'Employee(...)' se usa 'cls(...)' (la variable de clase) para llamar al constructor __init__.
        return cls(first, last, pay)


    # 3. MÉTODO ESTÁTICO (Static Method)
    # Se define usando el decorador '@staticmethod'.
    # No toman automáticamente ni la instancia ('self') ni la clase ('cls') como primer argumento.
    # Se comportan como funciones regulares, pero se incluyen en la clase porque tienen una conexión lógica con ella.

    # CASO DE USO C: Funciones utilitarias que no dependen de la instancia ni de la clase
    # Un indicio de que se debe usar un static method es si el código interno no accede
    # a 'self' o a 'cls' en ningún momento.
    @staticmethod
    def is_workday(day):
        # Esta función recibe un objeto 'day' y retorna si es un día laborable.
        # No necesita saber el salario (instancia) ni el porcentaje de aumento (clase).
        # En Python, 5 es Sábado y 6 es Domingo.
        if day.weekday() == 5 or day.weekday() == 6:
            return False # Fin de semana
        return True # Día laborable


# -----------------------------------------------------------
# DEMOSTRACIÓN DE CLASS METHODS
# -----------------------------------------------------------

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print("# 1. Demostración de set_raise_amount (Modificando la variable de clase)")
print(f"Aumento inicial (Clase): {Employee.raise_amount}")

# Llamamos al Class Method usando la clase (Employee) para cambiar la variable de clase global.
Employee.set_raise_amount(1.05) # Cambia el aumento al 5%

print(f"Aumento después de Class Method: {Employee.raise_amount}")
print(f"Aumento en emp_1: {emp_1.raise_amount}") # El cambio afecta a todas las instancias
print("-" * 50)


# Demostración de Class Method como Constructor Alternativo
# Definimos la información del empleado separada por guiones, un formato común que requiere parsing.
emp_str_3 = 'John-Doe-70000'
emp_str_4 = 'Steve-Smith-30000'

# En lugar de parsear la cadena manualmente y llamar a __init__, usamos el constructor alternativo.
print("# 2. Demostración de Class Method como Constructor Alternativo (from_string)")
new_emp_3 = Employee.from_string(emp_str_3)

print(f"Nombre de emp_3 creado por from_string: {new_emp_3.full_name()}")
print(f"Email de emp_3: {new_emp_3.email}")
print(f"Salario de emp_3: {new_emp_3.pay}")
print("-" * 50)


# -----------------------------------------------------------
# DEMOSTRACIÓN DE STATIC METHODS
# -----------------------------------------------------------

# Creamos algunas fechas de prueba:
# 2023-01-10 (Martes - Día laborable)
date_workday = datetime.date(2023, 1, 10)
# 2023-01-15 (Domingo - Fin de semana)
date_weekend = datetime.date(2023, 1, 15)

# Llamamos al Static Method usando la Clase (Employee), ya que no necesita una instancia específica.
print("# 3. Demostración de Static Method (is_workday)")
print(f"¿Es 2023-01-10 (Martes) un día laborable? {Employee.is_workday(date_workday)}")
print(f"¿Es 2023-01-15 (Domingo) un día laborable? {Employee.is_workday(date_weekend)}")
# Note que el método se comporta exactamente como una función regular,
# pero está lógicamente agrupado dentro de la clase Employee.
print("-" * 50)


# -----------------------------------------------------------
# RESUMEN: DIFERENCIAS ENTRE CLASS METHOD Y STATIC METHOD
# -----------------------------------------------------------

# REGULAR METHODS (Métodos de Instancia)
# Argumento Automático: Pasan automáticamente la INSTANCIA (`self`) como primer argumento.
# Dependencia: Requieren la instancia para funcionar (ej: acceder al nombre o salario).

# CLASS METHODS (Métodos de Clase)
# Argumento Automático: Pasan automáticamente la CLASE (`cls`) como primer argumento.
# Dependencia: Trabajan con la clase, no con una instancia específica.
# Casos de Uso:
# 1. Modificación de variables de clase que deben aplicarse a toda la clase y sus instancias.
# 2. Actuar como Constructores Alternativos: Permiten crear objetos a partir de datos formateados de forma inusual (ej: desde una cadena o un timestamp).

# STATIC METHODS (Métodos Estáticos)
# Argumento Automático: No pasan automáticamente ni la instancia (`self`) ni la clase (`cls`).
# Dependencia: Se comportan como funciones regulares y no dependen de ningún estado específico de la instancia o de la clase.
# Casos de Uso:
# 1. Funciones de utilidad o herramientas que tienen una conexión LÓGICA con la clase, pero cuyos resultados no dependen de la información contenida en la clase (ej: verificar si una fecha es un día laborable).
# 2. Si un método dentro de una clase no usa `self` o `cls` en absoluto, es probable que deba ser un Static Method.

```