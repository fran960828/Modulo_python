# --- Pedir nombre al usuario ---
nombre = input("Ingresa tu nombre: ")

# --- Saludar al usuario ---
print("¡Hola,", nombre, "!")

# --- Guardamos ingresos y horas trabajadas
ingresos_hora = float(input("Ingresa tus ingresos por hora: "))
#ingresos_hora = 25 # en euros
#horas_trabajadas = 25
horas_trabajadas = int(input("Ingresa las horas trabajadas: "))

# --- Calculamos la ganancia semanal
salario_semanal = ingresos_hora * horas_trabajadas

# --- Calculamos la ganancia anual
ganancia_anual = salario_semanal * 52

# --- Imprime ganancia anual por pantalla
print(nombre.title(), "tienes unas ganacias anuales de", ganancia_anual, "euros")

# --- Pedimos los gastos semanales al usuario
gastos_semanales = float(input("Ingresa tus gastos semanales: "))


# --- Calculamos el gasto anual 
gasto_anual = gastos_semanales * 52

# --- Calculamos los ahorros
ahorro_anual = ganancia_anual - gasto_anual

print("Tu ahorro anual será de", ahorro_anual, "euros")