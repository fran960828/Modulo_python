El siguiente documento presenta el contenido del video, explicando cada uno de los ejemplos de expresiones regulares (RegEx) utilizando comentarios en español dentro de un archivo Python ejecutable. Las explicaciones se basan en la información proporcionada en las fuentes.

Las expresiones regulares se utilizan para buscar y hacer coincidir patrones específicos de texto. Para usarlas en Python, se requiere importar el módulo `re`. Se utiliza la notación de cadena cruda (`r'patrón'`) para evitar que Python interprete las barras invertidas de forma especial, permitiendo que las expresiones regulares las manejen directamente.

```python
# python_regex_documentation.py
import re

# Definición del texto a buscar (cadena multilinea)
text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coruyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

start sentence end
"""

# Una cadena más corta utilizada para los ejemplos de anclas (^) y ($)
sentence = 'start sentence end'

# ----------------------------------------------------------------------------------------------------------------------
# FUNCIONES DE AYUDA
# ----------------------------------------------------------------------------------------------------------------------

# Usamos re.compile() para definir el patrón y poder reutilizarlo fácilmente
# Usamos pattern.finditer() para obtener un iterador de todos los objetos 'match'
# Estos objetos 'match' muestran el 'span' (índice de inicio y fin) y la coincidencia
def find_matches(pattern_compiled, text):
    """Ejecuta la búsqueda e imprime los objetos match encontrados."""
    matches = pattern_compiled.finditer(text)
    # Mostramos el patrón compilado para referencia
    print(f"\n--- Patrón: '{pattern_compiled.pattern}' ---")
    for match in matches:
        print(match)

# ----------------------------------------------------------------------------------------------------------------------
# 1. COINCIDENCIA DE CARACTERES LITERALES
# ----------------------------------------------------------------------------------------------------------------------

# Búsqueda literal de "ABC". La búsqueda es sensible a mayúsculas y minúsculas (case sensitive).
# El patrón busca la secuencia exacta "ABC".
pattern_literal = re.compile(r'ABC')
# find_matches(pattern_literal, text_to_search)

# ----------------------------------------------------------------------------------------------------------------------
# 2. ESCAPANDO METACARACTERES
# ----------------------------------------------------------------------------------------------------------------------

# El punto '.' es un metacarácter especial que coincide con cualquier carácter, excepto un salto de línea.
# Para buscar un punto literal (como en una URL), debe ser escapado con una barra invertida (\.).
pattern_escaped_dot = re.compile(r'coruyms\.com')
# find_matches(pattern_escaped_dot, text_to_search)

# ----------------------------------------------------------------------------------------------------------------------
# 3. SECUENCIAS ESPECIALES (METACARACTERES)
# ----------------------------------------------------------------------------------------------------------------------

# .: Coincide con cualquier carácter, excepto un salto de línea.
pattern_dot_any = re.compile(r'.')
# find_matches(pattern_dot_any, text_to_search)

# \d: Coincide con cualquier dígito (0-9).
pattern_digit = re.compile(r'\d')
# find_matches(pattern_digit, text_to_search)

# \D: Coincide con cualquier carácter que NO sea un dígito (la mayúscula niega la minúscula).
pattern_not_digit = re.compile(r'\D')
# find_matches(pattern_not_digit, text_to_search)

# \w: Coincide con un carácter de palabra: [a-zA-Z0-9_] (letras, dígitos o guion bajo).
pattern_word_char = re.compile(r'\w')
# find_matches(pattern_word_char, text_to_search)

# \W: Coincide con cualquier carácter que NO sea de palabra (opuesto a \w).
pattern_not_word_char = re.compile(r'\W')
# find_matches(pattern_not_word_char, text_to_search)

# \s: Coincide con cualquier carácter de espacio en blanco (espacios, tabulaciones y saltos de línea).
pattern_whitespace = re.compile(r'\s')
# find_matches(pattern_whitespace, text_to_search)

# \S: Coincide con cualquier carácter que NO sea de espacio en blanco.
pattern_not_whitespace = re.compile(r'\S')
# find_matches(pattern_not_whitespace, text_to_search)

# ----------------------------------------------------------------------------------------------------------------------
# 4. ANCLAS (ANCHORS)
# ----------------------------------------------------------------------------------------------------------------------
# Los anclas coinciden con posiciones invisibles, no con caracteres.

# \b: Límite de palabra (Word Boundary). La posición debe estar precedida o seguida por un carácter no alfanumérico o espacio.
# Ejemplo de búsqueda de 'ha' solo si tiene un límite de palabra antes (e.g., al inicio de línea o después de un espacio).
pattern_word_boundary = re.compile(r'\bha')
# find_matches(pattern_word_boundary, text_to_search)

# \B: No es un límite de palabra (Non-Word Boundary).
# Coincide con 'ha' solo si NO tiene un límite de palabra antes (e.g., está en medio de una palabra).
pattern_not_word_boundary = re.compile(r'\Bha')
# find_matches(pattern_not_word_boundary, text_to_search)

# ^: Coincide con la posición del COMIENZO de la cadena.
# Busca la palabra literal 'start' solo si está al inicio de la cadena 'sentence'.
pattern_start = re.compile(r'^start')
# find_matches(pattern_start, sentence)

# $: Coincide con la posición del FINAL de la cadena.
# Busca la palabra literal 'end' solo si está al final de la cadena 'sentence'.
pattern_end = re.compile(r'end$')
# find_matches(pattern_end, sentence)

# ----------------------------------------------------------------------------------------------------------------------
# 5. APLICACIÓN PRÁCTICA: NÚMEROS DE TELÉFONO (Usando '.' temporalmente)
# ----------------------------------------------------------------------------------------------------------------------

# Patrón: 3 dígitos, cualquier carácter, 3 dígitos, cualquier carácter, 4 dígitos.
# Utiliza el metacarácter '.' para coincidir con cualquier separador (- o .).
pattern_phone_simple = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# find_matches(pattern_phone_simple, text_to_search) # Esto coincide con * como separador también

# ----------------------------------------------------------------------------------------------------------------------
# 6. CONJUNTOS DE CARACTERES (CHARACTER SETS)
# ----------------------------------------------------------------------------------------------------------------------

# Los corchetes '[]' coinciden con CUALQUIER carácter dentro del conjunto, pero solo una vez.
# Ejemplo: Solo permitir el guion (-) o el punto (.) como separador.
# Nota: Dentro de los [] no es necesario escapar el punto '.'.
pattern_phone_set = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# find_matches(pattern_phone_set, text_to_search)

# Rangos de valores: El guion '-' dentro de un set define un rango (e.g.,).
# Ejemplo: Coincidir solo números que comiencen con 800 o 900.
pattern_phone_800_900 = re.compile(r'00[-.]\d\d\d[-.]\d\d\d\d')
# find_matches(pattern_phone_800_900, text_to_search)

# Ejemplo de rangos para letras (a-z) y (A-Z).
pattern_range_letters = re.compile(r'[a-zA-Z]')
# find_matches(pattern_range_letters, text_to_search)

# Negación: El acento circunflejo '^' al inicio de un set niega el conjunto.
# Coincide con todo lo que NO esté en el conjunto.
# Ejemplo: Busca tres caracteres que terminan en 'at', donde el primer carácter NO es 'b'.
# text_words = 'cat mat pat bat'
# pattern_negation_word = re.compile(r'[^b]at')
# find_matches(pattern_negation_word, text_words)

# ----------------------------------------------------------------------------------------------------------------------
# 7. CUANTIFICADORES (QUANTIFIERS)
# ----------------------------------------------------------------------------------------------------------------------

# {} : Coincidencia de cantidad exacta. {n} coincide exactamente n veces.
# Simplificando el patrón del teléfono (3, 3, 4 dígitos).
pattern_phone_quantifier = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
# find_matches(pattern_phone_quantifier, text_to_search)

# Cuantificadores adicionales:
# +: Uno o más.
# *: Cero o más.
# ?: Cero o uno (hace el elemento opcional).

# ----------------------------------------------------------------------------------------------------------------------
# 8. APLICACIÓN PRÁCTICA: PREFIJOS Y NOMBRES (Usando '?')
# ----------------------------------------------------------------------------------------------------------------------

# Patrón para coincidir prefijos 'Mr.' con o sin el punto (opcional).
# La secuencia '\.?' hace que el punto sea opcional (cero o una coincidencia).
# El patrón busca: Mr, punto opcional, espacio, una letra mayúscula [A-Z], y cero o más caracteres de palabra (\w*).
pattern_prefix_mr = re.compile(r'Mr\.?\s[A-Z]\w*')
# find_matches(pattern_prefix_mr, text_to_search)

# ----------------------------------------------------------------------------------------------------------------------
# 9. AGRUPAMIENTOS (GROUPS)
# ----------------------------------------------------------------------------------------------------------------------

# Los paréntesis '()' crean un grupo que puede tratarse como una unidad.
# El operador 'OR' (|) permite coincidir con diferentes patrones dentro de un grupo.
# Ejemplo: Coincidir prefijos (Mr, Ms, Mrs) seguido de un punto opcional.
pattern_prefix_group = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# find_matches(pattern_prefix_group, text_to_search)

# ----------------------------------------------------------------------------------------------------------------------
# 10. CAPTURA DE GRUPOS Y SUSTITUCIÓN (.sub)
# ----------------------------------------------------------------------------------------------------------------------

# URLs de ejemplo
urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# Patrón complejo para URLs, utilizando grupos de captura para extraer partes:
# Grupo 1: (https?://)? -> Protocolo opcional (http o https, 's' es opcional debido a '?').
# Grupo 2: (www\.)? -> 'www.' opcional.
# Grupo 3: (\w+) -> Nombre de dominio (uno o más caracteres de palabra).
# Grupo 4: (\.\w+) -> TLD (.com, .gov, etc.).
pattern_url_capture = re.compile(r'(https?://)?(www\.)?(\w+)(\.\w+)')

# 10.1. Impresión de Grupos Específicos
# find_matches(pattern_url_capture, urls) # Muestra el objeto match que permite acceder a los grupos.

# El método .group(index) en el objeto match permite acceder a los grupos capturados:
# Grupo 0: La coincidencia completa.
# Grupo 1, 2, 3, ...: Los grupos definidos por paréntesis.
# Si se quisiera imprimir solo el Dominio (Grupo 3):
# for match in pattern_url_capture.finditer(urls):
#     print(match.group(3)) # Imprime Google, coreyms, youtube, nasa

# 10.2. Sustitución
# El método .sub() se usa para sustituir las coincidencias con un nuevo texto.
# Se utilizan referencias inversas (\1, \2, \3, ...) para referenciar el contenido de los grupos capturados.
# Queremos sustituir la URL completa por solo el Dominio (\3) y el TLD (\4).
subbed_urls = pattern_url_capture.sub(r'\3\4', urls)

# print("\n--- Sustitución de URLs (Dominio.TLD) ---")
# print(subbed_urls) # Se obtiene una nueva cadena con las sustituciones realizadas.

# ----------------------------------------------------------------------------------------------------------------------
# 11. BANDERAS (FLAGS)
# ----------------------------------------------------------------------------------------------------------------------

# Las banderas modifican la forma en que el patrón encuentra coincidencias.
# re.IGNORECASE (o re.I): Ignora mayúsculas y minúsculas durante la búsqueda.
# Ejemplo: Buscar 'start' independientemente de la capitalización.
pattern_ignore_case = re.compile(r'start', re.IGNORECASE)
# find_matches(pattern_ignore_case, sentence)

# Otras banderas notables son: re.MULTILINE (para que ^ y $ coincidan con el inicio/fin de CADA línea) y re.VERBOSE (para añadir comentarios al patrón).


# ----------------------------------------------------------------------------------------------------------------------
# NOTA SOBRE OTROS MÉTODOS DE RE:
# ----------------------------------------------------------------------------------------------------------------------
# findall: Devuelve todas las coincidencias como una lista de cadenas (o lista de tuplas si hay grupos).
# match: Determina si la expresión regular coincide al COMIENZO de la cadena. Devuelve el objeto match o None.
# search: Busca la primera ubicación donde la RegEx produce una coincidencia en CUALQUIER PARTE de la cadena. Devuelve el objeto match o None.

# Ejemplo de uso de re.match (solo al inicio de la cadena 'sentence'):
# result_match = re.match(r'start', sentence)
# print(f"\nResultado re.match('start', sentence): {result_match}")
# result_match_fail = re.match(r'sentence', sentence)
# print(f"Resultado re.match('sentence', sentence): {result_match_fail}") # Devuelve None

# Ejemplo de uso de re.search (en toda la cadena 'sentence'):
# result_search = re.search(r'sentence', sentence)
# print(f"Resultado re.search('sentence', sentence): {result_search}")

