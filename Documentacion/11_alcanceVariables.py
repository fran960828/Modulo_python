"""
===============================================================
Guía de alcance de variables en Python — Ejemplos prácticos
===============================================================

Este archivo contiene ejemplos comentados sobre los diferentes
alcances de variables en Python (LEGB: Local, Enclosing, Global,
Built-in). Cada ejemplo está numerado y explicado. 
Conceptos basicos:
1. Conceptos básicos — la regla LEGB

--> Local — variables definidas dentro de una función. Solo accesibles dentro de esa función.

--> Enclosing (encapsulado) — variables de funciones externas (closures). Aplica a funciones anidadas; son accesibles desde la función interna.

--> Global — variables definidas al nivel del módulo (archivo). Accesibles desde cualquier función del mismo módulo (con limitaciones para reasignación).

--> Built-in — nombres incorporados por Python (p. ej. len, print, etc.) disponibles siempre a menos que los sobrescribas.

Python busca nombres en ese orden: Local → Enclosing → Global → Built-in.
Modo de uso:
------------
1. Ejecuta el archivo con `python3 alcance.py`.
2. Se mostrará un menú para elegir qué ejemplo correr.
3. Puedes revisar el código y comentarios para aprender paso a paso.

"""

import builtins

# ===========================
# Ejemplo 1 — Variables locales
# ===========================
def ejemplo1():
    def saludar():
        mensaje = "Hola desde una variable local"  # 'mensaje' es local a la función
        print(mensaje)

    saludar()
    # Si intentas acceder a 'mensaje' fuera de la función, obtendrás un error:
    # print(mensaje)


# =========================================================
# Ejemplo 2 — Lectura de variables globales y UnboundLocalError
# =========================================================
contador_global = 0

def ejemplo2():
    def mostrar_contador():
        print("contador_global (lectura):", contador_global)

    mostrar_contador()

    def incrementar_sin_global():
        try:
            # Sin 'global', Python trata 'contador_global' como local al asignar
            contador_global += 1
        except UnboundLocalError as e:
            print("Error esperado (UnboundLocalError):", e)

    incrementar_sin_global()


# ====================================
# Ejemplo 3 — Uso de 'global' para reasignar
# ====================================
contador_global2 = 0

def ejemplo3():
    global contador_global2
    print("antes:", contador_global2)
    def incrementar_con_global():
        global contador_global2
        contador_global2 += 1
    incrementar_con_global()
    print("después:", contador_global2)


# ===================================================
# Ejemplo 4 — Mutables vs Inmutables y globales
# ===================================================
lista_global = [1, 2, 3]
numero_global = 10

def ejemplo4():
    def mutar_lista():
        lista_global.append(4)   # muta objeto mutable sin 'global'
        print("lista dentro:", lista_global)

    def reasignar_lista_local():
        lista_global = "otra cosa"  # crea variable local distinta
        print("lista (local):", lista_global)

    def reasignar_numero_con_global():
        global numero_global
        numero_global += 5

    mutar_lista()
    print("lista fuera:", lista_global)

    reasignar_lista_local()
    print("lista después de reasignar local:", lista_global)

    print("numero antes:", numero_global)
    reasignar_numero_con_global()
    print("numero después:", numero_global)


# =====================================
# Ejemplo 5 — Scope Enclosing y Closure
# =====================================
def ejemplo5():
    def multiplicador(factor):
        def multiplicar(n):
            return n * factor
        return multiplicar

    doblar = multiplicador(2)
    triplicar = multiplicador(3)

    print("doblar 5 ->", doblar(5))
    print("triplicar 5 ->", triplicar(5))
'''
-> Llamas multiplicador(2). Python crea una nueva ejecución de multiplicador con el nombre local factor = 2.

-> Dentro de esa ejecución se define la función multiplicar(n). Esa función referencia a factor, pero no lo asigna. 
factor queda en el scope encerrante (enclosing scope).

-> multiplicador devuelve la función multiplicar. Esa función devuelta mantiene una referencia a la celda que contiene 
factor — eso es la closure.

-> Cuando llamas doblar(5), multiplicar se ejecuta y busca factor siguiendo LEGB: local (no), enclosing (sí → 2), 
global (no), built-in (no). Resultado 5 * 2 = 10.
'''

# =============================================
# Ejemplo 6 — Uso de 'nonlocal' en funciones
# =============================================
def ejemplo6():
    def contador_interno():
        cuenta = 0
        def incrementar():
            nonlocal cuenta
            cuenta += 1
            return cuenta
        return incrementar

    contar = contador_interno()
    print(contar())
    print(contar())
    print(contar())
'''
- contador_interno() define la variable local cuenta = 0 y la función interna incrementar.

- incrementar usa nonlocal cuenta para indicar que cuando hace cuenta += 1 debe modificar la cuenta 
definida en el scope encerrante, no crear una nueva variable local.

- contador_interno() devuelve la función incrementar. Esa función retiene la referencia a la celda que contiene cuenta.

- Cada llamada a contar() incrementa la celda y devuelve el nuevo valor. El estado (cuenta) se mantiene entre llamadas
 sin usar globals.

¿Por qué nonlocal?

- Sin nonlocal, la línea cuenta += 1 intentaría reasignar cuenta en el scope local de incrementar, provocando un UnboundLocalError porque se intenta leer antes de asignar.

- nonlocal permite rebindear la variable del scope inmediatamente superior (no del módulo).
'''

