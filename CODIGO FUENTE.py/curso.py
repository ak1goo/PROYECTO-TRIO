from evaluacion import evaluacion

class CourseError(Exception):
   pass

class DuplicateEnrollmentError(CourseError):
   pass

class CourseNotFoundError(CourseError):
   pass


class curso :
    def __init__(self, codigo,nombre, instructor):
      self.codigo=codigo
      self.nombre = nombre
      self.instructor=instructor
      self.estudiantes={}
      self.evaluaciones={}

    def inscribir_estudiante(self, id_delestudiante, nombre_estudiante):
       if id_delestudiante in self.estudiantes:
          raise DuplicateEnrollmentError(
             f"El estudiante {nombre_estudiante} el ya esta inscrito en {self.codigo}"
            )
       self.estudiantes[id_delestudiante]=nombre_estudiante
       print(f" el estudiante {nombre_estudiante} fue inscrito con el codigo {self.codigo} exitoso")


