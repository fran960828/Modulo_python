# 🕒 Colección de Ejercicios – Módulo `datetime` (Python)

Esta guía contiene una colección de ejercicios prácticos sobre el módulo `datetime` en Python, diseñados para aprender y dominar el trabajo con fechas, horas, zonas horarias, formateo y parsing.

---

## 🟢 Nivel 1 – Fundamentos del módulo `datetime`

### 🧩 Ejercicio 1 – Crear y mostrar fechas básicas
Crea una fecha que represente el **15 de marzo de 2025**.  
Imprime el año, mes y día por separado en una sola línea, separados por guiones.

> 💡 *Habilidad:* creación de objetos `date` y acceso a atributos.

---

### 🧩 Ejercicio 2 – Día de la semana
Crea un `date` para tu cumpleaños y muestra qué día de la semana fue (usando `weekday()` y `isoweekday()`).  
> 🔍 *Reto:* Muestra el nombre del día en texto (“lunes”, “martes”, etc.).  
> 💡 *Habilidad:* interpretación de enteros devueltos por `weekday()`.

---

### 🧩 Ejercicio 3 – Fecha actual + nombre del mes
Muestra la fecha de hoy con el formato `10 de noviembre de 2025` (usando `.today()` y `.strftime()`).  
> 💡 *Habilidad:* formateo básico con códigos `%d`, `%B`, `%Y`.

---

## 🟡 Nivel 2 – Operaciones con `timedelta`

### 🧩 Ejercicio 4 – Fecha futura y pasada
Calcula qué fecha será dentro de **45 días** y cuál fue hace **90 días** a partir de hoy.  
> 💡 *Habilidad:* suma y resta de `timedelta` sobre fechas.

---

### 🧩 Ejercicio 5 – Diferencia entre dos fechas
Calcula cuántos días faltan para el 1 de enero del próximo año.  
> 🔍 *Reto:* Muestra también el total en horas y segundos.  
> 💡 *Habilidad:* restar fechas y usar `.days`, `.total_seconds()`.

---

### 🧩 Ejercicio 6 – Edad exacta
Pide al usuario (o define manualmente) su fecha de nacimiento y calcula su edad exacta en años, meses y días.  
> 💡 *Habilidad:* diferencia entre fechas y lógica de años/meses.

---

## 🔵 Nivel 3 – `datetime` completo (fecha + hora)

### 🧩 Ejercicio 7 – Creación y acceso
Crea un objeto `datetime` que represente **el 31 de diciembre de 2025 a las 23:59:59** y muestra solo la hora.  
> 💡 *Habilidad:* construir objetos `datetime`, usar `.time()` y `.hour`.

---

### 🧩 Ejercicio 8 – Ajuste de hora con `timedelta`
A partir de un `datetime` de una reunión (por ejemplo, hoy a las 10:00 a.m.), calcula la hora de finalización si dura 2 horas y 45 minutos.  
> 💡 *Habilidad:* usar `timedelta(hours=..., minutes=...)`.

---

### 🧩 Ejercicio 9 – Combinar fecha y hora
Usa `datetime.combine()` para crear un objeto que combine la fecha actual con una hora personalizada (por ejemplo, 18:30).  
> 💡 *Habilidad:* combinación de `date` y `time`.

---

### 🧩 Ejercicio 10 – Comparaciones
Crea dos `datetime` (por ejemplo, inicio y fin de un evento) y determina si el evento ya terminó y cuánto duró en horas.  
> 💡 *Habilidad:* comparación de `datetime` y resta.

---

## 🟣 Nivel 4 – Zonas horarias (`pytz` y `zoneinfo`)

### 🧩 Ejercicio 11 – UTC actual (aware)
Obtén la hora UTC actual como un objeto *aware* y muéstrala junto con el desplazamiento de zona.  
> 💡 *Habilidad:* `datetime.now(tz=pytz.UTC)` o `datetime.now(ZoneInfo("UTC"))`.

---

### 🧩 Ejercicio 12 – Conversión de zona horaria
Convierte la hora UTC actual a:  
- Nueva York (`US/Eastern`)  
- Madrid (`Europe/Madrid`)  
- Tokio (`Asia/Tokyo`)  
> 💡 *Habilidad:* `.astimezone()` y comprensión del desplazamiento horario.

---

### 🧩 Ejercicio 13 – Localización de hora
Simula que un usuario te da una hora “local” (sin zona horaria). Por ejemplo: “2025-11-10 14:30”.  
Localízala correctamente como hora de Buenos Aires (`America/Argentina/Buenos_Aires`).  
> 💡 *Habilidad:* `timezone.localize()` o `ZoneInfo` equivalente.

---

### 🧩 Ejercicio 14 – Calcular diferencias entre zonas
Calcula cuántas horas de diferencia hay entre las zonas `Asia/Tokyo` y `America/Los_Angeles` *en este momento exacto*.  
> 💡 *Habilidad:* convertir ambos a UTC y comparar.

---

