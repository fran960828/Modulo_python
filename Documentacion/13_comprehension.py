"""
comprension_de_bucles.py

Guía práctica (archivo .py) sobre COMPRENSIONES (comprehensions) en Python
Autor: Experto en Python (20 años de experiencia)
Propósito: documentación + ejemplos incrementales y comentados paso a paso,
          pensados para que un principiante alcance nivel profesional.

Instrucciones:
 - Ejecuta este archivo con: python3 comprension_de_bucles.py
 - Usa el menú para ejecutar ejemplos individuales o todos a la vez.
 - Cada ejemplo está explicado con comentarios y produce salidas que puedes
   verificar al ejecutar el script.

Resumen rápido:
 - Las *list comprehensions* crean listas de forma concisa y legible.
 - Existen también *set comprehensions*, *dict comprehensions* y *generator expressions*.
 - Ventajas: expresividad, normalmente más rápidas que un bucle for explícito,
   y código más declarativo.
 - Riesgos: abusarlas en expresiones demasiado complejas reduce legibilidad;
   cuidado con efectos secundarios (side effects).

Contenido de ejemplos:
 1) Básico: transformar una lista con list comprehension
 2) Filtrado (condición simple)
 3) If-else dentro de la comprensión (mapeo con ternary)
 4) Comprensiones anidadas: flatten (aplanar) matrices
 5) Múltiples for: producto cartesiano y orden de iteración
 6) Dict comprehension: construir diccionarios eficientemente
 7) Set comprehension: obtener únicos y operaciones con conjuntos
 8) Generator expressions vs list comprehensions (memoria)
 9) Uso de enumerate y zip dentro de comprehensions
10) *Side effects* y por qué evitarlos dentro de una comprehension
11) Rendimiento comparativo (timeit) y cuándo preferir map/loops/generador
12) Transponer matriz (uso idiomático con zip)
13) Invertir mapeos y agrupar (patrones reales en trabajo)
14) Buenas prácticas y checklist profesional

Cada función imprime explicaciones cortas y los resultados del ejemplo.
"""

from typing import List, Dict, Tuple, Iterable
from collections import defaultdict
import timeit
import itertools

# ------------------------------------------------------------
# Ejemplo 1 — Básico: transformar una lista (squares)
# ------------------------------------------------------------
def ejemplo_1_basico():
    print("\n=== Ejemplo 1: Básico — List comprehension ===")
    # Queremos una lista de cuadrados a partir de una lista de enteros.
    nums = [1, 2, 3, 4, 5]
    print("Lista original:", nums)

    # Forma tradicional (bucle)
    cuadrados_loop = []
    for n in nums:
        cuadrados_loop.append(n * n)
    print("Cuadrados (bucle):", cuadrados_loop)

    # Forma con list comprehension (más concisa)
    cuadrados_comp = [n * n for n in nums]
    print("Cuadrados (comprehension):", cuadrados_comp)

    # Verificación sencilla
    assert cuadrados_comp == cuadrados_loop


# ------------------------------------------------------------
# Ejemplo 2 — Filtrado: usar if al final para seleccionar elementos
# ------------------------------------------------------------
def ejemplo_2_filtrado():
    print("\n=== Ejemplo 2: Filtrado — condición simple ===")
    nums = list(range(10))
    print("Nums:", nums)

    # Queremos solo los pares
    pares = [n for n in nums if n % 2 == 0]  # 'if' filtra elementos antes de añadirlos
    print("Pares:", pares)

    # Equivalente con bucle
    pares_loop = []
    for n in nums:
        if n % 2 == 0:
            pares_loop.append(n)
    assert pares == pares_loop


# ------------------------------------------------------------
# Ejemplo 3 — If-else dentro de la comprehension (expresión ternaria)
# ------------------------------------------------------------
def ejemplo_3_if_else():
    print("\n=== Ejemplo 3: If-else dentro — mapeo condicional ===")
    nums = [-2, -1, 0, 1, 2]
    print("Nums:", nums)

    # Queremos transformar a 'positivo' si >=0, sino 'negativo'
    etiquetas = ["positivo" if n >= 0 else "negativo" for n in nums]
    print("Etiquetas:", etiquetas)

    # Nota: el if-else va antes del for, diferente a un filtro 'if' al final:
    # [ <exp_if_true> if <cond> else <exp_if_false>  for x in seq ]


