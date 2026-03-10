Esta documentación está diseñada para que domines el control de acceso en Django utilizando **Class-Based Views (CBV)**. En el desarrollo profesional, no protegemos las páginas comprobando manualmente si el usuario existe en cada función; utilizamos **Mixins**. Un Mixin es una clase "heredada" que añade una funcionalidad específica a tu vista de forma limpia y reutilizable.

---

## 1. LoginRequiredMixin: Protección Básica

> **Explicación:** Este es el Mixin más fundamental. Su única misión es verificar si el usuario ha iniciado sesión. Si un usuario intenta acceder a una vista protegida sin estar logueado, Django lo redirigirá automáticamente a la página de login.
> **Nota Pro:** Siempre debe ser la **primera** clase en la lista de herencia (a la izquierda) para que se ejecute antes que cualquier otra lógica.

**Ejemplo en `views.py`:**

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Heredamos primero de LoginRequiredMixin
class PanelControlView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    
    # Si el usuario no está logueado, lo enviamos aquí:
    login_url = '/login/' 
    
    # Opcional: Si queremos que tras el login vuelva a esta página
    redirect_field_name = 'next'

```

---

## 2. UserPassesTestMixin: Control de Autoría

> **Explicación:** A veces estar logueado no es suficiente. Por ejemplo, solo el autor de un post debería poder editarlo. `UserPassesTestMixin` permite definir una función llamada `test_func()`. Si esta función devuelve `True`, el acceso se permite; si devuelve `False`, se deniega.
> **Uso Profesional:** Se combina con `LoginRequiredMixin` para asegurar que primero esté logueado y luego pase la prueba de autoría.

**Ejemplo en `views.py`:**

```python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from .models import Curso

class EditarCursoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Curso
    fields = ['nombre', 'descripcion']
    template_name = 'editar_curso.html'

    # Esta función define la "prueba" que el usuario debe pasar
    def test_func(self):
        # 1. Obtenemos el objeto que se intenta editar
        objeto = self.get_object()
        
        # 2. Comparamos el usuario actual con el autor del objeto
        # Solo devuelve True si son la misma persona
        return self.request.user == objeto.autor

    # Opcional: ¿Qué pasa si falla el test?
    # handle_no_permission puede lanzar un error 403 (Prohibido)
    raise_exception = True 

```

---

## 3. PermissionRequiredMixin: Sistema de Permisos de Django

> **Explicación:** Django tiene un sistema de permisos integrado por defecto (Añadir, Cambiar, Eliminar, Ver). `PermissionRequiredMixin` verifica si el usuario tiene un permiso específico asignado en la base de datos (ya sea directamente o a través de un grupo, como "Editores").
> **Sintaxis profesional:** Los permisos se definen como `'app_label.codename_del_permiso'`.

**Ejemplo en `views.py`:**

```python
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from .models import Curso

class CrearNuevoCursoView(PermissionRequiredMixin, CreateView):
    model = Curso
    fields = ['nombre', 'contenido']
    template_name = 'crear_curso.html'

    # Definimos el permiso necesario (Suele ser: app.accion_modelo)
    permission_required = 'cursos.add_curso'
    
    # Si el usuario no tiene el permiso, lanzamos un error 403 en lugar de redirigir
    raise_exception = True

    # También podemos requerir varios permisos a la vez
    # permission_required = ('cursos.add_curso', 'cursos.view_curso')

```

---

### Resumen de Comparación Profesional

| Mixin | ¿Cuándo usarlo? | Requisito principal |
| --- | --- | --- |
| **LoginRequiredMixin** | Acceso general a usuarios registrados. | `is_authenticated == True` |
| **UserPassesTestMixin** | Lógica personalizada (ej: autoría, mayoría de edad). | Que `test_func()` devuelva `True`. |
| **PermissionRequiredMixin** | Roles administrativos o de equipo (ej: Moderadores). | Tener el permiso en el perfil de usuario. |

### Verificación Final:

* Recuerda que si usas **vistas basadas en funciones** (FBV), usarías decoradores como `@login_required` o `@user_passes_test`, pero en **CBV** (clases) los Mixins son la única forma correcta y limpia de trabajar.

¿Te gustaría que viéramos cómo crear un **Mixin personalizado** que combine varias de estas reglas para no tener que repetir código en todas tus vistas?