## 🔴 Nivel 5 – Formateo y Parsing

### 🧩 Ejercicio 15 – Formateo personalizado
Formatea un `datetime` en el estilo:  
`Lunes, 10 de Noviembre de 2025 - 14:30:00`  
> 💡 *Habilidad:* uso avanzado de `.strftime()` con códigos `%A`, `%d`, `%B`, `%Y`, `%H`, `%M`, `%S`.

---

### 🧩 Ejercicio 16 – Parsing de string
Convierte la cadena `"2025-07-04 18:45"` a un objeto `datetime` y súmale 3 horas.  
> 💡 *Habilidad:* `strptime()` + `timedelta`.

---

### 🧩 Ejercicio 17 – ISO y parsing inverso
Convierte un `datetime` a formato ISO (`.isoformat()`), guárdalo en una variable string, y luego recupéralo con `fromisoformat()`.  
> 💡 *Habilidad:* serialización y deserialización ISO 8601.

---

## ⚫ Nivel 6 – Casos Profesionales (Integración y Aplicaciones Reales)

### 🧩 Ejercicio 18 – Registro de logs
Simula un sistema de logs que registra eventos con hora UTC (`datetime.now(tz=pytz.UTC)`).  
Cada vez que imprimas un evento, agrega una marca de tiempo ISO.  
> 🔍 *Reto:* Muestra además la hora local del usuario.  
> 💡 *Habilidad:* uso profesional de timestamps y UTC consistentes.

---

### 🧩 Ejercicio 19 – Planificador internacional
Dado un evento programado en horario de Madrid (`Europe/Madrid`), muestra automáticamente la hora equivalente en Nueva York y Tokio.  
> 🔍 *Reto:* Usa `input()` para pedir la hora en Madrid en formato `"YYYY-MM-DD HH:MM"`.  
> 💡 *Habilidad:* parsing, localización y conversión entre zonas.

---

### 🧩 Ejercicio 20 – Diferencia promedio de llegada
Tienes una lista de timestamps ISO de entregas realizadas por repartidores.  
Calcula la media del tiempo transcurrido entre cada entrega (en minutos).  
> 💡 *Habilidad:* parsing de múltiples fechas y cálculo estadístico con `timedelta`.

---

### 🧩 Ejercicio 21 – Validación de horarios laborales
Dada una hora local introducida por el usuario, determina si cae dentro del horario laboral (09:00–18:00) de su zona.  
> 🔍 *Reto:* Si no, muestra cuántas horas faltan para el próximo inicio de jornada.  
> 💡 *Habilidad:* manipulación condicional de `datetime.time`.

---

### 🧩 Ejercicio 22 – Cálculo de duración de vuelo
Simula un vuelo que sale de Londres (`Europe/London`) a las 22:15 y llega a Nueva York (`America/New_York`) a las 01:05 del día siguiente (hora local).  
Calcula la **duración real del vuelo** en horas.  
> 💡 *Habilidad:* `pytz` o `zoneinfo`, awareness, diferencias entre zonas.

---

### 🧩 Ejercicio 23 – Cronómetro o temporizador
Implementa un pequeño cronómetro que mida cuánto tarda en ejecutarse un bloque de código (por ejemplo, un bucle grande).  
> 💡 *Habilidad:* uso de `datetime.now()` para medir duración real de procesos.

---

### 🧩 Ejercicio 24 – Generador de reportes semanales
Genera una lista con las fechas de todos los **lunes** de un año determinado.  
> 🔍 *Reto:* Imprime también el número de semana ISO (`isocalendar()`).  
> 💡 *Habilidad:* iteración con `timedelta(days=7)` y uso de métodos ISO.

---

## 🧠 Meta Final – Proyecto Integrador (Ejercicio 25)

### 🧩 Ejercicio 25 – Dashboard de Fechas Inteligente
Crea un script que:
1. Muestre la fecha y hora actual en UTC y en tu zona local.  
2. Calcule automáticamente:
   - La fecha del próximo domingo.  
   - Cuántos días quedan para fin de año.  
3. Acepte una entrada de fecha en texto (en cualquier formato entre varios posibles) y la normalice a formato ISO.  
4. Permita convertir esa fecha a cualquier zona horaria elegida por el usuario (con `pytz` o `zoneinfo`).  
> 💡 *Habilidad:* integración total de `datetime`, `timedelta`, `strftime`, `strptime`, `pytz`/`zoneinfo`.

---

## 🏁 Conclusión

Con esta secuencia de **25 ejercicios progresivos**, dominarás todas las capacidades del módulo `datetime` en Python.

| Tema | Nivel de dominio alcanzado |
|------|-----------------------------|
| Fechas y horas básicas | ✅ Fluido |
| Operaciones con `timedelta` | ✅ Práctico |
| Uso de `datetime` completo | ✅ Intermedio |
| Zonas horarias y conversión | ✅ Avanzado |
| Formateo y parsing | ✅ Profesional |
| Casos reales y automatización | ✅ Experto |
