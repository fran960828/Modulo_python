
# ==============================================================================
# DOCUMENTACIÓN DE OBJETOS DE ARCHIVO (FILE OBJECTS) EN PYTHON
# Basado en el tutorial de video: "Python Tutorial: File Objects - Reading and Writing to Files"
# ==============================================================================

# INTRODUCCIÓN Y USO DE LOS OBJETOS DE ARCHIVO
# -------------------------------------------

# Los objetos de archivo son fundamentales en Python para interactuar con archivos,
# ya sea en aplicaciones de escritorio o web [1].
# Para obtener un objeto de archivo, se utiliza el comando incorporado 'open' [1].
# Si el archivo está en el mismo directorio que el script de Python, basta con pasar
# el nombre del archivo (ejemplo: 'test.txt'). De lo contrario, se debe pasar la ruta
# completa al comando 'open' [2].

# El comando 'open' permite especificar el modo de operación:
# - 'r': Lectura (Reading). Es el modo por defecto si no se especifica nada [2].
# - 'w': Escritura (Writing) [3].
# - 'a': Anexar (Appending) [3].
# - 'r+': Lectura y Escritura (Reading and Writing) [3].

# Práctica recomendada: Context Managers
# Aunque se puede abrir un archivo directamente (f = open(...)), la forma recomendada
# es usar un 'context manager' con la palabra clave 'with' [1, 4].
# Si un archivo se abre sin un 'context manager', se debe recordar cerrarlo explícitamente
# con 'f.close()' para evitar fugas (leaks) que pueden causar errores si se excede el
# máximo de descriptores de archivo permitidos [3, 4].
# El uso de 'with open(...) as F:' garantiza que el archivo se cierre automáticamente
# después de salir del bloque de código, incluso si ocurren excepciones. Esto maneja
# la limpieza automáticamente [5].

# ==============================================================================
# PASO A PASO Y CÓDIGO DEL VIDEO
# ==============================================================================

# 1. Apertura Básica y explícita (Método NO recomendado)
# ------------------------------------------------------------------------------

# Se abre 'test.txt' en modo de lectura ('r') [2].
# Fíjese que este método requiere el uso explícito de f.close() [3].

# f = open('test.txt', 'r')

# Se imprime el nombre del archivo y el modo con el que fue abierto [3, 4].

# print(f.name)
# print(f.mode) # Imprime 'r' [4].

# Se cierra el archivo explícitamente [3].
# f.close()


# 2. Uso del Context Manager (Método RECOMENDADO)
# ------------------------------------------------------------------------------

# Usamos 'with open(...) as F:' [4].
# La variable de archivo 'F' se declara usando 'as F' a la derecha [5].
# El archivo se cerrará automáticamente al salir del bloque [5].

with open('test.txt', 'r') as f:
    # Dentro del bloque, podemos usar el objeto de archivo 'f'.
    # print(f.name)
    # pass # Indica que no se realiza ninguna operación por ahora [5].
    
# Después de salir del bloque del Context Manager, el archivo está cerrado [5].
# Si intentamos acceder a la propiedad 'closed' en 'f', debería devolver True [6].
# print(f.closed)

# Nota: Intentar realizar una operación de E/S (I/O) en el archivo 'f' fuera del bloque
# arrojará un error `ValueError` ("IO operation on a closed file") [6].


# 3. Métodos para Leer Contenido
# ------------------------------------------------------------------------------
with open('test.txt', 'r') as f:
    
    # 3.1. f.read(): Lee el contenido COMPLETO del archivo [7].
    # Esto es adecuado para archivos pequeños [7].
    
    # f_contents = f.read()
    # print(f_contents)
    
    # 3.2. f.readlines(): Lee todas las líneas y devuelve una LISTA [7].
    # La lista incluye los caracteres de nueva línea ('\n') [7].
    
    # f_contents_list = f.readlines()
    # print(f_contents_list)
    
    # 3.3. f.readline(): Lee una SOLA línea [7].
    # Cada llamada posterior a f.readline() avanza y lee la siguiente línea [8].
    
    # f_line_1 = f.readline()
    # print(f_line_1, end='') # Se usa end='' para evitar doble nueva línea [8].
    
    # f_line_2 = f.readline()
    # print(f_line_2, end='') # Imprime la segunda línea [8].
    
    # 3.4. Iterar sobre el archivo (Manera eficiente para archivos grandes)
    # Esto lee el contenido línea por línea, evitando cargar todo el archivo
    # grande en la memoria a la vez [8, 9].
    
    # for line in f:
    #     print(line, end='')


# 4. Lectura Controlada por Tamaño (Chunks)
# ------------------------------------------------------------------------------
with open('test.txt', 'r') as f:
    
    # 4.1. f.read(size): Permite especificar la cantidad de datos (caracteres) a leer [9, 10].
    
    # chunk_size = 100
    
    # f_contents_chunk = f.read(chunk_size)
    # print(f_contents_chunk) # Imprime los primeros 100 caracteres [10].
    
    # f_contents_next_chunk = f.read(chunk_size)
    # print(f_contents_next_chunk) # Continúa donde se detuvo y lee 100 más [10].
    
    # Si se intenta leer al final del archivo, f.read() devuelve una cadena vacía [10].
    
    # 4.2. Usando un loop 'while' para leer archivos grandes por partes (chunks)
    
    size_to_read = 10 # Para demostrar el flujo, se usa un tamaño pequeño [11].
    
    f_contents = f.read(size_to_read) # Lee el primer chunk [12].
    
    while len(f_contents) > 0:
        # Se imprime el chunk leído (se usa '*' para visualizar el límite del chunk) [11].
        # print(f_contents, end='*')
        
        # Se lee el siguiente chunk. Si llega al final, f_contents será una cadena vacía,
        # lo que detendrá el loop 'while' [12].
        f_contents = f.read(size_to_read) 


