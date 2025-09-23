ventas_diarias = {}

continuar = True

while continuar:
    opcion = input("1. Registrar venta\n2. Actualizar cantidad vendida\n3. Calcular total de ventas\n4. Salir\nElige una opción: ")

    # Registrar ventas
    if opcion == "1":
        # Ingresar producto y cantidad vendida
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad vendida: "))
        # Si el prodcuto ya esta registrado
        if producto in ventas_diarias:
            # Sumamos la cantidad vendida a las cantidades anteriores
            ventas_diarias[producto] += cantidad
        # Si el prodcuto no esta registrado añadimos el producto 
        # el prodcuto y la cantidad vendida
        else:
            ventas_diarias[producto] = cantidad

    # Actualizar la cantidad vendida
    elif opcion == "2":
        # Ingresar producto
        producto = input("Ingrese el nombre del producto a actualizar: ")
        # Comprobamos que el producto existe en nuestro registro
        if producto in ventas_diarias:
            # Pedimos la cantidad vendida de ese producto
            nueva_cantidad = int(input("Ingrese la nueva cantidad vendida: "))
            # Actualizamos la cantidad total de unidades vendidas
            ventas_diarias[producto] = nueva_cantidad
        # En el caso de que el producto no exista en la base de datos lo indicamos
        else:
            print("El producto no existe en las ventas diarias.")

    # Calcular el total de las ventas
    elif opcion == "3":
        total = 0
        # recorremos los valores del diccionario
        for cantidad in ventas_diarias.values():
            # los sumamos al valor total de ventas
            total += cantidad
        # imprimimos el valor total de las ventas
        print("El total de ventas diarias es:", total)

    # Salir del programa
    elif opcion == "4":
        print("Saliendo del programa...")
        continuar = False

    # Si el numero introducido no es 1,2,3,4 pedimos que se elija
    # una opcion valida
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
