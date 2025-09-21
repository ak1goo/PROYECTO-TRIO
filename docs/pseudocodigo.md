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