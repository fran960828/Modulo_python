# ==============================================================================
# GUÍA PROFESIONAL: GESTIÓN DE SECRETOS Y VARIABLES DE ENTORNO EN PYTHON
# ==============================================================================

"""
EXPLICACIÓN PARA PRINCIPIANTES:

¿Qué es un "Secreto" en programación?
Es cualquier información que no quieres que otros vean: contraseñas de bases de 
datos, llaves maestras de APIs (como OpenAI o Google Maps) o tokens de acceso.

EL PELIGRO (Hard-coding):
Si escribes `password = "12345"` directamente en tu código y luego subes ese 
archivo a GitHub, cualquier persona en el mundo podrá ver tu contraseña. 
Incluso si borras el archivo después, la contraseña queda grabada en el historial.

LA SOLUCIÓN PROFESIONAL:
Usamos archivos ocultos (.env) y "Variables de Entorno". 
1. El archivo `.env` guarda tus secretos localmente en tu PC.
2. Usamos un archivo llamado `.gitignore` para decirle a Git que NUNCA suba 
   el archivo `.env` a internet.
3. Python lee esos secretos desde la memoria del sistema, no desde el código.

ESTÁNDAR DE LA INDUSTRIA:
Utilizamos la librería 'python-dotenv'. Es la forma más limpia de separar la 
configuración (privada) de la lógica del programa (pública).
"""

# 

# ------------------------------------------------------------------------------
# REQUISITOS PREVIOS (Ejecutar en tu terminal):
# 1. Instalar la librería: pip install python-dotenv
# 2. Crear un archivo llamado `.env` en la misma carpeta que este script.
# 3. Contenido del archivo .env:
#    DB_USER="mi_usuario_admin"
#    DB_PASS="SuperClaveSegura2026"
# ------------------------------------------------------------------------------

import os # Módulo nativo para interactuar con el Sistema Operativo
from dotenv import load_dotenv # Librería para cargar el archivo .env

# ------------------------------------------------------------------------------
# PASO 1: CARGAR LOS SECRETOS
# ------------------------------------------------------------------------------

# load_dotenv() busca un archivo llamado .env en la carpeta actual y 
# "inyecta" sus valores en las variables de entorno de tu sesión actual.
load_dotenv()

def conectar_base_datos():
    """
    Simulación de una conexión segura usando secretos.
    """
    
    # --------------------------------------------------------------------------
    # PASO 2: ACCEDER A LAS VARIABLES
    # --------------------------------------------------------------------------
    
    # Usamos os.getenv('NOMBRE_VARIABLE') para obtener el valor.
    # Es mejor que os.environ['NOMBRE'] porque si la variable no existe,
    # devuelve 'None' en lugar de romper el programa con un error.
    
    usuario = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')

    # Validación de seguridad: verificamos que las llaves existan antes de seguir
    if not usuario or not password:
        print("❌ ERROR: No se encontraron las credenciales en el archivo .env")
        print("Asegúrate de haber creado el archivo .env con DB_USER y DB_PASS.")
        return

    # --------------------------------------------------------------------------
    # PASO 3: USO DE LOS DATOS
    # --------------------------------------------------------------------------
    
    print("✅ Credenciales detectadas correctamente.")
    
    # IMPORTANTE: En producción, nunca imprimas la contraseña real.
    # Aquí solo simulamos la conexión.
    print(f"Conectando a la base de datos como el usuario: {usuario}...")
    print(f"Usando contraseña de {len(password)} caracteres (Oculta por seguridad).")
    
    print("\n--- ¡Conexión Establecida de Forma Segura! ---")

# ------------------------------------------------------------------------------
# EJECUCIÓN DEL SCRIPT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    conectar_base_datos()

# ------------------------------------------------------------------------------
# NOTA FINAL SOBRE SEGURIDAD (EL ARCHIVO .gitignore)
# ------------------------------------------------------------------------------
# Para que este sistema sea realmente profesional, DEBES crear un archivo 
# llamado `.gitignore` en tu proyecto y escribir dentro:
#
# .env
#
# Esto garantiza que cuando hagas 'git push', tus secretos se queden en TU 
# máquina y no terminen en un servidor público.