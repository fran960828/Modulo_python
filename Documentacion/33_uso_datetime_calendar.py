Este documento presenta la documentación y el código ejecutable de los tres ejemplos de programación Python presentados en el video, los cuales ilustran el cálculo del tiempo necesario (días, semanas o meses) para alcanzar objetivos específicos.

***

## Ejemplo 1: Pago de Tarjeta de Crédito (Progreso Mensual)

Este script es el más extenso y complejo de los tres, ya que simula el cálculo de interés anual (dividido mensualmente) y los pagos hasta liquidar el saldo.

```python
# Script para calcular el número de meses que tardará en pagar una tarjeta de crédito.
# Este ejemplo simula el progreso mensual.
# Se importan los módulos datetime y calendar para manejar fechas y determinar la duración de los meses.

import datetime
import calendar

# --- Constantes iniciales (Valores de ejemplo) ---
balance = 5000  # Saldo inicial de la tarjeta de crédito
interes_anual = 0.13  # Tasa de interés anual (13% se escribe como 0.13)
pago_mensual = 500  # Pago mensual a realizar

# --- Determinación de la fecha de inicio ---
today = datetime.date.today()  # Obtener la fecha actual

# Determinar el número de días en el mes actual usando calendar.monthrange.
# monthrange toma año y mes, y retorna una tupla donde el índice 1 es el número total de días.
dias_en_mes_actual = calendar.monthrange(today.year, today.month)

# Calcular los días restantes hasta el final del mes
dias_hasta_fin_de_mes = dias_en_mes_actual - today.day

# Establecer la fecha de inicio de pagos (el primer día del próximo mes).
# Se añade el número de días restantes hasta fin de mes MÁS UN DÍA.
start_date = today + datetime.timedelta(days=dias_hasta_fin_de_mes + 1)

# Usamos end_date para iterar y end_date se incrementará, mientras que start_date permanece fijo.
end_date = start_date

print(f"# Comenzando con saldo: ${balance}, Interés: {interes_anual*100}%, Pago: ${pago_mensual}/mes.")

# Bucle para simular el pago mientras el saldo sea mayor que cero.
while balance > 0:
    
    # 1. Calcular el cargo de interés acumulado del mes anterior.
    # La tasa de interés anual se divide por 12 para obtener la tasa mensual.
    tasa_interes_mensual = interes_anual / 12
    cargo_interes = tasa_interes_mensual * balance
    
    # 2. Agregar el cargo de interés al saldo.
    balance += cargo_interes
    
    # 3. Restar el pago mensual del saldo.
    balance -= pago_mensual
    
    # 4. Redondear el balance a dos decimales para simular moneda.
    balance = round(balance, 2)
    
    # 5. Asegurarse de que el balance no sea negativo; si se paga, se establece a 0.
    if balance < 0:
        balance = 0
        
    # Imprimir la fecha de pago simulada y el saldo restante.
    print(f"Fecha: {end_date} | Saldo restante: ${balance}")
    
    # 6. Incrementar la fecha al primer día del siguiente mes.
    # Obtener el número de días en el mes de la 'end_date' actual.
    dias_en_mes = calendar.monthrange(end_date.year, end_date.month)
    
    # Añadir los días para avanzar un mes. Esto lleva al primer día del mes siguiente.
    end_date += datetime.timedelta(days=dias_en_mes)
    
# Advertencia: Si el pago mensual es menor que el interés añadido, podría ocurrir un bucle infinito.
```

***

## Ejemplo 2: Meta de Peso (Progreso Semanal)

Este script es más simple que el anterior y se enfoca en el progreso semanal para alcanzar una meta de pérdida de peso.

```python
# Script para calcular el número de semanas para alcanzar un peso objetivo.
# Este ejemplo simula el progreso semanal.
# Solo se importa el módulo datetime.

import datetime

# --- Constantes iniciales (Valores de ejemplo) ---
current_weight = 220  # Peso actual (en libras, por ejemplo)
goal_weight = 180  # Peso objetivo
average_lbs_per_week = 1.5  # Promedio de libras a perder por semana (1.5 lbs/semana)

# Establecer las fechas
start_date = datetime.date.today()
end_date = start_date  # end_date se usa para iterar

# Bucle para simular la pérdida de peso semanal hasta que el peso actual sea menor o igual al objetivo.
while current_weight > goal_weight:
    # 1. Simular el paso de siete días (una semana).
    end_date += datetime.timedelta(days=7)
    
    # 2. Restar la pérdida de peso promedio semanal al peso actual.
    current_weight -= average_lbs_per_week

# Calcular el tiempo total transcurrido
time_delta = end_date - start_date
total_days = time_delta.days

# Calcular las semanas transcurridas. Se utiliza floor division (//) para obtener un número entero.
total_weeks = total_days // 7

# Imprimir los resultados
print(f"# Se alcanzó el objetivo de {goal_weight} lbs en {total_weeks} semanas.")
print(f"# Fecha aproximada de alcance de la meta: {end_date}")
```

***

## Ejemplo 3: Meta de Suscriptores (Progreso Diario)

Este es el script más simple, ya que el cálculo del tiempo es directo (sin necesidad de bucles) y simula el progreso diario.

```python
# Script para estimar la fecha en que se alcanzará una meta de suscriptores.
# Este ejemplo simula el progreso diario y es el más simple.

import datetime
import math # Necesario para la función ceiling (math.ceil)

# --- Constantes iniciales (Valores de ejemplo) ---
goal_subs = 100000  # Meta de suscriptores
current_subs = 85000  # Suscriptores actuales
average_subs_per_day = 200  # Promedio de suscriptores ganados por día

# Calcular los suscriptores restantes
subs_to_go = goal_subs - current_subs

# Calcular los días necesarios. La división puede dar un flotante.
dias_calculados = subs_to_go / average_subs_per_day

# Se utiliza math.ceil() para redondear al día completo más cercano hacia arriba.
days_to_go = math.ceil(dias_calculados)

# Obtener la fecha actual
today = datetime.date.today()

# Calcular la fecha de la meta sumando los días restantes a la fecha actual.
fecha_meta = today + datetime.timedelta(days=days_to_go)

# Imprimir el resultado
print(f"# Suscriptores restantes: {subs_to_go}")
print(f"# Días estimados para alcanzar la meta: {days_to_go}")
print(f"# Fecha en que se alcanzaría la meta de {goal_subs} suscriptores: {fecha_meta}")
```