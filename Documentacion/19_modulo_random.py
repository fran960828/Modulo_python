# Importamos el módulo 'random', que es parte de la librería estándar de Python [1].
# NOTA IMPORTANTE: Este módulo no debe usarse para propósitos de seguridad o criptografía; para eso se sugiere usar el módulo 'secrets' [2].
import random

# --- 1. random.random() ---
# Descripción: Obtiene un valor de punto flotante (float) aleatorio entre 0 (inclusivo) y 1 (no inclusivo) [1].
# Es decir, puede obtener exactamente 0, pero nunca exactamente 1 (solo hasta 0.999...) [1].
valor_aleatorio_0_1 = random.random()
print(f"--- 1. random.random() ---")
print(f"Valor entre 0 y 1: {valor_aleatorio_0_1}") # [1]

# --- 2. random.uniform(a, b) ---
# Descripción: Obtiene un valor de punto flotante aleatorio entre un rango específico (por ejemplo, entre 1 y 10) [3].
# Este método facilita obtener valores flotantes dentro de un rango deseado [3].
valor_flotante_rango = random.uniform(1, 10)
print(f"\n--- 2. random.uniform(a, b) ---")
print(f"Valor flotante entre 1 y 10: {valor_flotante_rango}") # [3]

# --- 3. random.randint(a, b) ---
# Descripción: Obtiene un número entero aleatorio dentro de un rango donde ambos límites (a y b) son inclusivos [3].

# Ejemplo 3a: Simular el lanzamiento de un dado de seis caras (valores entre 1 y 6, ambos inclusive) [3].
lanzamiento_dado = random.randint(1, 6)
print(f"\n--- 3a. random.randint(a, b) (Dado) ---")
print(f"Resultado del dado (entre 1 y 6): {lanzamiento_dado}") # [3]

# Ejemplo 3b: Simular el lanzamiento de una moneda (0 o 1) [4].
lanzamiento_moneda = random.randint(0, 1)
print(f"\n--- 3b. random.randint(a, b) (Moneda) ---")
print(f"Resultado de la moneda (0 o 1): {lanzamiento_moneda}") # [4]

# --- 4. random.choice(secuencia) ---
# Descripción: Selecciona un valor aleatorio de una lista de valores o cualquier secuencia [4].
greetings = ["Hola", "Qué tal", "Saludos", "Hey"] # [4]
saludo_aleatorio = random.choice(greetings)
print(f"\n--- 4. random.choice(secuencia) ---")
print(f"Saludo aleatorio de la lista: {saludo_aleatorio}") # [4]

# --- 5. random.choices(secuencia, k=n, weights=[...]) ---
# Descripción: Se utiliza para obtener múltiples valores aleatorios de una lista [5].
# El argumento 'k' define cuántas veces queremos seleccionar un valor [6].

# Ejemplo 5a: Simulación de 10 resultados de ruleta (Rojo, Negro, Verde) sin pesos [5, 6].
# Todos los resultados son igualmente probables [6].
colores_ruleta = ["rojo", "negro", "verde"] # [5]
resultados_sin_peso = random.choices(colores_ruleta, k=10) # [6]
print(f"\n--- 5a. random.choices(k=10) (Sin pesos) ---")
print(f"10 resultados (igual probabilidad): {resultados_sin_peso}") # [6]

# Ejemplo 5b: Simulación de resultados de ruleta con pesos/probabilidades [6, 7].
# Se utilizan pesos para reflejar las probabilidades reales (18/38 Rojo, 18/38 Negro, 2/38 Verde) [7].
# Esto hace que 'verde' sea mucho menos probable de ser seleccionado [7].
pesos = [1] # El orden corresponde a ["rojo", "negro", "verde"] [7].
resultados_con_peso = random.choices(colores_ruleta, k=10, weights=pesos) # [6]
print(f"\n--- 5b. random.choices(k=10, con pesos) ---")
print(f"10 resultados (probabilidad con pesos): {resultados_con_peso}") # [6, 7]

# --- 6. random.shuffle(lista) ---
# Descripción: Baraja o mezcla aleatoriamente los elementos de una lista *en el lugar* (modifica la lista original) [8].
# Ejemplo: Barajar un mazo de 52 cartas (rango de 1 a 52) [7, 8].
deck = list(range(1, 53)) # 53 es no inclusivo en range [8].
print(f"\n--- 6. random.shuffle(lista) ---")
print(f"Deck original (primeros 5): {deck[:5]}")
random.shuffle(deck) # Modifica la lista 'deck' [8].
print(f"Deck barajado (primeros 5): {deck[:5]}") # [8]

# --- 7. random.sample(secuencia, k=n) ---
# Descripción: Obtiene una muestra de 'k' valores aleatorios *únicos* de una secuencia [9].
# Es esencial cuando no se desean repeticiones (a diferencia de 'choices', que sí puede repetirlas) [9].
# Ejemplo: Obtener 5 cartas únicas del mazo [9].
hand = random.sample(deck, k=5) # [9]
print(f"\n--- 7. random.sample(secuencia, k=n) ---")
print(f"Mano de 5 cartas únicas: {hand}") # [9]

# --- 8. Uso Práctico (Generación de datos ficticios) ---
# Este es un ejemplo práctico que combina múltiples funciones (choice y randint) para generar datos de prueba [10].
print(f"\n--- 8. Ejemplo de Datos Ficticios Generados (Usando choice y randint) ---")

first_names = ["Juan", "Maria", "Pedro"] # Lista de nombres [10].
last_names = ["Gomez", "Perez", "Rodriguez"] # Lista de apellidos [10].
street_names = ["Calle Central", "Avenida Norte", "Via del Sol"] # Lista de calles [10].
cities = ["Springfield", "Gotham", "Metropolis"] # Lista de ciudades [10].
states = ["CA", "NY", "TX"] # Lista de estados [11].

# Generación de Nombre y Apellido: random.choice [11]
first = random.choice(first_names) # [11]
last = random.choice(last_names) # [11]

# Generación de Número de Teléfono: random.randint [11]
# El primer valor es un número de 3 dígitos (entre 100 y 999) [11].
area_code = random.randint(100, 999) # [11]
# El último valor es un número de 4 dígitos (entre 1000 y 9999) [11].
last_four = random.randint(1000, 9999) # [11]
phone_number = f"{area_code}-555-{last_four}" # Se usa '555' como número ficticio central [11].

# Generación de Dirección: random.randint y random.choice [11, 12]
street_num = random.randint(100, 999) # Número de calle de 3 dígitos [11].
street = random.choice(street_names) # [11]
city = random.choice(cities) # [11]
state = random.choice(states) # [12]
zip_code = random.randint(10000, 99999) # Código postal de 5 dígitos [12].

address = f"{street_num} {street}, {city}, {state} {zip_code}" # Combinando valores con f-string [12].
email = f"{first.lower()}.{last.lower()}@email.falso.com" # El email combina los nombres elegidos [12].

# Impresión de los datos ficticios generados [12]
print(f"Nombre: {first} {last}") 
print(f"Teléfono: {phone_number}") 
print(f"Dirección: {address}") 
print(f"Email: {email}") 