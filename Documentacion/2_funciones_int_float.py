# ==========================================
# Métodos y funciones aplicables a números int y float
# ==========================================

# Ejemplos con int y float
x_int = 42
y_int = 7
x_float = 3.75
y_float = -2.5

# ==========================================
# Métodos comunes a int y float (operadores especiales)
# ==========================================

# __add__: suma
print(x_int.__add__(y_int))   # 42 + 7 = 49
print(x_float.__add__(y_float))  # 3.75 + (-2.5) = 1.25

# __sub__: resta
print(x_int.__sub__(y_int))   # 42 - 7 = 35
print(x_float.__sub__(y_float))  # 3.75 - (-2.5) = 6.25

# __mul__: multiplicación
print(x_int.__mul__(y_int))   # 42 * 7 = 294
print(x_float.__mul__(y_float))  # 3.75 * -2.5 = -9.375

# __truediv__: división real
print(x_int.__truediv__(y_int))  # 42 / 7 = 6.0
print(x_float.__truediv__(y_float))  # 3.75 / -2.5 = -1.5

# __floordiv__: división entera (redondeo hacia abajo)
print(x_int.__floordiv__(y_int))  # 42 // 7 = 6
print(x_float.__floordiv__(y_float))  # 3.75 // -2.5 = -2.0

# __mod__: resto de división
print(x_int.__mod__(y_int))   # 42 % 7 = 0
print(x_float.__mod__(y_float))  # 3.75 % -2.5 = 1.25

# __pow__: potencia
print(x_int.__pow__(y_int))  # 42 ** 7 = número grande
print(x_float.__pow__(2))    # 3.75 ** 2 = 14.0625

# __neg__: negación
print(x_int.__neg__())   # -42
print(x_float.__neg__()) # -3.75

# __abs__: valor absoluto
print(x_int.__abs__())   # 42
print(y_float.__abs__()) # 2.5

# __eq__, __ne__, __lt__, __le__, __gt__, __ge__: comparaciones
print(x_int.__eq__(42))  # True
print(x_float.__lt__(0)) # False

# ==========================================
# Métodos específicos de int
# ==========================================

# bit_length: número de bits necesarios para representar el entero en binario
print((255).bit_length())  # 8

# to_bytes / from_bytes: representación en bytes
n = 1024
b = n.to_bytes(4, byteorder="big")
print(b)  # b'\x00\x00\x04\x00'
print(int.from_bytes(b, byteorder="big"))  # 1024

# conjugate: devuelve el mismo número (útil para compatibilidad con complejos)
print((5).conjugate())  # 5

# numerator y denominator (en int siempre denominator = 1)
print((7).numerator, (7).denominator)  # (7, 1)

# ==========================================
# Métodos específicos de float
# ==========================================

# as_integer_ratio: representa el float como fracción exacta
print((0.75).as_integer_ratio())  # (3, 4)

# is_integer: True si el número no tiene parte decimal
print((5.0).is_integer())   # True
print((5.1).is_integer())   # False

# hex: representación hexadecimal
print((3.5).hex())  # '0x1.c000000000000p+1'

# fromhex: construir un float desde un string hexadecimal
print(float.fromhex('0x1.c000000000000p+1'))  # 3.5

# real e imag: parte real e imaginaria (imag = 0.0 en float)
print(x_float.real, x_float.imag)  # (3.75, 0.0)

# conjugate: igual que en int, retorna el mismo float
print((-4.2).conjugate())  # -4.2

# numerator / denominator: fracción exacta del float
print((1.25).as_integer_ratio())  # (5, 4)

# ==========================================
# Métodos comunes de conversión
# ==========================================

# __int__: convertir a int
print(int(3.99))  # 3

# __float__: convertir a float
print(float(7))   # 7.0

# __round__: redondeo
print(round(3.14159, 2))  # 3.14

# __trunc__, __floor__, __ceil__ (a través de math)
import math
print(math.trunc(3.99))  # 3
print(math.floor(3.99))  # 3
print(math.ceil(3.01))   # 4

# ==========================================
# Atributos internos
# ==========================================

# __class__: clase del objeto
print(x_int.__class__)    # <class 'int'>
print(x_float.__class__)  # <class 'float'>

# __hash__: hash del número
print(hash(42), hash(3.14))

# __sizeof__: tamaño en memoria
print(x_int.__sizeof__())    # depende del sistema
print(x_float.__sizeof__())  # depende del sistema
