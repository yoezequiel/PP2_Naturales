import sqlite3


def conectar_db():
    conn = sqlite3.connect("alumnos.db")
    return conn


def crear_tablas():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS alumnos (
                        dni INTEGER PRIMARY KEY,
                        nombre TEXT,
                        apellido TEXT,
                        anio INTEGER)"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS admins (
                        dni INTEGER PRIMARY KEY)"""
    )
    conn.commit()
    conn.close()
