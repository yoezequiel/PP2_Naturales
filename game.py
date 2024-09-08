import pygame
from src.config import *

pygame.init()

window = pygame.display.set_mode((width, height))
pygame.display.set_caption(name)

background_image = pygame.image.load(img)


rects = {
    word: pygame.Rect(initial_position[0], initial_position[1] + i * 30, 150, 30)
    for i, word in enumerate(words)
}

targets = {word: pygame.Rect(pos, (150, 30)) for word, pos in target_position.items()}

placed_correctly = {word: False for word in words}


def get_top_visible_word(mouse_pos):
    for word in words:
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
        if dragging_word and targets[dragging_word].cooliderect(rects[dragging_word]):
            rects[dragging_word].topleft = targets[dragging_word].topleft
            placed_correctly[dragging_word] = True
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
    window.blit(background_image, (0, 0))

    for target in targets.values():
        pygame.draw.rect(window, BLACK, target, 3)

    for i, word in enumerate(words):
        if i <= current_word_index:
            text = font.render(word, True, BLACK)
        window.blit(text, text.get_rect(center=rects[word].center))
    pygame.display.update()


while True:
    for event in pygame.event.get():
        handle_event(event)
    draw_elements()
