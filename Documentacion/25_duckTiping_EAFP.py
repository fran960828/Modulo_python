'''
## Introducción: Conceptos Pythonic: Duck Typing y EAFP

El término **"Pythonic"** se refiere a seguir las convenciones y estilos de codificación del lenguaje Python para escribir código que sea limpio y legible. Dos aspectos fundamentales de ser Pythonic son el *duck typing* y la filosofía **EAFP** (Easier to Ask Forgiveness Than Permission, o Es más fácil pedir perdón que permiso). Estos dos conceptos están estrechamente relacionados.

### 1. Duck Typing (Tipado Pato)

El *duck typing* se basa en la asunción de que si un objeto camina como un pato y grazna como un pato, entonces es un pato.

**Concepto Clave:**
En Python, con el *duck typing*, no nos importa el tipo específico del objeto con el que estamos trabajando; **solo nos importa si el objeto puede hacer lo que le pedimos que haga** (es decir, si tiene los métodos o atributos necesarios). Esto significa que, si una clase `Persona` tiene un método `quack` y `fly`, se comportará como un pato dentro de una función que requiera esos métodos, incluso si no es una instancia de la clase `Duck`.

**Ventajas:**
*   Promueve un código más flexible y menos acoplado, ya que no se realizan comprobaciones estrictas de herencia o tipo.

**Inconvenientes y Cuándo No Usarlo:**
*   Si se pasa cualquier objeto que no tenga los métodos requeridos, potencialmente lanzará un error (`AttributeError`). Esto lleva a la necesidad de utilizar EAFP para manejar elegantemente estos errores.

**Contraste (Estilo No Pythonic):**
El estilo no Pythonic, en este contexto, implicaría comprobar específicamente si el objeto es una instancia de una clase concreta (por ejemplo, `if isinstance(thing, Duck)`) antes de llamar a sus métodos. Esto restringe la funcionalidad, ya que un objeto de otro tipo que podría realizar la misma acción quedaría excluido.

### 2. Filosofía EAFP (Easier to Ask Forgiveness Than Permission)

EAFP es un concepto Pythonic que prioriza la acción sobre la verificación. En lugar de comprobar si se tiene permiso para realizar una acción, simplemente se intenta realizarla, y si falla, se maneja la excepción.

**Concepto Clave:**
**"Intenta hacer algo, y si no funciona, entonces lo manejaremos"**. Esto se implementa utilizando bloques `try...except`. Se intenta ejecutar el código y, si se produce un error esperado (como `AttributeError`, `KeyError`, o `IndexError`), se captura y se maneja.

**Contraste (Estilo No Pythonic: Look Before You Leap - LBYL):**
El estilo "Look Before You Leap" (LBYL, o Mira antes de saltar) es la forma no Pythonic de abordar esto. Requiere pedir permiso en cada paso. Por ejemplo, en lugar de acceder directamente a un atributo, se comprobaría primero si el atributo existe (`hasattr`) y si es invocable (`callable`). Este método se considera engorroso (cumbersome) y menos legible que EAFP.

**Ventajas de EAFP:**
1.  **Legibilidad:** A menudo, el código EAFP es más legible que el código LBYL, ya que evita múltiples comprobaciones condicionales (por ejemplo, evitar tener que verificar la existencia de múltiples claves de diccionario o atributos).
2.  **Rendimiento:** Es ligeramente más rápido en situaciones donde no se esperan muchas excepciones, porque el objeto solo necesita ser accedido una vez. El enfoque de pedir permiso requiere acceder al objeto varias veces para realizar todas las comprobaciones.
3.  **Evitar Condiciones de Carrera (Race Conditions):** El enfoque EAFP es crucial para evitar condiciones de carrera, especialmente al trabajar con archivos. Si se comprueba si un archivo es accesible, y luego se intenta abrirlo, el estado de accesibilidad podría cambiar en ese breve lapso de tiempo, provocando un error sin manejar.

**Inconvenientes y Cuándo No Usarlo:**
*   EAFP no es un enfoque universal (an end all be-all approach). Hay situaciones donde podría ser necesario realizar ciertas comprobaciones específicas antes de la acción.
*   Si se espera que una acción falle muy a menudo, el costo de generar y manejar la excepción puede superar la ventaja de rendimiento (aunque el video se centra en los beneficios de EAFP en casos comunes).

---

## Ejemplos de Implementación de Duck Typing y EAFP

A continuación, se documentan los distintos ejemplos presentados en el video, incluyendo las comparaciones entre el enfoque no Pythonic (LBYL o verificación estricta de tipo) y el enfoque Pythonic (Duck Typing y EAFP).

### Ejemplo 1: Duck Typing (Comprobación de Tipo vs. Comprobación de Comportamiento)

#### Documentación
Este ejemplo ilustra la diferencia entre el código que exige un tipo específico (no Pythonic) y el código que solo exige el comportamiento (Duck Typing).

1.  **Definiciones:** Se definen dos clases, `Duck` y `Person`, ambas con los métodos `quack()` y `fly()`.
2.  **Función `quack_and_fly`:** Esta función intenta ejecutar los métodos `quack` y `fly` sobre un objeto pasado como argumento.
3.  **No Pythonic (LBYL/Tipo Estricto):** El código primero verifica explícitamente si el objeto es una instancia de `Duck` (`isinstance(thing, Duck)`). Si se pasa un objeto `Person` (que tiene los métodos), el código no se ejecuta, ya que la condición de tipo no se cumple, imprimiendo que "tiene que ser un pato".
4.  **Pythonic (Duck Typing):** Se eliminan las comprobaciones de tipo y se intenta simplemente ejecutar `thing.quack()` y `thing.fly()`. Dado que tanto el objeto `Duck` como el objeto `Person` tienen los métodos, ambos se ejecutan con éxito. El tipo de objeto no importa, solo su capacidad de realizar la acción.
'''

