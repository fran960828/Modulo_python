```python
# ==============================================================================
# DOCUMENTACIÓN DEL TUTORIAL: LOGGING BÁSICO EN PYTHON
# ==============================================================================
# El objetivo de este tutorial es mostrar cómo empezar a usar el módulo de registro
# (logging) en Python, reemplazando las declaraciones 'print' por declaraciones 'log',
# estableciendo diferentes niveles de registro y guardando la información en archivos.
#
# El módulo 'logging' está integrado en Python, por lo que no es necesario instalar
# nada adicional.
#
# Tener un buen sistema de registro es crucial para que una aplicación crezca
# más allá de un proyecto básico. Los logs permiten examinar el comportamiento
# y los errores a lo largo del tiempo, ofreciendo una mejor visión de lo que está
# sucediendo en el código.

import logging

# ==============================================================================
# 1. PREPARACIÓN INICIAL Y SUSTITUCIÓN DE 'PRINT' POR 'LOG'
# ==============================================================================

# Se definen cuatro funciones sencillas de calculadora.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Variables de ejemplo.
num_1 = 10
num_2 = 5

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Mapeo de Funciones y Variables)
# ------------------------------------------------------------------------------
# Nota: Inicialmente, las salidas se harían con print, pero las reemplazaremos
# con logging para demostrar el cambio de funcionalidad.


# ==============================================================================
# 2. INTRODUCCIÓN A LOS NIVELES DE REGISTRO (LOGGING LEVELS)
# ==============================================================================
# Los niveles permiten categorizar la información que queremos registrar.
# Hay cinco niveles estándar:
#
# 1. DEBUG: Información detallada, útil solo al diagnosticar problemas.
# 2. INFO: Confirmación de que las cosas están funcionando como se espera.
# 3. WARNING: Algo inesperado ocurrió o es indicativo de un problema,
#             pero el software sigue funcionando (ej: poco espacio en disco).
# 4. ERROR: Debido a un problema más grave, el software no pudo realizar una función.
# 5. CRITICAL: Un error grave que indica que el programa podría ser incapaz
#              de continuar ejecutándose.

# El nivel predeterminado (default) para el logging es WARNING.
# Esto significa que por defecto, solo se registrarán mensajes de nivel WARNING, ERROR y CRITICAL.
# Los mensajes DEBUG e INFO serán ignorados.

# Ejemplo de nivel por debajo del predeterminado (DEBUG):
# Si solo usamos logging.debug("Mensaje de prueba") sin configurar nada,
# no se mostrará nada en la consola porque el nivel por defecto es WARNING.


# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Demostración de niveles por defecto)
# ------------------------------------------------------------------------------

# Para demostrar el nivel por defecto (WARNING):
# Si esto fuera logging.debug(...), no se vería la salida.
# Si esto es logging.warning(...), sí se ve la salida.
logging.warning(f'Add: {num_1} + {num_2} = {add(num_1, num_2)}')
# Al ejecutar, el resultado muestra más información que un 'print',
# incluyendo el nivel (WARNING), 'root' (que se explicará en el siguiente video)
# y el mensaje.


# ==============================================================================
# 3. CAMBIANDO EL NIVEL PREDETERMINADO CON BASIC CONFIG
# ==============================================================================
# Para capturar mensajes de niveles inferiores, como DEBUG o INFO,
# debemos cambiar la configuración básica usando el método basicConfig.

# Se usa la palabra clave 'level' y se establece a la constante en mayúsculas.
# La constante en mayúsculas (logging.DEBUG) es diferente del método (logging.debug).
# Las constantes de nivel son realmente números enteros (DEBUG = 10, INFO = 20, etc.).

logging.basicConfig(level=logging.DEBUG) # Ahora capturamos DEBUG y niveles superiores.

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Uso de DEBUG tras reconfiguración)
# ------------------------------------------------------------------------------

num_1 = 10
num_2 = 5

# Ahora estos mensajes DEBUG se registran en la consola, ya que el nivel fue reconfigurado.
logging.debug(f'Add: {num_1} + {num_2} = {add(num_1, num_2)}')
logging.debug(f'Subtract: {num_1} - {num_2} = {subtract(num_1, num_2)}')
logging.debug(f'Multiply: {num_1} * {num_2} = {multiply(num_1, num_2)}')
logging.debug(f'Divide: {num_1} / {num_2} = {divide(num_1, num_2)}')


# ==============================================================================
# 4. REGISTRAR INFORMACIÓN EN UN ARCHIVO
# ==============================================================================
# En lugar de solo imprimir en la consola, podemos crear archivos de registro.
# Esto permite ver la información de registro a lo largo del tiempo en un solo lugar.
# Se hace agregando el parámetro 'filename' a basicConfig.

# NOTA: En un entorno de desarrollo, basicConfig solo se llama una vez.
# Aquí se vuelve a llamar para demostrar la nueva configuración.

logging.basicConfig(
    filename='test_log.log', # Especifica el archivo donde se guardará el registro.
    level=logging.DEBUG      # Mantiene el nivel en DEBUG.
)

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Guardando en archivo)
# ------------------------------------------------------------------------------
num_1 = 20
num_2 = 10

logging.debug(f'Add: {num_1} + {num_2} = {add(num_1, num_2)}')
logging.debug(f'Subtract: {num_1} - {num_2} = {subtract(num_1, num_2)}')
# Al ejecutar, no aparecerá nada en la consola, pero se creará o actualizará
# el archivo 'test_log.log' con los nuevos valores y los registros anteriores.


# ==============================================================================
# 5. PERSONALIZACIÓN DEL FORMATO DE REGISTRO
# ==============================================================================
# Para cambiar la estructura de la línea de registro (que por defecto incluye el nivel,
# el logger 'root' y el mensaje), usamos el parámetro 'format'.
# Se utilizan códigos de formato especiales (atributos de Log Record).

# Códigos de formato especiales comunes:
# - %(asctime)s: La hora legible.
# - %(levelname)s: El nombre del nivel (DEBUG, INFO, etc.).
# - %(message)s: El mensaje de registro.

logging.basicConfig(
    filename='test_formatted.log',
    level=logging.DEBUG,
    # El formato deseado es: Tiempo : Nivel de Nombre : Mensaje
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Uso del nuevo formato)
# ------------------------------------------------------------------------------

logging.info("El logging ahora incluye la marca de tiempo.")
logging.debug(f'Multiply: {num_1} * {num_2} = {multiply(num_1, num_2)}')

# El archivo 'test_formatted.log' mostrará el nuevo formato con la hora.


# ==============================================================================
# 6. REGISTRO EN UN MÓDULO SEPARADO (CLASE EMPLOYEE)
# ==============================================================================
# Se usa una clase simple (Employee) como ejemplo de un módulo separado.
# Queremos registrar la creación de empleados a lo largo del tiempo.

class Employee:
    """Clase que registra la creación de empleados."""
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # Reemplazamos el 'print' original por una llamada de logging.
        # La creación de un empleado es un buen candidato para el nivel INFO.

        logging.info(f'Created Employee: {self.first} {self.last}') #

# Configuramos logging.basicConfig específicamente para este "módulo".
logging.basicConfig(
    filename='employee.log', # Archivo de registro específico para empleados.
    level=logging.INFO,      # Nivel establecido a INFO, ignorando DEBUG.
    # Usamos un formato simplificado: Nivel de Nombre : Mensaje.
    format='%(levelname)s:%(message)s'
)

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Creación de Empleados)
# ------------------------------------------------------------------------------

# Creación de tres instancias de empleados.
Employee('Bob', 'Jones')
Employee('Sue', 'Smith')
Employee('Jane', 'Doe')

# El archivo 'employee.log' contendrá los registros de nivel INFO con el formato personalizado.


# ==============================================================================
# 7. LIMITACIONES DE LA CONFIGURACIÓN BÁSICA
# ==============================================================================
# Para aplicaciones pequeñas, este enfoque de logging es un buen comienzo.
# Sin embargo, tiene problemas cuando se importan múltiples módulos.
# Todos los módulos intentan compartir el mismo registrador ('root logger').
#
# Esto lleva a configuraciones conflictivas. La solución para aplicaciones
# más grandes implica:
# 1. Crear registradores (loggers) separados.
# 2. Añadir manejadores (handlers).
# 3. Añadir formateadores (formatters) a esos loggers.
# Esto permite enviar información a múltiples ubicaciones (archivos, consolas, etc.).
# Estos temas avanzados se cubren en videos posteriores.
```
# ==============================================================================
# TUTORIAL DE LOGGING AVANZADO EN PYTHON
# ==============================================================================
# Este tutorial se centra en cómo configurar registradores (Loggers) específicos,
# usar manejadores (Handlers) y formateadores (Formatters) para tener un control
# preciso sobre dónde y cómo se registran nuestros mensajes.
#
# Si bien es útil para proyectos pequeños, se recomienda aprender buenas prácticas
# de registro a medida que la aplicación crece.
#
# El módulo 'logging' es nativo de Python y no requiere instalación.

