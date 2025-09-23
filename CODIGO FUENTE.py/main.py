from reportes import registrar_calificaciones, generar_reporte, calcular_promedio

def main():
    registro = {}
    print(generar_reporte(registro, formato="normal", detalle=True))
    print()
    print(generar_reporte(registro, formato="tabla", detalle=False))

if __name__ == "__main__":
    main()