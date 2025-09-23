Clase Usuario:
    Atributos: nombre, correo
    Métodos:
        - mostrar información (toString)
        - get_nombre()
        - get_correo()

Clase Estudiante hereda Usuario:
    Atributos: carnet, cursos
    Métodos:
        - inscribir_curso(curso):
            si curso ya en cursos → lanzar error
            sino agregar curso a lista
        - listar_cursos()

Clase Instructor hereda Usuario:
    Atributos: especialidad
    Métodos:
        - asignar_curso(curso): curso.instructor = self

Gestion de Cursos:
Clase Curso:
    Atributos:
        - código
        - nombre
        - instructor
        - lista_estudiantes
        - lista_evaluaciones
    Métodos:
        - inscribir_estudiante(estudiante):
            si estudiante ya en lista_estudiantes:
                lanzar error "Estudiante duplicado"
            sino:
                agregar estudiante a lista_estudiantes
        - mostrar_estudiantes()
        - agregar_evaluacion(evaluacion):
            añadir evaluacion a lista_evaluaciones
        - mostrar_evaluaciones()

Gestion de Evaluaciones:
Clase Evaluacion:
    Atributos:
        - título
        - descripción
        - calificaciones (diccionario estudiante: nota)
    Métodos:
        - asignar_calificacion(estudiante, nota):
            si nota < 0 o nota > 100:
                lanzar error "Nota inválida"
            guardar nota en calificaciones[estudiante]

Clase Examen hereda de Evaluacion:
    Métodos:
        - puede redefinir asignar_calificacion() o agregar tipo="Examen"

Clase Tarea hereda de Evaluacion:
    Métodos:
        - puede redefinir asignar_calificacion() o agregar tipo="Tarea"

Registro de Calificaiones y Reportes:
Clase RegistroCalificaciones:
    Atributos:
        - diccionario_calificaciones {curso: {estudiante: [notas]}}
    Métodos:
        - registrar_calificacion(curso, estudiante, nota):
            si nota < 0 o > 100:
                lanzar error
            si curso no existe en diccionario:
                crear entrada
            si estudiante no existe en curso:
                crear lista
            agregar nota a la lista del estudiante

        - calcular_promedio(curso, estudiante):
            si no existen notas:
                lanzar error
            retornar suma(notas) / cantidad(notas)

        - generar_reporte(curso, *args, **kwargs):
            estudiantes = args (si se pasan) o todos en el curso
            calcular promedio para cada estudiante
            si existe min_promedio en kwargs:
                filtrar los estudiantes con promedio >= min_promedio
            retornar diccionario {estudiante: promedio}

Flujo Principal:
Inicio:
    Mostrar "Plataforma de Gestión de Cursos Online"

    Crear estudiantes
    Crear instructor
    Crear curso y asignar instructor

    Inscribir estudiantes en curso

    Crear evaluaciones (examen, tarea)
    Agregar evaluaciones al curso

    Registrar calificaciones para estudiantes

    Generar reporte de todos los estudiantes
    Mostrar en consola

    Generar reporte filtrado (ejemplo: promedio >= 60)
    Mostrar en consola