#### Código py


# EJEMPLO 1: Duck Typing (Comprobación de Tipo vs. Comprobación de Comportamiento)

# 1. Definición de Clases: Ambos tienen los métodos necesarios.
class Duck:
    def quack(self):
        print('Quack, quack')
    def fly(self):
        print('Flap, Flap!')

class Person:
    def quack(self):
        print("I'm quacking like a duck")
    def fly(self):
        print("I'm flapping my arms")

# Función de prueba que requiere los métodos 'quack' y 'fly'
def quack_and_fly(thing):
    print('\n--- Probando:', thing.__class__.__name__, '---')

    # --- INICIO: Ejemplo NO Pythonic (Comprobación Estricta de Tipo/LBYL) ---
    # Esto es NO Pythonic porque restringe la función a una sola clase, 
    # ignorando otros objetos que tienen los mismos métodos.
    
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a duck')
    # -------------------------------------------------------------------------


    # --- INICIO: Ejemplo Pythonic (Duck Typing) ---
    # No verificamos el tipo, solo intentamos ejecutar los métodos.
    # Funciona para cualquier objeto que tenga los métodos 'quack' y 'fly'.
    thing.quack()
    thing.fly()
    print("-" * 20)

d = Duck()
p = Person()

# Ejecución con Duck Typing: Ambos objetos funcionan
quack_and_fly(d)
quack_and_fly(p)


### Ejemplo 2: EAFP vs. LBYL (Comprobación de Atributos/Métodos)
'''
#### Documentación
Este ejemplo aborda el riesgo implícito en el *duck typing*: ¿Qué pasa si el objeto pasado no tiene los métodos necesarios y lanza un error? Aquí se compara el enfoque LBYL (pedir permiso) con EAFP (pedir perdón).

1.  **No Pythonic (LBYL - Pedir Permiso):** Implica verificar la existencia de cada atributo o método (`quack`, `fly`) antes de intentar invocarlo. Esto se hace comprobando si el atributo existe (`hasattr`) y luego si es invocable (`callable`). Este proceso es engorroso y repetitivo.
2.  **Pythonic (EAFP - Pedir Perdón):** Simplemente se intenta realizar la acción (llamar a `quack()`, `fly()`). Si la acción falla porque el atributo no existe (o es invocable), se captura la excepción específica **`AttributeError`** mediante un bloque `try...except`. Esto resulta en código mucho más legible. Se demuestra que si se añade un método inexistente (`bark`), el error es capturado y manejado sin detener la ejecución.

'''
#### Código py


# EJEMPLO 2: EAFP vs. LBYL (Manejo de AttributeError)
class Duck:
    def quack(self):
        print('Quack, quack')
    def fly(self):
        print('Flap, Flap!')

class Person:
    def quack(self):
        print("I'm quacking like a duck")
    def fly(self):
        print("I'm flapping my arms")

