import pygame

pygame.init()

font = pygame.font.Font("assets/fonts/MoreSugar-Regular.ttf", 26)
font_button = pygame.font.Font("assets/fonts/OpenSans-Bold.ttf", 43)
width = 800
height = 600
button = pygame.Rect((width // 2 - 200, height // 2), (436, 101))


name = "Cuerpo Humano"
img_start = "assets/img/Inicio.png"
img_game = "assets/img/Juego.png"
img_end = "assets/img/Final.png"
sound_button_dir = "assets/sound/button.wav"
check_sound = "assets/sound/check.mp3"

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
