# funcion para validar formularios
def validar_formulario(nombre, email, telefono):
    """ Esta funcion valida si los datos ingresados
    tienen el formato correcto"""
    # INPUT
    # - Nombre: str
    # - Email: str
    # - Telefono: str de digitos

    # Comprobamos las condiciones
    if len(nombre) < 3:
        return False

    if "@" not in email or "." not in email:
        return False

    if len(telefono) !=9 or not telefono.isdigit():
        return False

    return True



# pedir informacion al usuario
nombre = input("Ingrese su nombre: ")
email = input("Ingrese su correo electronico: ")
telefono = input("Ingrese su numero de telefono: ")

# validamos el formulario llamando a la 
# funcion de validacion
valido = validar_formulario(nombre, email, telefono)

# comprobamos el resultado de la validacion
if valido:
    print("Formulario valido")
else: 
    print("Formulario no valido")
