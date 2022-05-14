from datetime import datetime
from database.Venta import Venta as VentaDB

class Venta :

    def __init__(self, monto, servicio):
        self.fecha = datetime.now()
        self.monto = monto
        self.servicio = servicio

    def guardar_venta(self):
        VentaDB.agregar(self.monto,self.fecha,self.servicio)

        print("Factura Generada.")
        print("Total: " + str(self.monto))
        print("Folio Servicio: " + str(self.servicio))
        print("Fecha: " + str(self.fecha))
