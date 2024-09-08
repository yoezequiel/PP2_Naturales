import pygame
import random
from src.config import *

pygame.init()

window = pygame.display.set_mode((width, height))
pygame.display.set_caption(name)

background_start = pygame.image.load(img_start)
sound_button = pygame.mixer.Sound(sound_button_dir)
check = pygame.mixer.Sound(check_sound)


def draw_button():
    pygame.draw.rect(window, BUTTON, button, border_radius=50)
    text = font_button.render("JUGAR", True, BUTTON_FONT)
    text_rect = text.get_rect(center=button.center)
    window.blit(text, text_rect)


def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    sound_button.play()
                    return

        window.blit(background_start, (0, 0))
        draw_button()
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


def draw_elements():
    window.blit(background_game, (0, 0))

    for i, word in enumerate(words):
        if i <= current_word_index:
            text = font.render(word, True, TEXT)
            window.blit(text, text.get_rect(center=rects[word].center))

    if all(placed_correctly.values()):
        end = pygame.image.load(img_end)
        window.blit(end, (0, 0))

    pygame.display.update()


while True:
    for event in pygame.event.get():
        handle_event(event)
    draw_elements()
