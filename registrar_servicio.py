from time import sleep
from Servicio import Servicio
from utils.clear import clear

def pagar_y_guardar(descripcion_servicio,equipos,total,nombre_cliente):

    servicio = Servicio(descripcion_servicio,nombre_cliente)
    servicio.generar_folio()
    servicio.agregar_equipos(equipos)
    servicio.generar_factura(total)


    print("Se ha cobrado con exito")
    sleep(5)

    
def registrar():
    while True:
        clear()
        print("¿Desea registrar un servicio? : 1 SI, 2 NO")
        opcion = input()
        if opcion == "1":

            print("Nombre del cliente: ")
            nombre_cliente = input()

            print("Descripción del servicio brindado: ")
            descripcion_servicio = input()

            print("¿En cuantos equipos se llevó acabo este servicio?")
            n_equipos = int(input())

            print("A continuación se pedirá la información de cada equipo...")
            datos_equipos = []
            print("Total de equipos : " + str(n_equipos))
            for i in range(n_equipos):
                print("Equipo " + str(i+1))
                print("Descripción del equipo: ")
                descripcion_equipo = input()
                print("Costo del servicio al equipo")
                costo_equipo = int(input())

                datos_equipos.append([descripcion_equipo, costo_equipo])
            
            precio_bruto = 0
            for i in datos_equipos:
                precio_bruto += i[1]
            iva = precio_bruto * .16
            total = precio_bruto + iva
            
            clear()
            print("Servicio: " +  descripcion_servicio)
            print("Cliente: " + nombre_cliente)
            print("El costo del servicio sin IVA es de: $" + str(precio_bruto))

            print("El IVA a cargar es de $" + str(iva))

            print("El total a pagar es de $" + str(total))

            while True:
                print("¿Cobrar? : 1 SI, 2 NO")
                opcion = input()
                if opcion == "1":
                    pagar_y_guardar(descripcion_servicio,datos_equipos,total,nombre_cliente)
                    break
                elif opcion == "2":
                    break
                else:
                    print("Opción invalida")

            break

        elif opcion == "2":
            pass
            break
        else:
            print("Opcion inválida")
    