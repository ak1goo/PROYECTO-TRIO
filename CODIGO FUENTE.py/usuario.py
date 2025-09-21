class Usuario:
    def __init__(self, nombre, correo):
        self._nombre = nombre        # atributo privado
        self._correo = correo

    def __str__(self):
        return f"{self._nombre} ({self._correo})"

    def get_nombre(self):
        return self._nombre

    def get_correo(self):
        return self._correo


class Estudiante(Usuario):
    def __init__(self, nombre, correo, carnet):
        super().__init__(nombre, correo)
        self._carnet = carnet
        self._cursos = []

    def inscribir_curso(self, curso):
        if curso in self._cursos:
            raise ValueError("El estudiante ya está inscrito en este curso.")
        self._cursos.append(curso)

    def listar_cursos(self):
        return [curso.nombre for curso in self._cursos]


class Instructor(Usuario):
    def __init__(self, nombre, correo, especialidad):
        super().__init__(nombre, correo)
        self._especialidad = especialidad

    def asignar_curso(self, curso):
        curso.instructor = self
        return f"Curso {curso.nombre} asignado a {self._nombre}"
