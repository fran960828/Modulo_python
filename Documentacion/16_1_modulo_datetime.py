
"""
datetime_guia.py

Guía práctica y ejecutable sobre el módulo `datetime` de Python
Autor: Experto en Python (20 años)
Propósito: documentación paso a paso con ejemplos que suben en dificultad,
          pensados para principiantes que quieren llegar a nivel profesional.

Instrucciones:
 - Ejecuta: python datetime_guia.py
 - El script ofrece un menú para ejecutar cada ejemplo de forma aislada o todos.
 - Cada ejemplo está comentado con detalle; puedes copiar bloques a archivos
   pequeños para experimentar.

Cobertura:
 1. date: creación, atributos, isoformat
 2. time: creación y combinación con date -> datetime
 3. datetime naive vs aware, now(), utcnow(), timezone.utc
 4. formateo (strftime) y parseo (strptime)
 5. timedelta: aritmética, diferencias y total_seconds
 6. zoneinfo: timezones IANA, astimezone, conversión entre zonas (incluye fallback)
 7. DST y `fold` (ambigüedad en horarios de cambio de hora)
 8. timestamps Unix y fromtimestamp / timestamp
 9. ISO 8601, fromisoformat, manejo de 'Z' (UTC)
10. Serialización (JSON-safe) y buenas prácticas
11. Scheduling simple (recurrencias con timedelta) y notas profesionales
12. Errores comunes y checklist profesional

Notas importantes:
 - Diferencia clave: **naive** datetimes no llevan info de zona; **aware** sí.
 - No mezcles aware y naive en operaciones (TypeError).
 - Para soporte de zonas IANA usamos `zoneinfo` (Python 3.9+). Si tu Python
   es más antiguo tendrás que instalar backports.zoneinfo o usar pytz.
"""

from datetime import date, time, datetime, timedelta, timezone
from typing import Optional, List
import json

# Intentamos usar zoneinfo (estándar desde Python 3.9). Si no está, avisamos.
try:
    from zoneinfo import ZoneInfo  # type: ignore
    _HAS_ZONEINFO = True
except Exception:
    ZoneInfo = None  # type: ignore
    _HAS_ZONEINFO = False

# -------------------------
# Ejemplo 1: date (básico)
# -------------------------
def ejemplo_1_date_basico():
    print("\n=== Ejemplo 1: date (básico) ===")
    # Crear la fecha actual (solo fecha, sin tiempo)
    hoy = date.today()
    print("date.today() ->", hoy, type(hoy))

    # Crear una fecha específica
    fecha = date(2023, 3, 15)  # año, mes, día
    print("date(2023,3,15) ->", fecha)
    # Acceder a componentes
    print("Año:", fecha.year, "Mes:", fecha.month, "Día:", fecha.day)

    # Representaciones útiles
    print("ISO:", fecha.isoformat())         # 'YYYY-MM-DD'
    print("Tupla (year, month, day):", fecha.timetuple()[:3])

    # Comparaciones directas entre dates
    otra = date(2024, 1, 1)
    print("¿fecha < otra?", fecha < otra)   # True si fecha anterior


# -----------------------------------------
# Ejemplo 2: time y datetime.combine
# -----------------------------------------
def ejemplo_2_time_combine():
    print("\n=== Ejemplo 2: time y combinaciones ===")
    # time: hora/minuto/segundo/microsegundo opcional
    t = time(14, 30, 15, 123456)  # 14:30:15.123456
    print("time(14,30,15,123456) ->", t)
    print("Componentes:", t.hour, t.minute, t.second, t.microsecond)

    # Combinar date + time -> datetime (naive por defecto)
    fecha = date(2025, 10, 6)
    dt = datetime.combine(fecha, t)
    print("datetime.combine(date, time) ->", dt, type(dt))

    # También podemos crear datetime directamente
    dt2 = datetime(2025, 10, 6, 14, 30, 15, 123456)
    print("datetime(...) igual a combine?:", dt == dt2)


