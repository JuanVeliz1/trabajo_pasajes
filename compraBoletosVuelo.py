
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


def main():
    asientos = [
        [Asiento(1, 'normal'), Asiento(2, 'normal'), Asiento(3, 'normal'), Asiento(4, 'normal'), Asiento(5, 'normal'), Asiento(6, 'normal')],
        [Asiento(7, 'normal'), Asiento(8, 'normal'), Asiento(9, 'normal'), Asiento(10, 'normal'), Asiento(11, 'normal'), Asiento(12, 'normal')],
        [Asiento(13, 'normal'), Asiento(14, 'normal'), Asiento(15, 'normal'), Asiento(16, 'normal'), Asiento(17, 'normal'), Asiento(18, 'normal')],
        [Asiento(19, 'normal'), Asiento(20, 'normal'), Asiento(21, 'normal'), Asiento(22, 'normal'), Asiento(23, 'normal'), Asiento(24, 'normal')],
        [Asiento(25, 'normal'), Asiento(26, 'normal'), Asiento(27, 'normal'), Asiento(28, 'normal'), Asiento(29, 'normal'), Asiento(30, 'normal')],
        [Asiento(31, 'vip'), Asiento(32, 'vip'), Asiento(33, 'vip'), Asiento(34, 'vip'), Asiento(35, 'vip'), Asiento(36, 'vip')],
        [Asiento(37, 'vip'), Asiento(38, 'vip'), Asiento(39, 'vip'), Asiento(40, 'vip'), Asiento(41, 'vip'), Asiento(42, 'vip')]

    ]
    
    while True:
        print("     MENU    ")
        print("1. VER ASIENTOS DISPONIBLES")
        print("2. COMPRAR ASIENTO")
        print("3. ANULAR ASIENTO DE VUELO")
        print("4. MODIFICAR DATOS")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            print ("ASIENTOS DISPONIBLES")
            print ("asiento Normal: $78.900")
            print ("   asiento VIP: $240.000")
            mostrar_asientos(asientos)
        elif opcion == 2:
            print ("COMPRAR ASIENTOS")
            comprar_asiento(asientos)
        elif opcion == 3:
            print ("ANULAR VUELO")
            anular_asiento(asientos)
        elif opcion == 4:
            print ("MODIFICAR DATOS")
            modificar_datos_pasajero(asientos)
        elif opcion == 5:
            print ("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()