# ==================================
# Métodos especiales de strings (__metodos__)
# ==================================

# __add__ : Se usa al concatenar (sumar) cadenas con +.
texto1 = "Hola "
texto2 = "Mundo"
print(texto1.__add__(texto2))  # Hola Mundo
print(texto1 + texto2)         # Hola Mundo

# __class__ : Devuelve la clase del objeto.
texto = "Python"
print(texto.__class__)  # <class 'str'>

# __contains__ : Comprueba si un substring está dentro de la cadena.
print("Py" in texto)              # True
print(texto.__contains__("th"))   # True

# __delattr__ : Intenta borrar un atributo (no es común usarlo en str).
# Los strings no permiten atributos personalizados, esto dará error si lo usas.

# __dir__ : Muestra los métodos disponibles para el objeto.
print(dir(texto))

# __doc__ : Devuelve la documentación de la clase str.
print(str.__doc__)

# __eq__ : Compara si dos strings son iguales.
print("hola".__eq__("hola"))  # True
print("hola" == "hola")       # True

# __format__ : Define cómo se formatea un string.
nombre = "Ana"
print("Hola, {}".format(nombre))
print("Hola, {0}".__format__(nombre))

# __ge__, __gt__, __le__, __lt__ : Comparan cadenas según orden alfabético.
print("b".__gt__("a"))  # True (b > a)
print("a" < "b")        # True

# __getattribute__ : Llama cuando accedemos a un atributo del objeto.
print(texto.__getattribute__('upper')())  # PYTHON

# __getitem__ : Accede a un carácter por índice.
print(texto.__getitem__(0))  # P
print(texto[0])              # P

# __getnewargs__, __getstate__, __reduce__, __reduce_ex__ : Métodos usados en serialización/pickling.
# Normalmente no los usamos directamente como principiantes.

# __hash__ : Devuelve un número único que representa el string.
print(hash("hola"))

# __init__, __new__ : Se usan al crear objetos. En str, ya están definidos internamente.

# __iter__ : Permite recorrer el string en un bucle.
for letra in texto.__iter__():
    print(letra)

# __len__ : Devuelve la longitud de la cadena.
print(texto.__len__())  # 6
print(len(texto))       # 6

# __mod__ y __rmod__ : Se usan con el operador % (formato estilo antiguo).
nombre = "Luis"
print("Hola %s" % nombre)           # Hola Luis
print("Hola %s".__mod__(nombre))    # Hola Luis

# __mul__ y __rmul__ : Repite la cadena.
print("Hi" * 3)             # HiHiHi
print("Hi".__mul__(3))      # HiHiHi

# __ne__ : Verifica si dos strings NO son iguales.
print("a".__ne__("b"))  # True

# __repr__ y __str__ : Representación del string.
print(repr("hola"))   # 'hola'
print(str("hola"))    # hola

# __setattr__ : No se puede usar en strings (son inmutables).

# __sizeof__ : Devuelve el tamaño en bytes que ocupa en memoria.
print("hola".__sizeof__())

# __subclasshook__ : Usado en herencia, no lo usamos directamente.


# ==================================
# Métodos normales de strings
# ==================================

# capitalize : Primera letra en mayúscula, resto en minúscula.
print("juan".capitalize())  # Juan

# casefold : Convierte a minúsculas de forma más agresiva que lower().
print("ÁRbol".casefold())  # árbol

# center : Centra el texto, rellenando con espacios o un carácter.
print("hi".center(10, "-"))  # ----hi----

# count : Cuenta cuántas veces aparece un substring.
print("banana".count("a"))  # 3

# encode : Convierte a bytes.
print("hola".encode())  # b'hola'

# endswith : Verifica si termina con un substring.
print("programa.py".endswith(".py"))  # True

# expandtabs : Reemplaza tabulaciones con espacios.
print("uno\tdos".expandtabs(4))