import logging

# ------------------------------------------------------------------------------
# 1. EL PROBLEMA DE COMPARTIR EL REGISTRADOR RAÍZ (ROOT LOGGER)
# ------------------------------------------------------------------------------
# Inicialmente, en el logging básico, se utiliza logging.basicConfig().
# Cuando usamos basicConfig, estamos configurando implícitamente el 'Root Logger'.
#
# El problema surge cuando importamos un módulo (como 'employee.py') que también
# utiliza basicConfig. La configuración del Root Logger solo se realiza una vez.
# Si el módulo importado se configura primero (ej: Nivel INFO), el script
# principal que se ejecuta después no puede sobrescribir esa configuración (ej: Nivel DEBUG).
# Esto resulta en configuraciones no deseadas, niveles incorrectos y archivos de
# registro perdidos.
#
# La solución es usar registradores específicos para cada módulo.

# ==============================================================================
# 2. CREACIÓN Y CONFIGURACIÓN DE UN REGISTRADOR ESPECÍFICO (MÓDULO EMPLOYEE)
# ==============================================================================

# Paso A: Obtener el Logger
# Usamos logging.getLogger() para obtener un registrador. Si no existe, lo crea.
# Por convención, usamos __name__ como nombre del logger. Si el módulo es importado,
# __name__ será el nombre del módulo ('employee'); si se ejecuta directamente, será '__main__'.
employee_logger = logging.getLogger('employee_module')
employee_logger.setLevel(logging.INFO) # Establecemos el nivel INFO en el logger.

