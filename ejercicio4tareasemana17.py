#   Nombre:         Julio Alejandro Ramírez Lara
#   Carrera:        Ingeniería en Sistemas de Información y Ciencias de la Computación
"""
    Carnet:         0909-26-8531
    Curso:          Algoritmos
    Catedrático:    Ing. Amilcar Sagastume
    Fecha:          Octubre del 2026

"""
#   =================================================
#   Ejercicio 4: Polimorfismo y Arreglos de Objetos 
#   =================================================

class Empleado:
    #Clase base para el sistema de nómina
    def __init__(self, nombre: str, dpi: int):
        self.nombre = nombre
        self.dpi = dpi
    
    def calcular_salario(self) -> float:
        #Se sobreescribirá por sus clases derivadas
        return 0.0

class EmpleadoFijo(Empleado):
    #Clase derivada
    def __init__(self, nombre: str, dpi: int, sueldo_base: float):
        super().__init__(nombre, dpi)
        self.sueldo_base = sueldo_base
    
    def calcular_salario(self) -> float:
        return self.sueldo_base

class EmpleadoporHora(Empleado):
    #Otra clase derivida
    def __init__(self, nombre: str, dpi: int, tarifa_por_hora: float, horas_trabajadas: float):
        super().__init__(nombre, dpi)
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self) -> float:
        return self.tarifa_por_hora * self.horas_trabajadas

nomina = [
    EmpleadoFijo("Julio Ramírez", 2450123450101, 11000.00),
    EmpleadoporHora("Kelvyn Marroquín", 3012987650101, 50.00, 150.00),
    EmpleadoFijo("Nehemías Pérez", 1980456780101, 8500.00),
    EmpleadoporHora("Víctor Castillo", 2233445560101, 50.00, 200.00)
]

for empleado in nomina:
    salario = empleado.calcular_salario()
    print(f"Empleado: {empleado.nombre} | DPI: {empleado.dpi} | Salario Total: Q{salario:.2f}")    
