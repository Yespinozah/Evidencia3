from db import connect


(cursor,conn) = connect()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS Servicios(
            folio INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            cliente TEXT NOT NULL,
        );
    """)

cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ventas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            monto INTEGER NOT NULL,
            fecha DATE NOT NULL,
            folio_servicio INTEGER NOT NULL,
            FOREIGN KEY (folio_servicio) REFERENCES Servicios(folio)
        );
    """)


cursor.execute("""
        CREATE TABLE IF NOT EXISTS Equipos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            costo_unitario INTEGER NOT NULL,
            folio_servicio INTEGER NOT NULL,
            FOREIGN KEY (folio_servicio) REFERENCES Servicios(folio)
        );
    """)

conn.commit()
cursor.close()
