"""
slicing_en_listas.py

Guía práctica (archivo .py) sobre SLICING en listas (Python)
Autor: experto en Python
Propósito: documentación + ejemplos incrementales, comentados paso a paso,
         pensados para que un principiante llegue a un nivel profesional.

Instrucciones:
 - Ejecuta este archivo con: python slicing_en_listas.py
 - Usa el menú para ejecutar ejemplos individuales o todos a la vez.
 - Cada ejemplo es autónomo y puede copiarse a otro archivo para pruebas.

Contenido:
 1) Conceptos básicos de [start:stop]
 2) Índices negativos
 3) Paso/stride y reverso [start:stop:step] (incluye a[::-1])
 4) slice() objeto y normalización con slice.indices()
 5) Asignación y borrado con slices (mutar listas, restricciones con step)
 6) Copia superficial (shallow copy) y efecto en listas anidadas
 7) División en trozos (chunking), ventanas deslizantes (sliding windows)
 8) Modificaciones in-place usando slices (buenas prácticas y rendimiento)
 9) Errores comunes, trucos y checklist profesional

Notas profesionales (breve):
 - Slicing crea una nueva lista (shallow copy) excepto cuando se asigna a la
   porción del mismo objeto (por ejemplo, lst[:] = ... modifica en-place).
 - Operaciones con slices son O(k) en tiempo y memoria donde k es el tamaño
   de la porción resultante.
 - Para grandes volúmenes de datos considerar vistas (numpy) o iteradores.
"""

from typing import List, Iterable, Tuple

# ------------------------------------------------------------
# Ejemplo 1 — Conceptos básicos: start:stop (slice simple)
# ------------------------------------------------------------
def ejemplo_1_basico():
    print("\n=== Ejemplo 1: Básico [start:stop] ===")
    lst = ['a', 'b', 'c', 'd', 'e', 'f']
    print("Lista original:", lst)

    # slice start:stop -> incluye start, excluye stop
    sub1 = lst[1:4]  # elementos en índices 1,2,3
    print("lst[1:4] ->", sub1)  # ['b', 'c', 'd']

    # start omitido -> empieza en 0
    sub2 = lst[:3]   # índices 0,1,2
    print("lst[:3] ->", sub2)  # ['a', 'b', 'c']

    # stop omitido -> hasta el final
    sub3 = lst[3:]   # índices 3,4,5
    print("lst[3:] ->", sub3)  # ['d', 'e', 'f']

    # start == stop -> devuelve lista vacía
    sub_vacia = lst[2:2]
    print("lst[2:2] ->", sub_vacia)  # []

    # índices fuera de rango no lanzan error: se recortan
    fuera = lst[1:100]
    print("lst[1:100] ->", fuera)  # hasta el final

    # confirmación: el slicing produce una NUEVA lista (shallow copy)
    sub1[0] = 'Z'  # modificamos la sublista
    print("sub1 modificado:", sub1)
    print("lista original tras modificar sub1 (sin cambio en elementos no compartidos):", lst)
    # notemos que cambiar elementos de sub1 no afecta a lst porque sub1 es una copia
    # (si los elementos son mutables, comparten referencias; eso se explica en el ejemplo 6)


# ------------------------------------------------------------
# Ejemplo 2 — Índices negativos
# ------------------------------------------------------------
def ejemplo_2_indices_negativos():
    print("\n=== Ejemplo 2: Índices negativos ===")
    lst = [10, 20, 30, 40, 50]
    print("Lista original:", lst)

    # -1 es el último, -2 el penúltimo, etc.
    print("lst[-1] ->", lst[-1])  # 50
    print("lst[-3] ->", lst[-3])  # 30

    # en slices, start/stop negativos se traducen respecto al final
    print("lst[-3:] ->", lst[-3:])   # [30,40,50]
    print("lst[:-2] ->", lst[:-2])   # [10,20,30]
    print("lst[-4:-1] ->", lst[-4:-1])  # [20,30,40]

    # combinación: start negative, stop positive
    print("lst[-4:4] ->", lst[-4:4])  # [20,30,40] (stop no incluido)