# Objeto de prueba que no tendrá el método 'bark'
d = Duck()
p = Person()

def quack_and_fly_safe(thing, extra_method=None):
    print('\n--- Probando EAFP con:', thing.__class__.__name__, '---')
    
    # --- INICIO: Ejemplo NO Pythonic (LBYL - Look Before You Leap) ---
    # Se pide permiso en cada paso: '¿Puedes hacer esto? ¿Y esto otro?'.
    
    # if hasattr(thing, 'quack') and callable(thing.quack):
    #     thing.quack()
    
    # if hasattr(thing, 'fly') and callable(thing.fly):
    #     thing.fly()
    # --------------------------------------------------------------------

    
    # --- INICIO: Ejemplo Pythonic (EAFP) ---
    # Se intenta realizar la acción y se maneja la excepción.
    try:
        thing.quack()
        thing.fly()
        
        # Intentamos un método que no existe para forzar un error
        if extra_method:
            print(f"Intentando llamar a {extra_method}...")
            getattr(thing, extra_method)() # Esto generará AttributeError
            
    except AttributeError as e:
        # Si no se puede ejecutar el método, se captura el error de atributo.
        print(f"Error capturado (AttributeError): {e}")

quack_and_fly_safe(d)
quack_and_fly_safe(p, extra_method='bark') # Probando con método inexistente
```

### Ejemplo 3: EAFP vs. LBYL (Acceso a Claves de Diccionario)

#### Documentación
'''El concepto EAFP se extiende a otros casos de uso, como la verificación de la existencia de claves en un diccionario.

1.  **Escenario:** Se desea formatear una oración utilizando claves de un diccionario (`name`, `age`, `job`). Si faltan claves, se debe notificar.
2.  **No Pythonic (LBYL):** Requiere múltiples comprobaciones condicionales (`if 'name' in person and 'age' in person and 'job' in person`) antes de intentar acceder a las claves. Si falta alguna, no se ejecuta la sentencia.
3.  **Pythonic (EAFP):** Se intenta formatear la oración y acceder a todas las claves directamente dentro de un `try`. Si falta una clave, se lanza una **`KeyError`**, que se captura en el bloque `except` para imprimir el mensaje de que faltan claves. El código EAFP es más limpio ya que evita todas las comprobaciones previas.'''

#### Código py


# EJEMPLO 3: EAFP vs. LBYL (Manejo de KeyError en Diccionarios)

person_full = {'name': 'John', 'age': 30, 'job': 'Developer'}
person_missing = {'name': 'Jane', 'age': 25} # Falta 'job'

def check_person_keys(person):
    print('\n--- Probando claves de diccionario ---')
    
    # --- INICIO: Ejemplo NO Pythonic (LBYL) ---
    # Se pide permiso comprobando la existencia de todas las claves.
    
    # if 'name' in person and 'age' in person and 'job' in person:
    #     s = f"Name: {person['name']}, Age: {person['age']}, Job: {person['job']}"
    #     print(s)
    # else:
    #     print('Missing some keys (LBYL)')
    # --------------------------------------------------------------------


    # --- INICIO: Ejemplo Pythonic (EAFP) ---
    # Intentamos acceder a todas las claves. Si falta alguna, Key Error es capturado.
    try:
        s = f"Name: {person['name']}, Age: {person['age']}, Job: {person['job']}"
        print(s)
    except KeyError:
        # Se maneja el error específico de clave.
        print('Missing a key (EAFP)')

print("Diccionario COMPLETO:")
check_person_keys(person_full)

print("Diccionario INCOMPLETO:")
check_person_keys(person_missing)
```

### Ejemplo 4: EAFP vs. LBYL (Acceso a Índice de Lista)

#### Documentación
'''Este ejemplo demuestra cómo aplicar EAFP al acceder a índices de una lista para manejar errores de límites (`IndexError`).

1.  **Escenario:** Se necesita acceder a un índice específico de una lista (e.g., el índice 5).
2.  **No Pythonic (LBYL):** Se requiere comprobar la longitud de la lista (`len(my_list) >= 6`) para asegurarse de que el índice 5 existe antes de intentar acceder a él. Esta verificación se considera "fea" (ugly).
3.  **Pythonic (EAFP):** Simplemente se intenta acceder al índice. Si la lista es demasiado corta, se lanza una **`IndexError`**, que es capturada y manejada. Esto sigue el principio de no pedir permiso, sino intentar la acción y manejar el fallo.
'''
#### Código py

