# Nuestra estructura sera una lista de diccionarios
# [{producto: "nombre producto", precio: precio}, 
# {producto: "nombre producto", precio: precio}
# ...]

ventas = []

def agregar_venta(producto, precio):
    """ agrega ventas a nuestra base de datos """
    # Producto: nombre del producto vendido
    # Precio: precio del producto vendido

    venta = {
        "producto": producto,
        "precio": precio
        }

    ventas.append(venta)

def mostrar_ventas():
    """ muestra las ventas de nuestra base de datos """
    
    for venta in ventas:
        print("Producto", venta["producto"])
        print("Precio", venta["precio"])
        print("----")

# Ejemplo de uso
agregar_venta("Camisa", 25.99)
agregar_venta("Pantalon", 39.95)
agregar_venta("Zapatos", 61.25)

mostrar_ventas()