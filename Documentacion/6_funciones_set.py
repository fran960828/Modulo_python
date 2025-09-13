# ==========================================
# Métodos y funciones aplicables a los sets
# ==========================================

# Creamos ejemplos base
s = {1, 2, 3}
otro_set = {3, 4, 5}

# ==========================================
# MÉTODOS ESPECIALES (__metodos__)
# ==========================================

# __contains__: verificar si un elemento está en el set
print(s.__contains__(2))  # True
print(s.__contains__(99)) # False

# __len__: longitud del set
print(s.__len__())  # 3

# __iter__: devuelve un iterador
it = s.__iter__()
print(next(it))  # primer elemento (orden no garantizado)

# __eq__: comparar sets (mismos elementos = True)
print(s.__eq__({1, 2, 3}))  # True
print(s.__eq__({1, 2}))     # False

# __ne__, __lt__, __le__, __gt__, __ge__: comparaciones de subconjuntos
print({1, 2}.__lt__({1, 2, 3}))  # True
print({1, 2, 3}.__ge__({1, 2}))  # True

# __or__: unión de sets
print(s.__or__(otro_set))  # {1, 2, 3, 4, 5}

# __and__: intersección de sets
print(s.__and__(otro_set))  # {3}

# __sub__: diferencia
print(s.__sub__(otro_set))  # {1, 2}

# __xor__: diferencia simétrica
print(s.__xor__(otro_set))  # {1, 2, 4, 5}

# __iand__, __ior__, __ixor__, __isub__: operaciones en el mismo set
a = {1, 2, 3}
a.__iand__({2, 3, 4})
print(a)  # {2, 3}

b = {1, 2}
b.__ior__({3, 4})
print(b)  # {1, 2, 3, 4}

c = {1, 2, 3}
c.__isub__({2})
print(c)  # {1, 3}

d = {1, 2}
d.__ixor__({2, 3})
print(d)  # {1, 3}

# __sizeof__: tamaño en memoria
print(s.__sizeof__())  # depende del sistema

# __class__: clase del objeto
print(s.__class__)  # <class 'set'>

# ==========================================
# MÉTODOS NORMALES DE SET
# ==========================================

# add: añadir un elemento
s1 = {1, 2}
s1.add(3)
print(s1)  # {1, 2, 3}

# clear: vaciar el set
s2 = {1, 2, 3}
s2.clear()
print(s2)  # set()

# copy: copia superficial
s3 = s.copy()
print(s3)  # {1, 2, 3}

# difference: elementos en un set y no en otro
print(s.difference(otro_set))  # {1, 2}

# difference_update: elimina los elementos que están en otro set
s4 = {1, 2, 3}
s4.difference_update({2, 3})
print(s4)  # {1}

# discard: elimina un elemento si existe (sin error si no existe)
s5 = {1, 2, 3}
s5.discard(2)
s5.discard(99)  # no da error
print(s5)  # {1, 3}

# intersection: intersección
print(s.intersection(otro_set))  # {3}

# intersection_update: deja solo la intersección
s6 = {1, 2, 3}
s6.intersection_update({2, 3, 4})
print(s6)  # {2, 3}

# isdisjoint: True si no tienen elementos en común
print({1, 2}.isdisjoint({3, 4}))  # True
print({1, 2}.isdisjoint({2, 3}))  # False

# issubset: verificar si un set está contenido en otro
print({1, 2}.issubset({1, 2, 3}))  # True

# issuperset: verificar si un set contiene a otro
print({1, 2, 3}.issuperset({2, 3}))  # True

# pop: elimina y devuelve un elemento aleatorio
s7 = {10, 20, 30}
print(s7.pop())  # puede ser 10, 20 o 30
print(s7)

# remove: elimina un elemento (lanza error si no existe)
s8 = {1, 2, 3}
s8.remove(2)
print(s8)  # {1, 3}
try:
    s8.remove(99)
except KeyError as e:
    print("Error:", e)

# symmetric_difference: elementos en uno u otro pero no ambos
print({1, 2, 3}.symmetric_difference({3, 4, 5}))  # {1, 2, 4, 5}

# symmetric_difference_update: actualiza con diferencia simétrica
s9 = {1, 2, 3}
s9.symmetric_difference_update({3, 4, 5})
print(s9)  # {1, 2, 4, 5}

# union: unión de sets
print({1, 2}.union({2, 3}, {4}))  # {1, 2, 3, 4}

# update: agrega elementos de otro iterable
s10 = {1}
s10.update([2, 3], {4, 5})
print(s10)  # {1, 2, 3, 4, 5}

# ==========================================
# RESUMEN FINAL
# ==========================================
print("Ejemplos de TODOS los métodos de set ejecutados correctamente ✅")
