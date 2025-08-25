
'''Desarrolla un script en Python que dado una cadena 
de caracteres con la siguiente información: nombre, 
apellido, DNI, código_asignatura, convocatoria, nota1, 
nota2, nota3 ... Por ejemplo: David Fernandez 12311267A 43527 2 2.1 4.6 3.4. 
El script debe crear una lista con esos datos, introducirlo en una lista de 
listas donde se encuentra la información de todos los alumnos e imprimir 
la nota media de los alumnos junto con el DNI.

'''
# base de datos (lista de listas con los datos de los alumnos)
base_datos = [["Alvaro", "Gomez", "87654327B", "64782", "1", "7.6", "5.4", "9.3"]]

# Definir la cadena de caracteres con la información de un alumno
cadena = "David Fernandez 12311267A 43527 2 2.1 4.6 3.4"

# convertir la cadena de entrada en una lista
datos_alumno = cadena.split() # split separara la cadena en una lista de valores individuales

# introducir la lista con los datos del alumno en la base de datos
base_datos.append(datos_alumno)

for alumno in base_datos:
    dni = alumno[2] # extraemos el dni del alumno
    # calculculamos la media del alumno
    suma_notas = 0 # iniciamos la variable suma notas en 0 para cada alumno
    n_notas = 0
    for i in range(5,len(alumno)): # recorremos todas las notas del alumno
        suma_notas = suma_notas + float(alumno[i]) # sumamos todas las notas las notas del alumno
        n_notas = n_notas + 1 # calculamos el numero total de notas del alumno

    nota_media = suma_notas / n_notas # calculamos la nota media del alumno

    print(f"El alumno con dni {dni} tiene una nota media de {nota_media:.2f}")
