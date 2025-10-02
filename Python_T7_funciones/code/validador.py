def validar_contrasena(contrasena):
    """Esta funcion valida la contrasena 
    que recibimos dada como argumento"""
    # INPUT:
    # - contrasena: str

    # condiciones minimas
    longitud_minima = 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

    # comprobamos la longitud
    if len(contrasena) < longitud_minima:
        return False
    
    # comrpobamos la naturaleza de los 
    # carcateres de la contrasena
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero =  True
        else:
            tiene_caracter_especial = True

    # devolvemos true si todas las condiciones se cumplen
    # false si alguna de ellas no se cumple 
    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial