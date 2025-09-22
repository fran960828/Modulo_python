# ====================================================
# 📌 DOCUMENTACIÓN Y EJEMPLOS DE IMPORTACIÓN EN PYTHON
# ====================================================

# ----------------------------------------------------
# 1. Importar módulos estándar de Python
# ----------------------------------------------------
# Python trae una gran librería estándar lista para usar.
# Ejemplo: importamos el módulo math
import math

print("Raíz cuadrada de 16:", math.sqrt(16))
print("Pi:", math.pi)


# ----------------------------------------------------
# 2. Importar con alias
# ----------------------------------------------------
# Podemos dar un alias para abreviar nombres largos
import math as m

print("Seno de 90°:", m.sin(m.radians(90)))


# ----------------------------------------------------
# 3. Importar funciones o variables específicas
# ----------------------------------------------------
# Así no necesitamos usar el prefijo del módulo
from math import sqrt, pi

print("Raíz cuadrada con import directo:", sqrt(25))
print("Valor de pi importado directo:", pi)


# ----------------------------------------------------
# 4. Importar todos los elementos (NO recomendado)
# ----------------------------------------------------
# Puede causar conflictos de nombres y confusión.
# from math import *

# print(sin(0))  # Funciona, pero poco claro de dónde viene


# ----------------------------------------------------
# 5. Importar módulos externos (ejemplo con NumPy)
# ----------------------------------------------------
# Deben instalarse primero con:
#   pip install numpy
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print("Array de numpy:", array)
print("Media:", np.mean(array))


# ----------------------------------------------------
# 6. Importar módulos propios
# ----------------------------------------------------
# Supongamos que tenemos un archivo llamado `mimodulo.py`
# con este contenido:
#
# def saludar(nombre):
#     return f"Hola {nombre}"
#
# En este archivo lo podemos importar y usar.
# ⚠️ El archivo debe estar en el mismo directorio o en sys.path

# import mimodulo
# print(mimodulo.saludar("Pythonista"))

# También se puede importar una función específica:
# from mimodulo import saludar
# print(saludar("Ana"))


# ----------------------------------------------------
# 7. Uso del módulo sys en importaciones
# ----------------------------------------------------
import sys

# sys.path es una lista de directorios donde Python busca módulos
print("Rutas de búsqueda de módulos en sys.path:")
for ruta in sys.path:
    print(" -", ruta)

# Podemos añadir dinámicamente una ruta donde tengamos módulos propios
# Supongamos que tenemos un módulo en la carpeta "modulos_externos"
sys.path.append("modulos_externos")

# Ahora podríamos importar un módulo que esté ahí
# import modulo_personalizado


# ----------------------------------------------------
# 8. Importación condicional
# ----------------------------------------------------
# Útil cuando un módulo puede no estar disponible
try:
    import pandas as pd
    print("Pandas está instalado, versión:", pd.__version__)
except ImportError:
    print("Pandas no está instalado, omitiendo...")


# ----------------------------------------------------
# 9. Recargar módulos
# ----------------------------------------------------
# Cuando modificamos un módulo propio durante ejecución,
# podemos recargarlo sin reiniciar el intérprete
# Esto es útil en entornos interactivos (ejemplo: Jupyter)

# import importlib
# import mimodulo
# importlib.reload(mimodulo)


# ----------------------------------------------------
# 🔍 Buenas prácticas profesionales
# ----------------------------------------------------
# - Agrupar imports al inicio del archivo.
# - Orden recomendado:
#   1. Librerías estándar de Python.
#   2. Librerías externas (instaladas con pip).
#   3. Módulos propios del proyecto.
# - Usar alias claros (ej: import numpy as np, import pandas as pd).
# - Evitar "from modulo import *".
# - Usar importaciones absolutas en proyectos grandes.
# - Manipular sys.path solo si es estrictamente necesario
#   (mejor usar entornos virtuales y buenas estructuras de proyecto).
#
# Ejemplo de orden recomendado:
#
# import os
# import sys
#
# import numpy as np
# import pandas as pd
#
# import mimodulo
