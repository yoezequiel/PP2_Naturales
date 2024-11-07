import pygame
import subprocess
from db import conectar_db, verificar_dni
from config import *

pygame.init()

fuente = pygame.font.Font(None, 36)


def mostrar_texto(texto, x, y, color=NEGRO):
    texto_superficie = fuente.render(texto, True, color)
    ventana.blit(texto_superficie, (x, y))


def cuadro_texto():
    dni = ""
    cursor_visible = True
    cursor_tiempo = pygame.time.get_ticks()
    activo = True
    mensaje_error = ""

    while activo:
        ventana.fill(BG)
        mostrar_texto("Ingrese su DNI:", 100, 100)
        pygame.draw.rect(ventana, BLANCO, (100, 200, 200, 40), 2)

        texto_ingresado = fuente.render(dni, True, NEGRO)
        ventana.blit(texto_ingresado, (110, 210))
        if cursor_visible:
            pygame.draw.line(
                ventana,
                NEGRO,
                (110 + texto_ingresado.get_width(), 210),
                (110 + texto_ingresado.get_width(), 240),
            )

        if pygame.time.get_ticks() - cursor_tiempo > 500:
            cursor_visible = not cursor_visible
            cursor_tiempo = pygame.time.get_ticks()

        if mensaje_error:
            mostrar_texto(mensaje_error, 100, 300, ROJO)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    tipo, datos = verificar_dni(dni)
                    if tipo == "alumno":
                        iniciar_juego_por_anio(datos[3])
                        return
                    elif tipo == "admin":
                        print(f"Bienvenido administrador {datos[0]}")
                        panel_administracion()
                        return
                    else:
                        mensaje_error = "DNI no encontrado"
                        dni = ""
                elif evento.key == pygame.K_BACKSPACE:
                    dni = dni[:-1]
                else:
                    dni += evento.unicode


def iniciar_juego_por_anio(anio):
    try:
        juego_file = f"juego{anio}/game.py"
        subprocess.run(["python", juego_file])
    except FileNotFoundError:
        print(f"No se encontró el archivo {juego_file} para el año {anio}.")


opciones = [
    "Cargar Alumno",
    "Eliminar Alumno",
    "Cargar Admin",
    "Eliminar Admin",
    "Ver Usuarios",
    "Salir",
]


def panel_administracion():
    activo = True
    opcion_seleccionada = 0
    while activo:
        ventana.fill(COLOR_FONDO)

        mostrar_texto("Panel de Administración", 100, 50, COLOR_TEXTO)

        for i, opcion in enumerate(opciones):
            if i == opcion_seleccionada:
                color_fondo = COLOR_SELECCION
                color_texto = COLOR_BOTON_TEXTO
            else:
                color_fondo = COLOR_BOTON
                color_texto = COLOR_TEXTO

            pygame.draw.rect(ventana, color_fondo, (100, 150 + i * 50, 400, 40))
            mostrar_texto(opcion, 120, 160 + i * 50, color_texto)

        pygame.display.flip()

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    activo = False
                elif evento.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                elif evento.key == pygame.K_UP:
                    opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    ejecutar_opcion_panel(opcion_seleccionada)


def ejecutar_opcion_panel(opcion_seleccionada):
    if opcion_seleccionada == 0:
        cargar_alumno()
    elif opcion_seleccionada == 1:
        eliminar_alumno()
    elif opcion_seleccionada == 2:
        cargar_admin()
    elif opcion_seleccionada == 3:
        eliminar_admin()
    elif opcion_seleccionada == 4:
        ver_usuarios()
    elif opcion_seleccionada == 5:
        pygame.quit()


def cargar_alumno():
    dni = input_texto("Ingrese el DNI del alumno: ")
    nombre = input_texto("Ingrese el nombre del alumno: ")
    apellido = input_texto("Ingrese el apellido del alumno: ")
    anio = input_texto("Ingrese el año del alumno (1-7): ")

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


def ver_usuarios():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT dni, nombre, apellido, anio FROM alumnos")
    alumnos = cursor.fetchall()

    cursor.execute("SELECT dni FROM admins")
    admins = cursor.fetchall()

    conn.close()

    ventana.fill(COLOR_FONDO)
    mostrar_texto("Usuarios Registrados:", 100, 50, COLOR_TEXTO)

    y_offset = 100
    mostrar_texto("Alumnos:", 100, y_offset, COLOR_TEXTO)
    y_offset += 40
    for alumno in alumnos:
        mostrar_texto(
            f"DNI: {alumno[0]}, Nombre: {alumno[1]} {alumno[2]}, Año: {alumno[3]}",
            100,
            y_offset,
            COLOR_TEXTO,
        )
        y_offset += 40

    mostrar_texto("Administradores:", 100, y_offset, COLOR_TEXTO)
    y_offset += 40
    for admin in admins:
        mostrar_texto(f"DNI: {admin[0]}", 100, y_offset, COLOR_TEXTO)
        y_offset += 40

    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                esperando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    esperando = False
                    panel_administracion()


def input_texto(mensaje):
    activo = True
    texto = ""
    while activo:
        ventana.fill(COLOR_FONDO)
        mostrar_texto(mensaje, 100, 100)
        texto_ingresado = fuente.render(texto, True, COLOR_TEXTO)
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
    cuadro_texto()


if __name__ == "__main__":
    main()
    pygame.quit()
