import pygame
import sqlite3
from config import *

pygame.init()


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


def verificar_dni(dni):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alumnos WHERE dni=?", (dni,))
    alumno = cursor.fetchone()

    if alumno:
        return "alumno", alumno

    cursor.execute("SELECT * FROM admins WHERE dni=?", (dni,))
    admin = cursor.fetchone()

    if admin:
        return "admin", admin

    conn.close()
    return None, None


def mostrar_texto(texto, x, y):
    texto_superficie = fuente.render(texto, True, NEGRO)
    ventana.blit(texto_superficie, (x, y))


def cuadro_texto():
    dni = ""
    activo = True
    while activo:
        ventana.fill(BG)

        mostrar_texto("Ingrese su DNI:", 100, 100)

        texto_ingresado = fuente.render(dni, True, NEGRO)
        ventana.blit(texto_ingresado, (100, 200))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    tipo, datos = verificar_dni(dni)
                    if tipo == "alumno":
                        print(
                            f"Bienvenido {datos[1]} {datos[2]}, te dirigimos a tu juego."
                        )
                        return
                    elif tipo == "admin":
                        print(f"Bienvenido administrador {datos[0]}")
                        panel_administracion()
                        return
                    else:
                        print("DNI no encontrado")
                        dni = ""
                elif evento.key == pygame.K_BACKSPACE:
                    dni = dni[:-1]
                else:
                    dni += evento.unicode


def panel_administracion():
    activo = True
    opcion = ""
    while activo:
        ventana.fill(BG)
        mostrar_texto("Panel de Administración", 100, 100)
        mostrar_texto("1. Cargar Alumno", 100, 200)
        mostrar_texto("2. Eliminar Alumno", 100, 250)
        mostrar_texto("3. Cargar Admin", 100, 300)
        mostrar_texto("4. Eliminar Admin", 100, 350)
        mostrar_texto("Presione ESC para salir", 100, 400)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    activo = False
                elif evento.unicode in ["1", "2", "3", "4"]:
                    opcion = evento.unicode
                    ejecutar_opcion_panel(opcion)


def ejecutar_opcion_panel(opcion):
    if opcion == "1":
        cargar_alumno()
    elif opcion == "2":
        eliminar_alumno()
    elif opcion == "3":
        cargar_admin()
    elif opcion == "4":
        eliminar_admin()


def cargar_alumno():
    dni = input_texto("Ingrese el DNI del alumno: ")
    nombre = input_texto("Ingrese el nombre del alumno: ")
    apellido = input_texto("Ingrese el apellido del alumno: ")
    anio = input_texto("Ingrese el año del alumno: ")

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO alumnos (dni, nombre, apellido, anio) VALUES (?, ?, ?, ?)",
        (dni, nombre, apellido, anio),
    )
    conn.commit()
    conn.close()
    print("Alumno cargado exitosamente.")


def eliminar_alumno():
    dni = input_texto("Ingrese el DNI del alumno a eliminar: ")

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alumnos WHERE dni=?", (dni,))
    conn.commit()
    conn.close()
    print("Alumno eliminado exitosamente.")


def cargar_admin():
    dni = input_texto("Ingrese el DNI del nuevo admin: ")

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO admins (dni) VALUES (?)", (dni,))
    conn.commit()
    conn.close()
    print("Admin cargado exitosamente.")


def eliminar_admin():
    dni = input_texto("Ingrese el DNI del admin a eliminar: ")

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM admins WHERE dni=?", (dni,))
    conn.commit()
    conn.close()
    print("Admin eliminado exitosamente.")


def input_texto(mensaje):
    activo = True
    texto = ""
    while activo:
        ventana.fill(BG)
        mostrar_texto(mensaje, 100, 100)
        texto_ingresado = fuente.render(texto, True, NEGRO)
        ventana.blit(texto_ingresado, (100, 200))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return texto
                elif evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                else:
                    texto += evento.unicode


def main():
    crear_tablas()
    cuadro_texto()


if __name__ == "__main__":
    main()
    pygame.quit()