# find : Devuelve la posición de un substring (o -1 si no existe).
print("banana".find("na"))  # 2

# format : Inserta valores en un texto.
print("Hola, {}".format("Ana"))  # Hola, Ana

# format_map : Similar a format pero con diccionarios.
datos = {"nombre": "Ana"}
print("Hola, {nombre}".format_map(datos))  # Hola, Ana

# index : Devuelve la posición del substring (error si no lo encuentra).
print("banana".index("na"))  # 2

# isalnum : Verifica si es alfanumérico.
print("abc123".isalnum())  # True

# isalpha : Verifica si solo tiene letras.
print("abc".isalpha())  # True

# isascii : Verifica si todos los caracteres son ASCII.
print("hola".isascii())  # True

# isdecimal, isdigit, isnumeric : Verifican números.
print("123".isdecimal())  # True
print("123".isdigit())    # True
print("123".isnumeric())  # True

# isidentifier : Verifica si es un nombre válido de variable.
print("variable1".isidentifier())  # True

# islower : Verifica si todo está en minúsculas.
print("hola".islower())  # True

# isprintable : Verifica si se puede imprimir.
print("hola".isprintable())  # True

# isspace : Verifica si contiene solo espacios.
print("   ".isspace())  # True

# istitle : Verifica si cada palabra empieza en mayúscula.
print("Hola Mundo".istitle())  # True

# isupper : Verifica si todo está en mayúsculas.
print("HOLA".isupper())  # True

# join : Une elementos de una lista en un string.
print(",".join(["a", "b", "c"]))  # a,b,c

# ljust : Alinea a la izquierda rellenando.
print("hi".ljust(10, "-"))  # hi--------

# lower : Convierte todo a minúsculas.
print("HOLA".lower())  # hola

# lstrip : Quita espacios a la izquierda.
print("   hola".lstrip())  # "hola"

# maketrans y translate : Para reemplazar varios caracteres.
trans = str.maketrans("aeiou", "12345")
print("hola".translate(trans))  # h4l1

# partition : Divide en 3 partes (antes, separador, después).
print("uno-dos".partition("-"))  # ('uno', '-', 'dos')

# removeprefix : Quita un prefijo si existe.
print("pythonista".removeprefix("py"))  # thonista

# removesuffix : Quita un sufijo si existe.
print("archivo.txt".removesuffix(".txt"))  # archivo

# replace : Reemplaza partes de la cadena.
print("hola mundo".replace("mundo", "Python"))  # hola Python

# rfind y rindex : Igual que find/index pero desde la derecha.
print("banana".rfind("na"))  # 4
print("banana".rindex("na")) # 4

# rjust : Alinea a la derecha.
print("hi".rjust(10, "-"))  # --------hi

# rpartition : Igual que partition pero busca desde la derecha.
print("uno-dos-tres".rpartition("-"))  # ('uno-dos', '-', 'tres')

# rsplit : Divide desde la derecha.
print("a,b,c".rsplit(",", 1))  # ['a,b', 'c']

# rstrip : Quita espacios a la derecha.
print("hola   ".rstrip())  # "hola"

# split : Divide en una lista.
print("uno dos tres".split())  # ['uno', 'dos', 'tres']

# splitlines : Divide en una lista por saltos de línea.
print("uno\ndos\ntres".splitlines())  # ['uno', 'dos', 'tres']

# startswith : Verifica si empieza con algo.
print("python".startswith("py"))  # True

# strip : Quita espacios a ambos lados.
print("   hola   ".strip())  # "hola"

# swapcase : Invierte mayúsculas/minúsculas.
print("Hola".swapcase())  # hOLA

# title : Convierte en estilo título.
print("hola mundo".title())  # Hola Mundo

# upper : Convierte a mayúsculas.
print("hola".upper())  # HOLA

# zfill : Rellena con ceros a la izquierda hasta un ancho dado.
print("42".zfill(5))  # 00042
