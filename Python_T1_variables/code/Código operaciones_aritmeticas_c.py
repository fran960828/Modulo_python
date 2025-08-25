# Pedir al usuario dos números entreos
num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))

# Calcular el cociente y el resto 
cociente = num1 // num2
resto = num1 % num2

# Mostrar por pantalla numeros de entrada, cociente y resto
print("Los números de entrada son ", num1, "y", num2)
print("El cociente es ", cociente)
print("El resto es ", resto)