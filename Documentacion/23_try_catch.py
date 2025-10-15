"""
try_except_guia.py

Guía práctica (archivo .py) sobre el uso de try / except / else / finally en Python
Autor: Experto en Python (20 años de experiencia)
Propósito:
    - Enseñar de forma progresiva y con ejemplos comentados el manejo de excepciones
      en Python: try / except / else / finally, raising, re-raising, chaining, custom
      exceptions, patterns profesionales y errores comunes.
Modo de uso:
    - Ejecuta: python try_except_guia.py
    - Usa el menú para ejecutar ejemplos individuales o 'a' para todos.
    - Cada ejemplo es autónomo y está comentado paso a paso para que lo pruebes en un archivo .py.
Notas rápidas:
    - En Python se usa `try/except` (no 'try/catch'). `else` se ejecuta solo si no hubo excepción.
    - `finally` se ejecuta siempre, con o sin excepción (ideal para limpieza).
    - Evita `except:` sin especificar (atrapa BaseException, incluyendo KeyboardInterrupt).
    - Prefiere capturar excepciones específicas y documentar por qué las capturas.
"""

from typing import Any
import time
import logging
from contextlib import suppress

# Configuración simple de logging para algunos ejemplos
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(message)s")


# -------------------------
# Ejemplo 1: try/except básico
# -------------------------
def ejemplo_1_basico():
    """
    Muestra la estructura más simple: intentar convertir una entrada a entero
    y capturar ValueError si la conversión falla.
    """
    print("\n=== Ejemplo 1: try/except básico ===")
    valores = ["10", "abc", "42"]
    for v in valores:
        try:
            # Intentamos convertir a entero
            n = int(v)
        except ValueError as e:
            # Se captura ValueError (p. ej. 'abc' no es convertible)
            print(f"Valor inválido para int(): '{v}' -> {e!s}")
        else:
            # Este bloque se ejecuta solo si NO hubo excepción
            print(f"Conversión correcta: {v} -> {n}")


# -------------------------
# Ejemplo 2: múltiple except y orden
# -------------------------
def ejemplo_2_multiples_except():
    """
    Demuestra cómo capturar diferentes tipos de excepción y la importancia del orden.
    """
    print("\n=== Ejemplo 2: múltiples except y orden ===")
    datos = ["123", None, "0"]

    for x in datos:
        try:
            # Potencial AttributeError si x es None (x.strip())
            s = x.strip()
            # Potencial ZeroDivisionError más adelante
            resultado = 100 // int(s)
        except AttributeError as e:
            print("AttributeError: entrada no tiene método strip()", e)
        except ValueError as e:
            print("ValueError: no es un número válido ->", e)
        except ZeroDivisionError as e:
            print("ZeroDivisionError: división por cero ->", e)
        except Exception as e:
            # Captura todas las excepciones derivadas de Exception (fallback seguro)
            print("Excepción inesperada:", type(e).__name__, e)
        else:
            print("Resultado correcto:", resultado)


# -------------------------
# Ejemplo 3: finally para limpieza (archivo)
# -------------------------
def ejemplo_3_finally_limpieza():
    """
    Muestra el patrón tradicional de abrir un recurso y asegurar su cierre con finally.
    También compara con 'with' que es preferible cuando está disponible.
    """
    print("\n=== Ejemplo 3: finally para limpieza (archivo) ===")
    fname = "temp_demo.txt"

    # Ejemplo con finally
    f = None
    try:
        f = open(fname, "w")
        f.write("línea 1\n")
        # Simulamos error
        raise RuntimeError("simulación de error mientras el archivo está abierto")
    except Exception as e:
        print("Se capturó excepción:", e)
    finally:
        # finally se ejecuta siempre; aquí cerramos el archivo si fue abierto
        if f is not None:
            f.close()
            print("Archivo cerrado desde finally (patrón manual).")

    # Mejor patrón: usar 'with' (context manager) que cierra el archivo automáticamente
    try:
        with open(fname, "w") as f2:
            f2.write("otra línea\n")
            # Si ocurre error aquí, 'with' cerrará el archivo automáticamente
            # raise RuntimeError("otro error")
    except Exception as e:
        print("Error dentro de with:", e)
    else:
        print("Con 'with' no es necesario finally para cerrar el archivo.")


# -------------------------
# Ejemplo 4: raise y custom exception
# -------------------------
class MiErrorAplicacion(Exception):
    """Excepción personalizada para el dominio de la aplicación."""
    pass


def ejemplo_4_raising_custom():
    """
    Muestra cómo lanzar excepciones con raise y cómo definir y usar una excepción personalizada.
    """
    print("\n=== Ejemplo 4: raise y custom exception ===")
    def procesar(x: int):
        if x < 0:
            # Lanzamos una excepción específica para el dominio
            raise MiErrorAplicacion(f"El valor {x} no puede ser negativo.")
        return x * 2

    for v in [10, -5]:
        try:
            print("Procesando", v)
            r = procesar(v)
        except MiErrorAplicacion as e:
            print("MiErrorAplicacion capturada:", e)
        else:
            print("Procesado con éxito:", r)


