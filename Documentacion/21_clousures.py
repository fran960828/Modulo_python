
# ==============================================================================
# DOCUMENTACIÓN DE FUNCIONES DE PRIMERA CLASE (FIRST-CLASS FUNCTIONS)
# ==============================================================================

# Una función de primera clase es aquella que trata a las funciones como "ciudadanos de primera clase"
# o "objetos de primera clase".
# Esto significa que las funciones soportan todas las operaciones disponibles para otras entidades (objetos o variables).
# Estas operaciones incluyen:
# 1. Ser asignadas a una variable.
# 2. Ser pasadas como argumento a otra función.
# 3. Ser devueltas como resultado de otra función.

# ------------------------------------------------------------------------------
# 1. ASIGNAR UNA FUNCIÓN A UNA VARIABLE
# ------------------------------------------------------------------------------

# Podemos asignar una función a una variable sin ejecutarla. Para ello, debemos omitir los paréntesis.
# Una vez asignada, la variable se puede ejecutar como si fuera la función original.
def square(num):
    """Calcula el cuadrado de un número."""
    return num * num

print("# 1. ASIGNACIÓN A VARIABLE")

# La variable 'F' ahora es igual a la función 'square'.
F = square

# Si se imprime F, se muestra que es una función.
# Si se ejecuta F(5), se obtiene el resultado esperado.
print(f"La variable F es: {F}")
print(f"Resultado de ejecutar F(5): {F(5)}")


# ------------------------------------------------------------------------------
# 2. PASAR UNA FUNCIÓN COMO ARGUMENTO
# ------------------------------------------------------------------------------

# Si una función acepta otras funciones como argumentos, se denomina 'función de orden superior' (higher-order function).
# Un ejemplo práctico de esto es una función 'map' personalizada.
def cube(num):
    """Calcula el cubo de un número."""
    return num * num * num

def my_map(func, array):
    """Implementación personalizada de la función map."""
    result = []
    # Se recorre el array y se aplica la función pasada como argumento a cada ítem.
    for item in array:
        result.append(func(item))
    return result

print("\n# 2. PASAR COMO ARGUMENTO (Higher-Order Function)")

values =

# Pasamos la función 'square' como argumento a 'my_map' (sin paréntesis).
squares = my_map(square, values)
print(f"Valores originales: {values}")
print(f"Resultados al usar 'square': {squares}") # Esperado:

# Pasamos la función 'cube' como argumento a 'my_map'.
cubes = my_map(cube, values)
print(f"Resultados al usar 'cube': {cubes}")


# ------------------------------------------------------------------------------
# 3. DEVOLVER UNA FUNCIÓN
# ------------------------------------------------------------------------------

# Una función puede devolver otra función como su resultado.
# Este es un concepto fundamental para entender las clausuras (closures).

def simple_logger(message):
    """Función externa que toma un argumento y devuelve una función interna."""
    # Función interna que no toma argumentos.
    def log_message():
        # Utiliza la variable 'message' del scope exterior.
        print(f"LOG: {message}")
    
    # Se devuelve la función interna sin ejecutarla (sin paréntesis).
    return log_message

print("\n# 3. DEVOLVER UNA FUNCIÓN")

# 'log_hi' es ahora la función interna 'log_message', configurada con 'hi'.
log_hi = simple_logger("hi")

# Al ejecutar 'log_hi', se ejecuta la función interna que recuerda el mensaje.
print("Ejecutando log_hi:")
log_hi()


# ==============================================================================
# DOCUMENTACIÓN DE CLAUSURAS (CLOSURES)
# ==============================================================================

# Una clausura (closure) es una función interna que recuerda y tiene acceso a las variables
# en el ámbito local (local scope) en el que fue creada, incluso después de que la función externa
# haya terminado de ejecutarse.

# Se define formalmente como un registro que almacena una función junto con un "entorno" (environment)
# que asocia cada variable libre de la función con el valor o ubicación al que se vinculó cuando se creó la clausura.
# Una clausura "cierra" (closes over) las variables libres de su entorno.

