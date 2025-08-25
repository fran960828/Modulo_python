'''
Crea un programa en el que se pregunte al 
usuario por una frase y una letra, y muestre 
por pantalla el número de veces que aparece 
la letra en la frase.
'''

# --- pedir frase y letra
frase = input("Introduce una frase: ")
letra = input("Ingrese una letra: ")

# --- bucle para recorrer la frase 
# --- y contar las apariciones de la letra
contador = 0
for caracter in frase:
    if caracter == letra:
        #contador = contador +1
        contador += 1

print(f"La letra aparece {contador} veces en la frase")