# ------------------------------------------------------------
# Ejemplo 3 — Paso (step) y reverso [start:stop:step]
# ------------------------------------------------------------
def ejemplo_3_step_reverso():
    print("\n=== Ejemplo 3: Paso (step) y reverso ===")
    lst = list(range(8))  # [0,1,2,3,4,5,6,7]
    print("Lista original:", lst)

    # step positivo: cada 2 elementos
    print("lst[::2] ->", lst[::2])  # [0,2,4,6]

    # slice con step y start/stop
    print("lst[1:6:2] ->", lst[1:6:2])  # [1,3,5]

    # step negativo invierte el orden
    print("lst[::-1] ->", lst[::-1])  # [7,6,5,4,3,2,1,0]  -> forma idiomática de invertir una lista

    # paso negativo con start/stop específicos (ten cuidado: start > stop normalmente)
    print("lst[5:1:-1] ->", lst[5:1:-1])  # [5,4,3,2] -> incluye índice 5 hasta 2 (stop exclusivo)

    # step puede ser mayor que la longitud, devuelve como máximo un elemento por su lógica
    print("lst[0:8:20] ->", lst[0:8:20])  # [0]  (salto demasiado grande)


# ------------------------------------------------------------
# Ejemplo 4 — slice() objeto y slice.indices()
# ------------------------------------------------------------
def ejemplo_4_slice_objeto():
    print("\n=== Ejemplo 4: slice() objeto y normalización ===")
    lst = list("abcdefghij")  # 10 elementos
    print("Lista:", lst)

    # crear objeto slice: slice(start, stop, step)
    s = slice(2, 8, 2)
    print("slice(2,8,2):", lst[s])  # equivalente a lst[2:8:2] -> ['c','e','g']

    # atributos del objeto slice
    print("s.start, s.stop, s.step ->", s.start, s.stop, s.step)

    # normalizar índices para una secuencia de longitud n
    n = len(lst)
    normalized = s.indices(n)  # devuelve (start, stop, step) normalizados
    print("s.indices(len(lst)) ->", normalized)

    # ejemplo con índices fuera de rango y negativos
    s2 = slice(-20, 20, 3)
    print("slice(-20,20,3) sobre la lista ->", lst[s2])
    print("s2.indices(len(lst)) ->", s2.indices(len(lst)))

    # puedes usar el objeto slice para reusar una porción en múltiples listas
    otra = list(range(20))
    print("otra lista con s2 ->", otra[s2])


# ------------------------------------------------------------
# Ejemplo 5 — Asignación y borrado con slices
# ------------------------------------------------------------
def ejemplo_5_asignacion_borrado():
    print("\n=== Ejemplo 5: Asignación y borrado con slices ===")
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Original:", lst)

    # Reemplazar una porción (slice) por una lista de distinta longitud (step == 1)
    lst[2:5] = ['A', 'B', 'C', 'D']  # 3 elementos reemplazados por 4 -> lista cambia de tamaño
    print("Después lst[2:5] = ['A','B','C','D']:", lst)

    # Borrar una porción con del
    del lst[4:7]  # elimina elementos en esos índices
    print("Después del lst[4:7]:", lst)

    # Asignación con step == 1 es flexible en longitud:
    # Si paso == 1, la longitud del iterable asignado puede diferir.
    lst = list(range(10))
    print("Reset:", lst)
    lst[1:8] = ['x']  # colapsa la porción 1:8 en un solo elemento
    print("lst[1:8] = ['x'] ->", lst)

    # Asignación con step != 1 exige que el número de elementos coincida con la porción
    lst = list(range(6))  # [0,1,2,3,4,5]
    print("Nuevo lst:", lst)
    try:
        lst[1:5:2] = [10]  # la porción seleccionada por 1:5:2 tiene longitud 2 -> ValueError
    except ValueError as e:
        print("Asignación con step !=1 y longitud incompatible -> ValueError:", e)

    # Asignación válida con step != 1 (igual longitud)
    lst[1:5:2] = [10, 11]  # reemplaza posiciones 1 y 3
    print("Tras lst[1:5:2] = [10,11] ->", lst)

    # Borrar con step (elimina elementos alternos)
    lst = list(range(10))
    print("Reset:", lst)
    del lst[::2]  # elimina índices 0,2,4,6,8
    print("del lst[::2] ->", lst)


