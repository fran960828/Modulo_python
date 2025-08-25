# --- Pedir al usuario que ingrese el número de trajeta
num_tarjeta = input("Ingresa tu número de tarjeta ")

# --- Determinar la longitud del numero de la tarjeta de credito
longitud = len(num_tarjeta)

print("*" * (longitud-4) + num_tarjeta[longitud-4:longitud])
