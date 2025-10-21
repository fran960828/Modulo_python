"""
CUENTA BANCARIA
Crea una clase "CuentaBancaria" con atributos como número de cuenta y saldo.
Implementa métodos para depositar y retirar dinero, y muestra el saldo actual.
"""

class CuentaBancaria:
    # Constructor de la clase, inicializa la cuenta con un número y saldo opcional
    def __init__(self, numero_cuenta, saldo=0):
        self.numero_cuenta = numero_cuenta  # Número de cuenta
        self.saldo = saldo  # Saldo inicial

    # Método para depositar dinero en la cuenta
    def depositar(self, monto):
        self.saldo += monto  # Aumentar el saldo con el monto depositado
        print(f"Se depositaron {monto} EU. Saldo actual: {self.saldo} EU")

    # Método para retirar dinero de la cuenta
    def retirar(self, monto):
        if self.saldo >= monto:  # Verificar si hay suficiente saldo para retirar
            self.saldo -= monto  # Disminuir el saldo con el monto retirado
            print(f"Se retiraron {monto} EU. Saldo actual: {self.saldo} EU")
        else:
            print("Saldo insuficiente")

    # Método para mostrar el saldo actual de la cuenta
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo} EU")

# Ejemplo de uso
cuenta = CuentaBancaria("1200", 100)  # Crear una cuenta con número "1200" y saldo inicial 100
cuenta.depositar(100)  # Depositar 100 euros en la cuenta
cuenta.retirar(110)  # Intentar retirar 110 euros de la cuenta
cuenta.mostrar_saldo()  # Mostrar el saldo actual de la cuenta
