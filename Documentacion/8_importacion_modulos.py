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
'''
mi_proyecto/
│
├── mi_proyecto/             # Paquete principal
│   ├── __init__.py          # Convierte la carpeta en paquete
│   ├── modulo1.py           # Módulo con funciones/clases
│   ├── modulo2.py
│   └── subpaquete/          # Subpaquete
│       ├── __init__.py
│       └── herramientas.py
│
├── tests/                   # Carpeta para pruebas (unit tests)
│   └── test_modulo1.py
│
├── requirements.txt         # Lista de dependencias (pip freeze > requirements.txt)
├── setup.py                 # Configuración si lo distribuyes como paquete
├── README.md                # Documentación del proyecto
└── main.py                  # Punto de entrada del programa

'''
# ====================================================
# 📌 DOCUMENTACIÓN SOBRE ESTRUCTURA DE PROYECTOS PYTHON
# ====================================================

# ----------------------------------------------------
# 1. Paquetes y __init__.py
# ----------------------------------------------------
# Un archivo __init__.py convierte una carpeta en "paquete".
# Puede estar vacío, pero también se puede usar para inicializar.
#
# Ejemplo: en mi_proyecto/__init__.py
# print("Paquete mi_proyecto cargado")

# ----------------------------------------------------
# 2. Importaciones absolutas (RECOMENDADO)
# ----------------------------------------------------
# Se refieren siempre desde el "raíz del proyecto".
#
# Ejemplo: en main.py
# from mi_proyecto.modulo1 import funcion1

# ----------------------------------------------------
# 3. Importaciones relativas (usadas dentro de paquetes)
# ----------------------------------------------------
# Sirven cuando trabajamos dentro de un paquete.
#
# Ejemplo: en mi_proyecto/modulo2.py
# from .modulo1 import funcion1      # Import relativo (mismo nivel)
# from .subpaquete import herramientas  # Subpaquete

# ----------------------------------------------------
# 4. Ejemplo de módulo con funciones
# ----------------------------------------------------
# Archivo: mi_proyecto/modulo1.py
#
# def saludar(nombre):
#     return f"Hola {nombre}"
#
# Archivo: main.py
# from mi_proyecto.modulo1 import saludar
# print(saludar("Ana"))

# ----------------------------------------------------
# 5. Subpaquetes
# ----------------------------------------------------
# Archivo: mi_proyecto/subpaquete/herramientas.py
#
# def multiplicar(a, b):
#     return a * b
#
# Archivo: main.py
# from mi_proyecto.subpaquete.herramientas import multiplicar
# print(multiplicar(2, 3))

# ----------------------------------------------------
# 6. Uso de sys.path para pruebas rápidas
# ----------------------------------------------------
# En algunos casos, si el proyecto no está instalado,
# podemos añadir la carpeta raíz al sys.path
#
import sys
sys.path.append("mi_proyecto")  # ⚠️ Solo recomendable para pruebas rápidas

# ----------------------------------------------------
# 7. requirements.txt
# ----------------------------------------------------
# Se usa para listar dependencias de un proyecto.
# Se genera con:
#   pip freeze > requirements.txt
# Y se instala con:
#   pip install -r requirements.txt

# ----------------------------------------------------
# 8. setup.py (para empaquetar el proyecto)
# ----------------------------------------------------
# Ejemplo simple de setup.py:
#
# from setuptools import setup, find_packages
#
# setup(
#     name="mi_proyecto",
#     version="0.1",
#     packages=find_packages(),
#     install_requires=["numpy", "pandas"],
# )

# ----------------------------------------------------
# 9. Buenas prácticas profesionales
# ----------------------------------------------------
# ✅ Usar entornos virtuales (venv o conda).
# ✅ Mantener el código dividido en módulos y paquetes.
# ✅ No abusar de importaciones relativas.
# ✅ Documentar cada función con docstrings.
# ✅ Usar carpetas tests/ para pruebas unitarias.
# ✅ Incluir README.md con instrucciones de uso.
# ✅ Usar requirements.txt o poetry/conda para gestionar dependencias.