# -------------------------
# Ejemplo 5: re-raising (volver a lanzar) y encadenamiento (from)
# -------------------------
def ejemplo_5_reraise_chain():
    """
    Demuestra cuándo es apropiado volver a lanzar una excepción y cómo encadenar excepciones
    para mantener el contexto original usando 'raise ... from ...'.
    """
    print("\n=== Ejemplo 5: re-raise y chaining (raise ... from ...) ===")

    def funcion_baja():
        # Lanza un error bajo nivel
        raise ValueError("valor inválido en función de bajo nivel")

    def funcion_media():
        try:
            funcion_baja()
        except ValueError as e:
            # Traducimos la excepción a otra de nivel superior
            raise RuntimeError("error en función_media") from e

    try:
        funcion_media()
    except RuntimeError as e:
        # Veremos la cadena de excepciones en el traceback si mostramos e.__cause__
        print("Capturada RuntimeError:", e)
        print("Causa original (__cause__):", repr(e.__cause__))


# -------------------------
# Ejemplo 6: evitar excepciones silenciadas — no usar bare except
# -------------------------
def ejemplo_6_no_bare_except():
    """
    Ilustra por qué no se debe usar 'except:' sin especificar — esto también captura SystemExit/KeyboardInterrupt.
    """
    print("\n=== Ejemplo 6: evitar bare except ===")

    try:
        # Simulamos operación que puede fallar
        v = int("a")
    except Exception as e:  # BUENO: captura excepciones derivadas de Exception
        print("Capturado Exception:", e)

    # MAL: bare except
    try:
        v = int("a")
    except:  # pylint: disable=bare-except
        print("Se capturó 'todo' — pero esto también atrapa KeyboardInterrupt y SystemExit (no recomendado).")


# -------------------------
# Ejemplo 7: manejar KeyboardInterrupt separadamente
# -------------------------
def ejemplo_7_keyboardinterrupt():
    """
    Demuestra el patrón de capturar KeyboardInterrupt para permitir salidas limpias
    y re-lanzarlo si no lo queremos atrapar silenciosamente.
    """
    print("\n=== Ejemplo 7: capturar KeyboardInterrupt ===")
    try:
        print("Pulsa Ctrl-C en los próximos 5 segundos para probar KeyboardInterrupt...")
        time.sleep(5)
        print("No se pulsó Ctrl-C.")
    except KeyboardInterrupt:
        print("Se recibió KeyboardInterrupt: limpieza realizada y re-lanzando.")
        # Hacemos limpieza necesaria (si la hubiera) y re-lanzamos para que el proceso termine
        raise


# -------------------------
# Ejemplo 8: usar contextlib.suppress para ignorar excepciones esperadas
# -------------------------
def ejemplo_8_suppress():
    """
    `suppress` es útil cuando quieres ignorar explícitamente ciertas excepciones
    y que el flujo continúe silenciosamente (más legible que try/except vacío).
    """
    print("\n=== Ejemplo 8: contextlib.suppress ===")
    from contextlib import suppress
    import os

    fname = "archivo_que_puede_no_existir.tmp"

    # Queremos eliminar un archivo si existe, pero no queremos que falle si no existe.
    with suppress(FileNotFoundError):
        os.remove(fname)
        print(f"{fname} borrado (si existía).")

    # Equivalente con try/except (más verboso)
    try:
        os.remove(fname)
    except FileNotFoundError:
        pass  # intención explícita de ignorar el error


# -------------------------
# Ejemplo 9: retries con backoff (patrón práctico)
# -------------------------
def ejemplo_9_retries_backoff():
    """
    Patron práctico: reintentos ante excepciones transitorias (p. ej. redes).
    Este ejemplo simula fallos transitorios y aplica reintentos exponenciales.
    """
    print("\n=== Ejemplo 9: retries con backoff ===")
    max_retries = 4
    base_delay = 0.1  # segundos

    attempts = {"count": 0}

    def operacion_transitoria():
        # Simula fallo las primeras 2 llamadas y éxito en la 3ª
        attempts["count"] += 1
        if attempts["count"] < 3:
            raise ConnectionError(f"falla temporal (intento {attempts['count']})")
        return "éxito!"

    for intento in range(1, max_retries + 1):
        try:
            resultado = operacion_transitoria()
        except ConnectionError as e:
            print(f"Intento {intento} falló: {e}")
            if intento == max_retries:
                print("Alcanzado máximo de reintentos; propagando excepción.")
                raise
            delay = base_delay * (2 ** (intento - 1))  # backoff exponencial
            print(f"Esperando {delay:.2f}s antes del siguiente intento...")
            time.sleep(delay)
        else:
            print("Operación resultó:", resultado)
            break
        finally:
            # Finalmente se puede hacer logging o métricas por intento
            logging.debug("Intento %d terminado.", intento)


