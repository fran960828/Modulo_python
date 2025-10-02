"""
ordenacion_practica.py

Guía práctica para ordenar en Python (listas, tuplas, diccionarios y objetos)
Autor: Experto en Python (20 años de experiencia)
Propósito:
    - Explicar con detalle y ejemplos incrementales cómo ordenar estructuras
      habituales en Python.
    - Incluir diferencias entre list.sort() y sorted(), uso de reverse,
      uso de key con funciones normales, lambdas y operator.attrgetter/itemgetter,
      además de patrones profesionales (estabilidad, rendimiento, multi-criterio).

Modo de uso:
    - Ejecuta: python ordenacion_practica.py
    - Usa el menú para ejecutar ejemplos individuales o 'a' para todos.
    - Cada ejemplo está comentado paso a paso y es independiente.

Notas importantes:
    - list.sort() modifica la lista en-place y devuelve None.
    - sorted(iterable) devuelve una nueva lista ordenada a partir de cualquier iterable.
    - El parámetro key se evalúa **una sola vez por elemento** y sus resultados se usan para comparar.
    - La ordenación en Python es estable: valores iguales conservan su orden relativo previo.
"""

from dataclasses import dataclass
from operator import attrgetter, itemgetter
from functools import cmp_to_key
from typing import List, Dict, Tuple

# ------------------------------------------------------------
# Ejemplo 1 — Ordenar números (básico): sorted vs list.sort()
# ------------------------------------------------------------
def ejemplo_1_numeros_basico():
    print("\n=== Ejemplo 1: Números — sorted() vs list.sort() ===")
    nums = [5, 2, 9, 1, 5, 6]
    print("Original:", nums)

    # sorted(): devuelve una nueva lista ordenada (no modifica 'nums')
    ordenados = sorted(nums)
    print("sorted(nums) ->", ordenados)
    print("nums tras sorted ->", nums)  # sin cambios

    # list.sort(): modifica la lista in-place y no devuelve la lista
    nums.sort()
    print("nums tras nums.sort() ->", nums)
    # Nota: intentar asignar nums = nums.sort() dejaría nums = None (no hacerlo)


# ------------------------------------------------------------
# Ejemplo 2 — Orden descendente: reverse param y trick con key
# ------------------------------------------------------------
def ejemplo_2_descendente_reverse_key():
    print("\n=== Ejemplo 2: Orden descendente (reverse y key) ===")
    nums = [3, 1, 4, 1, 5, 9]
    print("Original:", nums)

    # Usando reverse=True (más claro y directo)
    print("sorted(..., reverse=True):", sorted(nums, reverse=True))

    # Alternativa: usar key con negativa (útil si quieres ordenar por transformada)
    # Para enteros simples key=lambda x: -x produce el mismo resultado que reverse=True
    print("sorted(..., key=lambda x: -x):", sorted(nums, key=lambda x: -x))


# ------------------------------------------------------------
# Ejemplo 3 — Ordenar strings: sensibilidad a mayúsculas/minúsculas
# ------------------------------------------------------------
def ejemplo_3_strings_case_insensitive():
    print("\n=== Ejemplo 3: Strings — orden case-insensitive ===")
    palabras = ["zeta", "Alpha", "beta", "Gamma"]
    print("Original:", palabras)

    # Orden por defecto es sensible a mayúsculas (ASCIIbetical): las mayúsculas suelen ir antes
    print("sorted (sensible a mayúsculas):", sorted(palabras))

    # Para ordenar ignorando mayúsculas/minúsculas usamos key=str.lower
    print("sorted (case-insensitive con key=str.lower):", sorted(palabras, key=str.lower))

    # Si además queremos invertido:
    print("sorted case-insensitive y reverse:", sorted(palabras, key=str.lower, reverse=True))


