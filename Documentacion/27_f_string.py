
# ==============================================================================
# Python Quick Tip: F-Strings - Uso y Formato Avanzado
# Los F-Strings son una característica de Python 3.6 en adelante.
# ==============================================================================

# Configuración inicial de variables para los primeros ejemplos
first_name = 'Corey'
last_name = 'Schafer'

# ------------------------------------------------------------------------------
# EJEMPLO 1: Formato Básico
# ------------------------------------------------------------------------------
# Los F-Strings son una forma nueva e intuitiva de formatear cadenas, preferida
# sobre métodos más antiguos como el método .format().
# Se usa una 'f' al inicio de la cadena (formatted string) para indicarle a Python
# que es un F-String.
# Las variables se incluyen directamente dentro de las llaves {}.
sentence_basic = f'My name is {first_name} {last_name}'
# print(sentence_basic)


# ------------------------------------------------------------------------------
# EJEMPLO 2: Ejecutar Funciones y Métodos
# ------------------------------------------------------------------------------
# Se pueden ejecutar funciones o métodos de Python (como .upper())
# directamente dentro de los marcadores de posición del F-String ({}).
sentence_methods = f'My name is {first_name.upper()} {last_name.upper()}'
# print(sentence_methods)


# ------------------------------------------------------------------------------
# EJEMPLO 3: Acceso a Valores de Diccionarios y Manejo de Comillas
# ------------------------------------------------------------------------------
# Configuración inicial de un diccionario
person = {'name': 'Jen', 'age': 23}

# ADVERTENCIA: Al acceder a claves de diccionario que usan comillas simples
# (ej., person['name']), si la F-String se abre también con comillas simples,
# esto causará un error de sintaxis al terminar la cadena prematuramente.
# La solución es usar comillas dobles (") para abrir y cerrar la F-String,
# permitiendo usar comillas simples (') dentro de las llaves para acceder a la clave.
sentence_dict = f"My name is {person['name']} and I am {person['age']} years old"
# print(sentence_dict)


# ------------------------------------------------------------------------------
# EJEMPLO 4: Realizar Cálculos
# ------------------------------------------------------------------------------
# Se pueden realizar cálculos matemáticos directamente dentro de los marcadores
# de posición ({}) del F-String.
calculation = f'4 times 11 is equal to {4 * 11}'
# print(calculation)


# ------------------------------------------------------------------------------
# EJEMPLO 5: Formato Avanzado - Relleno de Ceros (Zero Padding)
# ------------------------------------------------------------------------------
# El relleno de ceros puede ser importante al agregar datos a una base de datos
# o cuando se espera una longitud específica.
# Se especifica formato adicional usando un colon (:) después del valor.
# Para rellenar con ceros hasta N dígitos (ej. 2 dígitos), se usa la sintaxis :0N.
for n in range(1, 11):
    zero_padded = f'The value is {n:02}'
    # print(zero_padded)

# Si se cambia a 4 dígitos, se usa :04.
# print("\nEjemplo con 4 dígitos:")
for n in range(1, 11):
    zero_padded_4 = f'The value is {n:04}'
    # print(zero_padded_4)


# ------------------------------------------------------------------------------
# EJEMPLO 6: Precisión de Punto Flotante
# ------------------------------------------------------------------------------
# Configuración inicial de un valor de punto flotante
pi = 3.14159265

# Para limitar la precisión de un número flotante, se utiliza el colon (:)
# para formato adicional.
# La sintaxis es :.Nf, donde N es la cantidad de dígitos de precisión decimal.
# El F-String realiza el redondeo correcto, no solo la truncación.
pi_formatted = f'Pi is equal to {pi:.4f}'
# print(pi_formatted)

# Cambiando la precisión a 5 dígitos
pi_formatted_5 = f'Pi is equal to {pi:.5f}'
# print(pi_formatted_5)


# ------------------------------------------------------------------------------
# EJEMPLO 7: Formato de Fechas (datetime)
# ------------------------------------------------------------------------------
# Este tipo de formato se usa frecuentemente ya que la visualización de fechas varía mucho.
from datetime import datetime

# Creación de un objeto datetime (1 de enero de 1990).
birthday = datetime(1990, 1, 1)

# Para formatear, se usa el colon (:) seguido de los códigos de formato datetime.
# Los códigos deben consultarse en la documentación de Python.
# Códigos utilizados:
# %B: Nombre completo del mes (ej. January).
# %d: Día.
# %Y: Año de cuatro dígitos (mayúscula Y).
date_formatted = f'Jen has a birthday on {birthday:%B %d, %Y}'
# print(date_formatted)
```