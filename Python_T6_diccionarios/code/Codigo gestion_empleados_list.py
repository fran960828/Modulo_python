empleados = []

continuar = True
while continuar:
    # Imprimimos las opciones al usuario
    print("1. Agregar empleado")
    print("2. Actualizar salario de empleado")
    print("3. Mostrar lista de empleados")
    print("4. Calcular promedio salarial por departamento")
    print("5. Salir")

    # Solicitamos al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    # Agregar un nuevo empleado
    if opcion == "1":
        # Agregar un nuevo empleado
        nombre = input("Ingrese el nombre del empleado: ")
        salario = float(input("Ingrese el salario del empleado: "))
        departamento = input("Ingrese el departamento del empleado: ")

        # Creamos un diccionario con la información del empleado
        empleado = {
            "nombre": nombre,
            "salario": salario,
            "departamento": departamento
        }

        # Agregamos el empleado a la lista de empleados
        empleados.append(empleado)
        print("Empleado agregado exitosamente.")

    # Actualizar el salario de un empleado existente
    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado: ")
        nuevo_salario = float(input("Ingrese el nuevo salario del empleado: "))

        # Buscamos al empleado por su nombre
        for empleado in empleados:
            if empleado["nombre"] == nombre:
                # Actualizamos el salario del empleado encontrado
                empleado["salario"] = nuevo_salario
                break
        else:
            print("Empleado no encontrado.")

    # Mostrar la lista de empleados
    elif opcion == "3":
        for empleado in empleados:
            print(f"Nombre: {empleado['nombre']}, Salario: {empleado['salario']}, Departamento: {empleado['departamento']}")

    # Calcular el promedio salarial por departamento
    elif opcion == "4":
        departamento = input("Ingrese el departamento: ")
        total_salarios = 0
        contador = 0

        # Recorremos la lista de empleados y realizamos el cálculo
        for empleado in empleados:
            if empleado["departamento"] == departamento:
                total_salarios += empleado["salario"]
                contador += 1

        # Verificamos si hay empleados en el departamento y mostramos el resultado
        if contador > 0:
            promedio_salario = total_salarios / contador
            print(f"Promedio salarial del departamento {departamento}: {promedio_salario}")
        else:
            print(f"No hay empleados en el departamento {departamento}")
    
    # Salir del programa
    elif opcion == "5":
        print("Cerrando programa")
        continuar = False

    # Opción inválida
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
