#   Nombre:         Julio Alejandro Ramírez Lara
#   Carrera:        Ingeniería en Sistemas de Información y Ciencias de la Computación
"""
    Carnet:         0909-26-8531
    Curso:          Algoritmos
    Catedrático:    Ing. Amilcar Sagastume
    Fecha:          Octubre del 2026

"""
#   ==============================================
#   Ejercicio 1: Clases, Objetos y Métodos Básicos 
#   ==============================================
class Rectangulo:
    #Esta clase es la que representará una figura geométrica rectangular
    
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        #Esta función calcula y regresa el área del rectángulo
        return self.base * self.altura
    
    def calcular_perimetro(self) -> float:
        #Esta función calcula y regresa el perímetro del rectángulo
        return (self.base * 2) + (self.altura * 2) 

    def es_cuadrado(self) -> bool:
        #Esta función regresa True si la base y la altura son iguales y regresa False si no son iguales
        return self.base == self.altura

print("============================================")
#Prueba 1
r1 = Rectangulo(10.8, 5.4)
print(f"Rectángulo 1 (Base: {r1.base}, Altura: {r1.altura}):")
print(f"Área: {r1.calcular_area()}")
print(f"Perímetro: {r1.calcular_perimetro()}")
print(f"¿Es un cuadrado?: {r1.es_cuadrado()}")

print("============================================")
#Prueba 2
r2 = Rectangulo(7, 7)
print(f"Rectángulo 2 (Base: {r2.base}, Altura: {r2.altura}):")
print(f"Área: {r2.calcular_area()}")
print(f"Perímetro: {r2.calcular_perimetro()}")
print(f"¿Es un cuadrado?: {r2.es_cuadrado()}")        
print("============================================")