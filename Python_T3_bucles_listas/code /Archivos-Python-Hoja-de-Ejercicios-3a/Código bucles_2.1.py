'''Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la 
contraseña hasta que introduzca la contraseña correcta.
'''

# --- contraseña guardada
password = "secreto"
password_entrada = ""

# --- bucle para pedir la contraseña
# out: contraseña sea correcta
while password_entrada != password:
    password_entrada = input("Introduzca la contraseña: ")
    if password_entrada != password:
        print("Contraseña incorrecta. Inténtelo de nuevo")

print("Contraseña correcta. Acceso permitido")
