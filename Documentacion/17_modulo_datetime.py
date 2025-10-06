```python
# =================================================================
# MÓDULO DATETIME DE PYTHON
# DOCUMENTACIÓN DE EJEMPLOS BASADA EN FUENTES
# =================================================================

# La librería principal para trabajar con fechas en Python es el módulo 'datetime'.
# Este módulo permite manejar fechas, horas, combinaciones de fecha y hora (datetime),
# zonas horarias y 'timedeltas' (diferencias de tiempo).

import datetime

# La documentación debe distinguir entre:
# 1. Fechas/horas 'Naives' (ingenuas): No tienen suficiente información para determinar
#    la zona horaria o el horario de verano. Son más fáciles de usar si no se requiere
#    ese nivel de detalle.
# 2. Fechas/horas 'Awares' (conscientes): Sí tienen suficiente información para determinar
#    su zona horaria y seguir el horario de verano, lo que ayuda a evitar confusiones.

print("--- 1. DATETIME.DATE (Fechas Naives) ---")

# =================================================================
# EJERCICIO 1: Creación de una fecha específica
# Función utilizada: datetime.date(año, mes, día)
# Descripción: Crea un objeto 'date' especificando el año, mes y día.
# Importante: Se deben pasar números enteros. No se deben usar ceros a la izquierda
# en meses o días de un solo dígito, ya que esto provoca un error de sintaxis.
# =================================================================
# Crear una fecha para el 24 de julio de 2016
d = datetime.date(2016, 7, 24)
print(f"# La fecha creada es: {d}")


# =================================================================
# EJERCICIO 2: Obtener la fecha local actual
# Función utilizada: datetime.date.today()
# Descripción: Devuelve la fecha local actual.
# =================================================================
# Obtener la fecha de hoy
today = datetime.date.today()
print(f"# La fecha local actual es: {today}")


# =================================================================
# EJERCICIO 3: Acceso a atributos de la fecha
# Funciones utilizadas: .year, .month, .day
# Descripción: Permite acceder individualmente al año, mes o día del objeto 'date'.
# =================================================================
print(f"# El año de la fecha actual es: {today.year}")
print(f"# El día de la fecha actual es: {today.day}")


# =================================================================
# EJERCICIO 4: Obtener el día de la semana
# Funciones utilizadas: .weekday(), .isoweekday()
# Descripción: Devuelven el día de la semana como un entero.
# Diferencia clave:
# - .weekday(): Lunes es 0 y Domingo es 6.
# - .isoweekday(): Lunes es 1 y Domingo es 7.
# =================================================================
# Se imprime el día de la semana para la fecha actual
print(f"# Día de la semana (weekday): {today.weekday()} (Lunes=0)")
print(f"# Día de la semana (isoweekday): {today.isoweekday()} (Lunes=1)")

print("\n--- 2. TIMEDELTAS ---")

# =================================================================
# EJERCICIO 5: Creación de un Time Delta (diferencia de tiempo)
# Función utilizada: datetime.timedelta(days=N, hours=N, etc.)
# Descripción: Los Time Deltas son la diferencia entre dos fechas u horas y son
# útiles para realizar operaciones en fechas.
# =================================================================
# Crear un Time Delta de 7 días (una semana)
tdelta = datetime.timedelta(days=7)
print(f"# El Time Delta creado representa: {tdelta}")


# =================================================================
# EJERCICIO 6: Cálculos con Time Deltas
# Operación: Fecha + Time Delta
# Descripción: Sumar un Time Delta a un objeto 'date' o 'datetime' resulta en una nueva fecha.
# Operación: Fecha - Time Delta
# Descripción: Restar un Time Delta a un objeto 'date' o 'datetime' resulta en una fecha pasada.
# =================================================================
# Fecha de hoy + 7 días
future_date = today + tdelta
print(f"# Fecha dentro de 7 días: {future_date}")

# Fecha de hoy - 7 días
past_date = today - tdelta
print(f"# Fecha hace 7 días: {past_date}")


# =================================================================
# EJERCICIO 7: Calculando la diferencia entre dos fechas
# Operación: Fecha - Fecha
# Descripción: Restar una fecha de otra resulta en un Time Delta.
# =================================================================
# Calcular días hasta un cumpleaños (24 de septiembre de 2016)
bday = datetime.date(2016, 9, 24)
today_calc = datetime.date(2016, 7, 26) # Usamos la fecha de la fuente para reproducir el cálculo

# La diferencia es un Time Delta
till_bday = bday - today_calc
print(f"# Time Delta hasta el cumpleaños (2016/09/24 - 2016/07/26): {till_bday}")

# =================================================================
# EJERCICIO 8: Acceso a atributos del Time Delta
# Funciones utilizadas: .days, .total_seconds()
# Descripción: Permiten extraer la duración total del Time Delta en días o segundos.
# =================================================================
# Obtener solo los días de duración
print(f"# Días restantes hasta el cumpleaños: {till_bday.days}")

# Obtener los segundos totales de duración
# Función utilizada: .total_seconds()
print(f"# Segundos totales restantes: {till_bday.total_seconds()}")

print("\n--- 3. DATETIME.TIME (Horas Naives) ---")

# =================================================================
# EJERCICIO 9: Creación de un objeto 'time'
# Función utilizada: datetime.time(hora, minuto, segundo, microsegundo)
# Descripción: Trabaja con horas, minutos, segundos y microsegundos, pero NO incluye
# año, mes o día. Por defecto, es 'naive' (no tiene información de zona horaria).
# =================================================================
# Crear una hora (10:30:00.0)
t = datetime.time(10, 30, 0, 0)
print(f"# La hora creada es: {t}")

# Acceder individualmente a la hora
print(f"# La hora es: {t.hour}")


print("\n--- 4. DATETIME.DATETIME (Combinación de Fecha y Hora Naive) ---")

# =================================================================
# EJERCICIO 10: Creación de un objeto 'datetime'
# Función utilizada: datetime.datetime(año, mes, día, hora, minuto, segundo, microsegundo)
# Descripción: Da acceso tanto a la fecha (año, mes, día) como a la hora
# (horas, minutos, segundos, microsegundos).
# =================================================================
# Crear un objeto datetime (26 de julio de 2016, 12:30:45 y 100,000 microsegundos)
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(f"# El objeto datetime completo es: {dt}")

# =================================================================
# EJERCICIO 11: Extracción de componentes
# Funciones utilizadas: .date(), .time()
# Descripción: Permite obtener solo la parte de la fecha o solo la parte de la hora
# del objeto 'datetime'.
# =================================================================
print(f"# Solo la fecha: {dt.date()}")
print(f"# Solo la hora: {dt.time()}")
print(f"# Accediendo solo al año: {dt.year}")


# =================================================================
# EJERCICIO 12: Sumar Time Deltas a un 'datetime'
# Descripción: Al igual que con 'date', se pueden sumar o restar Time Deltas.
# Aquí se usa un Time Delta de 12 horas.
# =================================================================
# Time Delta de 12 horas
tdelta_12h = datetime.timedelta(hours=12)

# Sumar 12 horas a dt (12:30:45)
dt_plus_12h = dt + tdelta_12h
print(f"# DateTime original (12:30): {dt}")
print(f"# DateTime + 12 horas (debería ser el día siguiente a las 00:30): {dt_plus_12h}")


# =================================================================
# EJERCICIO 13: Constructores alternativos para obtener el tiempo actual (Naives)
# Funciones utilizadas: datetime.datetime.today(), datetime.datetime.now(), datetime.datetime.utcnow()
# Descripción: Métodos para obtener la fecha/hora local o UTC.
# - .today(): Devuelve la fecha/hora local actual sin zona horaria (TZ info es None).
# - .now(): Devuelve la fecha/hora local actual. Permite opcionalmente pasar una zona horaria.
#   Si se deja vacío, es similar a .today().
# - .utcnow(): Devuelve la hora UTC actual, pero la información de zona horaria (TZ info)
#   sigue siendo None, por lo que todavía es 'naive'.
# =================================================================
print(f"# Today (Local/Naive): {datetime.datetime.today()}")
print(f"# Now (Local/Naive): {datetime.datetime.now()}")
print(f"# UTC Now (UTC/Naive): {datetime.datetime.utcnow()}")


print("\n--- 5. DATETIMES CONSCIENTES DE ZONA HORARIA (AWARES) ---")

# Para trabajar con zonas horarias conscientes de reglas como el horario de verano,
# se recomienda usar la librería de terceros 'pytz', incluso según la documentación de Python.
# Se requiere instalar pytz: pip install pytz

try:
    import pytz

    # =================================================================
    # EJERCICIO 14: Creación de un DateTime consciente de UTC
    # Función utilizada: datetime.datetime.now(tz=pytz.UTC)
    # Descripción: Crea un objeto 'datetime' consciente de zona horaria, generalmente
    # utilizando UTC, lo cual es recomendado al trabajar con zonas horarias.
    # El método .now() permite pasar directamente la zona horaria (TZ).
    # =================================================================
    # Forma preferida de obtener la hora UTC actual y consciente de zona horaria
    dt_utc_aware = datetime.datetime.now(tz=pytz.UTC)
    print(f"# Current UTC Time (Aware): {dt_utc_aware}")
    # Nota: El formato muestra +00:00 o +00 para indicar el desplazamiento UTC.


    # =================================================================
    # EJERCICIO 15: Conversión a otra zona horaria
    # Función utilizada: .as_timezone(tz_object)
    # Descripción: Convierte un 'datetime' consciente de zona horaria (aware) a otra
    # zona horaria especificada.
    # La zona horaria se define usando pytz.timezone('nombre_zona').
    # =================================================================
    # Convertir de UTC a la Zona Horaria Montaña de EE. UU. (Mountain Time Zone)
    dt_mountain = dt_utc_aware.astimezone(pytz.timezone('US/Mountain'))
    print(f"# Convertido a US/Mountain Time: {dt_mountain}")
    # Nota: El formato muestra el desplazamiento correcto para Mountain (-06:00, por ejemplo).


    # =================================================================
    # EJERCICIO 16: Listar todas las zonas horarias disponibles
    # Función utilizada: pytz.all_timezones
    # Descripción: Proporciona una lista completa de todas las zonas horarias que
    # pytz soporta.
    # =================================================================
    # Solo imprimiremos un extracto, ya que la lista es muy larga.
    print("\n# Primeras 5 zonas horarias disponibles en pytz:")
    for i, tz in enumerate(pytz.all_timezones):
        if i < 5:
            print(f"  - {tz}")
        else:
            break


    print("\n--- 6. LOCALIZACIÓN DE DATETIMES NAIVES ---")

    # =================================================================
    # EJERCICIO 17: Convertir un datetime 'naive' local en 'aware' (Localizar)
    # Función utilizada: timezone.localize(naive_datetime)
    # Problema: Un objeto 'datetime' naive local (obtenido con datetime.now() sin tz)
    # no puede convertirse directamente a otra zona horaria usando .astimezone().
    # Solución: Primero debe ser 'localizado' a la zona horaria que representa.
    # =================================================================
    # 1. Obtener el datetime naive local actual (representando el tiempo Mountain)
    dt_local_naive = datetime.datetime.now()
    print(f"# Naive Local DateTime: {dt_local_naive}")

    # 2. Definir el objeto de zona horaria Mountain
    mt_tz = pytz.timezone('US/Mountain')

    # 3. Localizar el objeto naive usando .localize()
    # Esta función toma el objeto naive y le asigna la información de la zona horaria correcta.
    dt_mountain_aware = mt_tz.localize(dt_local_naive)
    print(f"# DateTime Localizado (Aware): {dt_mountain_aware}")

    # 4. Una vez localizado, se puede convertir a otra zona horaria (ej: US/Eastern)
    dt_eastern_aware = dt_mountain_aware.astimezone(pytz.timezone('US/Eastern'))
    print(f"# Convertido a US/Eastern Time: {dt_eastern_aware}")

except ImportError:
    print("\n--- SECCIÓN 5 Y 6 OMITIDA ---")
    print("# El paquete pytz no está instalado. Instálelo con 'pip install pytz' para ejecutar los ejemplos de zonas horarias.")

print("\n--- 7. FORMATEO Y PARSING DE STRINGS ---")

# =================================================================
# EJERCICIO 18: Formato ISO (International Standard)
# Función utilizada: .isoformat()
# Descripción: Convierte el objeto 'datetime' a una cadena en el formato ISO 8601,
# que es el formato preferido para guardar o pasar fechas internamente.
# =================================================================
dt_for_formatting = datetime.datetime.now() # Usamos una nueva hora local
print(f"# Formato ISO: {dt_for_formatting.isoformat()}")


# =================================================================
# EJERCICIO 19: Formato personalizado (DateTime a String)
# Función utilizada: .strftime(formato_código)
# Descripción: Convierte un objeto 'datetime' en una cadena con un formato específico
# utilizando códigos de formato (ej: %B para mes completo, %Y para año completo).
# =================================================================
# Formato deseado: Julio 26, 2016
custom_format = '%B %d, %Y'
# Usamos el dt creado previamente
formatted_string = dt.strftime(custom_format)
print(f"# Formato personalizado (strftime): {formatted_string}")


# =================================================================
# EJERCICIO 20: Conversión de String a DateTime (Parsing)
# Función utilizada: datetime.datetime.strptime(string_fecha, formato_código)
# Descripción: Es la función opuesta a strftime. Convierte una cadena (string)
# que representa una fecha en un objeto 'datetime'.
# Se debe especificar el formato exacto en el que está la cadena de entrada.
# =================================================================
dt_string = "July 26, 2016" # Cadena que queremos convertir
format_code = "%B %d, %Y" # El formato que tiene la cadena

# Convertir la cadena a un objeto datetime
dt_parsed = datetime.datetime.strptime(dt_string, format_code)
print(f"# String original: '{dt_string}'")
print(f"# String convertido a DateTime (strptime): {dt_parsed}")

# Resumen de funciones de formato:
# .strftime() (String Format Time): Convierte DateTime a String.
# .strptime() (String Parse Time): Convierte String a DateTime.
```