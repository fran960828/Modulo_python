# =============================================================================
# Tutorial de Herencia de Clases en Python
# Basado en la información proporcionada sobre la herencia de clases (class inheritance),
# que permite a las subclases heredar atributos y métodos de una clase padre.
# Esto es útil para crear funcionalidad sin reescribir código y permite anular (overwrite)
# o añadir funcionalidad nueva sin afectar a la clase padre.
#
# Para este ejemplo, se asume la existencia de la clase base 'Employee' (Empleado).
# =============================================================================

# Definición de la Clase Padre (Inferencia necesaria para la ejecución)
class Employee:
    # El atributo de clase raise_amount se hereda.
    raise_amount = 1.04 # 4%

    def __init__(self, first, last, pay):
        # La clase Employee maneja first, last, y pay.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def full_name(self):
        # El método full_name se hereda.
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # El método apply_raise se hereda.
        self.pay = int(self.pay * self.raise_amount)

# =============================================================================
# Ejemplo 1: Creación de Subclase 'Developer' (Desarrollador) e Herencia Básica
# =============================================================================

# Se crea la subclase Developer (Desarrollador) que hereda de Employee (Empleado).
# La herencia se especifica poniendo la clase padre entre paréntesis después del nombre de la subclase.
class Developer(Employee):
    # Inicialmente, la clase puede estar vacía, pero hereda toda la funcionalidad.
    pass


# Instanciación y prueba de herencia
# Se crean dos instancias de Developer con la misma información que se usaría para un Employee.
# La subclase hereda el método __init__ de Employee.
dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'User', 60000)

# Al imprimir los correos electrónicos, se verifica que los atributos (establecidos en el __init__ de Employee)
# fueron creados exitosamente.
print("# --- Ejemplo 1: Herencia Básica (Email) ---")
print(f"Email del Desarrollador 1 (Heredado): {dev_1.email}")
print(f"Email del Desarrollador 2 (Heredado): {dev_2.email}\n")


# -----------------------------------------------------------------------------
# Uso de help() y MRO
# -----------------------------------------------------------------------------
# La función help() es útil para visualizar la cadena de herencia, llamada Method Resolution Order (MRO).
# El MRO muestra las ubicaciones que Python busca para atributos y métodos.
# El orden es: Developer -> Employee -> object (todos heredan de la clase base 'object').
# También muestra los métodos y atributos heredados, como __init__, apply_raise, full_name, y raise_amount.

# print("--- Ejemplo 1b: help() y MRO ---")
# print(help(Developer)) # Descomentar para ver el output de ayuda completo
# print("-" * 30 + "\n")


# =============================================================================
# Ejemplo 2: Personalización de Atributos de Clase
# =============================================================================

# Prueba del aumento (raise) antes de personalizar
print("# --- Ejemplo 2a: Aplicar Aumento (Employee raise_amount: 4%) ---")
print(f"Salario inicial de {dev_1.first}: {dev_1.pay}") # 50000
dev_1.apply_raise() # Usa el raise_amount de Employee (1.04)
print(f"Salario después del aumento de Employee (4%): {dev_1.pay}\n") # 52000

# -----------------------------------------------------------------------------
# Personalización de raise_amount en Subclase
# -----------------------------------------------------------------------------
class Developer(Employee):
    # Se sobrescribe el atributo raise_amount a 10% (1.10).
    raise_amount = 1.10

# Se crea una nueva instancia de Developer con el nuevo raise_amount
dev_3 = Developer('Sam', 'Jones', 70000)

print("# --- Ejemplo 2b: Aumento Personalizado (Developer raise_amount: 10%) ---")
print(f"Salario inicial de {dev_3.first}: {dev_3.pay}")
dev_3.apply_raise() # Usa el raise_amount de Developer (1.10)
print(f"Salario después del aumento de Developer (10%): {dev_3.pay}") # 77000

# Nota importante: Cambiar el raise_amount en la subclase (Developer) no afecta a las instancias de la clase padre (Employee).
# -----------------------------------------------------------------------------


# =============================================================================
# Ejemplo 3: Personalización del Método __init__ (Constructor)
# =============================================================================

