# ====================================================
# 📌 DOCUMENTACIÓN Y EJEMPLOS DEL USO DE PIP (COMPLETO)
# ====================================================
# pip = "Pip Installs Packages"
# Gestor oficial de dependencias de Python.
#
# ⚠️ La mayoría de comandos se ejecutan en TERMINAL.
# Aquí los documentamos con ejemplos comentados y cómo correrlos desde Python.
#
# 💡 Importamos subprocess para ejecutar comandos desde el script.
import subprocess

# ----------------------------------------------------
# 1. pip help
# ----------------------------------------------------
# Muestra todos los comandos y opciones de pip
# Terminal: pip help
print("\n=== pip help ===")
subprocess.run(["pip", "help"])


# ----------------------------------------------------
# 2. pip --version
# ----------------------------------------------------
# Muestra la versión de pip y de Python
# Terminal: pip --version
print("\n=== Versión de pip ===")
subprocess.run(["pip", "--version"])


# ----------------------------------------------------
# 3. pip install <paquete>
# ----------------------------------------------------
# Instala un paquete desde PyPI
# Terminal: pip install requests
print("\n=== Instalando paquete requests ===")
subprocess.run(["pip", "install", "requests"])


# ----------------------------------------------------
# 4. pip uninstall <paquete>
# ----------------------------------------------------
# Desinstala un paquete
# Terminal: pip uninstall requests
print("\n=== Desinstalando paquete requests ===")
subprocess.run(["pip", "uninstall", "-y", "requests"])


# ----------------------------------------------------
# 5. pip show <paquete>
# ----------------------------------------------------
# Muestra información detallada sobre un paquete instalado
# Terminal: pip show numpy
print("\n=== Información del paquete numpy ===")
subprocess.run(["pip", "show", "numpy"])


# ----------------------------------------------------
# 6. pip list
# ----------------------------------------------------
# Lista todos los paquetes instalados
# Terminal: pip list
print("\n=== Lista de paquetes instalados ===")
subprocess.run(["pip", "list"])


# ----------------------------------------------------
# 7. pip list -o
# ----------------------------------------------------
# Lista paquetes que tienen actualizaciones disponibles
# Terminal: pip list -o
print("\n=== Paquetes con actualizaciones disponibles ===")
subprocess.run(["pip", "list", "-o"])


# ----------------------------------------------------
# 8. pip check
# ----------------------------------------------------
# Verifica que todas las dependencias instaladas son compatibles
# Terminal: pip check
print("\n=== Verificación de dependencias ===")
subprocess.run(["pip", "check"])


# ----------------------------------------------------
# 9. pip search <paquete> (⚠️ deprecado)
# ----------------------------------------------------
# En versiones modernas se usa:
#   pip index search requests
# Terminal: pip index search requests
print("\n=== Búsqueda de paquete 'requests' en PyPI ===")
subprocess.run(["pip", "index", "search", "requests"])


# ----------------------------------------------------
# 10. pip index versions <paquete>
# ----------------------------------------------------
# Muestra todas las versiones disponibles de un paquete
# Terminal: pip index versions numpy
print("\n=== Versiones disponibles de numpy ===")
subprocess.run(["pip", "index", "versions", "numpy"])


# ----------------------------------------------------
# 11. pip install -U <paquete>
# ----------------------------------------------------
# Actualiza un paquete a la última versión
# Terminal: pip install -U numpy
print("\n=== Actualizando numpy ===")
subprocess.run(["pip", "install", "-U", "numpy"])


# ----------------------------------------------------
# 12. pip freeze
# ----------------------------------------------------
# Muestra las dependencias instaladas con versión exacta
# Terminal: pip freeze
print("\n=== Dependencias con freeze ===")
subprocess.run(["pip", "freeze"])


# ----------------------------------------------------
# 13. pip freeze > requirements.txt
# ----------------------------------------------------
# Exporta dependencias a un archivo de requisitos
# Terminal: pip freeze > requirements.txt
print("\n=== Guardando dependencias en requirements.txt ===")
with open("requirements.txt", "w") as f:
    subprocess.run(["pip", "freeze"], stdout=f)


# ----------------------------------------------------
# 14. pip install -r requirements.txt
# ----------------------------------------------------
# Instala todas las dependencias desde un archivo de requisitos
# Terminal: pip install -r requirements.txt
print("\n=== Instalando desde requirements.txt ===")
subprocess.run(["pip", "install", "-r", "requirements.txt"])


# ----------------------------------------------------
# 15. pip cache dir
# ----------------------------------------------------
# Muestra la ubicación del caché de pip
# Terminal: pip cache dir
print("\n=== Directorio de caché de pip ===")
subprocess.run(["pip", "cache", "dir"])


# ----------------------------------------------------
# 16. pip cache purge
# ----------------------------------------------------
# Limpia la caché de pip
# Terminal: pip cache purge
print("\n=== Limpiando caché de pip ===")
subprocess.run(["pip", "cache", "purge"])


# ----------------------------------------------------
# 🔍 Buenas prácticas profesionales con pip
# ----------------------------------------------------
# ✅ Usar entornos virtuales (venv, conda) para aislar dependencias
# ✅ Fijar versiones exactas en requirements.txt (ej: numpy==1.25.0)
# ✅ Ejecutar `pip check` regularmente para evitar conflictos
# ✅ Usar `pip index versions <paquete>` para elegir versiones estables
# ✅ Evitar `pip install paquete --user` salvo que sea necesario
# ✅ Usar `requirements.txt` o `pyproject.toml` en proyectos compartidos
# ✅ Considerar Poetry o Pipenv en proyectos grandes para mejor gestión