# ------------------------------------------------------------
# Ejemplo 6 — Copia superficial (shallow copy) y listas anidadas
# ------------------------------------------------------------
def ejemplo_6_shallow_copy():
    print("\n=== Ejemplo 6: Copia superficial y listas anidadas ===")
    # Lista de listas (objetos mutables en el interior)
    lst = [[i] for i in range(3)]  # [[0],[1],[2]]
    print("Original (anidada):", lst)

    # Copia mediante slicing (shallow)
    copia = lst[:]  # nueva lista, pero referencias a los mismos sub-elementos
    print("Copia con lst[:] ->", copia)

    # Modificar un elemento interior afecta a ambos (porque comparten referencias internas)
    copia[0].append('X')
    print("Tras copia[0].append('X') -> copia:", copia)
    print("Tras copia[0].append('X') -> original:", lst)
    # Observa que tanto 'lst' como 'copia' ven el cambio del sub-elemento.

    # Para copiar profundamente (independiente), usar copy.deepcopy
    import copy
    profunda = copy.deepcopy(lst)
    profunda[0].append('Y')
    print("Tras deepcopy y modificación -> profunda:", profunda)
    print("Original tras deepcopy mod ->", lst)


# ------------------------------------------------------------
# Ejemplo 7 — Chunking y sliding window (uso práctico)
# ------------------------------------------------------------
def ejemplo_7_chunking_y_sliding():
    print("\n=== Ejemplo 7: Chunking y sliding windows ===")
    lst = list(range(1, 11))  # [1..10]
    print("Lista:", lst)

    # CHUNKING (trocear en bloques de tamaño n)
    n = 3
    chunks = [lst[i:i + n] for i in range(0, len(lst), n)]
    print(f"Chunks (tamaño {n}):", chunks)
    # Ejemplo práctico: dividir en paquetes para procesamiento por lotes

    # SLIDING WINDOW (ventana deslizante)
    k = 4
    sliding = [lst[i:i + k] for i in range(0, len(lst) - k + 1)]
    print(f"Sliding windows (tamaño {k}):", sliding)
    # Observación: las ventanas se solapan; útil en señales, NLP, features.

    # Versión generadora (memoria eficiente): no usa slice en la misma lista original
    def sliding_generator(seq: List[int], k: int) -> Iterable[List[int]]:
        # Generador que produce ventanas como SUBLISTAS nuevas (slices)
        for i in range(0, len(seq) - k + 1):
            yield seq[i:i + k]

    print("Sliding generator output:", list(sliding_generator(lst, k)))


