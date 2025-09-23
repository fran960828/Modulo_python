# base de datos diccionario
empleados = {}

# condicion del while veradera
continuar = True

# iniciamos bucle
while continuar:
    # imprimimos las opciones al usuario
    print("1. Agregar empleado")
    print("2. Actualizar salario de empleados")
    print("3. Mostrar lista de empleados")
    print("4. Calcular promedio salarial por departamente")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    # Agregar empleado
    if opcion == "1":
        nombre = input("Ingrese nombre del empleado: ")
        salario = float(input("Ingrese salario del empleado: "))
        departamento = input("Ingrese departamento del empleado: ")

        empleados[nombre] = {
            "salario": salario,
            "departamento": departamento
        }

        print("Empleado agregado exitosamente")

    # Actualizar salario empleados
    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado: ")
        # comprobamos la existencia del empleado en la base de datos
        if nombre in empleados:
            # pedimos nuevo salario
            nuevo_salario = float(input("Ingrese el nuevo salario del empleado: "))
            # actualizamos salario del empleado
            empleados[nombre]["salario"] = nuevo_salario
            print("Salario actualizado exitosamente")
        # si el empleado no existe en la base de datos lo indicamos
        else:
            print("Empleado no encontrado")

    # Mostrar lista de empleados
    elif opcion == "3":
        print("Lista de empleados: ")
        # recorremos pares clave-valor =  nombre-datos
        for nombre, datos_empleado in empleados.items():
            salario = datos_empleado["salario"] # extraemos valor del salario
            departamento = datos_empleado["departamento"] # extraemos departamento
            # imprimimos informacion
            print(f"Nombre: {nombre}, Salario: {salario}, Departamento: {departamento}")

    # Calcular promedio salarial por departamento
    elif opcion == "4":
        departamento = input("Ingrese el departamento: ")

        # inicializamos variables
        total_salarios = 0
        contador = 0
        # recorremos datos de los empleados guardados en los valores del dict
        for datos_empleado in empleados.values():
            # si el departamento coincide sumamos el salario
            if datos_empleado["departamento"] == departamento:
                total_salarios = total_salarios + datos_empleado["salario"]
                contador = contador + 1

        # si hay empleados en el departament calculamos el promedio
        if contador > 0:
            promedio_salario = total_salarios / contador
            print(f"Promedio salarial del departamento {departamento}: {promedio_salario}")
        # si no hay empleados en el departamento lo indicamos
        else:
            print(f"No hay empleados en el departamento {departamento}")

    elif opcion == "5":
        print("Cerrando programa")
        continuar = False

    else: 
        print("Opcion invalida. Por favor, seleccione una opcion valida.")


