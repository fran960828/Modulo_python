'''Escribe un programa que pida al usuario un número entero 
y muestre por pantalla una estructura como la de más abajo, 
donde el valor de entrada es el número de estrellas en el 
centro de la estructura.
*
** 
*** 
**** 
***** 
**** 
*** 
**
*

'''

# --- pedir al usuario un numero entero
num = int(input("Introduzca la anchura central (numero entero): "))
#num = 5
# --- bucle ascendente
for i in range(1, num + 1):
    print("*" * i + " " * (num - i))
# --- bucle descendente
for i in range(num-1,0,-1):
    print("*" * i + " " * (num - i))

    
