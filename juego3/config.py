import pygame

pygame.init()

font = pygame.font.Font("juego3/assets/fonts/MoreSugar-Regular.ttf", 30)
small_font = pygame.font.Font("juego3/assets/fonts/MoreSugar-Regular.ttf", 25)
font_button = pygame.font.Font("juego3/assets/fonts/OpenSans-Bold.ttf", 43)
width = 800
height = 600
button = pygame.Rect((width // 2 - 224, height // 2), (436, 101))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BUTTON = (0, 166, 81)
BUTTON_FONT = (150, 202, 63)

name = "Cuerpo Humano"
img_start = "juego3/assets/img/Inicio.png"
img_game = "juego3/assets/img/Juego.png"
img_end = "juego3/assets/img/Final.png"
sound_button_dir = "juego3/assets/sound/button.wav"
check_sound = "juego3/assets/sound/check.mp3"
background_sound_dir = "juego3/assets/sound/background.mp3"
win_sound = "juego3/assets/sound/win.wav"
correct_sound = pygame.mixer.Sound("juego3/assets/sound/check.mp3")

questions = [
    {
        "question": "¿Qué es la contaminación cruzada?",
        "options": [
            "Contaminación del agua",
            "Contaminación entre alimentos",
            "Contaminación del aire",
        ],
        "correct": 1,
    },
    {
        "question": "¿Cuál es más propenso a la contaminación cruzada?",
        "options": [
            "Carne cruda",
            "Frutas",
            "Verduras cocidas",
        ],
        "correct": 0,
    },
    {
        "question": "¿Cómo prevenir la contaminación cruzada en la cocina?",
        "options": [
            "Usando un solo cuchillo",
            "Separando alimentos crudos y cocidos",
            "Cocinando todo a la misma temperatura",
        ],
        "correct": 1,
    },
]
