# --- Pedimos un numero al usuario ---
numero = input("Por favor, introduce un número de cuatro cifras ") #string


print(numero[::-1])

# --- Creamos el strig inverso ---
numero_inverso = numero[3] + numero[2] + numero[1] + numero[0]

# --- imprimos el resultado por pantalla
print(numero_inverso)

