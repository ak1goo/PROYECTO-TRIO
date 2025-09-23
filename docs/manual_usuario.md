#Manual de Usuario - Sistema de Reportes Académicos
#¿Qué hace este módulo?

Permite registrar calificaciones, calcular promedios y generar reportes de estudiantes con diferentes formatos.

#uso#
--Importa módulo:
from reportes import registrar_calificaciones, generar_reporte, calcular_promedio

--Crear registro:
python
registro = {}

--Registra calificaciones:

-registrar_calificaciones(registro, "Nombre", 90, 80, 100)
-Acepta calificaciones múltiples mediante args.
-Ignora valores no numéricos o fuera de 0-100 con aviso.

4. Calcula promedio:

python
prom = calcular_promedio(registro["Ana"])


5. Genera reportes:
-Formato normal (con detalle):
  `generar_reporte(registro, formato="normal", detalle=True)`

-Formato tabla (sin detalle):
  `generar_reporte(registro, formato="tabla", detalle=False)`

