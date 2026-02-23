Esta es la **Guía Maestra de Tipado Avanzado en Python**, diseñada específicamente para alguien que ya domina TypeScript y quiere aplicar ese rigor profesional al backend.

En Python, a diferencia de TypeScript, el tipado es "voluntario" para el intérprete, pero **obligatorio** para un profesional del Clean Code. Usaremos la librería `typing` (nativa) y mencionaremos `Pydantic` (estándar de la industria).

---

## 1. Tipado de Variables y Funciones (Basic Types)

En TypeScript usas `: string`, en Python usamos `: str`. La lógica es idéntica.

> **Nota de experto:** Usa siempre la sintaxis de Python 3.10+ con el operador `|` para uniones, es mucho más limpia.

```python
# Comentario: Definición de tipos en funciones.
# '->' indica el tipo de retorno.

def procesar_id(id_usuario: int | str) -> str:
    # El linter (Mypy) nos avisará si intentamos retornar algo que no sea string
    return f"USER_{id_usuario}"

# Uso de tipos básicos
nombre: str = "Gemini"
activo: bool = True
precio: float = 19.99

```

---

## 2. Interfaces y Contratos (Protocols)

En TypeScript, una `interface` define qué métodos debe tener un objeto. En Python, usamos `Protocol`. Esto se llama **Static Duck Typing**.

```python
from typing import Protocol

# Comentario: Esto equivale a una interface de TypeScript.
# Cualquier clase que tenga un método 'dibujar' será considerada un 'Dibujable'.
class Dibujable(Protocol):
    def dibujar(self) -> None:
        ... # Elipsis: significa que no hay implementación aquí.

class Circulo:
    def dibujar(self) -> None:
        print("Dibujando un círculo")

def renderizar_escena(elemento: Dibujable):
    # Clean Code: No nos importa qué clase es, solo que sepa 'dibujar'
    elemento.dibujar()

renderizar_escena(Circulo()) # Funciona perfectamente

```

---

## 3. Enums y Literales

Para evitar "strings mágicos" por todo el código, usamos `Enum` y `Literal`.

```python
from enum import Enum
from typing import Literal

# Comentario: Enum para valores fijos con nombres claros
class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"

# Comentario: Literal para restringir un valor exacto (muy común en TS)
def configurar_tema(modo: Literal["dark", "light"]):
    print(f"Cambiando a modo {modo}")

configurar_tema("dark") # Correcto
# configurar_tema("blue") # Mypy lanzará un error de tipo

```

---

## 4. Genéricos (Generics)

Cuando una clase o función debe manejar tipos que no conocemos de antemano (como un contenedor o una respuesta de API), usamos `TypeVar`.

```python
from typing import TypeVar, Generic, List

# Comentario: T es un marcador de posición, como <T> en TypeScript
T = TypeVar('T')

class Repositorio(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def agregar(self, item: T) -> None:
        self._items.append(item)

    def obtener_todos(self) -> List[T]:
        return self._items

# Ejemplo de uso:
repo_nombres = Repositorio[str]()
repo_nombres.agregar("Ana") # Correcto
# repo_nombres.agregar(123)  # Error de tipo detectado por el linter

```

---

## 5. El "Siguiente Nivel": Pydantic

Si en el Frontend usas interfaces para validar los datos que vienen de una API, en el Backend de Python usamos **Pydantic**. Es la herramienta que hace que el tipado no sea solo decorativo, sino que **valide los datos en tiempo de ejecución**.

```python
from pydantic import BaseModel, EmailStr, Field

# Comentario: Esto es como una interface de TS con esteroides.
# Si los datos no coinciden, Pydantic lanza un error automáticamente.
class UsuarioSchema(BaseModel):
    id: int
    username: str = Field(min_length=3)
    email: EmailStr # Valida que sea un email real
    es_premium: bool = False

# Ejemplo de validación de un JSON externo
datos_externos = {
    "id": 1,
    "username": "alberto",
    "email": "correo@ejemplo.com"
}

user = UsuarioSchema(**datos_externos)
print(user.email) # Salida: correo@ejemplo.com

```

---

## 6. Configuración del Entorno Profesional

Para que esto funcione de verdad como en TypeScript, tu flujo de trabajo debe ser:

1. **Instalar Mypy:** `pip install mypy`
2. **Configurar VS Code:** En la configuración de Python, activa `"python.analysis.typeCheckingMode": "basic"` (o "strict").
3. **Ejecutar el Check:** Antes de hacer un commit, corre `mypy tu_archivo.py`.

---

### Resumen de Extrapolación

| Concepto       | TypeScript               | Python (Clean Code)         |
| -------------- | ------------------------ | --------------------------- | -------------------- | ---- |
| **Interface**  | `interface User { ... }` | `class User(Protocol): ...` |
| **Type Alias** | `type ID = string        | number`                     | `ID: TypeAlias = str | int` |
| **Generics**   | `Array<T>`               | `list[T]` o `List[T]`       |
| **Optional**   | `name?: string`          | `name: str                  | None`                |
| **Validación** | Manual o Zod             | **Pydantic**                |

**¿Te gustaría que hagamos un pequeño proyecto de "Sistema de Gestión de Biblioteca" aplicando todos estos principios de tipado y Clean Code para consolidar el conocimiento?**