# ------------------------------------------------------------
# Ejemplo 4 — Ordenar tuplas (lexicográfico y key personalizado)
# ------------------------------------------------------------
def ejemplo_4_tuplas_lexicografico():
    print("\n=== Ejemplo 4: Tuplas — orden lexicográfico y key personalizado ===")
    tuplas = [(2, 'b'), (1, 'a'), (2, 'a'), (1, 'b')]
    print("Original:", tuplas)

    # Por defecto las tuplas se ordenan lexicográficamente: primero índice 0, luego 1, ...
    print("sorted(tuplas) ->", sorted(tuplas))

    # Ordenar por segundo elemento prioritario (índice 1) y luego por primer elemento:
    # Podemos usar key que devuelva (segundo, primero)
    print("sorted(tuplas, key=lambda t: (t[1], t[0])) ->",
          sorted(tuplas, key=lambda t: (t[1], t[0])))


# ------------------------------------------------------------
# Ejemplo 5 — Ordenar diccionarios (por clave, por valor)
# ------------------------------------------------------------
def ejemplo_5_diccionarios():
    print("\n=== Ejemplo 5: Diccionarios — sorted sobre dicts y .items() ===")
    d = {'c': 3, 'a': 1, 'b': 2}
    print("Dict original (orden de inserción puede variar según creación):", d)

    # sorted(d) devuelve las claves ordenadas
    print("sorted(d) -> (claves ordenadas):", sorted(d))

    # Si queremos una lista de pares ordenada por clave:
    print("sorted(d.items()) ->", sorted(d.items()))

    # Para ordenar por valor usamos key sobre items: itemgetter(1) o lambda kv: kv[1]
    items_por_valor = sorted(d.items(), key=itemgetter(1))
    print("sorted(d.items(), key=itemgetter(1)) ->", items_por_valor)

    # Reconstruir un dict ordenado (desde Python 3.7 el dict preserva orden de inserción)
    d_ordenado_por_valor = dict(items_por_valor)
    print("Dict reconstruido en orden por valor:", d_ordenado_por_valor)

    # Ordenar solo claves por valor:
    claves_ordenadas_por_valor = sorted(d, key=lambda k: d[k])
    print("Claves ordenadas por su valor asociado:", claves_ordenadas_por_valor)


# ------------------------------------------------------------
# Ejemplo 6 — Objetos simples: ordenar por atributo (lambda vs attrgetter)
# ------------------------------------------------------------
@dataclass
class Persona:
    nombre: str
    edad: int

def ejemplo_6_objetos_attrgetter_lambda():
    print("\n=== Ejemplo 6: Objetos — key con lambda y with attrgetter ===")
    personas = [Persona("Ana", 30), Persona("Luis", 25), Persona("María", 30), Persona("Juan", 22)]
    print("Original (lista de Person):", personas)

    # Usando lambda (acceso explícito al atributo)
    orden_por_edad_lambda = sorted(personas, key=lambda p: p.edad)
    print("sorted(personas, key=lambda p: p.edad) ->", orden_por_edad_lambda)

    # Usando operator.attrgetter (más eficiente y legible cuando es solo atributo)
    orden_por_edad_attr = sorted(personas, key=attrgetter('edad'))
    print("sorted(personas, key=attrgetter('edad')) ->", orden_por_edad_attr)

    # Orden por edad (primario) y nombre (secundario) usando attrgetter con múltiples campos
    orden_compuesto = sorted(personas, key=attrgetter('edad', 'nombre'))
    print("sorted(..., key=attrgetter('edad','nombre')) ->", orden_compuesto)


# ------------------------------------------------------------
# Ejemplo 7 — Estabilidad de la ordenación (usando sort in-place)
# ------------------------------------------------------------
def ejemplo_7_estabilidad():
    print("\n=== Ejemplo 7: Estabilidad de sort() ===")
    registros = [
        {'id': 1, 'grupo': 'A', 'valor': 10},
        {'id': 2, 'grupo': 'B', 'valor': 5},
        {'id': 3, 'grupo': 'A', 'valor': 7},
        {'id': 4, 'grupo': 'B', 'valor': 3},
    ]
    print("Original:", registros)

    # Queremos ordenar por 'grupo' y dentro de cada grupo por 'valor' ascendente.
    # Método 1 (estable): ordenar primero por el criterio secundario, luego por el primario.
    regs = registros.copy()
    # Ordenamos por valor (secundario)
    regs.sort(key=itemgetter('valor'))
    # Ahora ordenamos por grupo (primario); como sort es estable, los registros con mismo 'grupo'
    # conservarán el orden relativo por 'valor'.
    regs.sort(key=itemgetter('grupo'))
    print("Ordenado por grupo (primario) y valor (secundario) usando sort estable:", regs)

    # Método 2 (tupla en key): más directo y legible
    regs2 = sorted(registros, key=lambda r: (r['grupo'], r['valor']))
    print("Ordenado usando key que devuelve tupla (grupo, valor):", regs2)


