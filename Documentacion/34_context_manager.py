
# ==============================================================================
# INTRODUCCIÓN A LOS GESTORES DE CONTEXTO (Context Managers)
# ==============================================================================

# Los gestores de contexto en Python son herramientas que nos permiten administrar
# recursos de manera adecuada. Esto significa que podemos especificar
# exactamente qué queremos configurar (setup) y qué queremos limpiar o cerrar (teardown)
# cuando trabajamos con ciertos objetos.

# Un ejemplo clásico y muy útil es el manejo de archivos.
# Cuando usamos un gestor de contexto (identificado por la instrucción 'with'),
# ya no tenemos que recordar cerrar el recurso (como un archivo) después de usarlo.
# Además, si ocurre un error mientras trabajamos con el recurso, el gestor
# de contexto se asegura de que el recurso se cierre correctamente.

# Son útiles para muchos recursos, como abrir y cerrar archivos, conectar y cerrar
# bases de datos automáticamente, o adquirir y liberar bloqueos (locks).

# ==============================================================================
# EJEMPLO 1: CREAR UN GESTOR DE CONTEXTO USANDO UNA CLASE
# ==============================================================================

# Este ejemplo replica la funcionalidad de abrir y cerrar un archivo, pero creando
# nuestra propia clase para entender cómo funciona la administración interna.

# 1. MÉTODOS ESPECIALES:
# Una clase para ser un gestor de contexto necesita al menos tres métodos especiales:
# __init__, __enter__ y __exit__.

# 2. __init__:
# Este método se usa para inicializar la clase y aceptar los argumentos que le pasamos
# (en este caso, el nombre del archivo y el modo de apertura, como 'r' o 'w').
# Estos argumentos se guardan como atributos de la instancia (`self.file_name`, `self.mode`)
# para que otros métodos puedan acceder a ellos.

# 3. __enter__ (CONFIGURACIÓN / SETUP):
# Este es el código que se ejecuta cuando comienza el bloque 'with'.
# Aquí es donde abrimos el recurso (el archivo).
# El valor que retornamos desde __enter__ es el objeto con el que trabajaremos
# dentro del bloque `with` (el que se asigna a la variable 'as F').

# 4. __exit__ (LIMPIEZA / TEARDOWN):
# Este es el código que se ejecuta al salir del bloque 'with'.
# Su propósito principal es realizar la limpieza, en este caso, cerrar el archivo (`self.file.close()`).
# Los parámetros adicionales de __exit__ son para manejar información si se lanza una excepción.

class OpenFile:
    """
    Gestor de contexto personalizado para abrir y cerrar archivos usando una clase.
    """
    def __init__(self, file_name, mode):
        # Configuración inicial: guardamos el nombre y el modo como atributos.
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        # FASE DE SETUP: Abrimos el archivo.
        self.file = open(self.file_name, self.mode)
        # Retornamos el objeto archivo, que se usará dentro del bloque 'with'.
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        # FASE DE TEARDOWN: Cerramos el archivo.
        # Esto se ejecuta al salir del bloque 'with', garantizando el cierre.
        self.file.close()

# USO DEL GESTOR DE CONTEXTO BASADO EN CLASE:
# Utilizamos la sintaxis 'with'.
FILE_NAME_1 = "sample_class.txt"

# El objeto retornado por __enter__ (el archivo abierto) se asigna a 'f'.
with OpenFile(FILE_NAME_1, 'w') as f:
    # Dentro del bloque 'with', trabajamos con el archivo 'f'.
    f.write("Probando el gestor de contexto de clase.\n")

# Verificamos que el archivo se cerró automáticamente al salir del bloque 'with'.
# Si se cerró, 'f.closed' debería ser True.
print(f"¿El archivo {FILE_NAME_1} se cerró (Clase)? {f.closed}\n")
# El resultado debería ser True, demostrando que __exit__ hizo su trabajo.


# ==============================================================================
# EJEMPLO 2: CREAR UN GESTOR DE CONTEXTO USANDO UNA FUNCIÓN GENERADORA
# ==============================================================================

# Una forma más sencilla y común de crear gestores de contexto es usando una
# función generadora con el decorador `@contextmanager` del módulo `contextlib`.

# 1. IMPORTACIÓN:
# Necesitamos importar el decorador de contextlib.
from contextlib import contextmanager

# 2. ESTRUCTURA:
# La función debe estar decorada con `@contextmanager`.
# Todo el código ANTES de la declaración 'yield' es la CONFIGURACIÓN (SETUP).
# Lo que se YIELD (cede) es el objeto con el que el usuario trabajará dentro del bloque 'with'.
# Todo el código DESPUÉS de la declaración 'yield' es la LIMPIEZA (TEARDOWN).

