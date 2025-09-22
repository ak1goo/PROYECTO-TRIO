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
      self.nombre=nombre
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

    def evaluacion_agregado(self, evaluacion):
       if evaluacion.codigo in self.evaluaciones:
          raise CourseError(f" evaluacion {evaluacion.titulo} ya existe en el  curso {self.codigo}")
               
       self.evaluaciones[evaluacion.codigo]= evaluacion
       print(f" evaluaciion{evaluacion.titulo} fue agregado al curso {self.codigo} ")

    def evaluaciones_agregar(self, evaluaciones_listado):
       for eva in evaluaciones_listado:
          self.evaluacion_agregado(eva)


    def mostrarestudiantes(self):
       if not self.estudiantes:
          return "no se encuntra estudiantes inscritos"
       return [f"{id}-{nombre}" for id, nombre in self.estudiantes.items()] 

    def mostrarevaluaciones(self):
       if not self.evaluaciones:
          return "no se encuentra evaluaciones asigandas por el momento"
       return [f"{eva.tipo()}({eva.codigo}), {eva.titulo})" for eva in self.evaluaciones.values()]

    def informacion(self):
       infor= f"curso: {self.nombre} ({self.codigo})\n instrutor es: {self.instructor}\n"
       infor+= "\n Estudiantes inscritos:\n" 
       
       estudiantes=self.mostrarestudiantes()
       if isinstance(estudiantes, list):
          for estu in estudiantes:
            infor += f" - {estu}\n"


       infor += "\nEvaluaciones: \n"
       evaluaciones= self.mostrarevaluaciones()
       if isinstance(evaluaciones, list):
          for eva in evaluaciones:
             infor+= f" - {eva}\n"
       else:
          infor+= f" - {evaluaciones}\n"
    
def __repr__(self):
   return f"curso({self.codigo}, {self.nombre}, Instructor={self.instructor})"
    
