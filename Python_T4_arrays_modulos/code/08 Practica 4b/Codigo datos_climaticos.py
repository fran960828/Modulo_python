# importar modulos
import numpy as np

# Datos de clima
clima = np.array([
    [20, 70, 1009, 1],
    [18, 75, 1012, 2],
    [16, 72, 1011, 2],
    [19, 73, 1011, 2],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [22, 60, 1013, 4],
    [24, 59, 1010, 4],
    [25, 61, 1011, 4],
    [28, 50, 1007, 5],
    [30, 45, 1005, 6],
    [10, 45, 1005, 6],
    [32, 40, 1002, 7],
    [30, 35, 1003, 8],
    [33, 35, 1001, 8],
    [32, 35, 1004, 8],
    [31, 45, 1003, 9],
    [28, 50, 1006, 10],
    [27, 48, 1008, 10],
    [25, 60, 1010, 11],
    [22, 70, 1011, 12]
])


# guardamos datos en arrays independientes
meses = clima[:,3]
temperaturas = clima[:,0]
humedad = clima[:,1]
presion = clima[:,2]

# inicializamos arrays de valores promedio por mes
temp_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)

# recorrer los valores para cada mes
for i in range(12):
    # calculamos valores medios
    temp_mes[i] = np.mean(temperaturas[meses == i+1])
    humedad_mes[i] = np.mean(humedad[meses == i+1])
    presion_mes[i] = np.mean(presion[meses == i+1])

    # imprimimos resultados para cada mes
    print("La temperatura promedio en el mes", i+1, " fue de", temp_mes[i], "grados")
    print("La humedad promedio en el mes", i+1, " fue de", humedad_mes[i])
    print("La presion promedio en el mes", i+1, " fue de", presion_mes[i], "bar")

