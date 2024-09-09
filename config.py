import pygame
import os
import sys

pygame.init()

width = 800
height = 600
button = pygame.Rect((width // 2 - 224, height // 2), (436, 101))


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


image_path = resource_path("assets/my_image.png")

font = pygame.font.Font(resource_path("assets/fonts/MoreSugar-Regular.ttf"), 26)
font_button = pygame.font.Font(resource_path("assets/fonts/OpenSans-Bold.ttf"), 43)
name = "Cuerpo Humano"
img_start = resource_path("assets/img/Inicio.png")
img_game = resource_path("assets/img/Juego.png")
img_end = resource_path("assets/img/Final.png")
sound_button_dir = resource_path("assets/sound/button.wav")
check_sound = resource_path("assets/sound/check.mp3")
background_sound_dir = resource_path("assets/sound/background.mp3")
win_sound = resource_path("assets/sound/win.wav")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
TEXT = (91, 55, 12)
BUTTON = (0, 166, 81)
BUTTON_FONT = (150, 202, 63)

words = [
    "Cabeza",
    "Oreja",
    "Ojo",
    "Boca",
    "Mano",
    "Hombro",
    "Codo",
    "Rodilla",
    "Pie",
    "Estomago",
    "Pierna",
]

initial_position = (10, 550)
current_word_index = 0

dragging = False
dragging_word = None

target_position = {
    "Cabeza": (85, 157),
    "Oreja": (605, 132),
    "Ojo": (85, 240),
    "Boca": (605, 198),
    "Mano": (85, 305),
    "Hombro": (605, 275),
    "Codo": (605, 363),
    "Rodilla": (605, 453),
    "Pie": (605, 543),
    "Estomago": (85, 394),
    "Pierna": (85, 467),
}
