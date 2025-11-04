# 🧠 Serie de Ejercicios: De Principiante a Profesional con JSON y Python

## Ejercicio 1 — Cargando y accediendo a datos JSON
**🎯 Objetivo:** Convertir una cadena JSON en un diccionario y acceder a valores anidados.  
**🧩 Descripción:**  
Tienes la siguiente cadena JSON:

```python
json_data = '''
{
  "company": "TechNova",
  "employees": [
    {"name": "Alice", "role": "Engineer", "active": true},
    {"name": "Bob", "role": "Designer", "active": false}
  ]
}
'''
```

Convierte la cadena a un objeto Python y muestra:
- El nombre de la empresa  
- El nombre del primer empleado  
- El rol del segundo empleado  

💡 Usa `json.loads()` y acceso por índice/claves.

🧠 Nivel: 🟢 *Básico*

---

## Ejercicio 2 — Modificación de objetos JSON
**🎯 Objetivo:** Modificar y volver a convertir un objeto Python en JSON.  
**🧩 Descripción:**  
A partir del JSON anterior, cambia el valor `"active"` de Bob a `True`, agrega un nuevo empleado y convierte de nuevo el resultado a una cadena JSON con `indent=2`.

💡 Usa `json.dumps()` para la salida.

🧠 Nivel: 🟢 *Básico – Intermedio*

---

## Ejercicio 3 — Eliminación y filtrado de datos
**🎯 Objetivo:** Manipular listas dentro de JSON.  
**🧩 Descripción:**  
Crea un JSON que contenga una lista de productos, cada uno con `nombre`, `precio` y `disponible`.  
Elimina todos los productos cuyo precio sea mayor a 100.

💡 Itera sobre la lista y crea una nueva filtrada.

🧠 Nivel: 🟡 *Intermedio*

---

## Ejercicio 4 — Lectura desde archivo (json.load)
**🎯 Objetivo:** Cargar datos desde un archivo JSON.  
**🧩 Descripción:**  
Crea un archivo llamado `students.json` con el siguiente contenido:

```json
{
  "students": [
    {"name": "Laura", "age": 22, "grades": [9, 8, 10]},
    {"name": "Mario", "age": 20, "grades": [6, 7, 8]}
  ]
}
```

Cárgalo en Python con `json.load()` y calcula la nota media de cada estudiante.

💡 Usa `sum()` y `len()` para promediar.

🧠 Nivel: 🟡 *Intermedio*

---

## Ejercicio 5 — Escritura a archivo (json.dump)
**🎯 Objetivo:** Guardar resultados procesados en un archivo nuevo.  
**🧩 Descripción:**  
Usando el resultado del ejercicio anterior, genera un nuevo archivo `averages.json` con el nombre del estudiante y su promedio.

💡 Utiliza `json.dump(objeto, archivo, indent=2)`.

🧠 Nivel: 🟡 *Intermedio*

---

## Ejercicio 6 — Ordenación y formateo de salida
**🎯 Objetivo:** Crear una versión ordenada y legible del JSON.  
**🧩 Descripción:**  
Toma el JSON del ejercicio 3 (productos) y genera una versión legible con:
- indentación de 4 espacios  
- claves ordenadas alfabéticamente  

Guárdala como `productos_pretty.json`.

💡 Usa `json.dumps(data, indent=4, sort_keys=True)`.

🧠 Nivel: 🟡 *Intermedio*

---

## Ejercicio 7 — Validación y manejo de errores
**🎯 Objetivo:** Manejar errores de decodificación JSON.  
**🧩 Descripción:**  
Intenta cargar una cadena JSON **inválida** (por ejemplo, con comillas simples o una coma extra).  
Usa `try/except` para capturar el error y mostrar un mensaje amigable.

💡 Atrapa `json.JSONDecodeError`.

🧠 Nivel: 🟠 *Intermedio-Avanzado*

---

