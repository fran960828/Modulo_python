import numpy as np

# Crear un array con los datos
datos = np.array([['2022-01-01', 'Componente 1', 'Lote A', 80],
                  ['2022-01-15', 'Componente 1', 'Lote B', 90],
                  ['2022-02-01', 'Componente 2', 'Lote C', 85],
                  ['2022-02-15', 'Componente 2', 'Lote D', 95],
                  ['2022-03-01', 'Componente 1', 'Lote E', 75],
                  ['2022-03-15', 'Componente 2', 'Lote F', 90]])

# ---- identificar componente con puntuacion mas alta ---- 
tipos_componente = datos[:,1] # extraemos el tipo de componente
tipos_unicos = np.unique(tipos_componente) # lista con los tipos sin repeticiones
calidad = datos[:, 3].astype(float) # lista con la calidad de los componentes
promedios = np.zeros(len(tipos_unicos)) # inicializamos array donde guardaremos promedios

i = 0
for tipo in tipos_unicos:
    promedios[i] = np.mean(calidad[tipos_componente  == tipo])  # calculamos valor 
                                                                # promedio para cada 
                                                                # componente
    i = i + 1

indice_maximo = np.argmax(promedios) # indice del promedio mas alto
tipo_mejor_calidad = tipos_unicos[indice_maximo] # tipo con promedio mas alto
 
print("El tipo de componente con la puntuacion de calidad mas alta es:", tipo_mejor_calidad)

# ---- cuantos componentes se produjeron en cada mes ---- 
fechas = datos[:,0] # extraemos las fechas completas de la base de datos
meses, counts = np.unique([fecha[0:7] for fecha in fechas], return_counts = True) # extraemos el mes de cada fecha
                                                    # y lo añadimos a una lista
for i in range(len(meses)):
    print("Mes:", meses[i], "Cantidad producida", counts[i])

# ---- puntuacion de calidad promedio de cada uno de los componentes ---- 
promedio_por_tipo = np.zeros(len(tipos_unicos))
for i in range(len(tipos_unicos)):
    promedio_por_tipo[i] = np.mean(calidad[tipos_componente == tipos_unicos[i]])
    print("La puntuacion de calidad promedio para el", tipos_unicos[i], "es:", promedio_por_tipo[i])