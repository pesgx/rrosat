import sqlite3

def obtener_conexion():
    """
    Establece la conexión con la base de datos SQLite.
    """
    return sqlite3.connect('bbdd_rosat.sqlite3')
