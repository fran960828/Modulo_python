

---

# 🚀 Guía Profesional de Pruebas Unitarias en Python (`unittest`)

Las pruebas unitarias son pequeños programas que verifican que una "unidad" de código (generalmente una función o método) se comporte exactamente como esperas.

### 💡 ¿Por qué molestarse?

1. **Refactorización segura:** Puedes cambiar todo el interior de una función para que sea más rápida y, si los tests pasan, sabes que no rompiste nada.
2. **Documentación viva:** Los tests dicen exactamente qué debe hacer el código.
3. **Ahorro de tiempo:** Es más rápido correr un script de prueba que rellenar formularios en una web o hacer 20 `print()` manualmente.

---

## 1. La Estructura Fundamental

Para que Python reconozca tus pruebas, el archivo debe empezar por `test_`. Esto permite que las herramientas de automatización encuentren los tests fácilmente.

### 📝 Comentario: De `print()` al primer Test

Olvídate de ejecutar tu programa y mirar la consola para ver si el resultado es correcto. Con `unittest`, creas una clase que hereda de `unittest.TestCase`. Esto te da "superpoderes" para comparar resultados.

```python
# Archivo: test_calculadora.py
import unittest
# Supongamos que tenemos un archivo llamado calculadora.py con una función add()
import calculadora 

class TestCalculadora(unittest.TestCase):

    # REGLA: El nombre del método DEBE empezar con "test_"
    def test_suma(self):
        # assertEqual(valor_real, valor_esperado)
        # Si calculadora.add(5, 5) devuelve 10, la prueba brilla en verde.
        self.assertEqual(calculadora.add(5, 5), 10)
        self.assertEqual(calculadora.add(-1, 1), 0)

# El bloque principal permite ejecutar: python test_calculadora.py
if __name__ == '__main__':
    unittest.main()

```

---

## 2. Cobertura y Casos Extremos (Edge Cases)

No pruebes solo lo que sabes que funciona (el "camino feliz"). Un profesional busca dónde podría romperse el código.

### 📝 Comentario: ¿Qué pasa si...?

Debes probar valores límite: números muy grandes, números negativos, ceros o tipos de datos inesperados. Si una función falla en un test, el `AssertionError` te dirá exactamente en qué línea y con qué valores falló.

```python
import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

    def test_division(self):
        # Caso normal
        self.assertEqual(calculadora.divide(10, 2), 5)
        # Caso con decimales (flotantes)
        self.assertEqual(calculadora.divide(5, 2), 2.5)
        # Caso con números negativos
        self.assertEqual(calculadora.divide(-10, 2), -5)

    def test_multiplicacion(self):
        self.assertEqual(calculadora.multiply(10, 0), 0)
        self.assertEqual(calculadora.multiply(-5, -5), 25)

```

---

## 3. Pruebas de Excepciones (Errores Esperados)

A veces, el éxito de una prueba es que el código **lance un error**. Por ejemplo, dividir por cero debería dar un error, no un número.

### 📝 Comentario: Forzando el error

Usamos un "Context Manager" (`with`). Le decimos a Python: "Espero que lo que pase aquí dentro lance un `ValueError`". Si el error ocurre, el test pasa. Si el código no lanza el error, el test falla porque el código es "demasiado permisivo".

```python
    def test_division_por_cero(self):
        # Verificamos que se lance la excepción correcta
        with self.assertRaises(ValueError):
            calculadora.divide(10, 0)

```

---

## 4. Organización con `setUp` y `tearDown`

En proyectos reales, solemos probar objetos complejos (como un Usuario o una Conexión). No queremos crear el objeto en cada test.

### 📝 Comentario: Mantén tu código DRY (Don't Repeat Yourself)

* **`setUp`**: Se ejecuta **antes** de cada test. Ideal para crear objetos frescos.
* **`tearDown`**: Se ejecuta **después** de cada test. Ideal para borrar archivos temporales o limpiar bases de datos.

```python
class TestEmpleado(unittest.TestCase):

    def setUp(self):
        # Esto se ejecuta antes de CADA test individual
        # Creamos 'self.emp' para que esté disponible en todos los métodos
        self.emp = Empleado('Ana', 'García', 3000)

    def tearDown(self):
        # Se ejecuta después de cada test. 
        # Útil si creaste un archivo real y quieres borrarlo para no dejar basura.
        pass

    def test_email(self):
        self.assertEqual(self.emp.email, 'Ana.García@email.com')

```

---

## 5. Optimizando con `setUpClass`

A veces, el `setUp` es muy lento (ej: conectar a una base de datos real). No quieres hacerlo 100 veces si tienes 100 tests.

### 📝 Comentario: Configuración de nivel superior

Usamos `@classmethod` para que se ejecute **una sola vez** al inicio de toda la clase.

```python
class TestBaseDeDatos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Se ejecuta una sola vez al principio de todo
        print("\nIniciando conexión a DB...")

    @classmethod
    def tearDownClass(cls):
        # Se ejecuta una sola vez al final de todo
        print("\nCerrando conexión a DB...")

```

---

## 6. El Arte del Mocking (Simulación)

Esta es la parte más avanzada y profesional. ¿Cómo pruebas un código que envía correos electrónicos reales o cobra dinero con una tarjeta de crédito? **No lo haces.** Simulas el comportamiento.

### 📝 Comentario: El uso de `patch`

`patch` intercepta una llamada a una función externa y devuelve lo que tú le digas, sin ejecutar la función real. Es vital para que tus tests no dependan de que internet funcione.

```python
from unittest.mock import patch
import unittest
from mi_modulo import obtener_clima_remoto

class TestClima(unittest.TestCase):

    def test_obtener_clima(self):
        # "Parcheamos" la librería requests en el módulo donde se usa
        with patch('mi_modulo.requests.get') as objeto_simulado:
            
            # Configuramos qué debe responder ese objeto falso
            objeto_simulado.return_value.ok = True
            objeto_simulado.return_value.text = "Soleado"
            
            # Ejecutamos la función. No irá a internet, usará el simulado.
            resultado = obtener_clima_remoto("Madrid")
            
            self.assertEqual(resultado, "Soleado")
            # Verificamos que se llamó a la URL correcta
            objeto_simulado.assert_called_with("http://api.clima.com/Madrid")

```

---

## 🏁 Resumen de Buenas Prácticas

1. **Independencia:** El `test_A` no debe necesitar que el `test_B` se ejecute primero.
2. **Rapidez:** Los tests unitarios deben ser instantáneos. Si tardan minutos, algo estás haciendo mal (probablemente te falta usar Mocks).
3. **Un solo concepto por test:** No intentes probar toda la aplicación en un solo método `test_`. Divide y vencerás.

**¿Te gustaría que te ayude a escribir las pruebas para una función específica que ya tengas escrita?**