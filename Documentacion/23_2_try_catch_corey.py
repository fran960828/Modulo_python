
# ======================================================================================
# PYTHON TUTORIAL: USO DE BLOQUES TRY/EXCEPT PARA MANEJO DE ERRORES
# Fuente: "Corey Schafer - Python Tutorial: Using Try/Except Blocks for Error Handling"
# ======================================================================================

# Introducción a Try y Except
# Los bloques try/except se utilizan para manejar errores y excepciones en Python.
# A menudo, solo se utilizan las secciones 'try' y 'except'.
# El objetivo principal es evitar que los usuarios finales vean el largo y verboso 'traceback error' de Python.

# --------------------------------------------------------------------------------------
# Ejemplo 1: Manejo Básico de Errores (Error Anticipado)
# --------------------------------------------------------------------------------------

# Simulamos un error FileNotFoundError.
# Supongamos que el archivo correcto es 'test_file.txt'.
try:
    # El código que podría generar un error o excepción se coloca dentro del bloque 'try'.
    # Intentamos abrir un archivo que no existe (ejemplo de error intencional).
    f = open('test file.txt')
except:
    # Si se lanza una excepción en el bloque 'try', se ejecuta el bloque 'except'.
    # Aquí, se imprime un mensaje de error personalizado en lugar del traceback de Python.
    print("Lo sentimos, este archivo no existe") # Mensaje personalizado

# Nota sobre la generalidad de 'except':
# Usar un 'except' general es "vago". Capturará errores que no son el FileNotFoundError.
# El objetivo de los try/except no es evitar todos los errores, sino atrapar y manejar los errores que se esperan.

# --------------------------------------------------------------------------------------
# Ejemplo 2: Especificidad en las Excepciones
# --------------------------------------------------------------------------------------

# Es recomendable ser tan específico como sea posible al capturar excepciones.

try:
    # 1. Intentamos abrir el archivo correctamente.
    f = open('test_file.txt')

    # 2. Generamos un error inesperado (NameError, debido a una mala asignación).
    VAR = bad_VAR
    # Si el 'except' fuera general, atraparía este error y mostraría el mensaje del archivo.

except FileNotFoundError:
    # Al ser específicos (solo atrapando FileNotFoundError),
    # el NameError inesperado no es capturado, y se mostrará el traceback por defecto de Python.
    print("Error de Archivo No Encontrado (Específico)")

# --------------------------------------------------------------------------------------
# Ejemplo 3: Manejo de Múltiples Excepciones y Acceso al Mensaje
# --------------------------------------------------------------------------------------

# Podemos añadir múltiples bloques 'except' para capturar diferentes errores.
# Es fundamental colocar las excepciones más específicas en la parte superior,
# y las más generales (como 'Exception') más abajo.

try:
    f = open('test_file.txt')
    # Generamos un NameError nuevamente:
    VAR = bad_VAR
except FileNotFoundError as e:
    # Capturamos el error específico. Usamos 'as e' para asignar la instancia de la excepción a 'e'.
    # Esto permite imprimir el mensaje de error por defecto de Python.
    print(f"Error específico (FileNotFoundError): {e}")
except Exception as e:
    # Capturamos cualquier excepción más general.
    # Si esta excepción general estuviera al inicio, siempre se ejecutaría primero.
    # Imprimimos el mensaje de la excepción general:
    print(f"Error general: Lo sentimos, algo salió mal. Mensaje: {e}") #

# Ejecutando este ejemplo, se lanza NameError, que es atrapado por el 'except Exception'.

# --------------------------------------------------------------------------------------
# Ejemplo 4: El Bloque Else y Finalmente (Finally)
# --------------------------------------------------------------------------------------

# Bloque 'else':
# Se ejecuta si la cláusula 'try' no lanza ninguna excepción.

# Bloque 'finally':
# Se ejecuta SIEMPRE, sin importar si el código fue exitoso o si se lanzó una excepción.
# Es útil para asegurar la liberación de recursos (como cerrar archivos o conexiones a bases de datos).

print("\n--- Demostración de Else y Finally (Caso Exitoso) ---")
try:
    # Aquí el archivo debe existir para que 'try' sea exitoso.
    f = open('test_file.txt')
    # Simulamos la lectura:
    contents = "test file contents" # Contenido que se leería
except FileNotFoundError:
    print("Error en el bloque try.")
else:
    # 'else' se ejecuta porque 'try' no lanzó excepción.
    print(f"El código 'try' fue exitoso.")
    print(f"Contenido del archivo: {contents}") # Impresión del contenido
    f.close() # Cierre del archivo
finally:
    # 'finally' se ejecuta siempre.
    print("Estoy ejecutando el finally") #


print("\n--- Demostración de Finally (Caso con Error) ---")
try:
    # Hacemos que el 'try' lance una excepción.
    f = open('archivo_que_falla.txt')
except FileNotFoundError:
    print("Se capturó la excepción de archivo no encontrado.")
finally:
    # Aunque se lanzó la excepción, 'finally' se ejecuta.
    # Esto asegura que los recursos se cierren, independientemente del resultado.
    print("El bloque finally se ejecutó (a pesar de la excepción)") #


# --------------------------------------------------------------------------------------
# Ejemplo 5: Lanzamiento Manual de Excepciones (Raise)
# --------------------------------------------------------------------------------------

# Es posible lanzar excepciones manualmente si se cumplen ciertas condiciones.

CORRUPT_FILE = 'corrupt_file.txt'

try:
    # Abrimos un archivo simulado.
    f = open(CORRUPT_FILE)

    # Condición para levantar la excepción:
    if f.name == CORRUPT_FILE:
        # Usamos 'raise' seguido de la excepción que queremos levantar.
        # Esto permite atrapar errores que Python no habría detectado por sí mismo.
        raise Exception("Error") # Se lanza una excepción manual

except Exception:
    # Se captura la excepción general que acabamos de levantar manualmente.
    print("¡Error! La línea sí lanzó esta excepción manual y fue manejada en el except.") #
else:
    # Si la línea 'raise' se comenta, el código continúa aquí.
    print("El código se ejecutó normalmente.")
    f.close()
finally:
    # Se ejecuta al final, como siempre.
    print("Ejecutando finally.")
