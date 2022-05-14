from .db import connect
class Venta:

    @classmethod
    def agregar(_class,monto,fecha,folio_servicio):
        (cursor,conn) = connect()
        
        cursor.execute('INSERT INTO Ventas (monto,fecha,folio_servicio) VALUES (?,?,?)', 
        (monto,fecha,str(folio_servicio),))
        conn.commit()

    
