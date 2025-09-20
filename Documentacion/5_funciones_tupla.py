# ==========================================
# Métodos y funciones aplicables a las tuplas
# ==========================================

# Creamos ejemplos base
tupla = (1, 2, 3, 4, 2)
otra_tupla = (5, 6, 7)

# ==========================================
# MÉTODOS ESPECIALES (__metodos__)
# ==========================================

# __add__: concatenar tuplas
print(tupla.__add__(otra_tupla))  # (1, 2, 3, 4, 2, 5, 6, 7)

# __contains__: verificar si un elemento está en la tupla
print(tupla.__contains__(3))  # True
print(tupla.__contains__(9))  # False

# __getitem__: acceder a un elemento por índice
print(tupla.__getitem__(2))  # 3

# __len__: obtener longitud
print(tupla.__len__())  # 5

# __iter__: devuelve un iterador
it = tupla.__iter__()
print(next(it))  # 1

# __mul__: repetir tupla
print(tupla.__mul__(2))  # (1, 2, 3, 4, 2, 1, 2, 3, 4, 2)

# __rmul__: repetición desde la izquierda
print((2).__rmul__(tupla))  # (1, 2, 3, 4, 2, 1, 2, 3, 4, 2)

# __eq__: comparar tuplas
print(tupla.__eq__((1, 2, 3, 4, 2)))  # True
print(tupla.__eq__((1, 2, 3)))        # False

# __hash__: obtener el hash (solo funciona porque las tuplas son inmutables)
print(tupla.__hash__())  # valor hash dependiente del contenido

# __class__: clase del objeto
print(tupla.__class__)  # <class 'tuple'>

# __sizeof__: tamaño en memoria
print(tupla.__sizeof__())  # depende del sistema

# ==========================================
# MÉTODOS NORMALES DE TUPLA
# ==========================================

# length: determinar la longitud de una tupla
print('longitud de tupla:',len(tupla))

# count: cuántas veces aparece un valor
print(tupla.count(2))  # 2

# index: devuelve la primera posición de un valor
print(tupla.index(4))  # 3
# Si no existe, lanza ValueError:
try:
    print(tupla.index(99))
except ValueError as e:
    print("Error:", e)

#max or min: devuelve maximo y mínimo
print(max(tupla),min(tupla))

# reversed:revertir la tupla
tuplaRevertida=tuple(reversed(tupla))
print(tuplaRevertida)
# sorted: ordenar tupla
tuplaOrdenada=tuple(sorted(tupla))
print(tuplaOrdenada)

#zip: formar una tupla de tuplas -> entre tuplas de la misma longitud
tupladoble=tuple(zip(tupla,otra_tupla))
print(tupladoble)
print(tupladoble[1][0])#->Método para acceder a una tupla doble

#slicing en tuplas
print(tupla[2:])
print(tupladoble[1][1:])

#Descompresión de tuplas
entero_1,entero_2,entero_3=otra_tupla
print(entero_1,entero_2,entero_3)
# ==========================================
# RESUMEN FINAL
# ==========================================
print("Ejemplos de TODOS los métodos de tupla ejecutados correctamente ✅")