# 5. Control de Posición: f.tell() y f.seek()
# ------------------------------------------------------------------------------
with open('test.txt', 'r') as f:
    size_to_read = 10
    
    # Se leen los primeros 10 caracteres [13].
    # f_contents = f.read(size_to_read)
    # print(f_contents)
    
    # f.tell(): Muestra la posición actual (en bytes o caracteres) [11, 13].
    # print(f.tell()) # Después de leer 10 caracteres, debería devolver 10 [13].
    
    # 5.1. f.seek(): Manipula la posición actual [13].
    # f.seek(0) mueve la posición al inicio del archivo [14].
    
    # f.seek(0)
    
    # Si leemos de nuevo después de f.seek(0), la segunda lectura comenzará
    # desde el inicio, no donde lo dejó la primera lectura [14].
    
    # f_contents_2 = f.read(size_to_read)
    # print(f_contents_2) # Imprime de nuevo los primeros 10 caracteres [14].


# 6. Escribir en Archivos ('w' y 'a')
# ------------------------------------------------------------------------------

# Nota: Intentar escribir ('f.write()') en un archivo abierto en modo lectura ('r')
# resultará en un error porque el archivo no es escribible [14, 15].

# Modo 'w' (Write):
# - Si el archivo no existe (ejemplo: 'test2.txt'), lo crea [15].
# - Si el archivo SÍ existe, lo SOBREESCRIBE (be careful!) [15].

# Modo 'a' (Append):
# - Si no se desea sobrescribir, se utiliza 'a' para anexar contenido al final [15].

with open('test2.txt', 'w') as f:
    # El archivo 'test2.txt' se crea simplemente al abrirlo en modo 'w' [15].
    
    # 6.1. Escritura simple
    # f.write('test') # Escribe 'test' [16].
    
    # 6.2. Escritura continua
    # La escritura avanza la posición, similar a la lectura [16].
    
    # f.write('test') # Escribe el segundo 'test' inmediatamente después [16].
    
    # 6.3. Uso de seek() durante la escritura
    # Usar seek(0) permite volver al inicio para sobrescribir [16].
    
    f.write('test') 
    f.seek(0) # Vuelve al inicio [16].
    
    # Si escribimos un contenido más corto, solo sobrescribirá lo necesario.
    # El resto del contenido anterior permanece [17].
    f.write('r') # Sobreescribe la 't' de 'test', dejando 'rest' [17].

# 7. Copiar Archivos de Texto
# ------------------------------------------------------------------------------

# Se abren dos archivos: uno para leer (RF) y uno para escribir (WF) [17, 18].
# Abrir múltiples archivos se puede hacer anidando los 'with' statements [18].

# 'test.txt' (original) se abre para lectura ('r') como RF [17].
# 'test_copy.txt' (copia) se abre para escritura ('w') como WF [18].

with open('test.txt', 'r') as rf: # RF: Read File [17].
    with open('test_copy.txt', 'w') as wf: # WF: Write File [18].
        
        # Iteramos sobre las líneas del archivo original (RF) [18].
        for line in rf:
            # Escribimos cada línea directamente al archivo de copia (WF) [18].
            wf.write(line)

# Esto crea una copia exacta de 'test.txt' en 'test_copy.txt' [19].


# 8. Copiar Archivos Binarios (Imágenes)
# ------------------------------------------------------------------------------

# Al tratar de copiar imágenes (o archivos no textuales) en modo de texto ('r'/'w'),
# se produce un error de codificación (ej. `UTF codec can't decode byte...`) [19, 20].

# Para trabajar con archivos binarios (imágenes), se debe usar el modo binario,
# añadiendo 'b' a los modos de lectura y escritura: 'rb' y 'wb' [20].
# Esto indica que leeremos y escribiremos bytes, no texto [20].

# Para copiar archivos grandes de forma eficiente, se utiliza la lectura por chunks
# en modo binario [21].

chunk_size = 4096 # Se establece un tamaño de chunk común para eficiencia [21].

with open('bronx.jpeg', 'rb') as rf_binary: # 'rb' para lectura binaria [20].
    with open('bronx_copy.jpeg', 'wb') as wf_binary: # 'wb' para escritura binaria [20].
        
        # Leemos el primer chunk binario [21].
        rf_chunk = rf_binary.read(chunk_size)
        
        # Mientras haya datos en el chunk (la longitud sea mayor que cero) [21].
        while len(rf_chunk) > 0:
            # Escribimos ese chunk al archivo de copia [21].
            wf_binary.write(rf_chunk)
            
            # Leemos el siguiente chunk para evitar un bucle infinito [21, 22].
            rf_chunk = rf_binary.read(chunk_size)
            
# Esto crea una copia binaria exacta de la imagen original [22].