"""
LISTA DE TAREAS
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes.
Implementa métodos para agregar una tarea,
marcar una tarea como completada y mostrar todas las tareas
"""

class ListaTareas:
    # Constructor de la clase, inicializa la lista de tareas vacía
    def __init__(self):
        self.tareas = []

    # Método para agregar una nueva tarea a la lista
    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})  # Agregar una tarea con su estado inicial como "Pendiente"

    # Método para marcar una tarea como completada
    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):  # Verificar que el índice sea válido
            self.tareas[indice]["completada"] = True  # Cambiar el estado de la tarea a "Completada"

    # Método para mostrar todas las tareas en la lista
    def mostrar_tareas(self):
        for indice, tarea in enumerate(self.tareas):  # Recorrer la lista de tareas con su índice
            estado = "Completada" if tarea["completada"] else "Pendiente"  # Determinar el estado de la tarea
            print(f"{indice + 1}. {tarea['tarea']} - {estado}")  # Imprimir la tarea con su estado

# Ejemplo de uso
lista_tareas = ListaTareas()  # Crear una instancia de ListaTareas
lista_tareas.agregar_tarea("Hacer la compra")  # Agregar una tarea a la lista
lista_tareas.agregar_tarea("Estudiar programación")  # Agregar otra tarea a la lista
lista_tareas.marcar_completada(1)  # Marcar la segunda tarea como completada
lista_tareas.mostrar_tareas()  # Mostrar todas las tareas con su estado