## Ejercicio 8 — Integración con APIs simuladas
**🎯 Objetivo:** Simular datos obtenidos desde una API.  
**🧩 Descripción:**  
Imagina que obtienes la siguiente respuesta de una API (cadena JSON):

```python
api_response = '''
{
  "status": "success",
  "data": {
    "users": [
      {"id": 1, "name": "Ana", "active": true},
      {"id": 2, "name": "Luis", "active": false}
    ]
  }
}
'''
```

Convierte esta respuesta a un objeto Python y genera una **lista de nombres de usuarios activos**.

💡 Accede a `data['data']['users']`.

🧠 Nivel: 🟠 *Intermedio-Avanzado*

---

## Ejercicio 9 — Anidamiento y escritura condicional
**🎯 Objetivo:** Crear JSON con estructura compleja a partir de datos.  
**🧩 Descripción:**  
Genera un objeto Python con esta estructura:

```json
{
  "departments": [
    {
      "name": "Sales",
      "employees": [
        {"name": "Carlos", "sales": 50},
        {"name": "Julia", "sales": 70}
      ]
    },
    {
      "name": "Engineering",
      "employees": [
        {"name": "Sofia", "projects": 3},
        {"name": "David", "projects": 5}
      ]
    }
  ]
}
```

Convierte el objeto a una cadena JSON **solo si el número total de empleados supera 3**.  
De lo contrario, imprime un mensaje.

💡 Combina estructuras anidadas y condicionales.

🧠 Nivel: 🔵 *Avanzado*

---

## Ejercicio 10 — Limpieza y normalización de datos JSON
**🎯 Objetivo:** Procesar JSON irregular o incompleto.  
**🧩 Descripción:**  
Tienes un JSON con usuarios, pero algunos campos están vacíos o son `null`.  
Crea una nueva lista que **ignore los usuarios incompletos** (sin nombre o sin email válido).

```python
json_data = '''
{
  "users": [
    {"name": "Eva", "email": "eva@mail.com"},
    {"name": null, "email": "no_name@mail.com"},
    {"name": "Pedro", "email": null}
  ]
}
'''
```

💡 Filtra usando condiciones en una comprensión de listas.

🧠 Nivel: 🔵 *Avanzado*

---

## Ejercicio 11 — Conversión entre JSON y otras fuentes de datos
**🎯 Objetivo:** Exportar JSON a CSV.  
**🧩 Descripción:**  
Crea un script que lea un JSON con una lista de personas (nombre, edad, país) y genere un archivo CSV con esas columnas.

💡 Combina `json.load()` con el módulo `csv`.

🧠 Nivel: 🔵 *Avanzado*

---

## Ejercicio 12 — Automatización profesional: JSON + API real
**🎯 Objetivo:** Simular un flujo profesional de datos.  
**🧩 Descripción:**  
Simula la respuesta de una API de clima como JSON:

```python
weather_data = '''
{
  "city": "Madrid",
  "forecast": [
    {"day": "Monday", "temp": 18, "rain": false},
    {"day": "Tuesday", "temp": 22, "rain": true}
  ]
}
'''
```

Procesa los datos para:
1. Mostrar solo los días con lluvia.  
2. Guardar el resultado en `rain_days.json`.  
3. Imprimir una cadena JSON formateada para enviar de vuelta a otra API.

🧠 Nivel: 🔴 *Profesional*

---

## Ejercicio 13 — Proyecto Final: Mini Gestor de Datos JSON
**🎯 Objetivo:** Integrar todos los conceptos.  
**🧩 Descripción:**  
Crea un pequeño script `gestor_json.py` que:
1. Cargue un archivo `employees.json`.  
2. Permita agregar, eliminar y modificar empleados (mediante input o funciones).  
3. Guarde los cambios automáticamente en `employees_updated.json`.  
4. Genere una versión legible (`pretty_employees.json`) con claves ordenadas.

💡 Usa `json.load`, `json.dump`, estructuras de control y funciones.

🧠 Nivel: 🔴 *Profesional / Proyecto completo*
