
class RegistroCalificaciones:
    def __init__(self):
        self._calificaciones = {}

    def registrar_calificacion(self, curso, estudiante, nota):
        if nota < 0 or nota > 100:
            raise ValueError("La calificación debe estar entre 0 y 100.")

        if curso not in self._calificaciones:
            self._calificaciones[curso] = {}

        if estudiante not in self._calificaciones[curso]:
            self._calificaciones[curso][estudiante] = []

        self._calificaciones[curso][estudiante].append(nota)

    def calcular_promedio(self, curso, estudiante):
        notas = self._calificaciones.get(curso, {}).get(estudiante)
        if not notas:
            raise ValueError("No hay calificaciones registradas.")
        return sum(notas) / len(notas)

    def generar_reporte(self, curso, min_promedio=0):
        if curso not in self._calificaciones:
            raise ValueError("Curso inexistente.")
        
        reporte = {}
        for estudiante, notas in self._calificaciones[curso].items():
            promedio = sum(notas) / len(notas)
            if promedio >= min_promedio:
                reporte[estudiante] = promedio
        return reporte

      