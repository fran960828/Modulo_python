# --- Pedir un numero al usuario
numero = input("Introduzca un numero: ") # es un string
numero = int(numero) # esto es un entero

# --- Comprobar si el numero es par o impar
# si es un multiplo de 2 sera par
if numero % 2 == 0:
    print("El numero", numero, "es par")
# si no será impar
else:
    print("El numero", numero, "es impar")