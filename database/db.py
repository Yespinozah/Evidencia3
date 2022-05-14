import sqlite3

def connect():
    conn = sqlite3.connect('servicios.db')
    cursor = conn.cursor()
    return (cursor,conn)

def close(cursor: sqlite3.Cursor):
    cursor.close()
