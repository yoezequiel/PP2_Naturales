import pygame
import random
from config import *

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Conociendo el Sistema Solar")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 30)


current_planet = 0
current_question = 0
score = 0
running = True
opciones_aleatorias = []


def mostrar_pregunta(planeta, pregunta):
    screen.fill(BLACK)

    planet_bg = pygame.image.load(planeta["background"])
    planet_bg = pygame.transform.scale(planet_bg, (600, 600))
    screen.blit(planet_bg, (100, 0))

    question_text = font.render(pregunta["question"], True, WHITE)
    screen.blit(question_text, (100, 100))

    y_offset = 200
    for idx, opcion in enumerate(opciones_aleatorias):
        opcion_text = font.render(f"{idx + 1}. {opcion}", True, WHITE)
        screen.blit(opcion_text, (100, y_offset))
        y_offset += 50

    pygame.display.flip()


while running:
    planeta = planets[current_planet]
    pregunta = planeta["questions"][current_question]

    if not opciones_aleatorias:
        opciones_aleatorias = pregunta["options"][:]
        random.shuffle(opciones_aleatorias)

    respuesta_correcta = pregunta["correct"]

    mostrar_pregunta(planeta, pregunta)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            seleccion = -1
            if event.key == pygame.K_1:
                seleccion = 0
            elif event.key == pygame.K_2:
                seleccion = 1
            elif event.key == pygame.K_3:
                seleccion = 2
            elif event.key == pygame.K_4:
                seleccion = 3

            if seleccion != -1 and opciones_aleatorias[seleccion] == respuesta_correcta:
                score += 1
                print("Respuesta correcta")
            elif seleccion != -1:
                print("Respuesta incorrecta")

            current_question += 1
            opciones_aleatorias = []
            if current_question >= len(planeta["questions"]):
                current_question = 0
                current_planet += 1
                if current_planet >= len(planets):
                    running = False

pantalla_final = True
while pantalla_final:
    screen.fill(BLACK)
    score_text = font.render(f"Puntaje Final: {score}", True, WHITE)
    screen.blit(
        score_text,
        (screen_width // 2 - score_text.get_width() // 2, screen_height // 2),
    )
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pantalla_final = False

pygame.quit()
