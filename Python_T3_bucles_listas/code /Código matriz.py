'''
Crea un script que dada una lista de listas M (numérica), 
identifique si se trata de una matriz y en ese caso imprima dos listas correspondientes a:
1. La fila cuyos elementos suman el máximo
2. La columna cuyos elementos suman el máximo

M1=[[2,5,3],[6,1,8],[7,5,4]] 
M2 = [[4,2,3],[4,5],[6,8,2]] 

'''

# Definir la lista de listas M
M = [[2,5,3],
     [6,1,8],
     [7,5,4]]

# --- Verificar si M es una matriz ---
n_columnas = len(M[0])
n_filas = len(M)
es_matriz = True

# recorrer todas las listas dentro de M (todas las filas de M)
for i in range(0,n_filas):
    # compruebo si la fila i tienen la misma dimension 
    # que la de referencia
    if len(M[i]) != n_columnas:  # si no tiene el mismo numero de columnas
        es_matriz = False # si alguna fila tiene un numero de elementos distinto
                          # a la de referencia, entonces es_matriz sera falso
        break

# Parte 1 -- calculamos fila con suma maxima y la imprimimos
# Si es una matriz ejecutamos
if es_matriz == True:

    sum_max = 0 # inicializamos la variable de suma maxima

    # recorremos las filas con un bucle 
    for i in range(0, n_filas):
        fila = M[i] # cada una de las filas
        suma_fila = sum(fila) # calculamos la suma de la fila
        
        # comprobamos si la suma de la fila es mayor al de la fila anterior
        if suma_fila > sum_max:  
            sum_max = suma_fila # actualizamos el valor de la suma maxima
            num_fila = i        # actualizamos el valor del indice de la
                                # fila con la suma mas alta


    print("La fila cuyos elementos suman el maximo es:", M[num_fila], "con una suma total de", sum_max)

                    
# Parte 2 -- calculamos columna con suma maxima y la imprimimos

'''
M = [[2,5,3],
     [6,1,8],
     [7,5,4]]
'''
# Ejecutamos solo si se trata de una matriz
if es_matriz == True:
    suma_max = 0 # inicializamos la variable que guarda la suma maxima
    # recorremos todas las columnas de la matriz
    for j in range(0,n_columnas):
        columna = [] # inicializamos nuestra lista donde guardamos los valores
                     # de cada una de las columnas en cada iteracion
        suma_columna = 0 # inicializamos la variable que contiene la suma de la columna

        # recorrer las filas de la matriz
        for fila in M:
            suma_columna = suma_columna + fila[j] # sumar cada elemento de la columna j
            columna.append(fila[j]) # añadir cada elemento de la columna j a nuestra lista columna

        # comprobar si la suma de la columna es mayor a la suma de la columna anterior
        if suma_columna > suma_max:
            suma_max = suma_columna # actualizamos el valor de la suma maxima
            columna_max = columna[:] # actualizamos el valor de la columna con suma maxima
            
    print("La columna cuyos elementos suman el maximo es:", columna_max, "con una suma total de", suma_max)
            
            
            
    
