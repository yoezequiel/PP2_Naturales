import pygame

pygame.init()


width = 800
height = 600
name = "Cuerpo Humano"
img = "assets/img/Juego.png"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

words = [
    "Cabeza",
    "Oreja",
    "Ojo",
    "Boca",
    "Mano",
    "Hombre",
    "Codo",
    "Rodilla",
    "Pie",
    "Estomago",
    "Pierna",
]
initial_position = (10, 550)

current_word_index = 0
font = pygame.font.Font(None, 36)
dragging = False
dragging_word = None

target_position = {
    "Cabeza": (0, 0),
    "Oreja": (0, 0),
    "Ojo": (0, 0),
    "Boca": (0, 0),
    "Mano": (0, 0),
    "Hombre": (0, 0),
    "Codo": (0, 0),
    "Rodilla": (0, 0),
    "Pie": (0, 0),
    "Estomago": (0, 0),
    "Pierna": (0, 0),
}
