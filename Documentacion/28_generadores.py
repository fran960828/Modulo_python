
# =================================================================
# DOCUMENTACIÓN DE GENERADORES EN PYTHON
# BASADO EN EL VIDEO "Python Tutorial: Generators..." de Corey Schafer
# =================================================================

# ---------------------------------------------------
# EJEMPLO 1: Función tradicional que devuelve una lista
# ---------------------------------------------------

# Esta función toma una lista de números (nums).
# Inicializa una lista vacía llamada 'result'.
# Itera sobre los números, calcula el cuadrado de cada uno (i * i),
# y adjunta el resultado a la lista 'result'.
# Finalmente, devuelve la lista 'result' completa.
# Esta aproximación almacena todos los valores en la memoria.
def square_numbers_list(nums):
    result = []
    for i in nums:
        result.append(i * i) # Se adjunta el cuadrado a la lista 'result'
    return result

# Uso del ejemplo 1
print("# --- Ejemplo 1: Lista (Almacenamiento completo) ---")
# Se pasa una lista y se asigna el resultado a my_nums.
my_nums_list = square_numbers_list()
print(f"Resultado de la lista: {my_nums_list}")
print("---------------------------------------------------\n")

# ---------------------------------------------------
# EJEMPLO 2: Conversión a Función Generadora usando 'yield'
# ---------------------------------------------------

# Para convertir la función anterior en un generador, se realizan tres cambios clave:
# 1. Se elimina la variable 'result' (la lista vacía).
# 2. Se elimina la sentencia 'return'.
# 3. Se reemplaza 'result.append()' por la palabra clave 'yield'.
# 'yield' convierte la función en un generador.
# Los generadores no almacenan el resultado completo en memoria; producen resultados uno por uno.
def square_numbers_generator(nums):
    for i in nums:
        yield i * i # 'yield' produce el número cuadrado

# Creación del objeto generador
my_gen = square_numbers_generator()

# --- Iteración usando next() ---
# Cuando se llama a 'my_gen', no se obtiene la lista completa, sino un objeto generador.
# El generador está esperando a que le pidamos el siguiente resultado.
print("# --- Ejemplo 2a: Generador (Iteración con next) ---")
print(f"Objeto generador creado: {my_gen}")
# Cada llamada a next() calcula y devuelve el siguiente valor.
print(f"Primer valor (1*1): {next(my_gen)}") # La i es 1, se genera 1
print(f"Segundo valor (2*2): {next(my_gen)}")
print(f"Tercer valor (3*3): {next(my_gen)}")

# Si se llama a next() después de que se hayan producido todos los valores,
# Python lanza la excepción 'StopIteration', indicando que el generador se ha agotado.
# Para fines de este código ejecutable, detenemos las llamadas a next() antes de agotarlo.

# --- Iteración usando bucle for ---
# La forma más común de usar generadores es mediante un bucle 'for'.
# El bucle 'for' sabe cuándo detenerse y maneja la excepción 'StopIteration' internamente.
print("\n# --- Ejemplo 2b: Generador (Iteración con bucle for) ---")
# Se debe recrear el generador si el anterior fue consumido.
my_gen_for = square_numbers_generator()

print("Valores producidos en el bucle:")
for num in my_gen_for:
    print(num)
print("---------------------------------------------------\n")

# NOTA: Aunque se puede convertir un generador a una lista (list(generator)),
# esto obliga a almacenar todos los valores en memoria, perdiendo las ventajas de rendimiento.


# ---------------------------------------------------
# EJEMPLO 3: Comprensión de Lista vs. Expresión de Generador
# ---------------------------------------------------

# La creación de un generador también se puede realizar mediante expresiones (generator expressions).

# Lista por Comprensión (List Comprehension):
# Utiliza corchetes [] y crea la lista completa y la almacena inmediatamente.
list_comp = [x*x for x in]
print("# --- Ejemplo 3a: Lista por Comprensión ---")
print(f"Resultado (Lista almacenada): {list_comp}")

# Expresión de Generador (Generator Expression):
# Utiliza paréntesis ().
# Esto crea un objeto generador y no calcula ni almacena los valores hasta que se iteran.
gen_exp = (x*x for x in)
print("\n# --- Ejemplo 3b: Expresión de Generador ---")
print(f"Resultado (Objeto Generador): {gen_exp}")

# Para usar los valores del generador:
print("Iteración sobre el generador:")
for val in gen_exp:
    print(val)
print("---------------------------------------------------\n")


# ---------------------------------------------------
# EJEMPLO 4: Comparación Estructural de Rendimiento (Grandes Datos)
# ---------------------------------------------------

# Los generadores ofrecen una gran mejora en rendimiento, no solo en tiempo de ejecución, sino también en memoria.
# Esto es crítico cuando se manejan millones de registros, donde almacenar todos los elementos se nota en la memoria.

# Definición de datos simulados (para estructurar los diccionarios de persona)
NAMES = ["Ana", "Beto", "Carlos"]
MAJORS = ["CS", "Physics", "Math"]

# Función que crea y devuelve una lista grande (simula alto consumo de memoria)
def create_list(num_people):
    result = []
    # Itera y adjunta el diccionario de persona a la lista 'result'.
    # En un caso real con N=1,000,000, esto incrementaría significativamente el uso de memoria.
    for i in range(num_people):
        person = {
            'id': i,
            'name': NAMES[i % len(NAMES)],
            'major': MAJORS[i % len(MAJORS)]
        }
        result.append(person)
    return result

# Función que crea un generador (simula bajo consumo de memoria)
def create_generator(num_people):
    # Usa 'yield' para producir el diccionario de persona.
    # La memoria base permanece casi igual después de esta llamada, ya que no se almacenan los datos.
    # El tiempo de ejecución inicial es casi cero, ya que se detiene en la sentencia 'yield'.
    for i in range(num_people):
        person = {
            'id': i,
            'name': NAMES[i % len(NAMES)],
            'major': MAJORS[i % len(MAJORS)]
        }
        yield person

# Simulación de uso
N = 5 # Usamos un número pequeño para ejecución rápida; el video usó N=1,000,000 para medir rendimiento

# 4a. Uso de la lista
list_result = create_list(N)
print("# --- Ejemplo 4a: Creación de Lista ---")
print(f"Lista creada. Primeros resultados: {list_result[:2]}...") # La lista se calcula y almacena inmediatamente.

# 4b. Uso del generador
gen_object = create_generator(N)
print("\n# --- Ejemplo 4b: Creación de Generador ---")
print(f"Objeto Generador: {gen_object}") # Solo se obtiene el objeto, sin cálculos ni almacenamiento masivo.

# Para obtener resultados del generador, se debe iterar.
print("\nIteración sobre el Generador:")
count = 0
for person in gen_object:
    if count < 2:
        print(person)
    count += 1
print(f"...(Se han producido {count} resultados uno por uno)")
print("---------------------------------------------------")