# Paso B: Crear el Manejador de Archivos (File Handler)
# El manejador es responsable de dirigir el mensaje a su destino (en este caso, un archivo).
file_handler = logging.FileHandler('employee.log')

# Paso C: Crear el Formateador (Formatter)
# El formateador define la estructura y el contenido de la línea de registro.
# Formato: Nivel de Nombre (levelname), Nombre del Logger (name), Mensaje (message).
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# Paso D: Asignar el Formato y Añadir el Handler
# Asignamos el formato al manejador de archivos.
file_handler.setFormatter(formatter)
# Añadimos el manejador al registrador específico.
employee_logger.addHandler(file_handler)

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Simulación del Módulo Employee)
# ------------------------------------------------------------------------------

# Definición de una clase simple (simulando el módulo employee.py).
class Employee:
    """Clase para demostrar el registro de creación de empleados."""
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # Usamos el logger específico en lugar de 'logging.info'.
        employee_logger.info(f'Created Employee: {self.first} {self.last}')

# Creación de empleados
Employee('Alice', 'Wonder')
Employee('Bob', 'Marley')

# NOTA: Este logger ya no utiliza el Root Logger y guarda los mensajes
# de nivel INFO o superior en 'employee.log' con el formato especificado.


# ==============================================================================
# 3. CONFIGURACIÓN DEL SEGUNDO REGISTRADOR (APLICACIÓN PRINCIPAL)
# ==============================================================================

# Simulamos la configuración para la aplicación principal (simple_app.py).
main_logger = logging.getLogger('simple_app_module')
# Establecemos el nivel a DEBUG (Queremos ver toda la información de depuración).
main_logger.setLevel(logging.DEBUG)

# Definimos funciones de calculadora
def add(x, y):
    main_logger.debug(f'Add: {x} + {y}')
    return x + y

def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        # Usaremos logger.exception más adelante, por ahora usamos error.
        main_logger.error('Tried to divide by zero')
        return None

# Configuramos un FileHandler específico para la aplicación principal ('sample.log').
main_file_handler = logging.FileHandler('sample.log')

# Configuramos un Formateador diferente, que incluye la hora (asctime).
main_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
main_file_handler.setFormatter(main_formatter)

