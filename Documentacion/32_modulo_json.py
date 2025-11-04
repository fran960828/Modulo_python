```python
# ==============================================================================
# INTRODUCCIÓN Y CONVERSIÓN DE CADENA JSON A OBJETO PYTHON (json.loads)
# ==============================================================================

# Para trabajar con datos JSON en Python, primero necesitamos importar el módulo `json`.
# Este módulo viene incluido en la librería estándar de Python, por lo que no necesitas
# instalar nada adicional.

import json #

# JSON (JavaScript Object Notation) es un formato de datos muy común para almacenar información.
# Es utilizado a menudo al obtener datos de APIs en línea o para archivos de configuración.
# A primera vista, los datos JSON se parecen mucho a un diccionario de Python.

# Definimos una cadena de texto que contiene datos JSON válidos.
# Observa que `emails` en el segundo objeto es `null`, y `has license` es `true` o `false`.
# JSON Objects se convierten a diccionarios de Python.
# JSON Arrays se convierten a listas de Python.
# JSON `true`, `false`, `null` se convierten a Python `True`, `False`, `None`.

json_string = """
{
    "people": [
        {
            "name": "John Doe",
            "phone": "555-555-5555",
            "emails": ["john.doe@example.com", "jd@work.com"],
            "has license": true
        },
        {
            "name": "Jane Smith",
            "phone": "555-555-1111",
            "emails": null,
            "has license": false
        }
    ]
}
""" # Simulando la estructura JSON descrita en y

# Para cargar esta cadena JSON en un objeto de Python (para poder trabajar con ella fácilmente),
# usamos el método `json.loads()` (Load String).

print("# 1. Convirtiendo la cadena JSON a objeto Python (json.loads)")
data = json.loads(json_string) #

# Si imprimimos la variable `data`, veremos que ahora se comporta como un objeto Python (un diccionario).
# Observa cómo los valores booleanos (true/false) y nulos (null) se han convertido
# a mayúsculas o `None` de Python (True, False, None).

print(data)

# Podemos verificar el tipo de dato. Debería ser un diccionario de Python, ya que la estructura
# de nivel superior en nuestro JSON es un objeto.

print(f"El tipo de 'data' después de la conversión es: {type(data)}") #

# ==============================================================================
# ACCESO A DATOS Y BUCLES
# ==============================================================================

# El diccionario `data` contiene una clave principal llamada "people".
# El valor asociado a "people" en el JSON es un array (lista de Python) de objetos (diccionarios de Python).

# Accedemos a la clave 'people' y verificamos que es una lista.
print("\n# 2. Accediendo a la lista de personas")
people_list = data['people']
print(f"El tipo de data['people'] es: {type(people_list)}") # Debería ser <class 'list'>

# Ahora que tenemos una lista de objetos Python, podemos iterar sobre ella.
# En el bucle, cada 'person' es un diccionario.

print("\n# 3. Iterando y extrayendo el nombre de cada persona")
for person in data['people']: #
    # Imprimimos el diccionario completo de la persona.
    print(f"Diccionario de la persona: {person}")

    # Accedemos a una clave específica dentro del diccionario de la persona, por ejemplo, 'name'.
    name = person['name']
    print(f"Nombre: {name}") #

# ==============================================================================
# MODIFICACIÓN Y CONVERSIÓN DE OBJETO PYTHON A CADENA JSON (json.dumps)
# ==============================================================================

# Queremos modificar nuestro objeto Python (data) y luego convertirlo de nuevo a una cadena JSON.
# Digamos que queremos eliminar los números de teléfono de cada persona.

print("\n# 4. Eliminando claves y convirtiendo de nuevo a cadena JSON (json.dumps)")

# Iteramos de nuevo y usamos `del` para borrar la clave 'phone' de cada diccionario de persona.
for person in data['people']:
    del person['phone'] #

# Usamos `json.dumps()` (Dump String) para convertir el objeto Python modificado (`data`)
# de nuevo a una cadena JSON.

new_json_string = json.dumps(data) #
print("Cadena JSON sin formato:")
print(new_json_string) # Muestra el JSON comprimido en una sola línea

# ==============================================================================
# FORMATO Y ORDENACIÓN DE LA SALIDA JSON
# ==============================================================================

# La cadena JSON generada arriba es difícil de leer. Podemos formatearla para que sea legible
# pasando el argumento `indent` (indentación) a `json.dumps()`.

print("\n# 5. Formateando la salida JSON con indentación")

# `indent=2` agrega dos espacios por nivel de anidamiento.
formatted_json_string = json.dumps(data, indent=2) #
print(formatted_json_string) # Mucho más fácil de leer

# También podemos ordenar las claves alfabéticamente en la salida JSON usando
# el argumento `sort_keys=True`.

print("\n# 6. Ordenando las claves alfabéticamente")
sorted_json_string = json.dumps(data, indent=2, sort_keys=True) #
print(sorted_json_string) # Ahora 'emails' va antes que 'has license' y 'name'

# ==============================================================================
# TRABAJO CON ARCHIVOS (json.load y json.dump)
# ==============================================================================

# Si queremos cargar JSON desde un archivo (no una cadena), usamos `json.load()`.
# Si queremos escribir un objeto Python en un archivo JSON, usamos `json.dump()`.

# NOTA: Los siguientes ejemplos simulan la estructura de archivos.
# En un entorno real, necesitarías tener un archivo llamado 'states.json' y 'new_states.json'
# en el mismo directorio.

# Ejemplo de Carga de Archivo (json.load)
# Usamos `with open(...)` para asegurarnos de que el archivo se cierre correctamente.

# print("\n# 7. Cargando datos de un archivo (json.load) - Estructura conceptual")
# # Suponiendo que existe 'states.json' en modo lectura ('r')
# try:
#     with open('states.json', 'r') as f: #
#         # data_from_file = json.load(f) # json.load() toma el objeto archivo
#         # Ahora podríamos iterar sobre data_from_file, por ejemplo, data_from_file['states'].
#         pass
# except FileNotFoundError:
#     print("# Comentario: No se puede ejecutar ya que el archivo 'states.json' no se proporcionó, pero así se usa json.load().")


# Ejemplo de Escritura a Archivo (json.dump)
# Usamos el objeto Python modificado (`data`) para escribir en un nuevo archivo.

# print("\n# 8. Escribiendo datos a un archivo (json.dump) - Estructura conceptual")
# # Abrimos un nuevo archivo ('new_states.json') en modo escritura ('w').
# try:
#     with open('new_states.json', 'w') as f: #
#         # json.dump toma (1) el objeto a escribir y (2) el objeto archivo.
#         # También podemos agregar indentación para que el archivo sea legible.
#         # json.dump(data, f, indent=2) #
#         pass
# except Exception as e:
#      print("# Comentario: No se puede ejecutar la escritura completa sin configurar un archivo, pero así se usa json.dump() con indentación.")


# ==============================================================================
# RESUMEN
# ==============================================================================

# Recuerda:
# 1. De Cadena a Python: `json.loads(cadena)`.
# 2. De Archivo a Python: `json.load(objeto_archivo)`.
# 3. De Python a Cadena: `json.dumps(objeto)` (Útil para depuración o APIs).
# 4. De Python a Archivo: `json.dump(objeto, objeto_archivo)`.

# Trabajar con JSON es como ser un traductor: el módulo `json` toma un idioma estructurado (JSON)
# y lo convierte a un idioma con el que Python se siente cómodo (diccionarios y listas),
# y viceversa. Los métodos `loads`/`load` son para "entrar" a Python, y `dumps`/`dump` son para "salir" a JSON.
