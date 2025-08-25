# --- Pedir contraseña al usuario
password = input("Introduce la contraseña ")

# --- Comprobar si la contraseña es segura
# Si cumple los requisistos diremos que es segura
# Debe tener una vocal (a,e,o)
# Debe tener un simbolo especial (*,#)
if ("a" in password or "e" in password or "o" in password) and ("*" in password or "#" in password):
     print("La contraseña es segura")
else:
    print("La constraseña no es segura")
# Si no los cumple diremos que es insegura