# Añadimos el FileHandler al logger principal.
main_logger.addHandler(main_file_handler)

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Operaciones de la aplicación principal)
# ------------------------------------------------------------------------------
num_a = 50
num_b = 25

add_result = add(num_a, num_b)
main_logger.debug(f'Result Add: {add_result}')

# NOTA: Los mensajes DEBUG ahora se registran en 'sample.log' y el 'employee.log'
# permanece sin cambios, demostrando la separación de configuraciones.


# ==============================================================================
# 4. ESTABLECER NIVELES EN MANEJADORES (FILTRADO)
# ==============================================================================
# La jerarquía de niveles permite que el logger tenga un nivel bajo (ej: DEBUG),
# pero sus manejadores tengan niveles más altos para filtrar qué mensajes registran.
#
# EJEMPLO: El logger principal está en DEBUG (captura todo), pero queremos que
# 'sample.log' solo registre mensajes de nivel ERROR o superior.

# Nivel del logger: DEBUG (Captura todos los mensajes)
# main_logger.setLevel(logging.DEBUG) # (Ya establecido)

# Nivel del manejador: ERROR (Solo escribe errores y mensajes críticos al archivo).
main_file_handler.setLevel(logging.ERROR)

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Demostración de filtrado por Handler)
# ------------------------------------------------------------------------------

# Mensaje DEBUG: Pasa el nivel del logger (DEBUG) pero es rechazado por el
# FileHandler (que solo acepta ERROR+).
main_logger.debug("Este mensaje DEBUG es ignorado por 'sample.log'")

# Mensaje ERROR: Pasa el nivel del logger y el nivel del FileHandler.
divide_result_error = divide(100, 0)
# El error 'Tried to divide by zero' aparecerá en 'sample.log'.


# ==============================================================================
# 5. REGISTRO DE EXCEPCIONES Y TRAZAS DE PILA (TRACEBACK)
# ==============================================================================
# Cuando se produce un error, es útil incluir la traza de pila (traceback) para
# una mejor depuración.
# Podemos lograr esto cambiando 'logger.error()' por 'logger.exception()'.
# 'logger.exception()' debe usarse solo dentro de un bloque 'except'.

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Usando logger.exception para incluir Traceback)
# ------------------------------------------------------------------------------

def divide_with_traceback(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        # Registra el mensaje Y la traza de pila completa.
        main_logger.exception('Tried to divide by zero (WITH TRACEBACK)')
        return None

divide_result_tb = divide_with_traceback(200, 0)

# NOTA: El archivo 'sample.log' registrará la traza de pila del error,
# proporcionando más detalles sobre la causa.


# ==============================================================================
# 6. MÚLTIPLES MANEJADORES: STREAM HANDLER (CONSOLA)
# ==============================================================================
# Un registrador puede tener varios manejadores. Por ejemplo, uno para archivos
# (FileHandler) y otro para la consola (StreamHandler).
# Esto permite ver la depuración en tiempo real en la consola sin llenar el archivo.

# Paso A: Crear un Stream Handler
# StreamHandler envía los mensajes al flujo de salida (ej: la terminal o consola).
stream_handler = logging.StreamHandler()
# No necesitamos configurar el nivel si queremos que herede el DEBUG del logger.

# Paso B: Formato específico para la consola
# Podemos reutilizar el formato existente o definir uno nuevo.
# Usamos el formato definido previamente (asctime:name:message).
stream_handler.setFormatter(main_formatter)

# Paso C: Añadir el Stream Handler
main_logger.addHandler(stream_handler)

# ------------------------------------------------------------------------------
# CÓDIGO EJECUTABLE (Doble Salida)
# ------------------------------------------------------------------------------
# Recordatorio: Logger: DEBUG; File Handler: ERROR; Stream Handler: DEBUG (heredado).

# Mensaje DEBUG: Aparece en la CONSOLA (Stream Handler), pero no en el archivo.
main_logger.debug("Mensaje DEBUG, visible solo en la consola.")

# Mensaje ERROR: Aparece en la CONSOLA y también en el ARCHIVO 'sample.log'.
main_logger.error("Error crítico, visible en ambos destinos.")

# NOTA FINAL: El uso de loggers, handlers y formatters específicos proporciona
# flexibilidad modular, permitiendo dirigir diferentes niveles de mensajes a
# diferentes destinos (archivos, consola, email, etc.).
```