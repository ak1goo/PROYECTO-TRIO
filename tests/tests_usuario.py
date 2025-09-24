import unittest
from reportes import calcular_promedio, generar_reporte, registrar_calificaciones

class TestReportes(unittest.TestCase):
    def test_calcular_promedio_vacio(self):
        self.assertIsNone(calcular_promedio([]))

    def test_calcular_promedio_normal(self):
        self.assertAlmostEqual(calcular_promedio([100, 50, 0]), 50.0)

    def test_registrar_calificaciones_valido(self):
        r = {}
        registrar_calificaciones(r, "Pablo", 80, 90, 100)
        self.assertEqual(r["Pablo"], [80,90,100])

    def test_registrar_calificaciones_invalido(self):
        r = {}
        registrar_calificaciones(r, "Sara", -10, 150, "b")
        self.assertEqual(r["Sara"], [])

    def test_generar_reporte_tabla(self):
        r = {"Ana": [100, 80], "Luis": []}
        rep = generar_reporte(r, formato="tabla", detalle=False)
        self.assertIn("Ana", rep)
        self.assertIn("Luis", rep)
        self.assertIn("N/A", rep)

if __name__ == '__main__':
    unittest.main()
