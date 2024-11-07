import pygame
from config import *
import sys

pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Preguntas y Respuestas: Contaminación Cruzada")

clock = pygame.time.Clock()

background_start = pygame.image.load(img_start)
sound_button = pygame.mixer.Sound(sound_button_dir)
check = pygame.mixer.Sound(check_sound)
win = pygame.mixer.Sound(win_sound)
pygame.mixer.music.load(background_sound_dir)
pygame.mixer.music.play(-1)


def draw_button(button_hovered, button_clicked):
    if button_clicked:
        button_rect = pygame.Rect((width // 2 - 224, height // 2), (436 - 10, 101 - 10))
    elif button_hovered:
        button_rect = pygame.Rect(
            (width // 2 - 224 - 5, height // 2 - 5), (436 + 10, 101 + 10)
        )
    else:
        button_rect = button

    pygame.draw.rect(window, BUTTON, button_rect, border_radius=50)

    if button_clicked:
        text = font_button.render("JUGAR", True, BUTTON_FONT)
        text_rect = text.get_rect(center=button_rect.center)
    elif button_hovered:
        font_hover = pygame.font.Font("juego1/assets/fonts/OpenSans-Bold.ttf", 48)
        text = font_hover.render("JUGAR", True, BUTTON_FONT)
        text_rect = text.get_rect(center=button_rect.center)
    else:
        text = font_button.render("JUGAR", True, BUTTON_FONT)
        text_rect = text.get_rect(center=button_rect.center)

    window.blit(text, text_rect)


def start_screen():
    button_hovered = False
    button_clicked = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEMOTION:
                if button.collidepoint(event.pos):
                    button_hovered = True
                else:
                    button_hovered = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    button_clicked = True
                    sound_button.play()

            elif event.type == pygame.MOUSEBUTTONUP:
                if button_clicked:
                    return
                button_clicked = False

        window.blit(background_start, (0, 0))
        draw_button(button_hovered, button_clicked)
        pygame.display.update()


start_screen()


def draw_text(text, font, color, surface, x, y):
    label = font.render(text, True, color)
    surface.blit(label, (x, y))


def draw_buttons(options, selected_option=None):
    button_height = 50
    button_width = width - 100
    start_y = 150

    for i, option in enumerate(options):
        option_color = BLUE if selected_option == i else (0, 0, 0)
        pygame.draw.rect(
            window,
            WHITE,
            (50, start_y + i * (button_height + 10), button_width, button_height),
        )
        pygame.draw.rect(
            window,
            option_color,
            (50, start_y + i * (button_height + 10), button_width, button_height),
            3,
        )
        draw_text(
            option,
            small_font,
            option_color,
            window,
            100,
            start_y + i * (button_height + 10),
        )


def get_mouse_click(options):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i, _ in enumerate(options):
        if 50 < mouse_x < width - 50 and 150 + i * 60 < mouse_y < 150 + (i + 1) * 60:
            return i
    return None


def draw_question_and_options(question, options, selected_option=None):
    window.fill(WHITE)
    draw_text(question, font, BLACK, window, 1, 50)
    draw_buttons(options, selected_option)
    pygame.display.update()


def draw_correct_answer_animation():
    for _ in range(20):
        window.fill(WHITE)
        draw_text("¡Respuesta Correcta!", font, GREEN, window, 200, 200)
        pygame.display.update()
        pygame.time.wait(50)


def run_game():
    question_index = 0
    score = 0
    answering = True
    selected_option = None
    win_sound_played = False

    while answering:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_option = get_mouse_click(questions[question_index]["options"])

                if selected_option is not None:
                    if selected_option == questions[question_index]["correct"]:
                        score += 1
                        draw_correct_answer_animation()
                        correct_sound.play()
                    else:
                        window.fill(WHITE)
                        draw_text("¡Respuesta Incorrecta!", font, RED, window, 250, 200)
                        pygame.display.update()
                        pygame.time.wait(500)

                    question_index += 1
                    selected_option = None

        if question_index < len(questions):
            question = questions[question_index]["question"]
            options = questions[question_index]["options"]
            draw_question_and_options(question, options, selected_option)
        else:
            img_end = "juego1/assets/img/Final.png"
            background_game = pygame.image.load(img_end)
            pygame.mixer.music.stop()
            window.blit(background_game, (0, 0))
            draw_text(
                f"Tu puntuación final: {score}/{len(questions)}",
                font,
                BLACK,
                window,
                200,
                250,
            )
            if not win_sound_played:
                win.set_volume(0.1)
                win.play()
                win_sound_played = True
        pygame.display.update()
    pygame.quit()


run_game()
