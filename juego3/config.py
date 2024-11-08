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
            "La transferencia de bacterias o alérgenos entre alimentos",
            "La cocción incompleta de los alimentos",
            "El exceso de sal en la comida",
        ],
        "correct": 0,
    },
    {
        "question": "¿Cuál de los siguientes es contaminación cruzada?",
        "options": [
            "Usar diferentes tablas de cortar para carne y vegetales",
            "Cortar pollo crudo y vegetales en la misma tabla sin lavarla",
            "Guardar carne y vegetales separados del refrigerador",
        ],
        "correct": 1,
    },
    {
        "question": "¿Cuál práctica ayuda a evitar la contaminación cruzada?",
        "options": [
            "Usar utensilios separados para alimentos crudos y cocidos",
            "Lavar todos los alimentos con jabón",
            "No lavar las manos mientras se cocina",
        ],
        "correct": 0,
    },
    {
        "question": "¿Por qué lavar los utensilios luego de manipular alimentos crudos?",
        "options": [
            "Para evitar sabores extraños",
            "Para evitar la transferencia de bacterias dañinas a otros alimentos",
            "Para hacer que los utensilios se vean mejor",
        ],
        "correct": 1,
    },
    {
        "question": "¿Cuál hábito ayuda a evitar la contaminación cruzada?",
        "options": [
            "Lavar las manos después de manipular alimentos crudos",
            "Usar el mismo paño para limpiar todas las superficies",
            "Dejar los alimentos cocidos al aire libre",
        ],
        "correct": 0,
    },
]
