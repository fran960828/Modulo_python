# --- Pedir al usuario tres longitudes
longitud1 = float(input("Ingresa la primera longitud: "))
longitud2 = float(input("Ingresa la segunda longitud: "))
longitud3 = float(input("Ingresa la tercera longitud: "))

# --- Comprobar si pueden conformar un triangulo: 
if (longitud1 + longitud2 > longitud3) and (longitud3 + longitud2 > longitud1) and (longitud1 + longitud3 > longitud2):
    print("Con las piezas puedes crear un triangulo")
else:
    print("Con las piezas no podras crear un triangulo")


