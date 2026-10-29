#   Nombre:         Julio Alejandro Ramírez Lara
#   Carrera:        Ingeniería en Sistemas de Información y Ciencias de la Computación
"""
    Carnet:         0909-26-8531
    Curso:          Algoritmos
    Catedrático:    Ing. Amilcar Sagastume
    Fecha:          Octubre del 2026

"""
#   ==============================================
#   Ejercicio 2: : Encapsulamiento y Validaciones  
#   ==============================================

class CuentaBancaria:
    #Esta será la clase que representerá la cuenta bancaria con saldo privado

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        #Atributo privado del saldo inicial
        self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0.0

    def depositar(self, cantidad: float):
        #Añade saldo a la cuenta si la cantidad es mayor a 0
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se realizó con éxito el depósito de: Q{cantidad:.2f}. Su saldo actual es de: Q{self.__saldo:.2f}")
        else:
            print("¡Error! La cantidad a depositar tiene que ser mayor a 0.")
    
    def retirar(self, cantidad: float):
        #Retira dinero de la cuenta si la cantidad es mayor a 0 y si la cantidad no es mayor a la del saldo actual
        if cantidad <= 0:
            print("¡Error! La cantidad de dinero a retirar debe ser mayor a 0")
        elif cantidad > self.__saldo:
            print("¡Error! No puede retirar más de lo que tiene")
        else:
            self.__saldo -= cantidad
            print(f"Se realizó con éxito el retiro de: Q{cantidad:.2f}. Su saldo actual es de: Q{self.__saldo:.2f}")

    def consultar_saldo(self) -> float:
        return self.__saldo

print("============================================")
#Prueba 1
cuentabancaria1 = CuentaBancaria("Julio Ramírez", 500.00)
print(f"Titular: {cuentabancaria1.titular}")
print(f"Saldo inicial: Q{cuentabancaria1.consultar_saldo():.2f}")
cuentabancaria1.depositar(200.00)
cuentabancaria1.retirar(100.00)
cuentabancaria1.retirar(200.00)

print("============================================")
#Prueba 2
cuentabancaria2 = CuentaBancaria("Víctor Castillo", 800.00)
print(f"Titular: {cuentabancaria2.titular}")
print(f"Saldo inicial: {cuentabancaria2.consultar_saldo():.2f}")
cuentabancaria2.retirar(500.00)
cuentabancaria2.depositar(-800.00)
cuentabancaria2.depositar(800.00)
cuentabancaria2.retirar(1500.00)
cuentabancaria2.retirar(1000.00)
print("--------------------------------------------")
print(f"Saldo final: Q{cuentabancaria2.consultar_saldo():.2f}. ¡Que tenga buen día!")
print("============================================")