import sqlite3


def conectar_db():
    conn = sqlite3.connect("alumnos.db")
    return conn


def verificar_dni(dni):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumnos WHERE dni=?", (dni,))
    alumno = cursor.fetchone()

    if alumno:
        conn.close()
        return "alumno", alumno

    cursor.execute("SELECT * FROM admins WHERE dni=?", (dni,))
    admin = cursor.fetchone()
    conn.close()

    if admin:
        return "admin", admin

    return None, None


def cargar_alumno(dni, nombre, apellido, anio):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO alumnos (dni, nombre, apellido, anio) VALUES (?, ?, ?, ?)",
        (dni, nombre, apellido, anio),
    )
    conn.commit()
    conn.close()
    print("Alumno cargado exitosamente.")


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