# -----------------------------------------------------
# Ejemplo 3: datetime naive vs aware, now() vs utcnow()
# -----------------------------------------------------
def ejemplo_3_naive_aware():
    print("\n=== Ejemplo 3: datetime naive vs aware ===")
    # naive: no contiene información de zona horaria
    ahora_naive = datetime.now()
    print("datetime.now() (naive) ->", ahora_naive, "tzinfo:", ahora_naive.tzinfo)

    # utcnow() también produce naive, representando UTC pero sin tzinfo
    ahora_utc_naive = datetime.utcnow()
    print("datetime.utcnow() (naive) ->", ahora_utc_naive, "tzinfo:", ahora_utc_naive.tzinfo)

    # Crear aware usando timezone.utc
    ahora_utc_aware = datetime.now(timezone.utc)
    print("datetime.now(timezone.utc) (aware) ->", ahora_utc_aware, "tzinfo:", ahora_utc_aware.tzinfo)

    # No mezcles naive y aware en operaciones -> TypeError
    try:
        _ = ahora_naive - ahora_utc_aware
    except TypeError as e:
        print("Operación naive - aware -> TypeError (ejemplo):", e)

    # Convertir naive a aware *siempre* conociendo su zona real:
    # Si tienes un naive que representa UTC, usa replace(tzinfo=timezone.utc)
    supuesto_utc = ahora_utc_naive.replace(tzinfo=timezone.utc)
    print("Naive convertido con replace(tzinfo=utc) ->", supuesto_utc)


# ------------------------------------------
# Ejemplo 4: formateo (strftime) y parseo
# ------------------------------------------
def ejemplo_4_strftime_strptime():
    print("\n=== Ejemplo 4: strftime y strptime ===")
    dt = datetime(2025, 10, 6, 9, 5, 3)  # 2025-10-06 09:05:03
    # strftime: formatear a string
    s = dt.strftime("%Y-%m-%d %H:%M:%S")
    print("strftime ->", s)

    # strptime: parsear string a datetime (note: devuelve naive si no hay info de zona)
    parsed = datetime.strptime("2025-10-06 09:05:03", "%Y-%m-%d %H:%M:%S")
    print("strptime ->", parsed, "tzinfo:", parsed.tzinfo)

    # Ejemplos comunes de formatos:
    print("Formatos útiles:")
    print(" - Fecha ISO corta:", dt.strftime("%Y-%m-%d"))
    print(" - Hora con AM/PM:", dt.strftime("%I:%M %p"))


# ------------------------------------------
# Ejemplo 5: timedelta - aritmética y diferencia
# ------------------------------------------
def ejemplo_5_timedelta():
    print("\n=== Ejemplo 5: timedelta (aritmética) ===")
    hoy = date.today()
    print("Hoy:", hoy)

    # Sumar días a una fecha
    dentro_de_10 = hoy + timedelta(days=10)
    print("Hoy + 10 días ->", dentro_de_10)

    # Restar fechas -> timedelta
    diff = dentro_de_10 - hoy
    print("dentro_de_10 - hoy ->", diff, "dias:", diff.days)

    # Timedelta en horas, minutos, segundos y total_seconds
    dt1 = datetime(2025, 10, 6, 8, 0, 0)
    dt2 = dt1 + timedelta(hours=2, minutes=30)
    print("dt1:", dt1, "dt2:", dt2)
    print("Diferencia segundos:", (dt2 - dt1).total_seconds())

    # Multiplicar y dividir timedeltas
    doble = timedelta(days=2) * 2
    mitad = timedelta(days=1) / 2
    print("doble:", doble, "mitad:", mitad)


# ---------------------------------------------------------
# Ejemplo 6: zoneinfo (IANA) — crear aware, astimezone()
# ---------------------------------------------------------
def ejemplo_6_zoneinfo_basico():
    print("\n=== Ejemplo 6: zoneinfo (Zonas IANA) ===")
    if not _HAS_ZONEINFO:
        print("AVISO: zoneinfo no disponible en este intérprete.")
        print("Si tu Python < 3.9, instala backports.zoneinfo o usa pytz.")
        return

    # Crear datetime aware en zona concreta
    madrid = ZoneInfo("Europe/Madrid")
    ny = ZoneInfo("America/New_York")

    # Ahora en hora local de Madrid
    ahora_madrid = datetime.now(madrid)
    print("Ahora Madrid (aware):", ahora_madrid, "tz:", ahora_madrid.tzinfo)

    # Convertir a otra zona con astimezone
    ahora_ny = ahora_madrid.astimezone(ny)
    print("Misma instant en New York:", ahora_ny, "tz:", ahora_ny.tzinfo)

    # Crear aware desde valores conocidos
    dt_naive = datetime(2025, 3, 30, 2, 30)  # potencialmente cerca de cambio DST
    dt_madrid = dt_naive.replace(tzinfo=madrid)
    print("dt_naive.replace(tzinfo=madrid) ->", dt_madrid)


