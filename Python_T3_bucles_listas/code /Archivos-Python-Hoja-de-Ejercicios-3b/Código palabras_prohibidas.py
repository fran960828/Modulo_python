''' 
Define una lista de 5 palabras aleatorias 
y una lista de letras prohibidas que contenga 
tres letras. Filtra las palabras en tu lista original
 crea una nueva lista de palabras filtradas que 
 solo contenga aquellas palabras que no tienen ninguna letra prohibida.

'''

# --- Crear lista de palabras aleatorias y otras de letras prohibidas
# --- + lista de palabras filtradas

palabras_aleatorias = ["casa", "perro", "gato", "libro", "ratón"]
letras_prohibidas = ["a", "u"]
# inicializamos una lista vacia donde
# añadiremos las palabras filtradas
lista_filtrada = []

# --- Bucle para recorrer la lista de palabras
for palabra in palabras_aleatorias:
    # en principio incluiremos la palabra a no ser que
    # se compruebe que contiene una letra prohibida
    incluir = True
    # Bucle para comprobar si los objetos tiene alguna letra prohibida.
    for letras_prohibida in letras_prohibidas:
        ## si tiene letra prohibida no lo incluimos en la lista filtrada
        if letras_prohibida in palabra:
            incluir = False
    
    # comprobamos si debemos incluir la palabra. En caso de
    # que no tenga letras prohibidas (incluir = True) la incluimos
    if incluir:
        lista_filtrada.append(palabra)

# --- Imprimimos por pantalla las tres listas.
print("Lista original:", palabras_aleatorias)
print("Letras prohibidas:", letras_prohibidas)
print("Lista filtrada:", lista_filtrada)