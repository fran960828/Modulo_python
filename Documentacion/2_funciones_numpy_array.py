import numpy as np

import numpy as np

# ==================================
# Creación de arrays
# ==================================

# np.array : Crea un array a partir de una lista de Python.
arr = np.array([1, 2, 3, 4])
print(arr)  # [1 2 3 4]

# np.zeros : Crea un array lleno de ceros.
arr = np.zeros((2, 3))
print(arr)  # [[0. 0. 0.]
            #  [0. 0. 0.]]

# np.ones : Crea un array lleno de unos.
arr = np.ones((2, 3))
print(arr)

# np.arange : Crea un array con un rango de números.
arr = np.arange(0, 10, 2)
print(arr)  # [0 2 4 6 8]

# np.linspace : Crea un array con valores espaciados de forma uniforme.
arr = np.linspace(0, 1, 5)
print(arr)  # [0.   0.25 0.5  0.75 1.  ]

# np.eye : Matriz identidad.
arr = np.eye(3)
print(arr)

# ==================================
# Propiedades básicas de arrays
# ==================================

arr = np.array([[1, 2, 3], [4, 5, 6]])

# shape : Tamaño del array (filas, columnas).
print(arr.shape)  # (2, 3)

# ndim : Número de dimensiones.
print(arr.ndim)  # 2

# size : Cantidad de elementos totales.
print(arr.size)  # 6

# dtype : Tipo de datos del array.
print(arr.dtype)

# ==================================
# Operaciones matemáticas
# ==================================

arr = np.array([1, 2, 3, 4])

# Suma, resta, multiplicación y división elemento a elemento.
print(arr + 10)   # [11 12 13 14]
print(arr * 2)    # [2 4 6 8]
print(arr - 1)    # [0 1 2 3]
print(arr / 2)    # [0.5 1.  1.5 2. ]

# Potencia
print(arr ** 2)  # [ 1  4  9 16]

# Raíz cuadrada
print(np.sqrt(arr))

# Logaritmo
print(np.log(arr))

# Exponencial
print(np.exp(arr))

# ==================================
# Estadísticas
# ==================================

arr = np.array([1, 2, 3, 4, 5])

print(arr.sum())   # 15
print(arr.mean())  # 3.0
print(arr.min())   # 1
print(arr.max())   # 5
print(arr.std())   # 1.414...

# ==================================
# Indexación y slicing
# ==================================

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])      # 10
print(arr[-1])     # 50
print(arr[1:4])    # [20 30 40]

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat[0, 0])   # 1
print(mat[:, 1])   # [2 5 8]
print(mat[1, :])   # [4 5 6]

# ==================================
# Manipulación de arrays
# ==================================

arr = np.array([[1, 2], [3, 4]])

# reshape : Cambiar la forma del array.
print(arr.reshape(4, 1))

# flatten / ravel : Convertir en un array 1D.
print(arr.flatten())

# transpose : Transponer filas y columnas.
print(arr.T)

# concatenate : Unir arrays.
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
print(np.concatenate([arr1, arr2]))  # [1 2 3 4]

# stack : Apilar arrays.
print(np.stack([arr1, arr2]))

# hstack y vstack : Concatenar horizontal o vertical.
print(np.hstack([arr1, arr2]))  # [1 2 3 4]
print(np.vstack([arr1, arr2]))  # [[1 2]
                               #  [3 4]]

# split : Dividir un array.
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr, 3))  # [array([1,2]), array([3,4]), array([5,6])]

# ==================================
# Comparaciones y máscaras booleanas
# ==================================

arr = np.array([1, 2, 3, 4, 5])

print(arr > 3)      # [False False False  True  True]
print(arr[arr > 3]) # [4 5]

# where : Condiciones en arrays.
print(np.where(arr % 2 == 0, "par", "impar"))

# any y all : Verificar condiciones.
print((arr > 0).all())  # True
print((arr > 3).any())  # True

# ==================================
# Funciones de álgebra lineal
# ==================================

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Producto de matrices (dot).
print(np.dot(A, B))

# Determinante
print(np.linalg.det(A))

# Inversa de una matriz
print(np.linalg.inv(A))

# Autovalores y autovectores
vals, vecs = np.linalg.eig(A)
print(vals)
print(vecs)

