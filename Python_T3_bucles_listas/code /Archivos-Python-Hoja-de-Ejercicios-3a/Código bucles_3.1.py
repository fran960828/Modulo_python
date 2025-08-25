'''
Crea un script que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última.
'''
# --- pedir palabra al usuario
palabra = input("Ingrese una palabra: ")
longitud = len(palabra)

# --- bucle que recorra el string de atras en adelante
for i in range(longitud - 1, -1, -1):
    # imprimir cada letra
    print(palabra[i])
