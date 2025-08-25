'''
Supongamos que eres un administrador de sistemas 
y necesitas validar el acceso de los usuarios a 
un sitio web. Crea un script que verifique si el 
+nombre de usuario y la contraseña ingresados son 
correctos y permita el acceso solo si ambos son correctos.

'''

# lista de nombres de usuario
nombres_usuario = ["juan123", "ana456", "pedro789"]
# lista de contraseña
passwords = ["clave123", "clave456", "clave789"]

# pedir al usuario su nombre de usuario
usuario = input("Ingrese su nombre de usuario: ")
# pedir al usuario la contraseña
password = input("Ingrese su contaseña: ")

# boolenano que sera true si el usuario
# y contraseña coinciden con algunos de 
# nuestra lista
credenciales = False
# iterador del bucle while para recorrer las listas
i = 0
# recorrer lista de usuarios y contraseñas
while i < len(nombres_usuario):
    ## comprobar si son iguales a los introducidos por el user
    if nombres_usuario[i] == usuario and passwords[i] == password:
        # como son un nombre y contraseñas validos 
        # credenciales pasa a ser true
        credenciales = True

    # aumentamos en uno el valor del iterador
    i = i + 1

### si el usuario y contaseña son validos damos la bienvenida
if credenciales == True:
    print("Acceso permitido")
    
### si no son validos denegamos acceso
else:
    print("Acceso denegado")

