# ==============================================================================
# CONCEPTOS FUNDAMENTALES (RECAPITULACIÓN)
# ==============================================================================

# Antes de abordar los decoradores, es crucial entender dos conceptos:
# 1. Funciones de Primera Clase (First-Class Functions)
# 2. Clausuras (Closures)

# ------------------------------------------------------------------------------
# 1. FUNCIONES DE PRIMERA CLASE
# ------------------------------------------------------------------------------
# Las funciones de primera clase permiten tratar las funciones como cualquier otro objeto.
# Esto implica que las funciones pueden:
# - Ser asignadas a variables.
# - Ser pasadas como argumentos a otras funciones.
# - Ser devueltas como resultado de otras funciones.

def saludo(nombre):
    """Función simple para saludar."""
    return f"Hola, {nombre}"

def mayuscula(func, nombre):
    """Función de orden superior que toma otra función como argumento (F-C Function)."""
    # Ejecuta la función pasada y convierte el resultado a mayúsculas.
    return func(nombre).upper()

print("--- 1. Funciones de Primera Clase ---")
print(mayuscula(saludo, "Alice"))
# La función 'saludo' fue pasada como argumento a 'mayuscula'.


# ------------------------------------------------------------------------------
# 2. CLAUSURAS (CLOSURES)
# ------------------------------------------------------------------------------
# Una clausura permite que una función interna recuerde y tenga acceso a las variables
# locales del ámbito (scope) en el que fue creada, incluso después de que la función externa
# haya terminado de ejecutarse. Las variables a las que se accede pero que no se
# definen en la función interna se denominan "variables libres" (free variables).

def outer_function(msg):
    """Función externa que toma un argumento (MSG) que será recordado."""
    # msg es la variable libre que la clausura recordará.
    
    def inner_function():
        """Función interna (la clausura) que imprime el mensaje recordado."""
        print(msg)
        
    # Se devuelve la función interna sin ejecutarla (sin paréntesis).
    return inner_function

print("\n--- 2. Clausuras ---")

# Creamos dos clausuras diferentes. Cada una tiene su propio entorno (environment)
# que recuerda el valor de 'msg' pasado a la función externa.
hi_function = outer_function('hi')
bye_function = outer_function('bye')

# Ejecutamos las clausuras. A pesar de que 'outer_function' ya finalizó,
# 'hi_function' y 'bye_function' recuerdan sus respectivos mensajes.
print("Ejecutando hi_function (recuerda 'hi'):")
hi_function()

print("Ejecutando bye_function (recuerda 'bye'):")
bye_function()


# ==============================================================================
# INTRODUCCIÓN A LOS DECORADORES
# ==============================================================================

# Un decorador es simplemente una función que toma otra función como argumento,
# le añade algún tipo de funcionalidad y luego devuelve una nueva función.
# Todo esto se logra sin modificar el código fuente de la función original.

def decorator_function(original_function):
    """La función decoradora que recibe la función original."""
    
    # La función interna, a menudo llamada 'wrapper' (envoltorio).
    # Esta es la clausura que se devuelve y ejecuta en lugar de la original.
    def wrapper_function():
        # Aquí es donde se añade la funcionalidad (por ejemplo, impresión extra).
        print(f"Wrapper ejecutada antes de {original_function.__name__}")
        
        # Ejecuta la función original que se pasó como argumento.
        original_function()
        
        # Opcional: añadir funcionalidad después de la ejecución.
        
    # Se devuelve la función wrapper sin ejecutar.
    return wrapper_function

def display():
    """Función original simple que queremos decorar."""
    print("La función 'display' se ejecutó.")

print("\n--- 3. Decorador Básico (Sintaxis de Asignación) ---")

# Método 1: Asignar el resultado del decorador a una nueva variable.
decorated_display = decorator_function(display)

# Ejecutando la variable decorada. En realidad, se está ejecutando el wrapper.
decorated_display()


# ==============================================================================
# SINTAXIS ESTÁNDAR DE DECORADORES (@)
# ==============================================================================

# En Python, el símbolo '@' es una abreviatura sintáctica (syntactic sugar) para
# el proceso de asignación visto anteriormente.
# @decorator_function sobre 'display' es lo mismo que decir:
# display = decorator_function(display).

@decorator_function
def display_v2():
    print("La función 'display_v2' se ejecutó.")

print("\n--- 4. Sintaxis Estándar (@) ---")
# Cuando llamamos a 'display_v2', en realidad se llama al 'wrapper'.
display_v2()


# ==============================================================================
# DECORADORES CON ARGUMENTOS (*ARGS, **KWARGS)
# ==============================================================================

# Si la función original acepta argumentos, el 'wrapper_function' debe estar
# preparado para recibirlos, de lo contrario, se producirá un error (TypeError).
# Se utiliza *args para argumentos posicionales arbitrarios y **kwargs para
# argumentos de palabra clave arbitrarios.

