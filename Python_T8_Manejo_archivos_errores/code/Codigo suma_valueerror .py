# Bucle infinito-break
while True:

    # Comprobamos que los numeros son enteros
    try:
        # pedimos los numeros por pantalla
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))

        # realizamos la suma
        result = num1 + num2
        # indicamos por pantalla el resultado
        print("La suma de los números es:", result)
        # una vez realizada la suma correctamente 
        # interrumpimos el programa
        break

    # Si no son numeros enteros manejamos el error
    except ValueError:
        # imprimimos el mensaje de error personalizado
        print("Error: Por favor, ingrese solo numeros enteros")