# ------------------------------------------------------------
# Ejemplo 8 — Comparator legacy mediante cmp_to_key
# ------------------------------------------------------------
def ejemplo_8_cmp_to_key():
    print("\n=== Ejemplo 8: cmp_to_key — cuando necesitas un comparador clásico ===")
    palabras = ['a', 'bb', 'ccc', 'dd', 'e']

    # Supongamos que queremos ordenar por longitud descendente y luego lexicográficamente.
    # Podemos hacerlo con key: key=lambda s: (-len(s), s)
    print("Podemos usar key simple:", sorted(palabras, key=lambda s: (-len(s), s)))

    # Para mostrar cmp_to_key (útil si tienes un comparador complejo):
    def comparador(a: str, b: str) -> int:
        # Primero por longitud descendente
        if len(a) > len(b):
            return -1
        if len(a) < len(b):
            return 1
        # Si igual longitud, orden lexicográfico ascendente
        if a < b:
            return -1
        if a > b:
            return 1
        return 0

    # Convertimos el comparador tradicional a una key usable por sorted
    palabras_ordenadas = sorted(palabras, key=cmp_to_key(comparador))
    print("sorted con cmp_to_key(comparador) ->", palabras_ordenadas)

    # Nota: hoy en día casi siempre es preferible construir un key tuple en lugar de usar cmp_to_key,
    # pero cmp_to_key es útil si ya tienes un comparador heredado o lógica difícil de expresar con key.


# ------------------------------------------------------------
# Ejemplo 9 — Ordenar estructuras inmutables (tuplas) y conversiones
# ------------------------------------------------------------
def ejemplo_9_tuplas_inmutables():
    print("\n=== Ejemplo 9: Tuplas inmutables y sorted() ===")
    tup = (3, 1, 4, 1, 5)
    print("Tupla original:", tup)

    # sorted() acepta cualquier iterable y devuelve lista
    tup_ordenada = sorted(tup)
    print("sorted(tup) devuelve lista ordenada:", tup_ordenada)

    # Si queremos una tupla ordenada de vuelta:
    tup_ordenada_tuple = tuple(sorted(tup))
    print("tuple(sorted(tup)) ->", tup_ordenada_tuple)


# ------------------------------------------------------------
# Ejemplo 10 — Ordenar conjuntos (set) y generadores
# ------------------------------------------------------------
def ejemplo_10_sets_generadores():
    print("\n=== Ejemplo 10: Set y generadores: sorted acepta iterables ===")
    s = {5, 2, 9, 1}
    print("Set original (sin orden):", s)

    # sorted() sobre set produce lista ordenada (sets no mantienen orden)
    print("sorted(set) ->", sorted(s))

    # sorted puede consumir generadores sin materializar toda la secuencia
    gen = (i * 2 for i in range(5))  # generador
    print("sorted(gen) ->", sorted(gen))  # consume el generador


