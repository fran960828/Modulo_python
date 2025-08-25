'''Supongamos que eres el propietario de una tienda 
en línea y tienes una lista de ventas de los últimos 
30 días. Quieres analizar las ventas por día de la 
semana para identificar los días de mayor venta.
'''

# lista con las ventas del mes
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
# lista con los dias de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# lista donde guardar las ventas por dia
ventas_totales = [0, 0, 0, 0, 0, 0, 0] 

# recorrer la lista de ventas con un bucle
dia_venta = 0
for venta in ventas:
    ## sumar para cada dia de la semana las ventas realizadas
    ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
    ## pasamos al dia siguiete
    dia_venta = dia_venta + 1
    ## si llegamos al domingo volvemos de nuevo al lunes
    if dia_venta == 7:
        # cambiamos el valor al indice del lunes
        dia_venta = 0

## imprimir las ventas realizadas para cada dia de la semana
## a lo a largo de ese mes
for i in range(len(dias_semana)):
    print(dias_semana[i]+ ":", ventas_totales[i])