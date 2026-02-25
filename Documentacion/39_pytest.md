Esta es la guía definitiva de **Pytest**, diseñada para llevarte desde los conceptos básicos hasta un nivel profesional. He complementado tu base de freeCodeCamp con **patrones de diseño de pruebas**, mejores prácticas de la industria y explicaciones técnicas detalladas.

---

# 🏆 Pytest: Guía Profesional de Testing en Python

Pytest es el estándar *de facto* en la industria debido a su filosofía **"Pythonic"**: permite escribir pruebas complejas con una sintaxis minimalista. A diferencia de `unittest`, que te obliga a usar clases y métodos específicos, Pytest te permite usar funciones simples y la palabra clave nativa `assert`.

---

## 1. Fundamentos y Autodescubrimiento

### 📝 Comentario: La Magia del Descubrimiento Automático

En un entorno profesional, no ejecutamos los archivos de prueba uno por uno. Pytest escanea tu proyecto buscando patrones:

* **Archivos:** `test_*.py` o `*_test.py`.
* **Funciones:** Cualquier función que empiece con `test_`.
* **Aserciones:** Solo necesitas `assert`. Si la condición es falsa, Pytest lanza una excepción y detiene el test, mostrando un "diff" detallado (la diferencia entre lo esperado y lo real).

```python
# Archivo: test_operaciones.py
import pytest

# Función simple a probar
def calcular_impuesto(precio, tasa):
    return precio * tasa

def test_calcular_impuesto_basico():
    # EXPLICACIÓN PROFESIONAL:
    # Definimos los valores de entrada y el resultado esperado.
    # El assert de Pytest es inteligente y desglosa objetos complejos si fallan.
    resultado = calcular_impuesto(100, 0.16)
    assert resultado == 16.0  # Si falla, Pytest te dirá exactamente cuánto valía 'resultado'

def test_concatenacion_listas():
    # Pytest brilla comparando estructuras de datos
    lista_1 = [1, 2]
    lista_2 = [3, 4]
    resultado = lista_1 + lista_2
    assert resultado == [1, 2, 3, 4]

```

---

## 2. Gestión de Excepciones y Errores

### 📝 Comentario: Validando el Comportamiento Negativo

Probar que el código funciona es solo la mitad del trabajo. Un profesional debe asegurar que el código **falle con gracia**. Usamos `pytest.raises` para capturar excepciones específicas. Si la excepción no ocurre, el test falla.

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def test_dividir_error_esperado():
    # EXPLICACIÓN: Usamos el gestor de contexto 'with'.
    # Si 'dividir' lanza ValueError, el test pasa.
    with pytest.raises(ValueError) as exc_info:
        dividir(10, 0)
    
    # Mejora Profesional: También podemos verificar el mensaje del error
    assert str(exc_info.value) == "No se puede dividir por cero"

```

---

## 3. Fixtures: El Corazón de Pytest

### 📝 Comentario: Inyección de Dependencias

Las `fixtures` reemplazan al viejo `setUp/tearDown`. Son funciones que preparan el terreno (crean una DB, cargan un archivo, inicializan una API).
**Ventaja Pro:** Son modulares. Puedes pedir múltiples fixtures en un solo test simplemente pasándolas como argumentos.

```python
import pytest

# Definimos una base de datos ficticia como fixture
@pytest.fixture
def base_de_datos_memoria():
    # SETUP: Preparamos los datos
    db = {"usuarios": ["Alice", "Bob"], "conectado": True}
    
    yield db  # Aquí se entrega el objeto al test
    
    # TEARDOWN: Limpiamos después del test (equivalente a teardown_method)
    db.clear()
    print("Base de datos limpiada")

def test_usuario_existe(base_de_datos_memoria):
    # El argumento 'base_de_datos_memoria' es el objeto devuelto por el yield del fixture
    assert "Alice" in base_de_datos_memoria["usuarios"]

def test_db_conectada(base_de_datos_memoria):
    assert base_de_datos_memoria["conectado"] is True

```

---

## 4. Parametrización: Evitando la Duplicación

### 📝 Comentario: Data-Driven Testing

Si tienes una función que debe ser probada con 20 combinaciones de datos, no escribas 20 tests. La parametrización crea una "plantilla" de test y la ejecuta una vez por cada conjunto de datos.

```python
# Probamos una función de validación de contraseñas
def es_segura(password):
    return len(password) >= 8

@pytest.mark.parametrize("clave, esperado", [
    ("12345", False),      # Caso: muy corta
    ("abcdefgh", True),    # Caso: longitud justa
    ("password123", True), # Caso: larga
    ("", False)            # Caso: vacía
])
def test_validacion_claves(clave, esperado):
    # Este test se ejecutará 4 veces automáticamente
    assert es_segura(clave) == esperado

```

---

## 5. Marcadores y Metadatos

### 📝 Comentario: Control de Ejecución

Los `markers` permiten clasificar tests. Puedes ejecutar solo los rápidos, saltar los que dependen de Windows si estás en Linux, o marcar tests que sabes que fallarán (útil en TDD).

```python
import sys

@pytest.mark.skip(reason="Falla en la versión actual de la API")
def test_func_rota():
    assert False

@pytest.mark.skipif(sys.platform == "win32", reason="No funciona en Windows")
def test_solo_linux():
    assert True

@pytest.mark.slow
def test_proceso_pesado():
    # Podrías ejecutarlo en la terminal como: pytest -m slow
    import time
    time.sleep(2)
    assert True

```

---

## 6. Mocking Profesional con `pytest-mock`

### 📝 Comentario: Aislamiento Total

En el desarrollo profesional, usamos el plugin `pytest-mock` (que proporciona el fixture `mocker`) sobre el `unittest.mock` estándar porque es más limpio y gestiona la limpieza automáticamente. El objetivo es "engañar" al código para que no llame a servicios externos.

```python
# Supongamos que esta función llama a una API externa que cobra dinero
def realizar_pago(servicio_api, monto):
    respuesta = servicio_api.cobrar(monto)
    return respuesta["status"] == "success"

def test_pago_exitoso(mocker):
    # 1. Creamos un objeto simulado (Mock)
    mock_api = mocker.Mock()
    
    # 2. Definimos qué debe devolver cuando se llame al método .cobrar()
    mock_api.cobrar.return_value = {"status": "success", "id": "PAY-123"}
    
    # 3. Ejecutamos nuestra lógica pasando el mock en lugar del servicio real
    resultado = realizar_pago(mock_api, 500)
    
    # 4. Verificaciones de integridad
    assert resultado is True
    # Verificamos que el código REALMENTE intentó cobrar los 500
    mock_api.cobrar.assert_called_once_with(500)

```

---

## 🚀 Mejores Prácticas de la Industria

1. **Estructura de Carpetas:** Mantén tus tests en una carpeta llamada `/tests` en la raíz de tu proyecto.
2. **Archivo `conftest.py`:** Si tienes fixtures que se usan en muchos archivos, ponlas en `conftest.py`. Pytest las cargará automáticamente sin necesidad de importarlas.
3. **Nombres Descriptivos:** No escatimes en el nombre: `test_usuario_no_puede_comprar_sin_saldo` es mejor que `test_compra_fail`.
4. **Uso de Plugins:** Instala `pytest-cov` para ver qué porcentaje de tu código está cubierto por pruebas: `pytest --cov=mi_proyecto`.