# A veces se necesita inicializar la subclase con más información de la que maneja la clase padre.
# Para los desarrolladores, se quiere añadir su lenguaje de programación principal.
class Developer(Employee):
    raise_amount = 1.10

    # Se define un __init__ personalizado que acepta un argumento adicional: prog_lang.
    def __init__(self, first, last, pay, prog_lang):
        # Para evitar repetir la lógica de la clase padre (Principio DRY),
        # se utiliza super().init() para que Employee maneje first, last y pay.
        super().__init__(first, last, pay)
        # Nota: Usar super() es más mantenible, especialmente con herencia múltiple, pero Employee.__init__(self, ...) también funciona.

        # La subclase maneja su argumento específico: prog_lang.
        self.prog_lang = prog_lang


# Instanciación de desarrolladores con el nuevo argumento 'prog_lang'.
dev_4 = Developer('Anna', 'Lee', 55000, 'Python')
dev_5 = Developer('Mike', 'Tyson', 65000, 'Java')

print("\n# --- Ejemplo 3: __init__ Personalizado (con super()) ---")
print(f"Email de {dev_4.first} (Heredado): {dev_4.email}") # Email configurado por Employee.__init__
print(f"Lenguaje de {dev_4.first} (Personalizado): {dev_4.prog_lang}\n") # prog_lang configurado por Developer.__init__


# =============================================================================
# Ejemplo 4: Creación de la Subclase Manager (Gestor)
# =============================================================================

# Se crea la subclase Manager (Gestor), que también hereda de Employee.
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        # Se llama al constructor de la clase padre para manejar first, last, y pay.
        super().__init__(first, last, pay)

        # Manager acepta una lista de empleados que supervisa.
        # Es crucial NO usar tipos de datos mutables (como listas o diccionarios) como argumentos predeterminados.
        if employees is None:
            self.employees = [] # Si no se proporciona la lista, se inicializa como una lista vacía.
        else:
            self.employees = employees # Si se proporciona, se asigna.

    # Método para añadir un empleado a la lista de supervisados.
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # Método para eliminar un empleado de la lista de supervisados.
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # Método para imprimir los nombres completos de los empleados supervisados.
    def print_employees(self):
        print("Empleados supervisados:")
        for emp in self.employees:
            # Llama al método full_name() que fue heredado de Employee.
            print(f'-> {emp.full_name()}')


# Instanciación del Manager
# Se usa dev_4 y dev_5 (instancias de Developer) para la lista de supervisados.
# Manager_1 supervisa inicialmente a dev_4.
manager_1 = Manager('Sue', 'Smith', 90000, [dev_4])

print("\n# --- Ejemplo 4: Funcionalidad de Manager ---")

# 4a: Prueba de herencia (Email)
print(f"Email del Manager (Heredado de Employee): {manager_1.email}")

# 4b: Prueba de print_employees (Lista inicial)
manager_1.print_employees()

# 4c: Prueba de add_employee (añadir dev_5)
manager_1.add_employee(dev_5)
print("\nDespués de añadir a dev_5:")
manager_1.print_employees()

# 4d: Prueba de remove_employee (eliminar dev_4)
manager_1.remove_employee(dev_4)
print("\nDespués de remover a dev_4:")
manager_1.print_employees()


# =============================================================================
# Ejemplo 5: Funciones Integradas: isinstance() e issubclass()
# =============================================================================

# Python tiene funciones incorporadas para verificar relaciones de herencia y tipado.

# -----------------------------------------------------------------------------
# isinstance(objeto, Clase)
# Verifica si un objeto es una instancia de una clase dada.
# -----------------------------------------------------------------------------
print("\n# --- Ejemplo 5a: isinstance() ---")

# ¿Manager_1 es una instancia de Manager? Sí.
print(f"¿manager_1 es instancia de Manager? {isinstance(manager_1, Manager)}")

# ¿Manager_1 es una instancia de Employee? Sí, porque hereda de Employee.
print(f"¿manager_1 es instancia de Employee? {isinstance(manager_1, Employee)}")

# ¿Manager_1 es una instancia de Developer? No, aunque ambas hereden de Employee.
print(f"¿manager_1 es instancia de Developer? {isinstance(manager_1, Developer)}")

# -----------------------------------------------------------------------------
# issubclass(Clase_A, Clase_B)
# Verifica si una clase es una subclase de otra.
# -----------------------------------------------------------------------------
print("\n# --- Ejemplo 5b: issubclass() ---")

# ¿Developer es subclase de Employee? Sí.
print(f"¿Developer es subclase de Employee? {issubclass(Developer, Employee)}")

# ¿Manager es subclase de Employee? Sí.
print(f"¿Manager es subclase de Employee? {issubclass(Manager, Employee)}")

# ¿Manager es subclase de Developer? No.
print(f"¿Manager es subclase de Developer? {issubclass(Manager, Developer)}")
