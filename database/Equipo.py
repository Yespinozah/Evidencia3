from .db import connect
class Equipo:

    @classmethod
    def agregar(_class,descripcion,c_u,folio):
        (cursor,conn) = connect()
        
        cursor.execute('INSERT INTO Equipos (descripcion,costo_unitario, folio_servicio) VALUES (?,?,?)',
             (descripcion,int(c_u),int(folio)))
        conn.commit()
        

    