# ------------------------------------------------------------
# Ejemplo 4 — Comprensiones anidadas: aplanar (flatten) una matriz
# ------------------------------------------------------------
def ejemplo_4_flatten():
    print("\n=== Ejemplo 4: Comprensión anidada — flatten de matriz ===")
    matriz = [
        [1, 2, 3],
        [4, 5],
        [6]
    ]
    print("Matriz:", matriz)

    # Aplanamos la matriz - equivalente a: for fila in matriz: for x in fila: append(x)
    aplanada = [x for fila in matriz for x in fila]
    print("Aplanada:", aplanada)

    # Orden importante: el primer for corresponde al primer bucle externo,
    # el segundo for al bucle interior (misma semántica que bucles anidados).
    # Equivalente con bucles:
    aplanada_loop = []
    for fila in matriz:
        for x in fila:
            aplanada_loop.append(x)
    assert aplanada == aplanada_loop


# ------------------------------------------------------------
# Ejemplo 5 — Múltiples for: producto cartesiano y comprensión
# ------------------------------------------------------------
def ejemplo_5_producto_cartesiano():
    print("\n=== Ejemplo 5: Producto cartesiano (múltiples for) ===")
    letras = ['a', 'b', 'c']
    numeros = [1, 2, 3]
    # Producto cartesiano: todas las parejas (letra, numero)
    producto = [(l, n) for l in letras for n in numeros]
    print("Producto (comprehension):", producto)

    # Equivalente con bucles
    producto_loop = []
    for l in letras:
        for n in numeros:
            producto_loop.append((l, n))
    assert producto == producto_loop

    # Observa el orden: el primer for en la comprehension es el externo.


# ------------------------------------------------------------
# Ejemplo 6 — Dict comprehension: crear diccionarios desde listas
# ------------------------------------------------------------
def ejemplo_6_dict_comprehension():
    print("\n=== Ejemplo 6: Dict comprehension ===")
    claves = ['x', 'y', 'z']
    valores = [9, 8, 7]

    # Construir un dict a partir de dos listas (usando zip)
    d = {k: v for k, v in zip(claves, valores)}
    print("Dict creado con dict comprehension:", d)

    # Otro ejemplo: índice -> valor (usando enumerate)
    lista = ['manzana', 'pera', 'uva']
    index_map = {i: val for i, val in enumerate(lista)}
    print("Index map (enumerate):", index_map)

    # Filtrado en dict comprehension: solo incluir pares con valor impar
    pares_filtrados = {k: v for k, v in d.items() if v % 2 == 1}
    print("Filtrado (valores impares):", pares_filtrados)


# ------------------------------------------------------------
# Ejemplo 7 — Set comprehension: únicos y operaciones con conjuntos
# ------------------------------------------------------------
def ejemplo_7_set_comprehension():
    print("\n=== Ejemplo 7: Set comprehension ===")
    datos = [1, 2, 2, 3, 4, 4, 4]
    print("Datos:", datos)

    # Obtener únicos al cuadrado
    cuadrados_unicos = {x * x for x in datos}
    print("Cuadrados únicos (set):", cuadrados_unicos)

    # Usar set comprehension para filtrar o transformar antes de operaciones de conjunto
    letras = ["a", "A", "b", "B"]
    minusculas_unicas = {s.lower() for s in letras}
    print("Minusculas únicas:", minusculas_unicas)


# ------------------------------------------------------------
# Ejemplo 8 — Generator expressions (expresiones generadoras)
# ------------------------------------------------------------
def ejemplo_8_generators():
    print("\n=== Ejemplo 8: Generator expressions (memoria eficiente) ===")
    nums = list(range(10))
    print("Nums:", nums)

    # List comprehension crea la lista entera en memoria:
    lista = [n * n for n in nums]
    print("Tipo lista (comprehension):", type(lista), "longitud:", len(lista))

    # Generator expression NO crea toda la lista, crea un iterador perezoso:
    gen = (n * n for n in nums)
    print("Tipo gen (generator expr):", type(gen))

    # Puedes iterar el generador (los valores se producen sobre la marcha):
    print("Valores producidos por gen:", list(gen))  # al convertirlo a lista consumimos el generador

    # Nota: una vez consumido, el generador está vacío:
    gen2 = (n * n for n in nums)
    it = iter(gen2)
    print("next(it):", next(it))  # 0
    # Si prefieres un generador con control explícito, define una función con yield.

    # Uso práctico: streaming de datos grandes sin cargar todo en memoria