# ---------------------------------------------------------
# Ejemplo 7: DST y `fold` — manejar ambigüedad en retroceso
# ---------------------------------------------------------
def ejemplo_7_dst_fold():
    print("\n=== Ejemplo 7: DST y fold (ambigüedad) ===")
    if not _HAS_ZONEINFO:
        print("AVISO: zoneinfo no disponible, omitiendo ejemplo DST/fold.")
        return

    # Ejemplo en Nueva York: cambio de hora (fall back) típico en noviembre:
    # El 1er periodo 01:30 ocurre dos veces (antes y después del retroceso).
    ny = ZoneInfo("America/New_York")

    # Creamos dos datetimes con la misma representación local, pero diferentes instancias UTC:
    # fold=0 -> la primera ocurrencia (antes del retroceso), fold=1 -> la segunda (después del retroceso)
    # Nota: Python 3.6+ soporta 'fold' en datetime
    dt_first = datetime(2021, 11, 7, 1, 30, fold=0, tzinfo=ny)
    dt_second = datetime(2021, 11, 7, 1, 30, fold=1, tzinfo=ny)

    # Convertimos a UTC para ver que son instantes distintos
    utc_first = dt_first.astimezone(timezone.utc)
    utc_second = dt_second.astimezone(timezone.utc)
    print("NY 2021-11-07 01:30 fold=0 -> UTC:", utc_first)
    print("NY 2021-11-07 01:30 fold=1 -> UTC:", utc_second)
    print("¿Son iguales instantes?", utc_first == utc_second, "-> deberían ser False")


# ---------------------------------------------------------
# Ejemplo 8: timestamps Unix y conversiones
# ---------------------------------------------------------
def ejemplo_8_timestamps():
    print("\n=== Ejemplo 8: timestamps Unix ===")
    # Obtener timestamp actual (segundos desde epoch) usando datetime aware
    now_utc = datetime.now(timezone.utc)
    ts = now_utc.timestamp()  # float segundos (incluye fracciones)
    print("Ahora UTC:", now_utc)
    print("Timestamp (segundos):", ts)

    # Reconstruir datetime desde timestamp
    dt_from_ts_utc = datetime.fromtimestamp(ts, tz=timezone.utc)
    print("fromtimestamp(ts, tz=utc) ->", dt_from_ts_utc)

    # También existe utcfromtimestamp (devuelve naive UTC)
    naive_utc = datetime.utcfromtimestamp(ts)
    print("utcfromtimestamp(ts) (naive, representa UTC):", naive_utc, "tzinfo:", naive_utc.tzinfo)


# ---------------------------------------------------------
# Ejemplo 9: ISO 8601 y fromisoformat (manipulaciones comunes)
# ---------------------------------------------------------
def ejemplo_9_iso_fromisoformat():
    print("\n=== Ejemplo 9: ISO 8601 e fromisoformat ===")
    # ISO 8601 con offset: '2025-10-06T09:05:03+02:00'
    s = "2025-10-06T09:05:03+02:00"
    dt = datetime.fromisoformat(s)  # desde Python 3.7+ soporta offset
    print("fromisoformat:", dt, "tzinfo:", dt.tzinfo)

    # Nota: datetime.fromisoformat no acepta 'Z' (literal) para UTC; tenemos que reemplazarlo:
    s_z = "2025-10-06T07:05:03Z"
    s_z_fixed = s_z.replace("Z", "+00:00")
    dt_z = datetime.fromisoformat(s_z_fixed)
    print("fromisoformat con 'Z' reemplazado:", dt_z, dt_z.tzinfo)

    # Serializar a ISO
    now = datetime.now(timezone.utc)
    print("now.isoformat() ->", now.isoformat())  # incluye offset +00:00


# ---------------------------------------------------------
# Ejemplo 10: Serialización JSON-safe y best practices
# ---------------------------------------------------------
def ejemplo_10_serializacion_json():
    print("\n=== Ejemplo 10: Serialización (JSON) ===")
    # datetime no es JSON serializable por defecto. Convención: usar ISO strings en UTC.
    dt = datetime(2025, 10, 6, 9, 5, 3, tzinfo=timezone.utc)

    # Serializar -> string ISO (seguro y legible)
    iso = dt.isoformat()
    print("ISO serializado:", iso)

    # En el receptor: parsear con fromisoformat (reparar 'Z' si fuera necesario)
    reparsed = datetime.fromisoformat(iso)
    print("Reconstruido con fromisoformat:", reparsed, "tzinfo:", reparsed.tzinfo)

    # Ejemplo de serialización en JSON
    obj = {"event": "backup", "time": iso}
    s_json = json.dumps(obj)
    print("JSON:", s_json)

    # Buenas prácticas:
    # - Serializa en UTC (evita ambigüedad).
    # - Incluye el offset '+00:00' o usa 'Z' pero acuerda formato en tu API.


