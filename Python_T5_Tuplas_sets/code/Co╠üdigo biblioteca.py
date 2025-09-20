# Se define una lista de tuplas con información sobre los libros y sus autores
lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Garbriel Garcia Márquez'), ('La ciudad y los perros', 'Mario Vargas Llosa')]

# Se crea una lista vacía para almacenar los títulos de los libros y los apellidos de los autores
titulos_y_apellidos = []

# Se recorre la lista de libros con un bucle for, desempaquetando cada tupla en título y autor
for tupla in lista_libros:
    titulo, autor = tupla
    
    # Se utiliza el método split() para dividir el nombre completo del autor en una lista de palabras,
    # y se selecciona el último elemento de la lista (que debería ser el apellido)
    apellido = autor.split()[-1]

    # Se agrega una nueva tupla a la lista titulos_y_apellidos, que contiene el título del libro
    # y el apellido del autor
    titulos_y_apellidos.append((titulo, apellido))

# Se imprime la lista completa de títulos de libros y apellidos de autores
print(titulos_y_apellidos)
