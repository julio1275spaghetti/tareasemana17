#   Nombre:         Julio Alejandro Ramírez Lara
#   Carrera:        Ingeniería en Sistemas de Información y Ciencias de la Computación
"""
    Carnet:         0909-26-8531
    Curso:          Algoritmos
    Catedrático:    Ing. Amilcar Sagastume
    Fecha:          Octubre del 2026

"""
#   ==============================================
#   Ejercicio 3: : Herencia  
#   ==============================================

class Material:
    #La clase padre que representará los materiales bibliotecarios

    def __init__(self, titulo: str, autor: str, año_publicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}  | Autor: {self.autor} | Año de Publicación: {self.año_publicacion}")

class Libro(Material):
    #La clase hija que representa un libro con número de páginas

    def __init__(self, titulo: str, autor: str, año_publicacion: int, numero_paginas: int):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f"LIBRO: {self.titulo} | Autor: {self.autor} | Año de Publicación: {self.año_publicacion} | Número de Páginas: {self.numero_paginas}")

class Revista(Material):
    #La otra clase hija que representa una revista con su número de edición

    def __init__(self, titulo: str, autor: str, año_publicacion: int, numero_edicion: int):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        print(f"REVISTA: {self.titulo} | Autor: {self.autor} | Año de Publicación: {self.año_publicacion} | Número de Edición: {self.numero_edicion}")

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 417)
libro2 = Libro("Clean Code", "Robert C. Martin", 2008, 464)
revista1 = Revista("National Geographic", "Varios Autores", 2024, 150)
revista2 = Revista("IEEE Software", "IEEE Computer Society", 2023, 42)

print("======================================================")
libro1.mostrar_informacion()
libro2.mostrar_informacion()
print("======================================================")
revista1.mostrar_informacion()
revista2.mostrar_informacion()
print("======================================================")
