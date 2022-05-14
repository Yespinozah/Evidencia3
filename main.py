from menus import print_menu
from utils.clear import clear
from registrar_servicio import registrar
from consultar_servicios import consultar_folio_cliente, consultar_por_fecha, consultar_por_folio

def run():
    while True:
        clear()
        print_menu()
        opcion = (input())
        if opcion == "1" :
            print("Registrar Servicio")
            registrar()
            
        elif opcion == "2":
            print("Consultar Servicio")
            consultar_por_folio()
        elif opcion == "3":
            print("Consultar Servicios Por determinada fecha")
            consultar_por_fecha()
        elif opcion == "4":
            consultar_folio_cliente()
            print("Consultar Servicios en determinadas fechas")
        elif opcion == "5":
            print("Vuelve pronto...")
            break
        else:
            print("Opción no válida")
        
if __name__ == "__main__":
    run()