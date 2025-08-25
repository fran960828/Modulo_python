# --- Pedir datos al usuario
# edad
edad = int(input("Ingresa tu edad: "))
# ingreso
ingreso = float(input("Introduce tu ingreso mensual euros: "))


# --- Comprobar si se debe aplicar el tipo impositivo y comprobar cual
# Comprobar si el usuario es mayor de edad y sus ingresos --> si debe tributar: Sí
if edad>=18 and ingreso>1000:
    print("Eres susceptible de tributar.")
    ## calcular su renta anual  
    renta_anual = ingreso * 12
    ## comprobar en que tramo se encuentra su ingreso anual
    if renta_anual < 15000:
        print("Tu tipo impositivo es del 5%")
    elif 15000 <= renta_anual < 25000:
        print("Tu tipo impositivo es del 15%")
    elif 25000 <= renta_anual < 35000:
        print("Tu tipo impositivo es del 20%")
    elif 35000 <= renta_anual < 60000:
        print("Tu tipo impositivo es del 30%")
    else:
        print("Tu tipo impositivo es del 45%")

# Si el usuario no esta en el rango de edad o ingresos
else:
    ## imprimir que no tiene obligacio de tributar 
    print("No eres susceptible de tributar.")