# Una "variable libre" (free variable) es una variable utilizada en la función interna
# que no está definida dentro de ella.

# ------------------------------------------------------------------------------
# 1. CLAUSURA BÁSICA (RECUERDA VARIABLES)
# ------------------------------------------------------------------------------

def outer_function():
    """Función externa que define una variable libre."""
    message = 'hi' # Esta variable será la variable libre capturada.

    def inner_function():
        """Función interna que accede a la variable 'message'."""
        print(message) # 'message' es una variable libre para inner_function.

    # Retornamos la función interna sin ejecutarla.
    return inner_function

print("\n# 1. CLAUSURA BÁSICA")

# Se ejecuta outer_function, que asigna 'message' = 'hi' y devuelve inner_function.
my_func = outer_function()

# Aunque outer_function ya terminó su ejecución, la clausura 'my_func' (inner_function)
# todavía tiene acceso a la variable 'message'.
print("Ejecutando my_func (clausura):")
my_func()
my_func()


# ------------------------------------------------------------------------------
# 2. CLAUSURA CON PARÁMETROS EXTERNOS (MÚLTIPLES ENTORNOS)
# ------------------------------------------------------------------------------

# Podemos usar parámetros en la función externa para crear múltiples instancias de la clausura,
# cada una con su propio entorno de variables recordado.

def outer_function_params(msg):
    """Función externa que toma un mensaje como parámetro."""
    # 'message' se establece al valor pasado en 'msg'.
    message = msg

    def inner_function():
        """La clausura que imprime el mensaje recordado."""
        print(message)

    return inner_function

print("\n# 2. CLAUSURA CON PARÁMETROS EXTERNOS")

# Creamos dos clausuras distintas, cada una cerrando sobre un valor diferente de 'message'.
hi_function = outer_function_params('hi')
hello_function = outer_function_params('hello')

# Cada función recuerda el valor específico de su propia variable 'message'.
print("Ejecutando hi_function:")
hi_function()

print("Ejecutando hello_function:")
hello_function()


# ------------------------------------------------------------------------------
# 3. EJEMPLO PRÁCTICO: FUNCIÓN DE LOGGING EN PYTHON
# ------------------------------------------------------------------------------

# Este ejemplo demuestra cómo se pueden usar las clausuras para añadir funcionalidad (como logging)
# a otras funciones sin modificarlas directamente.

import functools

# Nota: Este código ilustra un patrón similar al de un decorador en Python,
# que es un uso práctico de las clausuras.

def logger(func):
    """Función externa (logger) que toma una función como parámetro."""
    
    # La función interna, que actúa como la clausura.
    # *args permite que tome cualquier número de argumentos.
    def log_func(*args):
        # Lógica de logging: Se registra que la función se está ejecutando.
        log_message = f"Running function: {func.__name__} with arguments: {args}"
        
        # Opcional: Escribir el log a un archivo (simulado).
        with open('example.log', 'a') as f:
            f.write(log_message + '\n')
            
        print(f"LOG: {log_message}")

        # Ejecutamos la función original que fue pasada como argumento.
        result = func(*args)
        
        print(f"RESULT: {result}")
        return result

    # La clausura devuelve la función interna modificada.
    return log_func

# Funciones simples a las que queremos añadir la capacidad de logging.
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

print("\n# 3. EJEMPLO PRÁCTICO: CLAUSURA DE LOGGING")

# Creamos clausuras que envuelven las funciones 'add' y 'sub'.
add_logger = logger(add)
sub_logger = logger(sub)

# Usamos las nuevas variables como si fueran las funciones originales.
print("Ejecutando add_logger(3, 3):")
add_logger(3, 3) # La clausura log_func se ejecuta, llama a 'add', y registra los datos.

print("Ejecutando sub_logger(20, 10):")
sub_logger(20, 10) # La clausura log_func se ejecuta, llama a 'sub', y registra los datos.

# (Si se mira el archivo 'example.log' generado, contendrá los registros de ejecución.)
```