# ------------------------------------------------------------
# Ejemplo 8 — Modificaciones in-place usando slices (buenas prácticas)
# ------------------------------------------------------------
def ejemplo_8_inplace_y_rendimiento():
    print("\n=== Ejemplo 8: Modificaciones in-place y rendimiento ===")
    import timeit

    # In-place reversal using slice assignment vs list.reverse()
    lst = list(range(10000))

    # Método 1: slice assignment (crea copia intermedia)
    def reverse_slice(a):
        a[:] = a[::-1]  # sobrescribe el contenido en la lista original

    # Método 2: método in-place nativo (más eficiente en memoria)
    def reverse_native(a):
        a.reverse()

    # Medición simple (no riguroso; solo ilustrativo)
    t1 = timeit.timeit(lambda: reverse_slice(lst.copy()), number=100)
    t2 = timeit.timeit(lambda: reverse_native(lst.copy()), number=100)
    print(f"Tiempo reverse_slice (100 rep): {t1:.4f}s")
    print(f"Tiempo reverse_native (100 rep): {t2:.4f}s")
    print("Conclusión: .reverse() evita crear copia intermedia; preferirla cuando quieras invertir en-place.")

    # In-place replace entire list content sin rebindear variable
    data = [1, 2, 3]
    print("Antes data:", data)
    data[:] = [4, 5, 6]  # modifica el objeto de la lista sin crear un nuevo objeto
    print("Después data[:] = [4,5,6]:", data)

    # IMPORTANTE: si existen otras referencias al mismo objeto de lista, data[:] preserva la identidad del objeto
    alias = data
    data[:] = [7, 8]
    print("alias (mismo objeto) tras data[:] = [7,8]:", alias)


# ------------------------------------------------------------
# Ejemplo 9 — Errores comunes, trucos y checklist profesional
# ------------------------------------------------------------
def ejemplo_9_errores_trucos():
    print("\n=== Ejemplo 9: Errores comunes y trucos profesionales ===")

    # 1. Confusión entre slice copy y referencia
    original = [0, 1, 2]
    copia = original[:]  # copia superficial
    assert copia is not original  # no es la misma referencia
    copia[0] = 999
    print("Original tras modificar copia (sin efecto):", original)

    # 2. Reasignar vs modificar in-place
    a = [1, 2, 3]
    b = a
    a = [9, 9, 9]  # reasignación: 'b' sigue apuntando a la lista anterior
    print("b tras a = [9,9,9] ->", b)
    a = b  # restauramos a la misma referencia
    a[:] = [7, 7, 7]  # modificación in-place: afecta a todas las referencias
    print("b tras a[:] = [7,7,7] ->", b)

    # 3. Evitar usar slicing innecesariamente en loops grandes (coste de copia)
    big = list(range(1000000))
    # Evitar: for sub in [big[i:i+100] for i in range(0, len(big), 100)]: ...  # crea muchas listas
    print("Consejo: para grandes volúmenes considerar iteradores o estructuras que den vistas (numpy arrays).")

    # 4. Uso de slice con step negativo para invertir texto o listas
    s = "python"
    print("s[::-1] ->", s[::-1])
    # 5. Usar slice.indices para razonar sobre start/stop/step normalizados (ver ejemplo 4)


# ------------------------------------------------------------
# Helpers: menú interactivo para ejecutar ejemplos
# ------------------------------------------------------------
ejemplos = {
    "1": ("Básico [start:stop]", ejemplo_1_basico),
    "2": ("Índices negativos", ejemplo_2_indices_negativos),
    "3": ("Step y reverso [start:stop:step]", ejemplo_3_step_reverso),
    "4": ("slice() objeto y normalización", ejemplo_4_slice_objeto),
    "5": ("Asignación y borrado con slices", ejemplo_5_asignacion_borrado),
    "6": ("Copia superficial y listas anidadas", ejemplo_6_shallow_copy),
    "7": ("Chunking y sliding windows", ejemplo_7_chunking_y_sliding),
    "8": ("Modificaciones in-place y rendimiento", ejemplo_8_inplace_y_rendimiento),
    "9": ("Errores comunes y checklist", ejemplo_9_errores_trucos),
}

def menu():
    print("=== Documentación: Slicing en listas (ejecutable) ===")
    while True:
        print("\nElige un ejemplo para ejecutar (o 'a' para ejecutar todos, 'q' para salir):")
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
            ejemplos[elec][1]()  # ejecutar la función correspondiente
        else:
            print("Opción no válida. Introduce el número del ejemplo, 'a' para todos o 'q' para salir.")

# ------------------------------------------------------------
# Punto de entrada
# ------------------------------------------------------------
if __name__ == "__main__":
    menu()
