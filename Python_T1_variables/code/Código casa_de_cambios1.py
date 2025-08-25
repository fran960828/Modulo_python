# --- Pedir al usuario que ingrese la cantidad en euros ---
euros = input("Ingresa la cantidad de euros que deseas convertir: ") # tipo string

# --- Convertimos la cantidad ingresada a un float ---
euros = float(euros)

# --- Convertir la cantidad de euros a dolares ---
dolares = euros * 1.2

# --- Imprimir el resultado de la conversión ---
print(euros, "euros son", dolares, "dólares")
