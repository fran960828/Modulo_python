# --- Pedimos los tiempos por pantalla ---
#minutos_hannah = input("Ingresa los minutos para hannah")
#segundos_hannah = input("Ingresa los segundos para hannah")
#centesimas_hannah = input("Ingresa las centesimas para hannah")

tiempo_hannah = input("Ingresa el tiempo de Hannah Neise (formato: minutos segundos centésimas): ")
tiempo_jackie = input("Ingresa el tiempo de Jackie Narracott (formato: minutos segundos centésimas): ")
tiempo_kimberly = input("Ingresa el tiempo de Kimberly Bos (formato: minutos segundos centésimas): ")

# --- Extraer minutos segundos y centésimas ---
minutos_hannah, segundos_hannah, centesimas_hannah = tiempo_hannah.split(" ")
minutos_jackie, segundos_jackie, centesimas_jackie = tiempo_jackie.split(" ")
minutos_kimberly, segundos_kimberly, centesimas_kimberly = tiempo_hannah.split(" ")

# --- Convertimos los tiempos a segundos ---
tiempo_hannah = float(minutos_hannah) * 60 + float(segundos_hannah) + float(centesimas_hannah) * 0.01
tiempo_jackie = float(minutos_jackie) * 60 + float(segundos_jackie) + float(centesimas_jackie) * 0.01
tiempo_kimberly = float(minutos_kimberly) * 60 + float(segundos_kimberly) + float(centesimas_kimberly) * 0.01

# --- Calculamos la velocidad media ---
velocidad_hannah = 100.0/tiempo_hannah
velocidad_jackie = 100.0/tiempo_jackie
velocidad_kimberly = 100.0/tiempo_kimberly


# --- Imprimir los resultados por pantalla ---
print("La velocidad media de Hannah Neise fue de ", velocidad_hannah, " metros por segundo")
print("La velocidad media de Jackie Narracott fue de ", velocidad_jackie, " metros por segundo")
print("La velocidad media de Kimberly Bos fue de ", velocidad_kimberly, " metros por segundo")