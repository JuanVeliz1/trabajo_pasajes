
from gestion_asientos_func import Asiento, Pasajero, mostrar_asientos, comprar_asiento, anular_asiento, modificar_datos_pasajero

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
            print ("Boleto Normal: $78900")
            print ("Boleto VIP: $240000")
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