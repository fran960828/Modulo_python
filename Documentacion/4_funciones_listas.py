# ==========================================
# Métodos de las listas en Python
# ==========================================

# Creamos ejemplos base
lista = [1, 2, 3, 4]
otra_lista = [5, 6, 7]

# ==========================================
# MÉTODOS ESPECIALES (__metodos__)
# ==========================================

# __add__: concatenar listas
print(lista.__add__(otra_lista))  # [1, 2, 3, 4, 5, 6, 7]

# __contains__: verificar si un elemento está en la lista
print(lista.__contains__(3))  # True
print(lista.__contains__(9))  # False

# __getitem__: acceder a un elemento por índice
print(lista.__getitem__(2))  # 3

# __setitem__: asignar un valor a un índice
lista.__setitem__(0, 99)
print(lista)  # [99, 2, 3, 4]

# __delitem__: eliminar un valor por índice
lista.__delitem__(0)
print(lista)  # [2, 3, 4]

# __len__: obtener longitud
print(lista.__len__())  # 3

# __iter__: devuelve un iterador
it = lista.__iter__()
print(next(it))  # 2

# __reversed__: devuelve un iterador en orden inverso
print(list(lista.__reversed__()))  # [4, 3, 2]

# __mul__: repetir lista
print(lista.__mul__(2))  # [2, 3, 4, 2, 3, 4]

# __rmul__: repetición desde la izquierda
print((2).__rmul__(lista))  # [2, 3, 4, 2, 3, 4]

# __eq__: comparar listas
print(lista.__eq__([2, 3, 4]))  # True

# __iadd__: suma en el mismo objeto
lista2 = [1, 2]
lista2.__iadd__([3, 4])
print(lista2)  # [1, 2, 3, 4]

# __class__: clase del objeto
print(lista.__class__)  # <class 'list'>

# __sizeof__: tamaño en memoria
print(lista.__sizeof__())  # depende del sistema

# ==========================================
# MÉTODOS NORMALES DE LISTA
# ==========================================

lista = [1, 2, 3, 4]

# append: agregar un elemento al final
lista.append(5)
print(lista)  # [1, 2, 3, 4, 5]

# extend: agregar otra lista al final
lista.extend([6, 7])
print(lista)  # [1, 2, 3, 4, 5, 6, 7]

# insert: insertar en una posición
lista.insert(0, 99)
print(lista)  # [99, 1, 2, 3, 4, 5, 6, 7]

# remove: elimina la primera ocurrencia de un valor
lista.remove(99)
print(lista)  # [1, 2, 3, 4, 5, 6, 7]

# pop: elimina y devuelve un elemento por índice (default último)
print(lista.pop())   # 7
print(lista.pop(0))  # 1
print(lista)  # [2, 3, 4, 5, 6]

# clear: elimina todos los elementos
copia = lista.copy()
copia.clear()
print(copia)  # []

# index: devuelve la primera posición de un valor
print(lista.index(4))  # 2

# count: cuántas veces aparece un valor
print(lista.count(3))  # 1

# sort: ordena la lista
desordenada = [3, 1, 4, 2]
desordenada.sort()
print(desordenada)  # [1, 2, 3, 4]

# sort con reverse=True
desordenada.sort(reverse=True)
print(desordenada)  # [4, 3, 2, 1]

# sort con key
palabras = ["python", "c", "java", "go"]
palabras.sort(key=len)
print(palabras)  # ['c', 'go', 'java', 'python']

# reverse: invierte la lista
lista.reverse()
print(lista)  # [6, 5, 4, 3, 2]

# copy: devuelve una copia superficial de la lista
copia_lista = lista.copy()
print(copia_lista)  # [6, 5, 4, 3, 2]

# ==========================================
# RESUMEN FINAL
# ==========================================
print("Ejemplos de TODOS los métodos de lista ejecutados correctamente ✅")