def decorator_function_args(original_function):
    """Decorador que maneja argumentos."""
    
    # El wrapper debe aceptar *args y **kwargs y pasarlos a la función original.
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper ejecutada antes de {original_function.__name__} con argumentos: {args} {kwargs}")
        
        # Ejecutar la función original pasando todos los argumentos recibidos.
        result = original_function(*args, **kwargs)
        return result
        
    return wrapper_function

# Decoramos una función que requiere argumentos.
@decorator_function_args
def display_info(name, age):
    """Función que toma nombre y edad como argumentos posicionales."""
    print(f"display_info ejecutada con: Nombre={name}, Edad={age}")
    return True

print("\n--- 5. Decorador con *args y **kwargs ---")
# La clausura (wrapper) ahora puede recibir y manejar los argumentos.
display_info("John", 25)

# También funciona con funciones sin argumentos, como la versión simple:
@decorator_function_args
def simple_display():
    print("Ejecución simple.")
    
simple_display()


# ==============================================================================
# EJEMPLOS PRÁCTICOS: LOGGING Y TIMING
# ==============================================================================

import logging
import time

# Configuramos logging de forma simple para simular la escritura a archivos de log
# que usa el ejemplo del video.

# ------------------------------------------------------------------------------
# DECORADOR DE LOGGING (REGISTRO)
# ------------------------------------------------------------------------------
# Uso común para llevar un registro de cuándo se ejecutan ciertas funciones
# y qué argumentos se utilizaron.

def my_logger(orig_func):
    """Decorador para registrar información de ejecución de una función."""
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    
    def wrapper(*args, **kwargs):
        # Registramos que la función se ejecutó y con qué argumentos.
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        
        # Ejecutamos la función original y devolvemos el resultado.
        return orig_func(*args, **kwargs)
    
    return wrapper

# ------------------------------------------------------------------------------
# DECORADOR DE TIMING (TIEMPO DE EJECUCIÓN)
# ------------------------------------------------------------------------------
# Se utiliza para medir cuánto tiempo tarda en ejecutarse una función.

def my_timer(orig_func):
    """Decorador para medir el tiempo de ejecución de una función."""
    
    def wrapper(*args, **kwargs):
        t1 = time.time() # Registrar el tiempo de inicio.
        
        # Ejecutamos la función original y almacenamos el resultado.
        result = orig_func(*args, **kwargs)
        
        t2 = time.time() # Registrar el tiempo final.
        
        run_time = t2 - t1 # Calcular el tiempo transcurrido.
        
        print(f'{orig_func.__name__} ran in: {round(run_time, 4)} sec') # Imprimir el tiempo.
        
        return result # Devolver el resultado de la función original.
    
    return wrapper

@my_timer
@my_logger
def calculate_sum(a, b):
    """Función decorada con el temporizador y el registrador."""
    # Agregamos una pausa para que el temporizador sea evidente.
    time.sleep(1)
    return a + b

print("\n--- 6. Ejemplos Prácticos (Logger y Timer) ---")
print(f"Resultado de calculate_sum(10, 5): {calculate_sum(10, 5)}")
# Al ejecutarse, se imprime el tiempo y se registra la información en 'calculate_sum.log'.


# ==============================================================================
# ENCADENAMIENTO DE DECORADORES Y METADATOS
# ==============================================================================

import functools

# ------------------------------------------------------------------------------
# EL PROBLEMA CON EL ENCADENAMIENTO
# ------------------------------------------------------------------------------
# Al encadenar decoradores (apilarlos uno encima del otro), los decoradores inferiores
# se ejecutan primero.
# El decorador interior retorna el 'wrapper', lo que significa que el siguiente decorador
# recibe el 'wrapper', NO la función original.
# Esto causa problemas, ya que el nombre de la función ('__name__') y otra metadata
# se pierden, y los registros se crean con nombres como 'wrapper.log'.

@my_timer
def example_function():
    """Esta es una función de ejemplo."""
    pass

print("\n--- 7. Pérdida de Metadatos (Sin wraps) ---")
# Si imprimiéramos el nombre de la función decorada, obtendríamos 'wrapper'.
print(f"Nombre de la función decorada SIN wraps: {example_function.__name__}") # Se espera 'wrapper' si no se aplica wraps.

# ------------------------------------------------------------------------------
# SOLUCIÓN: FUNCTOOLS.WRAPS
# ------------------------------------------------------------------------------
# Es fundamental preservar la información de la función original al usar decoradores.
# El decorador '@functools.wraps(original_function)' se aplica al wrapper interno
# para copiar la metadata de la función original al wrapper.

def my_timer_fixed(orig_func):
    """Versión fija del decorador de timing que usa @wraps."""
    
    # Decoramos el wrapper con @wraps(la función original).
    @functools.wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        
        run_time = t2 - t1
        # Ahora se usa el nombre correcto gracias a @wraps.
        print(f'{orig_func.__name__} ran in: {round(run_time, 4)} sec') 
        
        return result
    
    return wrapper

@my_timer_fixed
def final_example_function():
    """Esta función preserva su nombre gracias a wraps."""
    pass