# ---------------------------------------------------------
# Ejemplo 11: Scheduling simple con timedelta (recurrencias)
# ---------------------------------------------------------
def ejemplo_11_scheduling_simple():
    print("\n=== Ejemplo 11: Scheduling simple con timedelta ===")
    start = datetime(2025, 10, 6, 9, 0, tzinfo=timezone.utc)
    interval = timedelta(days=7)  # evento semanal

    # Generar las próximas 5 ocurrencias (simple, no considera calendarios ni días laborables)
    ocurrencias = [start + i * interval for i in range(5)]
    print("Próximas 5 ocurrencias (semanal):")
    for o in ocurrencias:
        print(" -", o)

    # Si necesitas reglas más avanzadas (días laborables, último día del mes, etc.),
    # emplea librerías como `dateutil.rrule` o calendarios específicos (no mostrado aquí).


# ---------------------------------------------------------
# Ejemplo 12: Errores comunes y checklist profesional
# ---------------------------------------------------------
def ejemplo_12_errores_checklist():
    print("\n=== Ejemplo 12: Errores comunes y checklist profesional ===")
    print("1) No mezcles naive y aware en operaciones -> TypeError.")
    print("2) Evita asumir que datetime.now() es UTC; usa timezone.utc si necesitas UTC.")
    print("3) Para APIs, serializa en ISO 8601 con offset y preferiblemente en UTC.")
    print("4) Para zonas horarias use zoneinfo (IANA); evita offsets estáticos cuando haya DST.")
    print("5) Ten cuidado con ambigüedad en DST: usa fold al reconstruir instantes locales.")
    print("6) Para recurrencias complejas no reiventes la rueda: usa dateutil o librerías de dominio.")
    print("7) Documenta claramente si tus timestamps están en UTC o en hora local del servidor.")


# -------------------------
# Menú para ejecutar ejemplos
# -------------------------
ejemplos = {
    "1": ("date básico", ejemplo_1_date_basico),
    "2": ("time y combine", ejemplo_2_time_combine),
    "3": ("naive vs aware (now/utcnow)", ejemplo_3_naive_aware),
    "4": ("strftime / strptime (formateo y parseo)", ejemplo_4_strftime_strptime),
    "5": ("timedelta (aritmética)", ejemplo_5_timedelta),
    "6": ("zoneinfo: zonas IANA y astimezone", ejemplo_6_zoneinfo_basico),
    "7": ("DST y fold (ambigüedad)", ejemplo_7_dst_fold),
    "8": ("timestamps Unix", ejemplo_8_timestamps),
    "9": ("ISO 8601 y fromisoformat", ejemplo_9_iso_fromisoformat),
    "10": ("Serialización JSON-safe", ejemplo_10_serializacion_json),
    "11": ("Scheduling simple con timedelta", ejemplo_11_scheduling_simple),
    "12": ("Errores comunes / checklist", ejemplo_12_errores_checklist),
}

def menu():
    print("=== Guía: módulo datetime (ejecutable) ===")
    if not _HAS_ZONEINFO:
        print("AVISO: zoneinfo no disponible. Algunos ejemplos relacionados con zonas IANA se omitirán.")
        print("Si tu Python <3.9 puedes instalar backports.zoneinfo o usar pytz (cuidado con la API).")
    while True:
        print("\nElige un ejemplo (número), 'a' para todos, o 'q' para salir:")
        for k, (desc, _) in ejemplos.items():
            print(f" {k}. {desc}")
        elec = input(">>> ").strip().lower()
        if elec in ("q", "exit", "salir"):
            print("Saliendo.")
            break
        if elec == "a":
            for k in sorted(ejemplos.keys(), key=int):
                print("\n" + "-" * 60)
                print(f"Ejecutando {k}. {ejemplos[k][0]}")
                try:
                    ejemplos[k][1]()
                except Exception as e:
                    print("Error al ejecutar ejemplo", k, ":", e)
            print("\nTodos los ejemplos ejecutados.")
            continue
        if elec in ejemplos:
            try:
                ejemplos[elec][1]()
            except Exception as e:
                print("Error al ejecutar ejemplo:", e)
        else:
            print("Opción no válida. Introduce el número del ejemplo, 'a' o 'q'.")


if __name__ == "__main__":
    menu()
