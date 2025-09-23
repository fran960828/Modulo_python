resultados = {}

continuar = True
while continuar:
    print("1. Registrar voto")
    print("2. Mostrar lista de candidatos y votos")
    print("3. Encontrar candidato ganador")
    print("4. Calcular porcentaje de votos")
    print("5. Salir")
    opcion = input("Seleccione un opción: ")


    # Resgistrar voto
    if opcion == "1":
        # pedimos nombre de candidato
        candidato = input("Ingrese nombre del candidato: ")
        # comprobamos si el candidato esta en la base de datos
        if candidato in resultados:
            # sumamos voto
            resultados[candidato] = resultados[candidato] + 1
        # si no esta en la base de datos añadimos par clave valor
        else:
            # añadimos voto
            resultados[candidato] = 1

        print("Voto registrado satisfactoriamente")

    # Mostrar lista de candidatos y votos
    elif opcion == "2":
        print("Lista de candidatos y votos: ")
        # recorremos pares clave-valor
        for candidato, votos in resultados.items():
            # imprimimos candidatos-votos
            print(f"Candidato: {candidato}, Votos: {votos}")

    # Encontrar candidato ganador
    elif opcion == "3":
        # comprobamos si se ha votado ya
        # si no
        if len(resultados) == 0:
            print("No hay candidatos registrados.")

        # si hay votaciones registadas
        else:
            # extraemos la clave asociada al numero de votos mas alto
            ganador = max(resultados, key = resultados.get)
            print(f"El candidato ganador es: {ganador}")

    # Calcular el porcentaje de votos
    elif opcion == "4":
        total_votos = sum(resultados.values())
        print("Porcentaje de votos por candidato")
        for candidato, votos in resultados.items():
            porcentaje = (votos/total_votos) * 100
            print(f"Candidato: {candidato}, Porcentaje de votos {porcentaje:.2f}%")

    # Cerrar script
    elif opcion == "5":
        print("Cerrando votaciones")
        continuar = False

    # Indicar que la opcion no es valida
    else:
        print("Opcion invalida. Por favor, seleccione una opcion valida.")


