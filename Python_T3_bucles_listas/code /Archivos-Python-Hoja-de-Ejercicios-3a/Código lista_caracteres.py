# 1. crear lista
frutas = ["manzana", "platano", "cereza", "pera", "higo", "frambuesa", "fresa"]

# 2. Longitud de la lista
print(len(frutas))

# 3. Acceder al objeto 3 de la lista
print(frutas[2])
print("--------")

# 4. Modificar el segundo objeto
frutas[1]="mora"

# 5. Añadir mango al final de la list
frutas.append("mango")

# 6. Añadir uva al comienzo de la lista
frutas.insert(0, "uva")

# 7. Recorrer lista, imprimir cada fruta

for i in range(0,len(frutas)):
    print(frutas[i])
print("-----")

# 8. Eliminar el ultimo elemento de la lista y guardalo
ultima_fruta = frutas.pop()

# 9. recorrer lista e imprimir frutas
for fruta in frutas:
    print(fruta)

print("-------")

# 10. Imprimir la longitud de cada nombre de fruta
for fruta in frutas:
    print(f"Fruta {fruta}. Longitud {len(fruta)}")

print("-------")

# 11. Imprimir nombres de mas de 5 caracteres
for fruta in frutas:
    if len(fruta) > 5:
        print(fruta)

print("-------")
# 12. borrar string cereza

frutas.remove("cereza")
print(frutas)

# 13. vaciar la lista con clear
frutas.clear()
print(frutas)