print("\n--- 8. Preservando Metadatos (Con wraps) ---")
print(f"Nombre de la función decorada CON wraps: {final_example_function.__name__}") # Se espera 'final_example_function'.

# Este uso de 'wraps' resuelve el problema de la pérdida de metadatos cuando se
# utilizan decoradores encadenados.

# ==============================================================================
# DOCUMENTACIÓN: CREACIÓN DE DECORADORES QUE ACEPTAN ARGUMENTOS
# Basado en el video "Python Tutorial: Decorators With Arguments"
# ==============================================================================

# El objetivo de este material es mostrar cómo se pueden crear decoradores que
# aceptan argumentos.

# Un ejemplo común de esto se ve en aplicaciones web Flask, donde las rutas
# (routes) se definen utilizando decoradores como `app.route`, y se pasa
# una cadena (string) como argumento que representa la ruta URL (por ejemplo,
# la página "about").

# ------------------------------------------------------------------------------
# EJEMPLO 1: RECAPITULACIÓN DEL DECORADOR BÁSICO
# Este código muestra la estructura de un decorador simple sin argumentos.
# ------------------------------------------------------------------------------

def decorator_function(original_func):
    # La función decoradora toma la función original como argumento.
    
    def wrapper_function(*args, **kwargs):
        # La función wrapper anidada toma cualquier número de argumentos o
        # argumentos de palabra clave.
        
        # Ejecutando código antes de la función original.
        print('Executed before original function') 
        
        # Ejecución de la función original y guardando el resultado.
        result = original_func(*args, **kwargs)
        
        # Ejecutando código después de la función original.
        print('Executed after the original function')
        
        # Retornando el resultado de la ejecución.
        return result
    
    # Retornando la función wrapper, esperando a ser ejecutada.
    return wrapper_function

# Función a ser decorada
@decorator_function
def display_info(name, age):
    # Esta función simple solo imprime el nombre y la edad.
    print(f'display_info ran with arguments ({name}, {age})')

# Ejecución del ejemplo 1
# print("\n--- Ejecución del Ejemplo 1 (Básico) ---")
# display_info('John', 25) # Se ejecuta dos veces, añadiendo la funcionalidad del decorador.
# display_info('Sara', 30)

# ------------------------------------------------------------------------------
# EJEMPLO 2: CREANDO UN DECORADOR CON ARGUMENTOS
# ------------------------------------------------------------------------------

# Para permitir que el decorador acepte un argumento (como un prefijo
# personalizable para las declaraciones de impresión dentro del wrapper),
# se debe añadir una capa externa adicional a la estructura.

def prefix_decorator(prefix):
    # La nueva capa externa toma el argumento deseado (en este caso, 'prefix').
    
    # La función `decorator_function` (ahora anidada) toma la función original.
    def decorator_function(original_func):
        
        def wrapper_function(*args, **kwargs):
            # Ahora, todo lo anidado aquí tiene acceso al argumento 'prefix'.
            
            # Usando el argumento 'prefix' en las declaraciones de impresión.
            print(prefix, 'Executed before original function') 
            
            result = original_func(*args, **kwargs)
            
            # Usando el argumento 'prefix' en la declaración de impresión posterior.
            print(prefix, 'Executed after the original function')
            
            return result
        
        # Después de que la función wrapper retorna, retornamos la función wrapper.
        return wrapper_function
    
    # Dado que se anidó un nivel más, se necesita otro retorno. 
    # La función externa retorna la función decoradora sin ejecutar.
    # Esta anidación múltiple de funciones puede resultar confusa rápidamente.
    return decorator_function

# Función a ser decorada (usando el decorador que acepta argumentos)
# Cuando decoramos, usamos la función más externa y pasamos el argumento.

@prefix_decorator('Testing:')
def display_info_with_prefix_1(name, age):
    print(f'display_info_with_prefix_1 ran with arguments ({name}, {age})')

@prefix_decorator('LOG:')
def display_info_with_prefix_2(name, age):
    print(f'display_info_with_prefix_2 ran with arguments ({name}, {age})')


# Ejecución del ejemplo 2

print("\n--- Ejecución del Ejemplo 2 (Con Argumento: 'Testing:') ---")
# Se puede observar que el prefijo 'Testing:' aparece antes de las
# declaraciones de impresión añadidas por el wrapper.
display_info_with_prefix_1('Michael', 45) 

print("\n--- Ejecución del Ejemplo 2 (Con Argumento: 'LOG:') ---")
# El prefijo puede cambiarse en cualquier momento, usando 'LOG:' en este caso.
display_info_with_prefix_2('Jane', 21) 

# ------------------------------------------------------------------------------
# RESUMEN
# ------------------------------------------------------------------------------

# Para crear un decorador que acepta argumentos, se debe añadir una capa
# adicional que acepta esos argumentos y envuelve al decorador original.
# Esta capa exterior devuelve la función decoradora, que a su vez devuelve
# la función wrapper.
# Esta técnica es útil cuando se necesita una funcionalidad personalizable
# que se pasa al decorador, como se ve en frameworks como Flask.
```