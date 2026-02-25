

# 🚀 Guía Profesional de Pipenv: Gestión de Entornos y Paquetes

```python
"""
EXPLICACIÓN PARA PRINCIPIANTES:
Imagina que Python es un taller de cocina. Si instalas todas tus herramientas (librerías) 
en una sola mesa, pronto no tendrás espacio y las migajas de un pastel ensuciarán tu sopa.

Pipenv es como crear una "Mini Cocina" privada para cada receta (proyecto). 
1. Crea el espacio (Entorno Virtual).
2. Compra los ingredientes (Pip / Paquetes).
3. Escribe una lista exacta para que otro chef haga lo mismo (Pipfile / Lock).

Ventaja profesional: Evitas el "En mi computadora sí funciona", porque Pipenv
garantiza que todos los desarrolladores usen exactamente las mismas versiones.
"""

# =========================================================
# EJEMPLO PRÁCTICO: FLUJO DE TRABAJO REAL
# =========================================================
import os

def flujo_proyecto_profesional():
    # 1. Instalamos una librería de desarrollo (solo para nosotros, no para el cliente)
    # Usamos pytest porque un profesional siempre prueba su código.
    print("Instalando herramientas de desarrollo...")
    os.system("pipenv install pytest --dev")

    # 2. Instalamos una librería de producción (la que necesita la app para funcionar)
    # 'requests' es el estándar para hacer peticiones web.
    print("Instalando librería de producción...")
    os.system("pipenv install requests")

    # 3. Consultamos el Grafo de Dependencias
    # Esto nos dice qué librerías instaló 'requests' por debajo (sus hijos).
    print("Mostrando jerarquía de paquetes...")
    os.system("pipenv graph")

    # 4. Generamos el archivo de seguridad (Lock)
    # Bloquea las versiones actuales para que nadie instale algo diferente por error.
    print("Bloqueando versiones para producción...")
    os.system("pipenv lock")

    # 5. Ejecutamos un script sin entrar a la consola manual
    # 'pipenv run' es la forma más limpia de ejecutar código aislado.
    print("Ejecutando script de prueba...")
    os.system("pipenv run python -c 'import requests; print(\"Conexión exitosa\")'")

# Para ejecutar este ejemplo, descomenta la línea de abajo:
# flujo_proyecto_profesional()

```

---

## 🛠️ 1. Conceptos Fundamentales

### ¿Por qué Pipenv y no solo Pip?

El flujo tradicional con `requirements.txt` tiene un problema: no especifica las sub-dependencias. Si una librería se actualiza hoy, tu proyecto podría romperse mañana. Pipenv introduce el **Pipfile.lock**, que utiliza **hashes (huellas digitales)** para asegurar que cada bit del paquete sea idéntico en cualquier máquina.

### Los dos archivos clave:

1. **Pipfile:** Es legible para humanos. Aquí defines qué quieres (ej. `requests = "*"`).
2. **Pipfile.lock:** Es para la máquina. Contiene versiones exactas y firmas de seguridad. **Nunca lo edites a mano.**

---

## 📂 2. Gestión del Ciclo de Vida del Proyecto

### Iniciar y Configurar

* **Especificar versión de Python:** Si tu servidor usa una versión específica, oblígale a Pipenv a usarla:
`pipenv --python 3.9`
* **Instalación desde cero:** Si acabas de clonar un proyecto de GitHub que tiene Pipenv:
`pipenv install` (Esto lee el Pipfile e instala todo).

### El comando "Mágico" de Producción

Cuando despliegues tu código en un servidor real, usa:
`pipenv install --deploy --ignore-pipfile`

> **Nota Pro:** El flag `--deploy` hará que el proceso falle si tu `Pipfile.lock` está desactualizado, y `--ignore-pipfile` asegura que se instale lo del Lock, no lo del Pipfile.

---

## 🛡️ 3. Seguridad y Mantenimiento

Un profesional no solo escribe código, lo protege.

* **Auditoría de Seguridad:**
`pipenv check`
Este comando escanea tus librerías contra una base de datos de vulnerabilidades conocidas (CVE). Si una librería es insegura, te avisará para que la actualices.
* **Limpieza de Entorno:**
Si instalaste paquetes con `pip` manual dentro del entorno y quieres limpiar todo para que coincida solo con tu Pipfile:
`pipenv clean`

---

## 🔑 4. Variables de Entorno (.env)

Pipenv tiene integración nativa con archivos `.env`.

1. Crea un archivo llamado `.env` en la raíz.
2. Escribe: `DB_PASSWORD=super_secreto`.
3. En tu código Python:

```python
import os
password = os.getenv('DB_PASSWORD') # Pipenv lo carga automáticamente

```

---

## 📝 5. Resumen de Comandos Rápidos

| Acción | Comando |
| --- | --- |
| **Crear entorno e instalar** | `pipenv install <paquete>` |
| **Instalar para test/dev** | `pipenv install <paquete> --dev` |
| **Entrar al entorno** | `pipenv shell` |
| **Salir del entorno** | `exit` |
| **Ver huecos de seguridad** | `pipenv check` |
| **Borrar todo el entorno** | `pipenv --rm` |
| **Ver dónde está el entorno** | `pipenv --venv` |

---

