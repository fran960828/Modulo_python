# --- Tenemos la contraseña correcta
key = "micontraseña123"

# --- Pedimos al usuario la contraseña
password = input("Introduce la contraseña: ")

# --- Comprobamos que el password introducido coincide con nuestra key
if password.lower() == key:
# Si coincide damos la bienvenida
    print("Contraseña correcta. ¡Bienvenido!")
else:
# Si no coincide damos un error y pedimos la contraseña de nuevo
    print("Error, la contraseña no es correcta")
    password = input("Introduzca la cintraseña de nuevo: ")
    if password.lower() == key:
        ## si esta vez la contraseña coincide damos la bienvenida
        print("Contraseña correcta. ¡Bienvenido!")
    else:
        ## si no damos un mensaje de error y se termina el programa
        print("Error, la contaseña no es correcta")
        print("Cerramos el sistema")

