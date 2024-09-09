import pygame
import random
from config import *

pygame.init()
pygame.mixer.init()


window = pygame.display.set_mode((width, height))
pygame.display.set_caption(name)

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
        font_hover = pygame.font.Font(
            resource_path("assets/fonts/OpenSans-Bold.ttf"), 43
        )

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

background_game = pygame.image.load(img_game)

random.shuffle(words)
rects = {
    word: pygame.Rect(initial_position[0], initial_position[1] + i * 30, 150, 30)
    for i, word in enumerate(words)
}
targets = {word: pygame.Rect(pos, (150, 30)) for word, pos in target_position.items()}
placed_correctly = {word: False for word in words}


def get_top_visible_word(mouse_pos):
    for word in reversed(words):
        if rects[word].collidepoint(mouse_pos) and not placed_correctly[word]:
            return word
    return None


def handle_event(event):
    global dragging, dragging_word, current_word_index

    if event.type == pygame.QUIT:
        pygame.quit()
        running = False

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if not dragging:
            dragging_word = get_top_visible_word(event.pos)
            dragging = bool(dragging_word)

    elif event.type == pygame.MOUSEBUTTONUP and dragging:
        if dragging_word and targets[dragging_word].colliderect(rects[dragging_word]):
            rects[dragging_word].topleft = targets[dragging_word].topleft
            placed_correctly[dragging_word] = True
            check.play()
            current_word_index += 1
            if current_word_index < len(words):
                rects[words[current_word_index]].topleft = initial_position
        else:
            rects[dragging_word].topleft = initial_position
        dragging, dragging_word = False, None
    elif event.type == pygame.MOUSEMOTION and dragging:
        if dragging_word:
            rects[dragging_word].move_ip(event.rel)


win_sound_played = False


def draw_elements():
    window.blit(background_game, (0, 0))

    for i, word in enumerate(words):
        if i <= current_word_index:
            text = font.render(word, True, TEXT)
            window.blit(text, text.get_rect(center=rects[word].center))

    if all(placed_correctly.values()):
        pygame.mixer.music.stop()
        end = pygame.image.load(img_end)
        window.blit(end, (0, 0))
        global win_sound_played
        if not win_sound_played:
            win.set_volume(0.1)
            win.play()
            win_sound_played = True
    pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        handle_event(event)
    draw_elements()
