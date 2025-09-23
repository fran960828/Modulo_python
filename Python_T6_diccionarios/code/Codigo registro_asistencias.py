# diccionario base de datos
asistencias = dict()

# Registrar asistencias de estudiantes
asistencias["Estudiante1"] = ["2022-01-01", "2022-01-03", "2022-01-05"]
asistencias["Estudiante2"] = ["2022-01-02", "2022-01-05", "2022-01-07"]
asistencias["Estudiante3"] = ["2022-01-01", "2022-01-07", "2022-01-09"]

# Agregar nuevas fechas de asistencia para un estudiante existente
asistencias["Estudiante1"].append("2022-01-07")
asistencias["Estudiante2"].append("2022-01-09")

# Mostrar la lista de estudiantes y las fechas en las que asistieron
print("Registro de Asitencias:")
for estudiante, fechas in asistencias.items():
    print("Estudiante:", estudiante)
    print("Fechas de Asistencia:", ", ".join(fechas))
    print()