# diccionario de ventas
ventas = {}

# registrar las ventas
ventas["Producto1"] = 10
ventas["Producto2"] = 5
ventas["Producto3"] = 3

# Actualizar cantidad vendida de un producto existente
ventas["Producto2"] = ventas["Producto2"] + 2
##ventas["Producto2"] += 2

# Calcular el total de ventas diarias
total_ventas= sum(ventas.values())

# Imprimir el registro de ventas y el total de ventas diarias
print("Registro de ventas:")
for producto, cantidad in ventas.items():
    print(producto + ": " + str(cantidad))

print("Total de ventas diarias: " + str(total_ventas))