# ------------------------------------------------------------
# Ejemplo 11 — Buenas prácticas: evitar key costosa repetida (ya optimizado)
# ------------------------------------------------------------
def ejemplo_11_key_costosa():
    print("\n=== Ejemplo 11: Claves costosas — notas y ejemplo práctico ===")
    # Supongamos que calcular la clave es caro (p. ej., parsear una fecha compleja).
    # Python llama a key **una sola vez por elemento** y cachea el resultado internamente,
    # por tanto no hace falta manualmente implementar el decorate-sort-undecorate.

    datos = ["2020-01-01", "1999-12-31", "2021-06-15"]

    # key que parsea fecha (simulada con split y tuple)
    def parsear_fecha(s):
        # costosa en escenarios reales (aquí es simple)
        y, m, d = s.split('-')
        return (int(y), int(m), int(d))

    # sorted llamará parsear_fecha exactamente una vez por cada string
    ordenadas = sorted(datos, key=parsear_fecha)
    print("Fechas ordenadas por parse (key cached internamente):", ordenadas)

    # Si quisieras usar el valor parsed en posteriores operaciones, podrías precalcular:
    precalc = [(parsear_fecha(s), s) for s in datos]  # decorate
    precalc.sort()  # ordena por la clave precomputada
    resultado_precalc = [s for _, s in precalc]  # undecorate
    print("Resultado vía decorate-sort-undecorate (equivalente):", resultado_precalc)


# ------------------------------------------------------------
# Ejemplo 12 — Errores comunes y cómo evitarlos
# ------------------------------------------------------------
def ejemplo_12_errores_comunes():
    print("\n=== Ejemplo 12: Errores comunes al ordenar ===")

    # 1) Intentar ordenar una lista que contiene tipos no comparables entre sí (ej: int y str)
    mezcla = [1, 'a', 2]
    print("Mezcla:", mezcla)
    try:
        sorted(mezcla)
    except TypeError as e:
        print("TypeError esperado al mezclar tipos no comparables:", e)

    # 2) Confundir list.sort() con sorted()
    lst = [3, 2, 1]
    resultado = lst.sort()  # resultado es None
    print("lst after lst.sort():", lst, " y valor devuelto por lst.sort():", resultado)

    # 3) Usar key que falla para algunos elementos
    datos = [{'x': 1}, {'y': 2}]
    try:
        sorted(datos, key=lambda d: d['x'])  # KeyError para el segundo diccionario
    except KeyError as e:
        print("KeyError esperado si algunos elementos no cumplen la suposición del key():", e)


# ------------------------------------------------------------
# Menú interactivo para ejecutar ejemplos
# ------------------------------------------------------------
ejemplos = {
    "1": ("Números — sorted vs sort", ejemplo_1_numeros_basico),
    "2": ("Orden descendente: reverse y key", ejemplo_2_descendente_reverse_key),
    "3": ("Strings — case-insensitive", ejemplo_3_strings_case_insensitive),
    "4": ("Tuplas y key personalizado", ejemplo_4_tuplas_lexicografico),
    "5": ("Diccionarios — ordenar por clave/valor", ejemplo_5_diccionarios),
    "6": ("Objetos — lambda vs attrgetter", ejemplo_6_objetos_attrgetter_lambda),
    "7": ("Estabilidad de sort()", ejemplo_7_estabilidad),
    "8": ("cmp_to_key — comparadores clásicos", ejemplo_8_cmp_to_key),
    "9": ("Tuplas inmutables y sorted()", ejemplo_9_tuplas_inmutables),
    "10": ("Sets y generadores (sorted acepta iterables)", ejemplo_10_sets_generadores),
    "11": ("Keys costosas y optimización", ejemplo_11_key_costosa),
    "12": ("Errores comunes al ordenar", ejemplo_12_errores_comunes),
}

def menu():
    print("=== Guía: Ordenación en Python (ejecutable) ===")
    while True:
        print("\nElige un ejemplo (número), 'a' para ejecutar todos, o 'q' para salir:")
        for k, (desc, _) in ejemplos.items():
            print(f" {k}. {desc}")
        elec = input(">>> ").strip().lower()
        if elec in ("q", "salir", "exit"):
            print("Saliendo.")
            break
        if elec == "a":
            for k in sorted(ejemplos.keys(), key=int):
                print("\n" + "-" * 60)
                print(f"Ejecutando {k}. {ejemplos[k][0]}")
                ejemplos[k][1]()
            print("\nTodos los ejemplos ejecutados.")
            continue
        if elec in ejemplos:
            ejemplos[elec][1]()
        else:
            print("Opción no válida. Introduce el número del ejemplo, 'a' o 'q'.")


# ------------------------------------------------------------
# Punto de entrada
# ------------------------------------------------------------
if __name__ == "__main__":
    menu()
