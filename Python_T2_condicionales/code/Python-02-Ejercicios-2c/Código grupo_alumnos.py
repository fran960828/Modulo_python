# --- Pedir por pantalla los datos
#chico/chica
genero = input("Ingresa tu genero (chica/chico): ")
#nombre
nombre = input("Ingresa tu nombre: ")
nombres_chicas_A = "EHIJKLM"
nombres_chicos_A = "ABCDEFGHRSTUVWXYZ"

# --- Elegir grupo que corresponde
# chica
if genero.lower() == "chica":
    ## E hasta M --> grupo A
    if nombre[0].upper() in nombres_chicas_A:
        print("Tu grupo es el A")
    ## el resto --> grupo B
    else:
        print("Tu grupo es el B")

# chico
elif genero.lower() == "chico":
    ## A hasta H, R hasta Z --> grupo A
    if nombre[0].upper() in nombres_chicos_A:
        print("Tu grupo es el A")
    ## el resto --> grupo B
    else: 
        print("tu grupo es el B")

else:
    print("ERROR: Vuelva a inicializar el programa e introduzca un genero válido")
