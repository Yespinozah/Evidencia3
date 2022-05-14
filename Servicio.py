from datetime import datetime
from time import sleep
from Equipo import Equipo
from Venta import Venta
from database.Servicio import Servicio as ServicioDB

class Servicio :

    def __init__(self, descripcion,cliente):
        self.descripcion = descripcion
        self.folio = 0
        self.equipos = []
        self.nombre_cliente = cliente

    def generar_factura(self,total):
        venta = Venta(total, self.folio)
        venta.guardar_venta()
        

    def generar_folio(self):
        self.folio = ServicioDB.agregar(self.descripcion,self.nombre_cliente)


    def agregar_equipos(self,equipos):
        self.equipos = equipos
        for i in self.equipos:
            equipo = Equipo(self.folio, i[0], i[1])
            print("Guardando equipo " + equipo.descripcion)
            equipo.registrar()
    @classmethod
    def consultar(_class, folio):
        rows = ServicioDB.consultar(folio)
        for row in rows:
            print("Folio: " + str(row[0]))
            print("Cliente: " + str(row[1]))
            print("Descripción: " + str(row[2]))
            print("Total: " + str(row[3]))
            print("Fecha: " + str(row[4]))

    @classmethod
    def consultar_por_fecha(_class, fecha):
        fecha = datetime.strptime(fecha, '%Y-%m-%d')
        fecha = str(fecha)[0:10]

        servicios = ServicioDB.consultar_por_fecha(fecha)
        if servicios:
            print("*"*100)

            
            for servicio in servicios:
                print ("{:<8} {:<20} {:<20} {:<8} {:<8} {:<8}".format('Servicio','Descripción','Cliente','Sub Total','IVA','Total'))

                print("-"*100)
                sub_total = 0
                for i in servicio.get('equipos'):
                    sub_total += i.get('costo_unitario')
                folio = servicio.get('folio_servicio')
                descripcion = servicio.get('descripcion_servicio')
                cliente = servicio.get('cliente')
                monto_total = servicio.get('monto_total')
                iva = round(monto_total - sub_total,2)
                print ("{:<8} {:<20} {:<20} {:<8} {:<8} {:<8}".format(
                    folio,descripcion,cliente,sub_total,iva,monto_total
                    ))
                print("Equipos")
                print("{:<20} {:<15} {:<8} {:<8}".format(
                    'Descripción',"Costo Unitario","IVA","Total"
                ))
                print("."*100)

                for i in servicio.get('equipos'):
                    descripcion_equipo = i.get('descripcion')
                    costo_unitario = i.get('costo_unitario')
                    iva = round(costo_unitario*.16,2)
                    total = iva + costo_unitario
                    print("{:<20} {:<15} {:<8} {:<8}".format(
                        descripcion_equipo,costo_unitario,iva,total
                    ))
                    


                
            print("*"*100)

        sleep(10)
    
    @classmethod
    def consultar_folio_cliente(class_,fecha0,fecha1):
        
        clientes_folios = ServicioDB.consultar_folio_cliente(fecha0,fecha1)
        print(f"***** Reporte del {fecha0} al {fecha1} ****")
        print("{:<10} {:<20}".format(
                'Folio Servicio','Venta'
            ))
        print("*"*100)
        for i in clientes_folios:
            
            print("{:<15} {:<20}".format(
                i[0],i[1]
            ))
            print("-"*100)
        print("*"*100)

        
        