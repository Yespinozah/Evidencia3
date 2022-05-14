from time import sleep
from .db import connect
class Servicio:

    @classmethod
    def agregar(_class,descripcion,nombre_cliente):
        (cursor,conn) = connect()
        
        cursor.execute('INSERT INTO Servicios (descripcion,cliente) VALUES (?,?)', (descripcion,nombre_cliente))
        conn.commit()
        cursor.execute('SELECT folio from Servicios order by folio desc LIMIT 1')
        row = cursor.fetchone()
        conn.close()
        return row[0]

    @classmethod
    def consultar(_class,folio):

        (cursor,conn) = connect()
        cursor.execute("""
        SELECT 
        Servicios.folio, 
        Servicios.cliente,
        Servicios.descripcion, 
        Ventas.monto, 
        Ventas.fecha 
        FROM Servicios 
        JOIN Ventas 
        ON Ventas.folio_servicio = Servicios.folio
        WHERE Servicios.folio = ? """,(folio,))

        rows = cursor.fetchall();

        conn.close()

        return rows
    
    @classmethod
    def consultar_por_fecha(_class,fecha):

        (cursor,conn) = connect()
        cursor.execute("""
        SELECT 
        Ventas.folio_servicio,
        Ventas.monto
        FROM Ventas 
        
        WHERE Ventas.fecha LIKE ? """,(f"{fecha}%",))
        rows = cursor.fetchall();



        lista_ventas = []
        for i in rows:
            servicio_dic = {'monto_total' : i[1], 'folio_servicio' : i[0]}
            
            cursor.execute("""
            SELECT 
            Servicios.descripcion,
            Servicios.cliente
            FROM Servicios 
            WHERE Servicios.folio = ? """,(servicio_dic.get('folio_servicio'),))

            servicio = cursor.fetchone()

            servicio_dic.update({'descripcion_servicio' : servicio[0],'cliente' : servicio[1]})

            cursor.execute("""
            SELECT 
            Equipos.descripcion,
            Equipos.costo_unitario
            FROM Equipos 
            WHERE Equipos.folio_servicio = ? """,(servicio_dic.get('folio_servicio'),))

            equipos = cursor.fetchall();

            equipos_list = []
            for row in equipos:
                equipos_list.append({"descripcion" : row[0], "costo_unitario" : row[1]})

            servicio_dic.update({'equipos' : equipos_list})

            lista_ventas.append(servicio_dic)


        conn.close()


        return lista_ventas

    @classmethod
    def consultar_folio_cliente(class_,fecha0,fecha1):

        (cursor,conn) = connect()
        cursor.execute(
            """
            select servicios.folio,  servicios.cliente 
            from ventas 
            join servicios
            on Servicios.folio = ventas.folio_servicio
            where ventas.fecha  
            BETWEEN ? AND ?;  
            """,
            (fecha0,fecha1)
        )

        rows = cursor.fetchall()
        conn.close()
        return rows