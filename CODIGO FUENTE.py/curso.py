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
      