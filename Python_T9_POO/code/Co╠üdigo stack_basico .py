"""
PILA (STACK) BÁSICA
Crea una clase "Pila" que represente una pila (stack) básica.
Implementa métodos para agregar elementos a la pila, quitar
elementos y mostrar el contenido actual.
"""

class Pila:
    # Constructor de la clase, inicializa una pila vacía
    def __init__(self):
        self.items = []

    # Método para agregar un elemento a la pila (push)
    def agregar(self, elemento):
        self.items.append(elemento)

    # Método para quitar y devolver el último elemento de la pila (pop)
    def quitar(self):
        if not self.esta_vacia():  # Verificar si la pila no está vacía
            return self.items.pop()
        else:
            print("La pila está vacía.")

    # Método para verificar si la pila está vacía
    def esta_vacia(self):
        return len(self.items) == 0

    # Método para mostrar el contenido actual de la pila
    def mostrar_contenido(self):
        print("Contenido de la pila:", self.items)


# Ejemplo de Uso
pila = Pila()  # Crear una instancia de Pila
pila.agregar(5)  # Agregar el número 5 a la pila
pila.agregar(10)  # Agregar el número 10 a la pila
pila.mostrar_contenido()  # Mostrar el contenido actual de la pila
pila.quitar()  # Quitar el último elemento de la pila
pila.mostrar_contenido()  # Mostrar el contenido actual de la pila después de quitar
