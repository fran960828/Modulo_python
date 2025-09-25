# ==========================================
# Métodos y funciones aplicables a diccionarios
# ==========================================

# Creamos ejemplos base
d = {"a": 1, "b": 2, "c": 3}
otro_dict = {"c": 30, "d": 4}

# ==========================================
# MÉTODOS ESPECIALES (__metodos__)
# ==========================================

# __getitem__: acceder a un valor por clave
print(d.__getitem__("a"))  # 1

# __setitem__: asignar un valor a una clave
d.__setitem__("e", 5)
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'e': 5}

# __delitem__: eliminar un par clave-valor
d.__delitem__("e")
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# __contains__: verificar si una clave existe
print(d.__contains__("a"))  # True
print(d.__contains__("z"))  # False

# __len__: cantidad de pares clave-valor
print(d.__len__())  # 3

# __iter__: devuelve un iterador sobre las claves
it = d.__iter__()
print(next(it))  # "a" (primer clave, orden de inserción)

# __eq__: comparar diccionarios
print(d.__eq__({"a": 1, "b": 2, "c": 3}))  # True
print(d.__eq__({"a": 1}))  # False

# __class__: clase del objeto
print(d.__class__)  # <class 'dict'>

# __sizeof__: tamaño en memoria
print(d.__sizeof__())  # depende del sistema

# ==========================================
# MÉTODOS NORMALES DE DICCIONARIO
# ==========================================

# clear: eliminar todo el contenido
d2 = {"x": 1, "y": 2}
d2.clear()
print(d2)  # {}

# copy: copia superficial del diccionario
copia = d.copy()
print(copia)  # {'a': 1, 'b': 2, 'c': 3}

# fromkeys: crear diccionario a partir de una secuencia de claves
nuevo = dict.fromkeys(["k1", "k2"], 0)
print(nuevo)  # {'k1': 0, 'k2': 0}

# get: obtener un valor con clave, con valor por defecto si no existe
print(d.get("a"))       # 1
print(d.get("z", "NA")) # "NA"

# items: obtener pares clave-valor como vista
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# keys: obtener claves
print(d.keys())  # dict_keys(['a', 'b', 'c'])

# values: obtener valores
print(d.values())  # dict_values([1, 2, 3])

# pop: eliminar y devolver el valor de una clave
valor = d.pop("a")
print(valor)  # 1
print(d)  # {'b': 2, 'c': 3}

# popitem: elimina y devuelve el último par insertado
par = d.popitem()
print(par)  # ('c', 3)  (clave, valor)
print(d)    # {'b': 2}

# setdefault: obtener valor si existe o insertar clave con valor por defecto
d3 = {"x": 1}
print(d3.setdefault("x", 99))  # 1 (ya existía)
print(d3.setdefault("y", 99))  # 99 (insertado)
print(d3)  # {'x': 1, 'y': 99}

# update: fusionar otro diccionario o pares clave-valor
d4 = {"a": 1, "b": 2}
d4.update({"b": 20, "c": 30})
print(d4)  # {'a': 1, 'b': 20, 'c': 30}

# También funciona con kwargs
d4.update(d=40, e=50)
print(d4)  # {'a': 1, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# Eliminara pares clave valor diccionario o diccionario entero
del d4['a']
print(d4)

# Convertir listas a diccionarios
materias = ['Matemáticas', 'Física', 'Química']
notas = [8, 7, 6]
diccionario_notas = dict(zip(materias, notas))
print(diccionario_notas)

#Recorrer pares clave-valor
for clave, valor in diccionario_notas.items():
    print(f"{clave}: {valor}")

#Ordenar diccionario por clave
for clave in sorted(diccionario_notas.keys()):
    print(f"{clave}")

#Eliminar valores repetidos en un diccionario
for values in set(diccionario_notas.values()):
    print(f"{values}")

# Anidamiento de diccionarios
estudiantes = {
    "001": {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería"},
    "002": {"nombre": "Luis", "edad": 22, "carrera": "Medicina"},
    "003": {"nombre": "Marta", "edad": 21, "carrera": "Derecho"}
}
for id, info in estudiantes.items():
    print(f"ID: {id}, Nombre: {info['nombre']}, Edad: {info['edad']}, Carrera: {info['carrera']}")



# ==========================================
# RESUMEN FINAL
# ==========================================
print("Ejemplos de TODOS los métodos de dict ejecutados correctamente ✅")
