Esta documentación técnica está diseñada para enseñarte a gestionar el "alma" de tu aplicación: los datos. En el desarrollo profesional de Django, a menudo necesitamos mover información de un ordenador a otro, hacer copias de seguridad antes de una actualización crítica o precargar datos por defecto (como una lista de países o categorías). Para ello, Django nos ofrece un sistema de **Serialización**, que convierte los registros de la base de datos en archivos de texto y viceversa.

---

## 1. Conceptos Clave: dumpdata y loaddata

> **Explicación:** > \* **`dumpdata`**: Es el comando que "vuelca" (extrae) los datos de tu base de datos y los convierte en un archivo de texto plano. Piensa en ello como una "foto" de tus datos en un momento dado.
>
> - **`loaddata`**: Es el comando inverso. Toma un archivo de texto generado previamente y "carga" esos datos en la base de datos actual.
>
> **Formatos soportados:**
>
> 1. **JSON (JavaScript Object Notation):** El estándar de la industria. Es ligero, fácil de leer para humanos y máquinas, y es el formato por defecto de Django.
> 2. **XML:** Más verboso y antiguo. Útil si necesitas integrar los datos con sistemas empresariales legacy.
> 3. **YAML:** Muy limpio y legible (parecido a Python), pero requiere instalar una librería adicional (`PyYAML`).

---

## 2. Usos Profesionales de la Gestión de Datos

A nivel laboral, no solo usamos esto para "copiar y pegar". Sus aplicaciones son vitales:

- **Backups (Copias de seguridad):** Guardar el estado de la web antes de una migración peligrosa.
- **Migración de Base de Datos:** Por ejemplo, pasar de SQLite (desarrollo) a MySQL/PostgreSQL (producción).
- **Fixtures (Datos Iniciales):** Cargar automáticamente categorías, tipos de usuario o productos iniciales cuando alguien instala tu app por primera vez.
- **Testing:** Cargar un conjunto de datos específico para probar que un buscador o un filtro funciona correctamente.
- **Entornos de Desarrollo Colaborativo:** Pasar a un compañero los últimos cursos creados para que trabaje sobre datos reales.

---

## 3. Uso de Fixtures para Datos Iniciales

> **Explicación:** Una "fixture" es simplemente un archivo (normalmente JSON) que Django busca dentro de una carpeta llamada `fixtures/` en tu aplicación. Si ejecutas `loaddata`, Django sabrá encontrarlo automáticamente.

**Ejemplo de estructura:**

1. Crea la carpeta: `tu_app/fixtures/`
2. Crea el archivo: `categorias.json`

```json
[
  {
    "model": "tu_app.categoria",
    "pk": 1,
    "fields": {
      "nombre": "Programación",
      "slug": "programacion"
    }
  }
]
```

---

## 4. Sintaxis y Comandos Básicos

### Extraer datos (dumpdata)

Para hacer una copia de seguridad profesional, usamos el siguiente comando:

```bash
# --format: especificamos json
# --indent 4: para que el archivo sea legible (con espacios)
# --output: nombre del archivo de salida
# apps.Modelo: opcional, si quieres solo una tabla específica
python manage.py dumpdata --format=json --indent=4 --output=backup_total.json

```

### Cargar datos (loaddata)

Para restaurar esa copia o cargar una fixture:

```bash
# Django buscará el archivo en la raíz o en las carpetas 'fixtures' de tus apps
python manage.py loaddata backup_total.json

```

---

## 5. Migración de SQLite a MySQL

Este es uno de los procesos más delicados en el despliegue de una app profesional. El flujo es el siguiente:

### Paso 1: Instalar el conector MySQL

Para que Django pueda hablar con MySQL, necesitamos una librería llamada `mysqlclient`.

```bash
# Con pipenv
pipenv install mysqlclient

```

_Nota: En algunos sistemas podrías necesitar instalar antes las librerías de desarrollo de MySQL (`default-libmysqlclient-dev` en Ubuntu o `mysql-connector-c` en Mac)._

### Paso 2: Extraer datos de SQLite

Con SQLite aún configurado en `settings.py`:

```bash
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 4 --output=datos_migracion.json

```

_Tip Pro: Excluimos `auth.permission` y `contenttypes` porque Django los regenera automáticamente al migrar y suelen dar errores de duplicidad._

### Paso 3: Cambiar a MySQL en `settings.py`

Configuramos la nueva base de datos (vacía):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_bd',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```

### Paso 4: Crear la estructura y cargar datos

```bash
# 1. Creamos las tablas vacías en MySQL
python manage.py migrate

# 2. Cargamos los datos extraídos de SQLite
python manage.py loaddata datos_migracion.json

```

---

## 6. Verificación de Seguridad

- **Codificación:** Asegúrate siempre de que tus archivos JSON estén en **UTF-8** para evitar problemas con tildes o eñes.
- **Orden de carga:** Si tus modelos tienen claves foráneas (`ForeignKeys`), `loaddata` es inteligente y suele manejar el orden, pero asegúrate de que los archivos de datos contengan todas las dependencias necesarias.

¿Te gustaría que viéramos cómo automatizar este proceso para que se genere un **backup diario** de tu base de datos de forma automática en el servidor?
