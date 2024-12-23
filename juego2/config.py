import pygame
import os
import sys

pygame.init()


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


name = "El Bosque en Peligro"

WIDTH, HEIGHT = 800, 600
BUTTON = (0, 166, 81)
BUTTON_FONT = (150, 202, 63)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(name)

RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load("juego2/assets/img/forest.png")

trash_images = {
    "plastico": pygame.image.load("juego2/assets/img/plastico.png"),
    "vidrio": pygame.image.load("juego2/assets/img/vidrio.png"),
    "papel": pygame.image.load("juego2/assets/img/papel.png"),
    "organico": pygame.image.load("juego2/assets/img/organico.png"),
}
recycle_bins = {
    "plastico": pygame.image.load("juego2/assets/img/contenedor_plastico.png"),
    "vidrio": pygame.image.load("juego2/assets/img/contenedor_vidrio.png"),
    "papel": pygame.image.load("juego2/assets/img/contenedor_papel.png"),
    "organico": pygame.image.load("juego2/assets/img/contenedor_organico.png"),
}
font_button = pygame.font.Font(
    resource_path("juego2/assets/fonts/OpenSans-Bold.ttf"), 43
)
image_path = resource_path("juego2/assets/my_image.png")

font = pygame.font.Font(resource_path("juego2/assets/fonts/MoreSugar-Regular.ttf"), 26)
font_button = pygame.font.Font(
    resource_path("juego2/assets/fonts/OpenSans-Bold.ttf"), 43
)
img_start = resource_path("juego2/assets/img/Inicio.png")
img_game = resource_path("juego2/assets/img/Juego.png")
img_end = resource_path("juego2/assets/img/Final.png")
sound_button_dir = resource_path("juego2/assets/sound/button.wav")
check_sound = resource_path("juego2/assets/sound/check.mp3")
background_sound_dir = resource_path("juego2/assets/sound/background.mp3")
win_sound = resource_path("juego2/assets/sound/win.wav")
button = pygame.Rect((WIDTH // 2 - 224, HEIGHT // 3.2), (436, 101))
trash_count = 20
correct_sound = pygame.mixer.Sound(check_sound)
