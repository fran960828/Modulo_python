# --- Pedir NUMEROS al usuario
a = float(input("Introduce un numero: "))
b = float(input("Introduce otro numero: "))
c = float(input("Introduce otro numero: "))
d = float(input("Introduce otro numero: "))


# --- Imprimir el mayor de los cuatro numeros
if (a>b):
    a, b = b, a 

if (b>c):
    b, c = c, b

if (c>d):
    c, d = d, c

print(" El mayor de los 4 es ", d)
print("El orden de los numeros es: ", a, b, c, d)