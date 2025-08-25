# ---- Pedimos un precio al usuario
precio = float(input("Ingresa el precio en dolares: "))

# --- Comprobar el precio y ver si debemos comprar, holderar o vender
if precio < 100.0:
    print("Es hora de comprar")
elif 100.0 <= precio <= 150.0:
    print("Toca holdear")
else:
    print("Es hora de vender")

