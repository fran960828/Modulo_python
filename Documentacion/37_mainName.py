# ==============================================================================
# GUÍA PROFESIONAL: EL PUNTO DE ENTRADA EN PYTHON (if __name__ == "__main__")
# ==============================================================================

"""
EXPLICACIÓN PARA PRINCIPIANTES:

En Python, cada archivo (.py) tiene una "doble personalidad":
1. Puede ser un SCRIPT: Un programa que ejecutas directamente para que haga algo.
2. Puede ser un MÓDULO: Una biblioteca de funciones que importas en otro archivo.

EL PROBLEMA:
Cuando importas un archivo (ej. 'import mi_script'), Python lee y ejecuta TODO 
el código que hay en él. Si tienes un comando para "borrar base de datos" suelto 
en ese archivo, se ejecutará en cuanto lo importes, ¡aunque no quieras!

LA SOLUCIÓN:
Python crea automáticamente una variable invisible llamada `__name__` para cada archivo.
- Si ejecutas el archivo DIRECTAMENTE: Python le asigna el valor "__main__".
- Si el archivo es IMPORTADO: Python le asigna el valor del nombre del archivo.

La línea `if __name__ == "__main__":` actúa como un "GUARDIÁN". 
Todo lo que pongas dentro de ese bloque SOLO se ejecutará si el archivo es el 
protagonista (el que tú lanzaste). Si alguien lo importa para usar sus funciones, 
el guardián bloqueará la ejecución automática de la lógica principal.

ESTÁNDAR PROFESIONAL:
A nivel profesional, se acostumbra a meter toda la lógica de ejecución en una 
función llamada main() y llamarla al final usando este condicional.
"""

# 

# ------------------------------------------------------------------------------
# EJEMPLO PRÁCTICO: "El Calculador de Impuestos"
# ------------------------------------------------------------------------------

import os

# 1. DEFINICIÓN DE FUNCIONES (Lógica de Negocio)
# Estas funciones están disponibles para ser usadas aquí O en cualquier otro archivo.
def calcular_iva(monto):
    """Calcula el 21% de un monto dado."""
    return monto * 0.21

def formatear_precio(precio):
    """Devuelve un string con formato de moneda."""
    return f"${precio:,.2f}"

# 2. LA FUNCIÓN PRINCIPAL (Main)
# Aquí va el flujo de trabajo que queremos que ocurra cuando usemos este archivo.
def main():
    print("--- ASISTENTE DE CONTABILIDAD v1.0 ---")
    
    try:
        # Pedimos un dato al usuario
        subtotal = float(input("Introduce el subtotal de la factura: "))
        
        # Usamos nuestras funciones para procesar la lógica
        impuesto = calcular_iva(subtotal)
        total = subtotal + impuesto
        
        # Mostramos resultados
        print(f"\nSubtotal: {formatear_precio(subtotal)}")
        print(f"IVA (21%): {formatear_precio(impuesto)}")
        print(f"TOTAL:     {formatear_precio(total)}")
        
    except ValueError:
        print("Error: Por favor, introduce un número válido.")

# 3. EL GUARDIÁN DEL PUNTO DE ENTRADA
# Esta es la parte más importante para el nivel profesional.
if __name__ == "__main__":
    # Si este archivo se ejecuta con 'python mi_archivo.py', 
    # la variable __name__ valdrá "__main__" y entrará aquí.
    
    print(f"[INFO] Ejecutando archivo directamente. Identidad: {__name__}")
    main()
else:
    # Si este archivo se importa desde otro (ej: import mi_archivo),
    # el bloque anterior se ignora y solo se imprimen mensajes informativos si los hay.
    
    print(f"[INFO] El módulo '{__name__}' ha sido importado con éxito.")
    print("[INFO] Las funciones calcular_iva y formatear_precio están listas para usarse.")

# ------------------------------------------------------------------------------
# ¿POR QUÉ ESTO ES NIVEL PROFESIONAL?
# ------------------------------------------------------------------------------
# 1. MODULARIDAD: Si mañana creas un software gigante, puedes importar 'calcular_iva'
#    sin que el programa te pregunte "Introduce el subtotal" de repente.
# 2. TESTING: Las herramientas de pruebas automáticas (como PyTest) pueden importar
#    tus funciones para verificar que funcionan sin disparar el input() de la función main.
# 3. ORDEN: Separa claramente qué partes del código "definen cosas" (funciones)
#    de qué partes "hacen cosas" (ejecución).