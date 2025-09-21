class evaluacion:
    def __init__(self,codigo, titulo, descripcion=""):
        self.codigo=codigo
        self.titulo=titulo
        self.descripcion=descripcion

    
    def tipo(self):
        return "Evaluacion"
    
    def __repr__(self):
        return f"{self.tipo()}({self.codigo}, {self.titulo})"


class examen(evaluacion):
    def tipo(self):
        return "Examen"
    
class tarea(evaluacion):
    def tipo(self):
        return "tarea"
    