# EJEMPLO 4: EAFP vs. LBYL (Manejo de IndexError en Listas)

my_list_long = # Índice 5 existe
my_list_short =            # Índice 5 NO existe
INDEX_TO_ACCESS = 5

def access_list_index(my_list):
    print(f"\n--- Probando lista de longitud {len(my_list)} ---")

    # --- INICIO: Ejemplo NO Pythonic (LBYL) ---
    # Se pide permiso comprobando la longitud.
    
    # if len(my_list) >= (INDEX_TO_ACCESS + 1):
    #     print(f"Index {INDEX_TO_ACCESS}: {my_list[INDEX_TO_ACCESS]}")
    # else:
    #     print("That index does not exist (LBYL)")
    # --------------------------------------------------------------------
    

    # --- INICIO: Ejemplo Pythonic (EAFP) ---
    # Intentamos acceder directamente. Si falla, el IndexError es capturado.
    try:
        print(f"Index {INDEX_TO_ACCESS}: {my_list[INDEX_TO_ACCESS]}")
    except IndexError:
        # Manejamos el error si el índice está fuera de los límites.
        print("That index does not exist (EAFP)")

print("Lista Larga:")
access_list_index(my_list_long)

print("Lista Corta:")
access_list_index(my_list_short)
```

### Ejemplo 5: EAFP (Evitar Condiciones de Carrera - Acceso a Archivos)

#### Documentación
'''Este ejemplo es crucial para demostrar una ventaja mayor de EAFP: **evitar condiciones de carrera**.

1.  **Escenario:** Intentar abrir y leer un archivo.
2.  **Riesgo LBYL (Condición de Carrera):** Si se utiliza LBYL, se verificaría si el archivo es accesible (`os.access`). El problema es que el estado del archivo (si es accesible o si existe) podría cambiar en el breve momento entre la comprobación y el intento real de abrir el archivo (`open()`). Esto podría resultar en un error no capturado, ya que el código asumió que podía acceder al archivo.
3.  **Pythonic (EAFP):** Simplemente se intenta abrir el archivo directamente. Si hay un problema de acceso, permisos o existencia, se lanza una excepción como **`IOError`** (o sus subclases), que se captura y maneja de manera segura. Se continúa el tema: se intenta hacer algo, y si no se puede, se maneja el error.

'''
#### Código py

# EJEMPLO 5: EAFP (Manejo de IOError y Evitar Race Conditions)
import os # Necesario para simular la verificación LBYL

# Nota: Dado que no podemos simular el entorno del sistema de archivos y las race conditions, 
# este código ilustra la estructura lógica.
FILE_PATH = "some_file.txt"

def read_file_safe():
    
    # --- INICIO: Ejemplo NO Pythonic (LBYL) ---
    # ESTO PRESENTA RIESGO DE CONDICIÓN DE CARRERA.
    
    # try:
    #     # 1. Chequeo de acceso: Pido permiso.
    #     if os.access(FILE_PATH, os.R_OK): 
    #         # 2. Abrir archivo: Si el estado cambia aquí, se lanza un error no capturado.
    #         f = open(FILE_PATH)
    #         contents = f.read()
    #         print(contents)
    #         f.close()
    #     else:
    #         print("File cannot be accessed (LBYL check)")
    # except FileNotFoundError:
    #     # Solo se captura si el archivo no existe, pero si el acceso es denegado entre el chequeo, falla.
    #     pass
    # --------------------------------------------------------------------


    # --- INICIO: Ejemplo Pythonic (EAFP) ---
    # Se intenta abrir directamente. Si hay un problema de acceso o el archivo desaparece, 
    # se captura el IOError de forma segura.
    try:
        # Intentamos abrir el archivo de una sola vez.
        with open(FILE_PATH) as f:
            contents = f.read()
            print(f"Contenido leído (EAFP): {contents}")
            
    except IOError:
        # Se captura el error de entrada/salida si no se pudo acceder al archivo.
        print('The file cannot be accessed (EAFP handling)')

# Para probar este ejemplo en la práctica, FILE_PATH debe ser un archivo real.
# Aquí solo se ejecutará el bloque except si el archivo no existe o no se puede acceder:
print("Simulando lectura de archivo (EAFP):")
read_file_safe() 
