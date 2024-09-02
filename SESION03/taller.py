'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
# Tarea
from datetime import datetime

class CuentaBancaria:
    def __init__(self, numeroCta="", nombreCliente="", saldoCta=0.0, fechaApertura=None):
        if fechaApertura is None:
            fechaApertura = datetime.now()
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaApertura = fechaApertura
        self.__ultimoRetiro = None
        self.__ultimaConsignacion = None

    def set(self, numeroCta, nombreCliente, saldoCta, fechaApertura=None):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        if fechaApertura is None:
            self.__fechaApertura = datetime.now()
        else:
            self.__fechaApertura = fechaApertura

    def set_numeroCta(self, numeroCta):
        self.__numeroCta = numeroCta

    def set_nombreCliente(self, nombreCliente):
        self.__nombreCliente = nombreCliente

    def set_saldoCta(self, saldoCta):
        if saldoCta < 0:
            self.__saldoCta = 0
        else:
            self.__saldoCta = saldoCta

    def set_fechaApertura(self, fechaApertura):
        self.__fechaApertura = fechaApertura

    def get_numeroCta(self):
        return self.__numeroCta

    def get_nombreCliente(self):
        return self.__nombreCliente

    def get_saldoCta(self):
        return self.__saldoCta

    def get_fechaApertura(self):
        return self.__fechaApertura

    def get_ultimoRetiro(self):
        return self.__ultimoRetiro

    def get_ultimaConsignacion(self):
        return self.__ultimaConsignacion

    def consignar(self, monto):
        if monto > 0:
            self.__saldoCta += monto
            self.__ultimaConsignacion = datetime.now()
            print(f"Consignación exitosa. Nuevo saldo: {self.__saldoCta}")
        else:
            print("El monto debe ser mayor a cero.")

    def retirar(self, monto):
        if monto > 0:
            if self.__saldoCta >= monto:
                self.__saldoCta -= monto
                self.__ultimoRetiro = datetime.now()
                print(f"Retiro exitoso. Nuevo saldo: {self.__saldoCta}")
            else:
                print("Saldo insuficiente.")
        else:
            print("El monto debe ser mayor a cero.")

    def transferencia(self, monto, cuenta_destino):
        if monto > 0:
            if self.__saldoCta >= monto:
                self.retirar(monto)
                cuenta_destino.consignar(monto)
                print(f"Transferencia exitosa a la cuenta {cuenta_destino.get_numeroCta()}.")
            else:
                print("Saldo insuficiente para la transferencia.")
        else:
            print("El monto debe ser mayor a cero.")

def main():
    cuentas = {}
    
    while True:
        print("\n--- Menú ---")
        print("1. Apertura de cuenta")
        print("2. Consignar")
        print("3. Retirar")
        print("4. Transferencia")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            numero = input("Número de cuenta: ")
            nombre = input("Nombre del cliente: ")
            saldo = float(input("Saldo inicial: "))
            fecha = datetime.now()
            cuenta = CuentaBancaria(numero, nombre, saldo, fecha)
            cuentas[numero] = cuenta
            print("Cuenta abierta exitosamente.")
        
        elif opcion == '2':
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                monto = float(input("Monto a consignar: "))
                cuentas[numero].consignar(monto)
            else:
                print("Número de cuenta no encontrado.")
        
        elif opcion == '3':
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                monto = float(input("Monto a retirar: "))
                cuentas[numero].retirar
            else:
                print("Número de cuenta no encontrado.")
        
        elif opcion == '4':
            numero_origen = input("Número de cuenta origen: ")
            numero_destino = input("Número de cuenta destino: ")
            if numero_origen in cuentas and numero_destino in cuentas:
                monto = float(input("Monto a transferir: "))
                cuentas[numero_origen].transferencia(monto, cuentas[numero_destino])
            else:(monto)
                print("Número de cuenta origen o destino no encontrado.")
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