# -------------------------
# Ejemplo 10: transformar excepciones (wrap) para API pública
# -------------------------
def ejemplo_10_wrap_exceptions_api():
    """
    En APIs es común "envolver" excepciones internas y exponer errores de alto nivel,
    manteniendo la causa original para debugging.
    """
    print("\n=== Ejemplo 10: wrap/convertir excepciones para API pública ===")

    class InternalError(Exception):
        pass

    class ApiError(Exception):
        pass

    def interna():
        # error de bajo nivel
        raise InternalError("fallo interno X")

    def fachada_operacion():
        try:
            interna()
        except InternalError as e:
            # En lugar de propagar InternalError, lanzamos ApiError para el consumidor
            raise ApiError("error en la operación de la API") from e

    try:
        fachada_operacion()
    except ApiError as e:
        print("ApiError capturado por el cliente:", e)
        # Si el desarrollador necesita debug, puede inspeccionar __cause__
        print("Causa interna:", repr(e.__cause__))


# -------------------------
# Ejemplo 11: logging de excepciones completas con traceback
# -------------------------
def ejemplo_11_logging_traceback():
    """
    Muestra cómo loggear una excepción con su traceback (útil en aplicaciones reales).
    """
    print("\n=== Ejemplo 11: logging con traceback ===")
    try:
        1 / 0
    except Exception:
        # logger.exception registra la excepción actual con traceback
        logging.exception("Se produjo un error grave durante la operación")


# -------------------------
# Ejemplo 12: errores comunes y checklist
# -------------------------
def ejemplo_12_errores_checklist():
    print("\n=== Ejemplo 12: Errores comunes y checklist profesional ===")
    checklist = [
        "1. No uses 'except:' sin especificar; usa 'except Exception:' como mínimo.",
        "2. No captures Exception si no vas a manejarlo o registrar (evita 'swallowing').",
        "3. Usa bloques 'else' para el código que debe ejecutarse solo si no hubo excepción.",
        "4. Usa 'finally' para liberar recursos cuando no uses context managers.",
        "5. Evita lógica compleja dentro de except; extrae a funciones para testear.",
        "6. Prefiere capturar excepciones específicas (ValueError, KeyError...) para evitar ocultar bugs.",
        "7. Asegúrate de re-lanzar KeyboardInterrupt/SystemExit si no quieres suprimirlos.",
        "8. Usa logging.exception(...) para guardar tracebacks en producción.",
    ]
    for item in checklist:
        print(item)


# -------------------------
# Menú interactivo
# -------------------------
ejemplos = {
    "1": ("try/except básico", ejemplo_1_basico),
    "2": ("Múltiples except y orden", ejemplo_2_multiples_except),
    "3": ("finally para limpieza (archivo)", ejemplo_3_finally_limpieza),
    "4": ("raise y excepción personalizada", ejemplo_4_raising_custom),
    "5": ("re-raise y chaining", ejemplo_5_reraise_chain),
    "6": ("Evitar bare except", ejemplo_6_no_bare_except),
    "7": ("Capturar KeyboardInterrupt (demo)", ejemplo_7_keyboardinterrupt),
    "8": ("contextlib.suppress (ignorar excepciones esperadas)", ejemplo_8_suppress),
    "9": ("Retries con backoff (patrón práctico)", ejemplo_9_retries_backoff),
    "10": ("Wrap/convertir excepciones para API", ejemplo_10_wrap_exceptions_api),
    "11": ("Logging con traceback", ejemplo_11_logging_traceback),
    "12": ("Errores comunes y checklist", ejemplo_12_errores_checklist),
}

def menu():
    print("=== Guía: try / except / else / finally (ejecutable) ===")
    while True:
        print("\nElige un ejemplo (número), 'a' para todos, o 'q' para salir:")
        for k, (desc, _) in ejemplos.items():
            print(f" {k}. {desc}")
        elec = input(">>> ").strip().lower()
        if elec in ("q", "salir", "exit"):
            print("Saliendo.")
            break
        if elec == "a":
            for k in sorted(ejemplos.keys(), key=int):
                print("\n" + "-" * 60)
                print(f"Ejecutando {k}. {ejemplos[k][0]}")
                try:
                    ejemplos[k][1]()
                except Exception as e:
                    print(f"Ejemplo {k} lanzó excepción durante la ejecución: {e!r}")
            print("\nTodos los ejemplos ejecutados.")
            continue
        if elec in ejemplos:
            try:
                ejemplos[elec][1]()
            except KeyboardInterrupt:
                print("Recepción de KeyboardInterrupt durante la ejecución del ejemplo; saliendo.")
                break
            except Exception as e:
                print("La ejecución del ejemplo produjo una excepción:", type(e).__name__, e)
        else:
            print("Opción no válida. Introduce el número del ejemplo, 'a' o 'q'.")


# -------------------------
# Punto de entrada
# -------------------------
if __name__ == "__main__":
    menu()

