#   Nombre:         Julio Alejandro Ramírez Lara
#   Carrera:        Ingeniería en Sistemas de Información y Ciencias de la Computación
"""
    Carnet:         0909-26-8531
    Curso:          Algoritmos
    Catedrático:    Ing. Amilcar Sagastume
    Fecha:          Octubre del 2026

"""
#   ==================================================
#   Ejercicio 5: Composición y Relación entre Clases
#   ==================================================

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_stock: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock
    
    def actualizar_stock(self, cantidad: int):
        self.cantidad_stock += cantidad 

class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            print("¡Error! La cantidad a ingresar tiene que ser mayor a 0")
        
        if producto.cantidad_stock >= cantidad:
            producto.actualizar_stock(-cantidad)
            self.productos.append((producto, cantidad))
            print(f"Añadido: {cantidad}x '{producto.nombre}' al carrito")
        else:
            print(f"Stock insuficiente para '{producto.nombre}' al carrito")

    def calcular_total(self) -> float:
        total = 0.0
        for producto, cantidad in self.productos:
            total += producto.precio * cantidad
        return total
    
    def mostrar_resumen(self):
        print("===============Resumen de Compra================")
        if not self.productos:
            print("Elcarrito está vacío")
            return
        
        for producto, cantidad in self.productos:
            subtotal = producto.precio * cantidad
            print(f"{producto.nombre:<15} | x{cantidad:<3} | Q{producto.precio:.2f} c/u = Q{subtotal:.2f}")

            print("================================================")
            print(f"TOTAL A PAGAR: Q{self.calcular_total():.2f}")
            print("================================================")

prod1 = Producto("Teclado Mecánico", 350.0, 5)
prod2 = Producto("Mouse Gamer", 180.0, 8)
prod3 = Producto("Monitor 24\"", 1200.0, 2)

carrito = CarritoCompras()

# Operaciones de compra
carrito.agregar_producto(prod1, 2)
carrito.agregar_producto(prod2, 1)
carrito.agregar_producto(prod3, 3)  # Intento que supera el stock disponible
carrito.agregar_producto(prod3, 1)  # Compra válida

# Mostrar resumen
carrito.mostrar_resumen()

# Verificación de inventario restante
print("\nStock restante en tienda:")
print(f"{prod1.nombre}: {prod1.cantidad_stock}")
print(f"{prod2.nombre}: {prod2.cantidad_stock}")
print(f"{prod3.nombre}: {prod3.cantidad_stock}")
