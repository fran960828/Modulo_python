# importar modulos
import numpy as np

# calificaciones de los estudiantes / input 
calificaciones = np.array([
    [8, 7, 9, 10],
    [6, 8, 7, 9],
    [9, 9, 8, 8],
    [7, 6, 6, 7],
    [10, 9, 10, 10]
])

# --- Calcular la nota final de cada estudiante ---
# guardamos datos en arrays independientes
examen1 = calificaciones[:,0]
examen2 = calificaciones[:,1]
trabajo_final = calificaciones[:,2]
participacion = calificaciones[:,3]

# calculamos nota final para los n alumnos
nota_final = examen1 * 0.3 + examen2 * 0.3 + trabajo_final * 0.3 + participacion * 0.1

# imprimir las notas finalews de cada estudiante
for i in range(len(nota_final)):
    print("La nota final del estudiante", i+1, "es:", nota_final[i])

# nota final = 30% * examen 1 + 30% * examen 2 + 30% trabajo final + 10% participacion en clase