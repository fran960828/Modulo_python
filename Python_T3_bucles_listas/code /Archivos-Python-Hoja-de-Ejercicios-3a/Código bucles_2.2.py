'''Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la 
contraseña hasta que introduzca la contraseña correcta.
'''

password = "secreto"

while True:
    password_entrada = input("Ingrese la contraseña: ")
    if password_entrada == password:
        print("Constraseña correcta. Acceso permitido.")
        break
    
    else:
        print("Constraseña incorrecta. Intentelo de nuevo.")