import random
import string

def generar_contrasena_segura(longitud, incluir_mayusculas = True, incluir_minusculas = True,  incluir_numeros = True, incluir_caracteres_especiales = True):
    """Genera una contrasena segura dada una longitud"""
    # longitud: numero de caracteres de la contrasena
    # incluir_mayusculas: si true la contrasena incluira al menos una mayuscula
    # incluir_minusculas: si true la contrasena incluira al menos una minuscula
    # incluir_numeros: si true la contrasena incluira al menos un numero
    # incluir_caracteres_especiales: si true la contrasena incluira al menos un caracter especial

    caracteres = ""

    # le indicamos que tipo de caracteres anadir a la 
    # nueva contrasena
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase

    if incluir_minusculas:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    # creamos una mezcla aleatoria con los caracteres que le hemos indicado en los if
    contrasena = "".join(random.choice(caracteres) for i in range(longitud))

    return contrasena
