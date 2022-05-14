from database.Equipo import Equipo as EquipoDB

class Equipo:

    def __init__(self,servicio, descripcion, costo):
        self.servicio = servicio
        self.descripcion = descripcion
        self.costo_final = costo

    def registrar(self):
        EquipoDB.agregar(self.descripcion,self.costo_final,self.servicio)
        