# 3. MANEJO DE ERRORES:
# Para asegurar que la limpieza (teardown) se ejecute incluso si ocurre un error
# dentro del bloque 'with', debemos poner el setup y el yield dentro de un bloque 'try',
# y la limpieza dentro de un bloque 'finally'.

FILE_NAME_2 = "sample_function.txt"

@contextmanager
def open_file_context(file_name, mode):
    # FASE DE SETUP (dentro de try):
    f = open(file_name, mode)
    try:
        # Aquí se pausa la función y se cede el control al bloque 'with'.
        # F es el objeto que se asignará a la variable 'as F'.
        yield f
    # Después de salir del bloque 'with' (ya sea normal o por error),
    # se ejecuta la limpieza en 'finally'.
    finally:
        # FASE DE TEARDOWN: Cerramos el archivo.
        f.close()

# USO DEL GESTOR DE CONTEXTO BASADO EN FUNCIÓN:
with open_file_context(FILE_NAME_2, 'w') as f:
    # Trabajamos con 'f' dentro del contexto.
    f.write("Probando el gestor de contexto de función/generador.\n")

# Verificamos que la limpieza se ejecutó (el archivo está cerrado).
print(f"¿El archivo {FILE_NAME_2} se cerró (Función)? {f.closed}\n")


# ==============================================================================
# EJEMPLO 3: GESTOR DE CONTEXTO PRÁCTICO (CAMBIO DE DIRECTORIOS)
# ==============================================================================

# Este es un ejemplo práctico para manejar recursos que no son archivos.
# El objetivo es poder cambiar temporalmente a un directorio específico,
# hacer un trabajo allí, y luego volver automáticamente al directorio original.

# La secuencia requerida es: 1. Guardar la ubicación actual. 2. Cambiar a la nueva.
# 3. Trabajar. 4. Volver a la ubicación guardada.
# Los pasos 1 y 2 son el SETUP, y el paso 4 es el TEARDOWN.

import os

@contextmanager
def change_dir(destination):
    # El módulo 'os' debe importarse para trabajar con directorios.

    # FASE DE SETUP:
    try:
        # 1. Guardamos el Directorio de Trabajo Actual (Original).
        cwd = os.getcwd()
        # 2. Cambiamos al Directorio de Destino.
        os.chdir(destination)

        # 3. Cedemos el control para que el usuario trabaje en el nuevo directorio.
        # Como no estamos pasando un objeto para trabajar con 'as F', solo usamos yield.
        yield

    # FASE DE TEARDOWN (dentro de finally para manejar errores):
    finally:
        # 4. Volvemos al Directorio de Trabajo Original.
        os.chdir(cwd)

# USO DEL GESTOR DE CONTEXTO PARA CAMBIAR DIRECTORIOS:
# (Nota: Para que este código funcione, las carpetas 'sample_dir_1' y 'sample_dir_2'
# deben existir en el mismo lugar donde se ejecuta este script. Asumimos que existen
# y contienen archivos, tal como se describe en las fuentes).

# Definimos directorios (se asume que existen por el contexto del video):
DIR_1 = "sample_directory_1"
DIR_2 = "sample_directory_2"

# Sin gestor de contexto, tendríamos que guardar la ubicación y volver manualmente.
# Con el gestor de contexto, el setup y el teardown son automáticos.

print(f"Directorio inicial: {os.getcwd()}") # Muestra la ubicación antes de empezar

# Bloque 1: Trabajando en el Directorio 1
with change_dir(DIR_1):
    # Setup: Ya estamos en DIR_1. No necesitamos usar 'as'.
    print(f"\nEntrando en {DIR_1}:")
    # Realizamos la tarea (por ejemplo, listar contenidos).
    print(os.listdir(os.getcwd()))
# Teardown: El gestor de contexto automáticamente regresa al directorio original.

# Bloque 2: Reutilizando el gestor con el Directorio 2
with change_dir(DIR_2):
    # Setup: Ya estamos en DIR_2.
    print(f"\nEntrando en {DIR_2}:")
    # Realizamos la tarea.
    print(os.listdir(os.getcwd()))
# Teardown: El gestor de contexto automáticamente regresa al directorio original.

print(f"\nDirectorio final: {os.getcwd()}") # Debería ser el mismo que el inicial

# Conclusión: Los gestores de contexto limpian el código y aseguran que los recursos
# (como la ubicación del directorio, archivos o conexiones de base de datos)
# se manejen y se cierren apropiadamente, incluso si hay errores.