# ------------------------------------------------------------
# Ejemplo 9 — enumerate y zip dentro de comprehensions
# ------------------------------------------------------------
def ejemplo_9_enumerate_zip():
    print("\n=== Ejemplo 9: enumerate y zip en comprehensions ===")
    palabras = ["uno", "dos", "tres"]
    # Índice -> palabra (enumerate)
    mapa = {i: p for i, p in enumerate(palabras)}
    print("Mapa (enumerate):", mapa)

    # Combinar dos listas con zip y una comprehension
    keys = ["a", "b", "c"]
    vals = [1, 2, 3]
    combinado = [f"{k}:{v}" for k, v in zip(keys, vals)]
    print("Combinado (zip):", combinado)

    # Si las listas de diferente longitud, zip corta al menor.
    keys2 = ["x", "y"]
    vals2 = [9, 8, 7]
    combinado2 = [f"{k}:{v}" for k, v in zip(keys2, vals2)]
    print("Zip corta al menor (combinado2):", combinado2)


# ------------------------------------------------------------
# Ejemplo 10 — *Side effects* y por qué evitarlos en comprehensions
# ------------------------------------------------------------
def ejemplo_10_side_effects():
    print("\n=== Ejemplo 10: Side effects — mala práctica dentro de comprehensions ===")
    datos = [1, 2, 3]
    acumulador = []

    # MAL: usar comprehension para ejecutar efectos secundarios (append devuelve None)
    resultado_malo = [acumulador.append(x) for x in datos]  # crea lista de None y modifica acumulador
    print("resultado_malo (lista devuelta por comprehension):", resultado_malo)
    print("acumulador tras comprehension (side effects):", acumulador)
    # Observa: comprehension devolvió [None, None, None] porque append() devuelve None.
    # Esto demuestra que usar comprehensions por sus side effects es confuso y frágil.

    # BUENO: usar un bucle explícito para efectos secundarios (claro y legible)
    acumulador2 = []
    for x in datos:
        acumulador2.append(x)
    print("acumulador2 tras for clásico:", acumulador2)

    # REGLA: las comprehensions deben producir valores (expresiones puras),
    # NO realizar efectos secundarios. Si necesitas side effects, usa bucles.


# ------------------------------------------------------------
# Ejemplo 11 — Rendimiento: comprehension vs bucle vs map (timeit)
# ------------------------------------------------------------
def ejemplo_11_rendimiento():
    print("\n=== Ejemplo 11: Rendimiento (timeit) — comparativa ===")
    N = 10000
    data = list(range(N))

    # 1) Bucle clásico que construye una lista de cuadrados
    def loop_squares():
        out = []
        for x in data:
            out.append(x * x)
        return out

    # 2) List comprehension
    def comp_squares():
        return [x * x for x in data]

    # 3) Map + lambda (nota: en Python 3 map devuelve iterador; list() para materializar)
    def map_squares():
        return list(map(lambda x: x * x, data))

    # Medir (número reducido para que sea rápido en ejecución interactiva)
    reps = 50
    t_loop = timeit.timeit(loop_squares, number=reps)
    t_comp = timeit.timeit(comp_squares, number=reps)
    t_map = timeit.timeit(map_squares, number=reps)

    print(f"Reps={reps}, N={N}")
    print(f"bucle: {t_loop:.4f}s, comprehension: {t_comp:.4f}s, map+lambda: {t_map:.4f}s")
    print("Típicamente la comprehension es tan rápida o más que map+lambda y más legible que el bucle en operaciones simples.")

    # Nota: para operaciones muy simples map puede ser comparable; si usas funciones ya existentes sin lambda,
    # map(func, iterable) puede ser preferible. Para legibilidad y expresividad, la comprehension es habitual.


# ------------------------------------------------------------
# Ejemplo 12 — Transponer una matriz con zip(*) y comprehension
# ------------------------------------------------------------
def ejemplo_12_transponer():
    print("\n=== Ejemplo 12: Transponer matriz (zip + comprehension) ===")
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Matriz original:")
    for row in matriz:
        print(row)

    # Transponer: filas <-> columnas
    transpuesta = [list(col) for col in zip(*matriz)]
    print("Transpuesta:")
    for row in transpuesta:
        print(row)

    # Aclaración: zip(*matriz) devuelve tuplas (col,), por eso convertimos a list() para consistencia.


