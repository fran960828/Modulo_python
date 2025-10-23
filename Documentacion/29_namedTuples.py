
# Este código documenta los ejemplos presentados en el video sobre 'namedtuples',
# comparando su uso con tuplas normales y diccionarios para mejorar la legibilidad del código.

# === Introducción: Namedtuples, Tuplas y Legibilidad ===
# Las 'namedtuples' (tuplas con nombre) son un objeto ligero que funciona como una tupla normal
# pero está diseñado para ser más legible.
# Actúan como un buen término medio entre una tupla y un diccionario.

# === Ejemplo A: Tupla Normal para Representar Colores RGB ===

# Representación de valores RGB (Rojo, Verde, Azul) usando una tupla normal.
# (55 = Rojo, 155 = Verde, 255 = Azul).
color = (55, 155, 255)

# Acceso al valor rojo mediante el índice cero.
print(f"--- Ejemplo A: Tupla Normal ---")
print(f"Valor rojo (índice 0): {color}")

# Problema de la tupla normal: Es poco legible.
# Cuando otra persona (o el propio autor semanas después) mire 'color',
# no sabrá inmediatamente qué significa ese valor (ej. ¿es matiz, saturación, luminosidad?).


# === Ejemplo B: Uso de un Diccionario para Lograr Legibilidad ===

# Una alternativa inicial para mejorar la legibilidad es usar un diccionario.
color_dict = {'red': 55, 'green': 155, 'blue': 255}

# Acceso al valor rojo mediante la clave 'red', lo que es mucho más legible que usar el índice 0.
print(f"\n--- Ejemplo B: Diccionario ---")
print(f"Valor rojo (clave 'red'): {color_dict['red']}")

# Problemas del diccionario:
# 1. Se pierde la inmutabilidad de la tupla, si esto era un requisito.
# 2. Requiere escribir más. Para crear un color nuevo, hay que volver a escribir todas las claves ('red', 'green', 'blue').
# 3. Se requiere el uso de corchetes ['clave'], lo cual es menos conciso que la sintaxis de punto.


# === Ejemplo C: Uso de Namedtuple (El buen término medio) ===

# Paso 1: Importar namedtuple del módulo 'collections'.
from collections import namedtuple

# Paso 2: Definición de la Namedtuple.
# Se define la clase 'Color' y se especifican los campos deseados: 'red', 'green', 'blue'.
Color = namedtuple('Color', ['red', 'green', 'blue'])

# Paso 3: Creación de una instancia de 'Color'.
color_namedtuple = Color(55, 155, 255)

print(f"\n--- Ejemplo C: Namedtuple ---")

# La namedtuple sigue funcionando como una tupla, permitiendo el acceso por índice.
print(f"Acceso por índice (ej. valor rojo): {color_namedtuple}")

# Principal Ventaja: Permite el acceso por nombre, lo que la hace mucho más legible.
# La sintaxis con punto (color.red) es más fácil de usar que los corchetes del diccionario.
print(f"Acceso por nombre (ej. valor rojo): {color_namedtuple.red}")

# Ventaja de la creación: Es más fácil y requiere menos escritura que un diccionario al instanciar.
# Creamos un nuevo color, 'blanco' (255, 255, 255), solo pasando los valores.
white = Color(255, 255, 255)

# Acceso al valor azul del nuevo color 'white'.
print(f"Valor azul del color 'white': {white.blue}")

# La legibilidad mejora drásticamente, ya que el código indica instantáneamente lo que se está accediendo.
```