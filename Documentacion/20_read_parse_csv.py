
# ===================================================================================================
# Módulo CSV de Python: Lectura, Análisis y Escritura de Archivos (Corey Schafer Tutorial)
# ===================================================================================================

# Importamos el módulo CSV. Este módulo hace que el análisis de archivos de datos estructurados sea mucho
# más fácil que usar métodos básicos de división de cadenas (split).
import csv 

# ---------------------------------------------------------------------------------------------------
# INFORMACIÓN GENERAL SOBRE ARCHIVOS CSV
# ---------------------------------------------------------------------------------------------------

# CSV significa Valores Separados por Comas (Comma Separated Values).
# Un archivo CSV es un archivo de texto sin formato que almacena datos utilizando un delimitador
# (generalmente una coma) para separar diferentes campos.
# Aunque la coma es el delimitador más común, se puede usar casi cualquier cosa, como tabuladores, guiones o barras.
# En el archivo de ejemplo utilizado en la fuente, los campos son: nombre, apellido y correo electrónico.

# ---------------------------------------------------------------------------------------------------
# CONFIGURACIÓN (PREPARACIÓN PARA LA EJECUCIÓN)
# ---------------------------------------------------------------------------------------------------
# Para que los ejemplos 1, 2 y 5 funcionen, debe crear manualmente un archivo de entrada.
# Lo nombraremos 'datos_originales.csv' en el mismo directorio que este script.
#
# Contenido esperado de 'datos_originales.csv':
# first_name,last_name,email
# John,Doe,john.doe@example.com
# Jane,Smith-Robinson,jane_smith-robinson@other.net
# ... (más líneas de datos)

nombre_archivo_original = 'datos_originales.csv' 


# ---------------------------------------------------------------------------------------------------
# Ejemplo 1: Lectura Básica con csv.reader
# ---------------------------------------------------------------------------------------------------

# El método más común para trabajar con datos CSV es utilizando el 'reader' y 'writer'.
try:
    # Usamos un gestor de contexto ('with open') para abrir el archivo en modo de lectura ('r').
    with open(nombre_archivo_original, 'r', newline='') as archivo_csv:
        
        # Creamos el objeto lector_csv.
        # El método reader espera por defecto que los valores estén separados por una coma.
        lector_csv = csv.reader(archivo_csv) 
        
        print("\n--- Ejemplo 1: Lectura con csv.reader (Cada línea como una lista) ---")
        
        # El objeto lector_csv es un iterable, por lo que necesitamos un bucle para recorrerlo.
        for linea in lector_csv:
            # Cada 'linea' se imprime como una lista, donde cada elemento es un valor.
            print(linea)

except FileNotFoundError:
    print(f"\n[AVISO]: El archivo '{nombre_archivo_original}' no fue encontrado. Saltando Ejemplo 1.")

# ---------------------------------------------------------------------------------------------------
# Ejemplo 2: Acceso a Campos Específicos y Omisión de Encabezados
# ---------------------------------------------------------------------------------------------------

