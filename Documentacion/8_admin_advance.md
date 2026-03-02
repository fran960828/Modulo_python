## 1. Gestión de Usuarios y Permisos

> **Explicación:** Un usuario en Django no es solo un login. Tiene tres niveles de acceso:
>
> - **Active (is_active):** Si es `False`, el usuario no puede loguearse (útil para "borrar" sin perder datos).
> - **Staff (is_staff):** Permite entrar al panel `/admin`.
> - **Superuser (is_superuser):** Tiene todos los permisos automáticamente.

```python
from django.contrib.auth.models import User

# Creación profesional de un usuario de Staff (no superusuario)
usuario = User.objects.create_user(username='pedro', password='123')
usuario.is_staff = True
usuario.is_active = True
usuario.save()

```

---

## 2. Grupos y Permisos Granulares

> **Explicación:** Los permisos se dividen en: `add`, `change`, `delete` y `view`. En lugar de asignar permisos uno a uno a 100 usuarios, creamos un **Grupo** (ej: "Editores"), le asignamos permisos y metemos a los usuarios ahí.

```python
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import Libro

# 1. Crear el grupo
grupo_editores, created = Group.objects.get_or_create(name='Editores')

# 2. Buscar el permiso específico para el modelo Libro
content_type = ContentType.objects.get_for_model(Libro)
permiso_cambio = Permission.objects.get(codename='change_libro', content_type=content_type)

# 3. Asignar permiso al grupo y usuario al grupo
grupo_editores.permissions.add(permiso_cambio)
usuario.groups.add(grupo_editores)

```

---

## 3. Ayuda de Comandos (`manage.py help`)

> **Explicación:** Django es enorme. Si olvidas cómo se usa un comando, `help` te muestra la documentación integrada.

```bash
# Lista todos los comandos disponibles (incluyendo los de librerías instaladas)
python manage.py help

# Muestra cómo usar un comando específico (ej: cómo cambiar una contraseña)
python manage.py help changepassword

```

---

## 4. Estética Avanzada: `django-grappelli`

> **Explicación:** Grappelli cambia el look visual del Admin de Django por uno más moderno y añade utilidades como menús desplegables.

1. **Instalar:** `pip install django-grappelli`
2. **Configurar (`settings.py`):** **MUY IMPORTANTE:** Debe ir **antes** de `django.contrib.admin`.

```python
INSTALLED_APPS = [
    'grappelli', # Siempre antes de admin
    'django.contrib.admin',
    # ...
]

```

---

## 5. Optimización: `django-debug-toolbar` (DDT)

> **Explicación:** Es una barra lateral que aparece en el navegador (solo en desarrollo) para auditar el rendimiento.

1. **Instalar:** `pip install django-debug-toolbar`
2. **Configurar:** Requiere añadir un Middleware y configurar `INTERNAL_IPS`.

### Herramientas clave de DDT:

- **SQL:** Te dice cuántas consultas se hicieron y cuánto tardaron (ideal para detectar el problema N+1).
- **Static Files:** Muestra qué archivos estáticos se están cargando.
- **Templates:** Te dice qué plantillas y bloques se renderizaron.

---

## 6. Superpoderes con `django-extensions`

> **Explicación:** Una navaja suiza de comandos extra para la terminal.

1. **Instalar:** `pip install django-extensions`
2. **Configurar:** Añadir `'django_extensions'` a `INSTALLED_APPS`.

### Comandos Imprescindibles:

- **`shell_plus`:** Abre la shell importando **todos** tus modelos automáticamente.
- **`runscript`:** Ejecuta un script de Python dentro del contexto de Django.
- **`graph_models`:** Genera una imagen (diagrama) de tu base de datos (requiere `pygraphviz`).
- **`admin_generator`:** Genera el código para `admin.py` automáticamente basado en tus modelos.
- **`generate_password`:** Genera una clave aleatoria segura.

```bash
# Ejemplo de uso
python manage.py shell_plus
python manage.py graph_models -a -o mi_base_de_datos.png

```

---

## 7. Importar y Exportar Datos (`django-import-export`)

> **Explicación:** Permite subir Excels o CSVs desde el Admin para crear registros, o descargar tus tablas en PDF, XLS, etc.

1. **Instalar:** `pip install django-import-export`
2. **Uso en `admin.py`:**

```python
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(ImportExportModelAdmin):
    # Heredar de ImportExportModelAdmin habilita los botones Importar/Exportar
    pass

```

---

## 8. Auditoría: `django-simple-history`

> **Explicación:** ¿Quién borró este registro? ¿Qué precio tenía este producto ayer? Esta librería guarda una "foto" de cada objeto cada vez que se crea, edita o elimina.

1. **Instalar:** `pip install django-simple-history`
2. **Uso en `models.py`:**

```python
from simple_history.models import HistoricalRecords

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    history = HistoricalRecords() # Esto crea una tabla espejo de auditoría automática

```

---

## 9. Sobre Django Suite

> **Nota de experto:** Históricamente, "Django Suite" se refería a una colección de temas (basados en Bootstrap) para el admin. Sin embargo, en el desarrollo profesional moderno de 2026, ha sido desplazado por **Jet**, **Grappelli** o simplemente por el nuevo **Admin Responsivo** nativo de Django. No se recomienda su uso en proyectos nuevos ya que suele tener problemas de compatibilidad con versiones recientes de Django.
