# ====================================================
# 📌 DOCUMENTACIÓN Y EJEMPLOS DEL MÓDULO os
# ====================================================
# El módulo `os` permite interactuar con el sistema operativo.
# Con él podemos:
#   - Manejar directorios y archivos
#   - Acceder a variables de entorno
#   - Recorrer estructuras de carpetas
#   - Consultar información de archivos
#
# ⚠️ Los ejemplos son seguros: se crean carpetas/archivos temporales para mostrar su funcionamiento.

import os

# ----------------------------------------------------
# 1. os.getcwd()
# ----------------------------------------------------
# Devuelve el directorio de trabajo actual.
print("\n=== os.getcwd() ===")
print("Directorio actual:", os.getcwd())


# ----------------------------------------------------
# 2. os.chdir(path)
# ----------------------------------------------------
# Cambia el directorio de trabajo.
# ⚠️ Hay que tener cuidado, puede afectar rutas relativas en tu programa.
print("\n=== os.chdir() ===")
actual = os.getcwd()
os.chdir("..")  # Subimos un nivel
print("Directorio tras cambiar:", os.getcwd())
os.chdir(actual)  # Volvemos al original


# ----------------------------------------------------
# 3. os.listdir(path)
# ----------------------------------------------------
# Lista los archivos y carpetas dentro de un directorio.
print("\n=== os.listdir() ===")
print("Contenido del directorio actual:", os.listdir("."))


# ----------------------------------------------------
# 4. os.mkdir(path)
# ----------------------------------------------------
# Crea un directorio (error si ya existe).
print("\n=== os.mkdir() ===")
if not os.path.exists("carpeta_ejemplo"):
    os.mkdir("carpeta_ejemplo")
    print("Carpeta 'carpeta_ejemplo' creada")


# ----------------------------------------------------
# 5. os.makedirs(path)
# ----------------------------------------------------
# Crea directorios anidados de forma recursiva.
print("\n=== os.makedirs() ===")
if not os.path.exists("carpeta_ejemplo/subcarpeta/anidada"):
    os.makedirs("carpeta_ejemplo/subcarpeta/anidada")
    print("Carpetas anidadas creadas")


# ----------------------------------------------------
# 6. os.rmdir(path)
# ----------------------------------------------------
# Elimina un directorio vacío.
print("\n=== os.rmdir() ===")
if not os.path.exists("para_borrar"):
    os.mkdir("para_borrar")
os.rmdir("para_borrar")
print("Directorio 'para_borrar' eliminado")


# ----------------------------------------------------
# 7. os.removedirs(path)
# ----------------------------------------------------
# Elimina directorios de forma recursiva si están vacíos.
print("\n=== os.removedirs() ===")
os.makedirs("para_borrar2/subdir", exist_ok=True)
os.removedirs("para_borrar2/subdir")
print("Carpetas eliminadas recursivamente")


# ----------------------------------------------------
# 8. os.rename(src, dst)
# ----------------------------------------------------
# Renombra un archivo o carpeta.
print("\n=== os.rename() ===")
if not os.path.exists("carpeta_renombrar"):
    os.mkdir("carpeta_renombrar")
os.rename("carpeta_renombrar", "carpeta_renombrada")
print("Carpeta renombrada a 'carpeta_renombrada'")


# ----------------------------------------------------
# 9. os.stat(path)
# ----------------------------------------------------
# Devuelve información del archivo (tamaño, permisos, fecha modif.).
print("\n=== os.stat() ===")
with open("archivo.txt", "w") as f:
    f.write("Hola mundo")
info = os.stat("archivo.txt")
print("Tamaño archivo:", info.st_size, "bytes")


# ----------------------------------------------------
# 10. os.walk(path)
# ----------------------------------------------------
# Recorre un directorio de forma recursiva.
print("\n=== os.walk() ===")
for ruta, carpetas, archivos in os.walk("."):
    print("Ruta:", ruta)
    print("Carpetas:", carpetas)
    print("Archivos:", archivos)
    break  # solo mostramos la primera iteración


# ----------------------------------------------------
# 11. os.environ.get(key)
# ----------------------------------------------------
# Obtiene variables de entorno (ejemplo: PATH).
print("\n=== os.environ.get() ===")
print("PATH:", os.environ.get("PATH"))


# ====================================================
# 📂 Funciones útiles de os.path
# ====================================================

# ----------------------------------------------------
# 12. os.path.join(path, *paths)
# ----------------------------------------------------
# Une rutas de forma segura (independiente del SO).
print("\n=== os.path.join() ===")
ruta = os.path.join("carpeta_ejemplo", "subcarpeta", "archivo.txt")
print("Ruta unida:", ruta)


# ----------------------------------------------------
# 13. os.path.basename(path)
# ----------------------------------------------------
# Obtiene el nombre del archivo o carpeta al final de la ruta.
print("\n=== os.path.basename() ===")
print("Basename:", os.path.basename(ruta))


# ----------------------------------------------------
# 14. os.path.dirname(path)
# ----------------------------------------------------
# Obtiene el directorio que contiene el archivo.
print("\n=== os.path.dirname() ===")
print("Directorio:", os.path.dirname(ruta))


# ----------------------------------------------------
# 15. os.path.split(path)
# ----------------------------------------------------
# Devuelve una tupla (directorio, nombre_archivo).
print("\n=== os.path.split() ===")
print("Split:", os.path.split(ruta))


# ----------------------------------------------------
# 16. os.path.splitext(path)
# ----------------------------------------------------
# Separa el nombre de archivo de su extensión.
print("\n=== os.path.splitext() ===")
print("Splitext:", os.path.splitext("ejemplo.py"))


# ----------------------------------------------------
# 17. os.path.isfile(path)
# ----------------------------------------------------
# Verifica si una ruta es un archivo.
print("\n=== os.path.isfile() ===")
print("¿archivo.txt es archivo?:", os.path.isfile("archivo.txt"))


# ----------------------------------------------------
# 18. os.path.exists(path)
# ----------------------------------------------------
# Verifica si un archivo o carpeta existe.
print("\n=== os.path.exists() ===")
print("¿Existe archivo.txt?:", os.path.exists("archivo.txt"))
print("¿Existe carpeta_renombrada?:", os.path.exists("carpeta_renombrada"))


# ----------------------------------------------------
# 🔍 Buenas prácticas profesionales con os
# ----------------------------------------------------
# ✅ Usar os.path.join en lugar de concatenar rutas con + o "/"
# ✅ Validar siempre con os.path.exists antes de borrar/crear
# ✅ Usar pathlib (más moderno y orientado a objetos) en proyectos nuevos
# ✅ Usar os.walk para recorrer grandes estructuras de carpetas
# ✅ Evitar rutas absolutas "hardcodeadas", preferir rutas relativas seguras
# ✅ Para compatibilidad multiplataforma, siempre usar funciones de os.path
