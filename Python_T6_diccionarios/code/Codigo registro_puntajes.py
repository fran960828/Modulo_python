# base de datos con puntajes
registros = {}
continuar = True


# seguimiento de los puntajes --> actualizados
while continuar:
    # pedir al usuario su nombre
    nombre = input("Ingrese nombre del jugador (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        continuar = False
    else:
        puntaje = int(input("Ingrese el puntaje del jugador: "))
        registros[nombre] = puntaje

    # Obtener puntaje más alto
    jugador_mas_alto = max(registros, key=registros.get)
    puntaje_mas_alto = registros[jugador_mas_alto]
    print("Puntaje más alto:")
    print("Jugador:", jugador_mas_alto)
    print("Puntaje:", puntaje_mas_alto)

    # Obtener el promedio de puntajes
    total_puntajes = sum(registros.values())
    cantidad_jugadores = len(registros)
    promedio = total_puntajes / cantidad_jugadores
    print("Promedio de puntajes:", promedio)

    # Cantidad total de jugadores
    print("La cantidad de jugadores es: ", cantidad_jugadores)