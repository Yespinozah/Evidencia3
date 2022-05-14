from datetime import datetime
from Servicio import Servicio

def consultar_por_folio():
    while True:
        print("¿Desea consultar un servicio en base al folio?: 1 SI, 2 NO.")
        opcion = input()
        if opcion == "1":
            print("Folio: ")
            folio = input()

            Servicio.consultar(folio)  
        elif opcion == "2":
            break
        else:
            print("Opción inválida")
        

def consultar_por_fecha():
    while True:
        print("¿Desea generar un reporte de servicios en base a la fecha?: 1 SI, 2 NO.")
        opcion = input()
        if opcion == "1":
            while True:
                
                try:
                    fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
                    datetime.strptime(fecha, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Fecha inválida")
                    continue
            Servicio.consultar_por_fecha(fecha)
            
            #Servicio.consultar(folio)  
        elif opcion == "2":
            break
        else:
            print("Opción inválida")

def consultar_folio_cliente():
    while True:
        print("¿Desea generar un reporte de servicios en base a un intervalo de fecha?: 1 SI, 2 NO.")
        opcion = input()
        if opcion == "1":
            while True:
                print("Se pedirán a continuación 2 fechas, la primera es la fecha en la que inicia el reporte")
                print("La segunda es la fecha limite más un día.")
                try:
                    _fecha0 = input("Ingresa la primera fecha en el formato YYYY-MM-DD: ")
                    fecha0 = datetime.strptime(_fecha0, '%Y-%m-%d')
                    fecha0 = str(fecha0)[0:10]

                    
                    break
                except ValueError:
                    print("Fecha inválida")
                    continue

            while True:
                try:
                    _fecha1 = input("Ingresa la segunda fecha en el formato YYYY-MM-DD: ")
                    fecha1 = datetime.strptime(_fecha1, '%Y-%m-%d')
                    fecha1 = str(fecha1)[0:10]

                    print(fecha1)
                    print(fecha0)
                    if fecha1 == fecha0:
                        print("Las fechas son iguales, favor de cambiar la segunda.")
                        continue

                    break
                except ValueError:
                    print("Fecha inválida")
                    continue
            
            
            Servicio.consultar_folio_cliente(fecha0,fecha1)
            
            #Servicio.consultar(folio)  
        elif opcion == "2":
            break
        else:
            print("Opción inválida")