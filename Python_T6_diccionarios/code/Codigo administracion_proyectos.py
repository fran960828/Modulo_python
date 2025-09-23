# diccionario base de datos
tareas = {}

# Agregar tareas nuevas
tareas["Tarea1"] = {"descripcion": "Realizar analisis de requisitos", "responsable": "Juan"}
tareas["Tarea2"] = {"descripcion": "Desarrollar funcionalidad principal", "responsable": "Marta"}
tareas["Tarea3"] = {"descripcion": "Realizar validacion de proceso", "responsable": "Jacobo"}

# Asignar responsables a las tareas existentes
tareas["Tarea1"]["responsable"] = "Elena"
tareas["Tarea3"]["responsable"] = "Maria"

# Actualizar las descripciones de las tareas
tareas["Tarea2"]["descripcion"] = "Realizar test de hiperparametros"

# Mostrar la lista de tareas y responsables
print("Lista de Tareas y Responsables:")
for tarea, detalles in tareas.items():
    print("Tarea", tarea)
    print("Descripcion:", detalles["descripcion"])
    print("Responsable:", detalles["responsable"])
    print()