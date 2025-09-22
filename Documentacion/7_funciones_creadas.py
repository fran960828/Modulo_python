# ====================================================
# 📌 DOCUMENTACIÓN Y EJEMPLOS DE FUNCIONES EN PYTHON
# ====================================================

# ----------------------------------------------------
# 1. Función SIN parámetros
# ----------------------------------------------------
# Definimos una función que no recibe nada y solo imprime algo
def saludar():
    print("Hola, esta es una función sin parámetros.")

saludar()  # Llamada a la función


# ----------------------------------------------------
# 2. Función CON parámetros
# ----------------------------------------------------
# Definimos una función que recibe valores al llamarla
def saludar_nombre(nombre):
    print(f"Hola {nombre}, bienvenido a Python.")

saludar_nombre("Ana")
saludar_nombre("Luis")


# ----------------------------------------------------
# 3. Función CON return
# ----------------------------------------------------
# Las funciones pueden devolver un valor con 'return'
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print("Resultado de la suma:", resultado)


# ----------------------------------------------------
# 4. Función SIN return (retorno implícito None)
# ----------------------------------------------------
# Si no usamos 'return', la función devuelve None por defecto
def imprimir_suma(a, b):
    print("Suma:", a + b)

valor = imprimir_suma(2, 4)
print("Valor devuelto:", valor)  # None


# ----------------------------------------------------
# 5. Función con *args
# ----------------------------------------------------
# *args permite pasar una cantidad variable de argumentos
def sumar_varios(*args):
    return sum(args)

print("Suma de varios números:", sumar_varios(1, 2, 3, 4, 5))


# ----------------------------------------------------
# 6. Función con **kwargs
# ----------------------------------------------------
# **kwargs permite pasar argumentos nombrados (clave=valor)
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=30, ciudad="Madrid")


# ----------------------------------------------------
# 7. Pasar LISTAS como parámetros
# ----------------------------------------------------
# Podemos pasar una lista y procesarla dentro de la función
def procesar_lista(lista):
    return [x * 2 for x in lista]

numeros = [1, 2, 3, 4]
print("Lista procesada:", procesar_lista(numeros))


# También podemos desempaquetar una lista con * al pasarla
def multiplicar(a, b, c):
    return a * b * c

valores = [2, 3, 4]
print("Multiplicación con *lista:", multiplicar(*valores))


# ----------------------------------------------------
# 8. Pasar DICCIONARIOS como parámetros
# ----------------------------------------------------
# Podemos desempaquetar diccionarios con **
def mostrar_persona(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Sevilla"}
mostrar_persona(**persona)  # Se pasan como kwargs


# ----------------------------------------------------
# 9. Funciones anidadas (funciones dentro de funciones)
# ----------------------------------------------------
def exterior(x):
    def interior(y):
        return y * 2
    return interior(x)

print("Resultado función anidada:", exterior(5))


# ----------------------------------------------------
# 10. Funciones lambda (funciones anónimas)
# ----------------------------------------------------
# Son funciones pequeñas que se definen en una sola línea
doble = lambda x: x * 2
print("Lambda doble:", doble(4))

# Uso común con funciones de orden superior
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados con lambda:", cuadrados)


# ----------------------------------------------------
# 11. Buenas prácticas profesionales
# ----------------------------------------------------
# - Usar nombres descriptivos para las funciones.
# - Documentar con docstrings.
# - Mantener funciones cortas y específicas.
# - Evitar modificar variables globales.
# - Preferir argumentos con valores por defecto para configuraciones.

def calcular_area(base: float, altura: float = 1.0) -> float:
    """
    Calcula el área de un rectángulo.

    Parámetros:
        base (float): longitud de la base.
        altura (float, opcional): altura del rectángulo. Por defecto 1.0.

    Retorna:
        float: área del rectángulo.
    """
    return base * altura

print("Área con base=5 y altura=2:", calcular_area(5, 2))
print("Área solo con base=5:", calcular_area(5))
