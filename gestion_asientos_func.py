
class Asiento:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo  # 'normal' o 'vip'
        self.ocupado = False
        self.pasajero = None

class Pasajero:
    def __init__(self, nombre, rut, telefono, banco):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        self.banco = banco

def mostrar_asientos(asientos):
    for i, fila in enumerate(asientos):
        print("[" + " ".join("X" if asiento.ocupado else str(asiento.numero) for asiento in fila) + "]")
        if i == 4:
            print("|_________________|")

def comprar_asiento(asientos):
    nombre = input("Ingrese su nombre: ")
    rut = input("Ingrese su RUT: ")
    telefono = input("Ingrese su numero telefónico: ")
    banco = input("Ingrese su banco asociado: ")
    asiento_num = int(input("Ingrese el n° de asiento que desea comprar: "))
    
    for fila in asientos:
        for asiento in fila:
            if asiento.numero == asiento_num:
                if asiento.ocupado:
                    print("El asiento ya está ocupado.")
                    return
                pasajero = Pasajero(nombre, rut, telefono, banco)
                asiento.ocupado = True
                asiento.pasajero = pasajero
                if asiento.tipo == "vip":
                    precio = 240000
                else:
                    precio = 78900
                if banco.lower() == "bancoduoc":
                    precio = precio - (precio*0.15)
                    print ("Se aplicó un 15 porciento de dcto.")
                    print ("Asiento comprado con éxito. Precio: $",precio)
                
def anular_asiento(asientos):
    asiento_num = int(input("Ingrese el número de asiento que desea anular: "))
    for fila in asientos:
        for asiento in fila:
            if asiento.numero == asiento_num:
                if not asiento.ocupado:
                    print("El asiento ya está disponible.")
                    return
                asiento.ocupado = False
                asiento.pasajero = None
                print("Asiento anulado con éxito.")
                return

def modificar_datos_pasajero(asientos):
    rut = input("Ingrese el RUT del pasajero: ")
    asiento_num = int(input("Ingrese el número de asiento: "))
    for fila in asientos:
        for asiento in fila:
            if asiento.numero == asiento_num and asiento.ocupado and asiento.pasajero.rut == rut:
                print("1. Modificar nombre")
                print("2. Modificar teléfono")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    asiento.pasajero.nombre = nuevo_nombre
                elif opcion == 2:
                    nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                    asiento.pasajero.telefono = nuevo_telefono
                else:
                    print("Datos inválidos. Ingrese nuevamente")
                print("Datos modificados con éxito.")
                return