# ------------------------------------------------------------
# Ejemplo 13 — Invertir mapeos y agrupar (pattern useful en el trabajo)
# ------------------------------------------------------------
def ejemplo_13_invertir_y_agrupar():
    print("\n=== Ejemplo 13: Invertir mapping y agrupar (uso real) ===")
    # Ejemplo: lista de dicts (por ejemplo, rows de una consulta)
    filas = [
        {"id": 1, "grupo": "A", "valor": 10},
        {"id": 2, "grupo": "B", "valor": 20},
        {"id": 3, "grupo": "A", "valor": 30},
        {"id": 4, "grupo": "C", "valor": 40},
    ]
    print("Filas:", filas)

    # Invertir: id -> fila (dict comprehension muy útil)
    id_map = {row["id"]: row for row in filas}
    print("Mapa id -> row:", id_map)

    # Agrupar por 'grupo' -> lista de filas (aquí comprehension directa no es ideal,
    # es más legible usar defaultdict)
    grupos = defaultdict(list)
    for row in filas:
        grupos[row["grupo"]].append(row)
    print("Agrupado (defaultdict):", dict(grupos))

    # Si quieres crear dict con listas por grupo en una sola expresión:
    # primero obtén los grupos únicos y luego comprehension que filtre (menos eficiente)
    grupos_unicos = sorted({r["grupo"] for r in filas})
    agrupacion_via_comp = {g: [r for r in filas if r["grupo"] == g] for g in grupos_unicos}
    print("Agrupación vía comprehension (útil a pequeña escala):", agrupacion_via_comp)

    # Conclusión práctica: para grandes volúmenes o en pipeline, usar defaultdict o itertools.groupby
    # (itertools.groupby requiere datos ordenados por la clave).


# ------------------------------------------------------------
# Ejemplo 14 — Buenas prácticas y checklist profesional
# ------------------------------------------------------------
def ejemplo_14_buenas_practicas():
    print("\n=== Ejemplo 14: Buenas prácticas y checklist ===")
    recomendaciones = [
        "Usa comprehensions para transformar y filtrar de forma clara y declarativa.",
        "Evita expresiones demasiado largas o anidadas que reduzcan la legibilidad.",
        "No uses comprehensions para efectos secundarios: usa bucles explícitos.",
        "Para operaciones con grandes volúmenes considera generator expressions para ahorrar memoria.",
        "Prefiere comprehensions cuando la operación es simple (map + filter); para operaciones complejas, extrae a una función.",
        "Compara legibilidad y rendimiento: a veces un bucle claro es preferible.",
        "Usa dict/set comprehensions cuando la intención sea crear esos tipos directamente.",
    ]
    for i, r in enumerate(recomendaciones, 1):
        print(f"{i}. {r}")


# ------------------------------------------------------------
# Menú interactivo para ejecutar ejemplos
# ------------------------------------------------------------
ejemplos = {
    "1": ("Básico — transformar lista (squares)", ejemplo_1_basico),
    "2": ("Filtrado — if al final", ejemplo_2_filtrado),
    "3": ("If-else dentro de comprehension", ejemplo_3_if_else),
    "4": ("Aplanar matriz — comprensión anidada", ejemplo_4_flatten),
    "5": ("Producto cartesiano — múltiples for", ejemplo_5_producto_cartesiano),
    "6": ("Dict comprehension", ejemplo_6_dict_comprehension),
    "7": ("Set comprehension", ejemplo_7_set_comprehension),
    "8": ("Generator expressions (memoria)", ejemplo_8_generators),
    "9": ("Enumerate y zip en comprehensions", ejemplo_9_enumerate_zip),
    "10": ("Side effects — por qué evitarlos", ejemplo_10_side_effects),
    "11": ("Rendimiento — timeit comparativo", ejemplo_11_rendimiento),
    "12": ("Transponer matriz (zip + comprehension)", ejemplo_12_transponer),
    "13": ("Invertir mapping y agrupar (uso real)", ejemplo_13_invertir_y_agrupar),
    "14": ("Buenas prácticas y checklist", ejemplo_14_buenas_practicas),
}

def menu():
    print("=== Documentación: Comprensión de bucles en Python (ejecutable) ===")
    while True:
        print("\nElige un ejemplo para ejecutar (número), 'a' para todos, o 'q' para salir:")
        for k, (desc, _) in ejemplos.items():
            print(f" {k}. {desc}")
        elec = input(">>> ").strip().lower()
        if elec in ("q", "salir", "exit"):
            print("Saliendo.")
            break
        if elec == "a":
            for k in sorted(ejemplos.keys(), key=int):
                print("\n" + ("-" * 60))
                print(f"Ejecutando {k}. {ejemplos[k][0]}")
                ejemplos[k][1]()  # ejecutar la función
            print("\nTodos los ejemplos ejecutados.")
            continue
        if elec in ejemplos:
            ejemplos[elec][1]()
        else:
            print("Opción no válida. Introduce el número del ejemplo, 'a' para todos o 'q' para salir.")


# ------------------------------------------------------------
# Punto de entrada
# ------------------------------------------------------------
if __name__ == "__main__":
    menu()
