from usuario import Estudiante, Instructor
from evaluacion import examen, tarea
from curso import curso, DuplicateEnrollmentError, CourseError
from reportes import RegistroCalificaciones

if __name__ == "__main__":
    print("-Plataforma de Cursos-")

    ana = Estudiante("Ana", "Anarodriguez@gmail.com", "2025009")
    rodrigo = Estudiante("Rodrigo", "rodrianleu@gmail.com", "2025200")
    evelyn = Instructor("Evelyn", "evelyntri@gmail.com", "Programacion")

    python = curso("B201", "Python Basico", "Profe")

    try:
        python.inscribir_estudiante(ana._carnet, ana.get_nombre())
        python.inscribir_estudiante(rodrigo._carnet, ana.get_nombre())

        python.inscribir_estudiante(ana._carnet, ana.get_nombre())
    except DuplicateEnrollmentError as e:
        print("Error: {e}")


    examen1 = examen("Primer examen", "Examen Introduccion")
    tarea1 = tarea("t1", "Tarea 1: Polimorfismo")

    try:
        python.evaluacion_agregado(examen1)
        python.evaluacion_agregado(tarea1)

        python.evaluacion_agregado(tarea1)
    except CourseError as e:
        print("Error: {e}")

    print("-INFORMACION DEL CURSO-")
    print(python.informacion())

    registro = RegistroCalificaciones()
    registro.registrar_calificacion("B201", ana.get_nombre(), 85)
    registro.registrar_calificacion("PY101", ana.get_nombre(), 90)
    registro.registrar_calificacion("PY101", rodrigo.get_nombre(), 55)

    print("-REPORTE DEL CURSO-")
    reporte = registro.generar_reporte("B201")

    for estudiante, promedio in reporte.items():
        print(f"{estudiante}: {promedio:}")


    print("Reporte filtrado {promedio >=65}")
    reporte_filtrado = registro.generar_reporte("B202", min_promedio=60)

    for estudiante, promedio in reporte_filtrado.items():
        print(f"{estudiante}: {promedio}") 
