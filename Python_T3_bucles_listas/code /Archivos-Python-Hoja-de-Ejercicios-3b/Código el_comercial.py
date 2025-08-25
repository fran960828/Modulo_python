

# --- Lista de productos y precios
# + lista de unidades vendidas de cada producto

precio_productos = [30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
unidades_producto = [3, 1, 0, 0, 7, 2, 0, 0, 4, 0]
#facturacion_producto = []

# el numero total de unidades vendidas es la suma de las unidades
# vendidas de cada producto
total_ventas = sum(unidades_producto)

# --- Bucle que recorra los productos (precips + unidades vendidas)

dinero_total = 0
# recorrecmos cada uno de los productos
for i in range(0, len(precio_productos)):
    # el dinero obtenido por cada producto será el precio del mismo
    # multiplicado por la cantidad de unidades vendidas
    dinero_por_producto = precio_productos[i] * unidades_producto[i]
    
    ###facturacion_producto.append(dinero_por_producto)

    # sumamos el dinero obtenido por cada producto al dinero total
    dinero_total = dinero_total + dinero_por_producto
    print(f"El dinero facturado por el producto {i + 1} es: {dinero_por_producto} EU.")

# --- Imprimir resultados
print("El numero total de unidades vendidas es:", total_ventas)
print("El dinero total facturado es:", dinero_total)


# output:
# cantidad total de ventas
# el dinero facturado por producto
# el dinero total

