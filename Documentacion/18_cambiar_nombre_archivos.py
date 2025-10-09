# Documentación del Script de Python para Renombrar Archivos
# Basado en el video "Python Tutorial: Automate Parsing and Renaming of Multiple Files"

import os

# 1. Importar el módulo OS
# El módulo 'os' (Operating System) permite navegar por el sistema de archivos, 
# cambiar directorios y renombrar archivos [1].

# 2. Cambiar el directorio de trabajo (Working Directory)
# Se utiliza os.chdir() para mover el script al directorio que contiene los archivos
# que se desean renombrar. Esto evita tener que usar rutas completas más tarde [1].
# NOTA: Reemplace 'RUTA/A/SU/CARPETA' con la ruta real de los archivos.
# El proceso original para obtener la ruta era arrastrar la carpeta a la terminal [2].
try:
    os.chdir('RUTA/A/SU/CARPETA')
except FileNotFoundError:
    print("Error: Asegúrese de que la ruta del directorio sea correcta.")
    # Puede optar por salir del script aquí si la ruta es crucial.
    # exit()

# Opcional: Verificar que estamos en el directorio correcto [2].
# print(os.getcwd())

# 3. Iterar sobre todos los archivos en el directorio
# Usamos os.listdir() para obtener una lista de todos los elementos en la carpeta [2].
for f in os.listdir(os.getcwd()):
    
    # 4. Dividir el nombre del archivo y la extensión
    # Usamos os.path.splitext(f) para dividir el nombre base del archivo y su extensión.
    # Esto devuelve una tupla (nombre_sin_extensión, .extensión) [3, 4].
    # Asignamos la tupla a dos variables: nombre_archivo y extensión_archivo.
    file_name, f_ext = os.path.splitext(f)
    
    # 5. Dividir el nombre del archivo en sus componentes usando el guión ('-')
    # Los nombres de archivo de ejemplo estaban en el formato: 
    # Título - Nombre del Curso - #Número [4, 5].
    # Al dividir por el guion, obtenemos tres elementos [6].
    f_title, f_course_name, f_num = file_name.split('-')
    
    # 6. Eliminar el espacio en blanco (whitespace)
    # Los componentes a menudo tienen espacios no deseados al principio o al final 
    # debido a los guiones, lo que se soluciona con el método strip() [7].
    f_title = f_title.strip()
    f_course_name = f_course_name.strip()
    f_num = f_num.strip()
    
    # 7. Limpiar y formatear el número para la ordenación
    
    # a) Eliminar el signo de número (#)
    # Se utiliza el slicing [1:] para tomar todos los caracteres excepto el primero (el '#') [8].
    # Ejemplo: '#1' se convierte en '1'.
    f_num = f_num[1:]

    # b) Rellenar con ceros (Zero Padding)
    # Se usa zfill(2) para asegurar que los dígitos simples (1, 2, 3...) tengan un cero
    # al principio (01, 02, 03...). Esto es crucial para la ordenación alfabética, 
    # ya que evita que el 10 aparezca inmediatamente después del 1 [9].
    f_num = f_num.zfill(2)
    
    # NOTA: El curso se eliminó de la cadena final por preferencia personal [10].
    
    # 8. Construir el nuevo nombre del archivo
    # El nuevo formato deseado es: Número-Título.Extensión [10].
    # Se utiliza una cadena formateada (f-string o .format, aquí se usa .format como en el video) [6, 7].
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    
    # 9. Renombrar el archivo
    # Se usa os.rename(nombre_original, nuevo_nombre) [10].
    # 'f' es el nombre original del archivo dentro del bucle [10].
    os.rename(f, new_name)
    
    # Opcional: Mostrar los resultados (descomentar para depuración)
    # print(f"Original: {f} -> Nuevo: {new_name}")

# Ejemplo de los pasos de transformación (no ejecutar, solo comentario):
# Original: 'Custom Title - Course Name - #1.mp4'
# 1. splitext -> file_name='Custom Title - Course Name - #1', f_ext='.mp4'
# 2. split('-') -> f_title='Custom Title', f_course_name='Course Name', f_num='#1' (con espacios)
# 3. strip() -> f_title='Custom Title', f_course_name='Course Name', f_num='#1' (sin espacios)
# 4. f_num[1:] -> f_num='1'
# 5. f_num.zfill(2) -> f_num='01'
# 6. Formato -> new_name = '01-Custom Title.mp4'