try:
    with open(nombre_archivo_original, 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        
        # La primera línea contiene los nombres de los campos.
        # Para saltar esta primera línea y comenzar con los datos, se llama a la función next().
        # Si quisiéramos capturar esos encabezados en una variable, también podríamos usar next().
        next(lector_csv) 
        
        print("\n--- Ejemplo 2: Imprimir solo el Correo Electrónico (Índice 2) ---")
        
        # En nuestro ejemplo de archivo, los índices son: Nombre (0), Apellido (1), Correo Electrónico (2).
        for linea in lector_csv:
            # Imprimimos solo el valor en el índice 2 (el correo electrónico).
            print(linea) 
            
except FileNotFoundError:
    pass # Ya se manejó la excepción de archivo

# ---------------------------------------------------------------------------------------------------
# Ejemplo 3: Escritura Básica con un Delimitador Personalizado
# ---------------------------------------------------------------------------------------------------

nombre_archivo_nuevo = 'nuevos_nombres_tabulados.csv'

# Datos simulados para escribir (lista de listas):
datos_para_escribir = [
    ['first_name', 'last_name', 'email'],
    ['John', 'Doe', 'john.doe@example.com'],
    # El escritor CSV maneja automáticamente el entrecomillado si el valor contiene el delimitador.
    # Si hubiéramos usado '-' como delimitador, 'Smith-Robinson' se citaría.
    ['Jane', 'Smith-Robinson', 'jane_smith-robinson@other.net'] 
]

# Abrimos un nuevo archivo en modo escritura ('w').
with open(nombre_archivo_nuevo, 'w', newline='') as nuevo_archivo:
    
    # Creamos el escritor CSV utilizando el método csv.writer.
    # Para usar tabuladores ('\t') en lugar de comas, pasamos 'delimiter' como argumento.
    escritor_csv = csv.writer(nuevo_archivo, delimiter='\t') 
    
    print(f"\n--- Ejemplo 3: Escribiendo en '{nombre_archivo_nuevo}' con delimitador de tabulación ---")
    
    # Recorremos los datos y escribimos cada fila usando writerow().
    for fila in datos_para_escribir:
        escritor_csv.writerow(fila)
        
    print(f"Archivo '{nombre_archivo_nuevo}' creado exitosamente (separado por tabuladores).")


# ---------------------------------------------------------------------------------------------------
# Ejemplo 4: Lectura con Delimitador Incorrecto vs. Delimitador Correcto
# ---------------------------------------------------------------------------------------------------

# Si intentamos leer un archivo que usa un delimitador (ej: tabulador) sin especificarlo en el lector,
# Python seguirá esperando comas.

print("\n--- Ejemplo 4a: Lectura fallida (Esperando comas en archivo tabulado) ---")
try:
    with open(nombre_archivo_nuevo, 'r', newline='') as archivo_tabulado:
        # El lector asume ',' como delimitador.
        lector_fallido = csv.reader(archivo_tabulado)
        for linea in lector_fallido:
            # Cada línea aparecerá con un solo valor, ya que no se dividió por la pestaña.
            print(linea) 
except FileNotFoundError:
    pass
    
print("\n--- Ejemplo 4b: Lectura correcta especificando el delimitador ---")
try:
    with open(nombre_archivo_nuevo, 'r', newline='') as archivo_tabulado:
        # Pasamos explícitamente el argumento 'delimiter' para que el análisis sea correcto.
        lector_correcto = csv.reader(archivo_tabulado, delimiter='\t') 
        for linea in lector_correcto:
            print(linea)
except FileNotFoundError:
    pass


# ---------------------------------------------------------------------------------------------------
# Ejemplo 5: Lectura usando csv.DictReader (Lector de Diccionario)
# ---------------------------------------------------------------------------------------------------

# DictReader es un método preferido porque el código es más legible (más "evidente").
try:
    with open(nombre_archivo_original, 'r', newline='') as archivo_csv:
        # Usamos DictReader en lugar de reader.
        # DictReader utiliza la primera línea automáticamente como claves (nombres de campo).
        lector_dict = csv.DictReader(archivo_csv)
        
        print("\n--- Ejemplo 5: Lectura con csv.DictReader (Accediendo por clave) ---")
        
        for linea in lector_dict:
            # 'linea' es ahora un diccionario ordenado.
            # Accedemos a los valores usando el nombre del campo como clave.
            # Esto es más claro que usar un índice numérico (linea).
            print(linea['email'])
            
except FileNotFoundError:
    pass # Ya se manejó la excepción de archivo


# ---------------------------------------------------------------------------------------------------
# Ejemplo 6: Escritura usando csv.DictWriter y Selección de Campos
# ---------------------------------------------------------------------------------------------------

# DictWriter requiere que proporcionemos explícitamente los nombres de los campos (fieldnames).
nombre_archivo_dict_salida = 'nombres_reducidos_dict.csv'

# Definimos solo los campos que queremos incluir en el nuevo archivo (omitiendo 'email').
nombres_de_campo = ['first_name', 'last_name'] 

# Datos simulados en formato de lista de diccionarios (el formato de salida de DictReader):
datos_dict_para_escribir = [
    {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com'},
    {'first_name': 'Jane', 'last_name': 'Smith-Robinson', 'email': 'jane_smith-robinson@other.net'}
]

with open(nombre_archivo_dict_salida, 'w', newline='') as nuevo_archivo:
    
    # Creamos el escritor de diccionario, pasando el archivo y la lista de 'fieldnames'.
    escritor_dict = csv.DictWriter(nuevo_archivo, fieldnames=nombres_de_campo) 
    
    print(f"\n--- Ejemplo 6: Escribiendo con csv.DictWriter (Omitiendo Email) ---")
    
    # Escribimos los encabezados (nombres de campo) en la primera fila.
    escritor_dict.writeheader() 
    
    # Recorremos los datos originales
    for fila_dict in datos_dict_para_escribir:
        
        # Opcional: Para asegurarnos de que solo se escriban los campos deseados, 
        # eliminamos el campo 'email' del diccionario antes de escribir la fila.
        if 'email' in fila_dict:
            del fila_dict['email']
            
        # Escribir la fila. Ahora solo contendrá 'first_name' y 'last_name'.
        escritor_dict.writerow(fila_dict) 

    print(f"Archivo '{nombre_archivo_dict_salida}' creado exitosamente (email omitido).")

```