# ========================================================
# Ejemplo 7 — Captura tardía en closures dentro de bucles
# ========================================================
def ejemplo7():
    funcs = []
    for i in range(3):
        funcs.append(lambda i=i: i)  # solución con default arg

    for f in funcs:
        print(f())
'''
Cada lambda i=i: i crea una función que se queda con el valor actual de i.

- La primera lambda es como lambda: 0

- La segunda es como lambda: 1

- La tercera es como lambda: 2

Por eso, al recorrer funcs, obtienes 0, 1, 2.
'''

# ===================================================
# Ejemplo 8 — Decorador con closure y 'nonlocal'
# ===================================================
def ejemplo8():
    def contador_de_llamadas(func):
        llamadas = 0
        def wrapper(*args, **kwargs):
            nonlocal llamadas
            llamadas += 1
            print(f"[DEBUG] {func.__name__} llamada #{llamadas}")
            return func(*args, **kwargs)
        return wrapper

    @contador_de_llamadas
    def saludar(nombre):
        print("Hola", nombre)

    saludar("Ana")
    saludar("Luis")
    saludar("María")


# =========================================
# Ejemplo 9 — Built-ins y sombreado
# =========================================
def ejemplo9():
    print(len([1,2,3]))  # built-in len

    len = "esto es una variable llamada len"  # sombreado
    print("len ahora es:", len)

    print("builtins.len([1,2,3]) ->", builtins.len([1,2,3]))
'''
👉 Al principio len es la función incorporada que mide la longitud.
Pero cuando haces len = "...", a partir de ahí len deja de ser la función y pasa a ser un string.
Es como si hubieras quitado la herramienta len y la hubieras reemplazado con un texto.
Si luego necesitas la herramienta original, tienes que pedirla desde builtins.len.
'''

# ===================================================
# Ejemplo 10 — Scope en clases (atributos)
# ===================================================
def ejemplo10():
    class Contenedor:
        contador_clase = 0

        def __init__(self, valor):
            self.valor = valor
            Contenedor.contador_clase += 1

        def incrementar_valor(self):
            self.valor += 1

    a = Contenedor(10)
    b = Contenedor(20)
    print("a.valor:", a.valor)
    print("b.valor:", b.valor)
    print("contador_clase:", Contenedor.contador_clase)

    a.contador_clase = 100
    print("a.contador_clase (instancia):", a.contador_clase)
    print("Contenedor.contador_clase (clase):", Contenedor.contador_clase)
'''
👉 contador_clase vive en la clase y es compartido por todas las instancias.
Cada vez que haces Contenedor(...), se suma 1 al contador.

Pero si desde una instancia (a) haces a.contador_clase = 100, no estás cambiando el de la clase, sino que creas una copia solo dentro de a, que oculta el original.
Así:

- Contenedor.contador_clase sigue con el valor compartido.

- a.contador_clase muestra 100 solo en ese objeto.
'''

# ==========================================================
# Ejemplo 11 — Evitar globals con inyección de dependencias
# ==========================================================
config_global = {"modo": "dev"}

def ejemplo11():
    def servicio_malo():
        if config_global["modo"] == "dev":
            print("modo desarrollo")
        else:
            print("modo producción")

    def servicio_bueno(config):
        if config.get("modo") == "dev":
            print("modo desarrollo (config inyectada)")
        else:
            print("modo producción (config inyectada)")

    servicio_malo()
    servicio_bueno({"modo": "dev"})
    servicio_bueno({"modo": "prod"})

    '''
    👉 servicio_malo siempre depende de config_global.
Es como una función que mira un archivo fijo en disco: no puedes cambiarle de qué archivo leer.

En cambio, servicio_bueno recibe la configuración como argumento.
Es como darle a la función su propia copia del archivo de configuración:

Si le das {"modo": "dev"} actúa en desarrollo.

Si le das {"modo": "prod"} actúa en producción.

Mucho más flexible y fácil de probar.
    '''


# ==========================================================
# Menú interactivo para ejecutar ejemplos
# ==========================================================
ejemplos = {
    "1": ejemplo1,
    "2": ejemplo2,
    "3": ejemplo3,
    "4": ejemplo4,
    "5": ejemplo5,
    "6": ejemplo6,
    "7": ejemplo7,
    "8": ejemplo8,
    "9": ejemplo9,
    "10": ejemplo10,
    "11": ejemplo11,
}

def menu():
    while True:
        print("\n================ Menú de ejemplos ================")
        for k in sorted(ejemplos.keys(), key=lambda x: int(x)):
            print(f"{k}. Ejemplo {k}")
        print("0. Salir")
        opcion = input("Elige un ejemplo a ejecutar: ")
        if opcion == "0":
            break
        elif opcion in ejemplos:
            print(f"\n>>> Ejecutando Ejemplo {opcion}...\n")
            ejemplos[opcion]()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
