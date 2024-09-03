import pygame
import sys

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cuerpo Humano")

WHITE, BLACK, GREEN, BACKGROUND = (255, 255, 255), (0, 0, 0), (0, 255, 0), (51, 51, 51)

images = {
    "head": pygame.image.load("head.png"),
    "body": pygame.image.load("body.png"),
    "left_arm": pygame.image.load("left_arm.png"),
    "right_arm": pygame.transform.flip(pygame.image.load("left_arm.png"), True, False),
    "left_leg": pygame.image.load("leg.png"),
    "right_leg": pygame.transform.flip(pygame.image.load("leg.png"), True, False),
}

initial_positions = {
    "head": (50, 50),
    "body": (50, 150),
    "left_arm": (50, 250),
    "right_arm": (50, 350),
    "left_leg": (50, 450),
    "right_leg": (50, 550),
}
rects = {
    part: img.get_rect(topleft=initial_positions[part]) for part, img in images.items()
}

target_positions = {
    "head": (500, 85),
    "body": (500, 150),
    "left_arm": (467, 150),
    "right_arm": (565, 150),
    "left_leg": (500, 248),
    "right_leg": (533, 248),
}
targets = {
    part: pygame.Rect(target_positions[part], images[part].get_size())
    for part in images
}

dragging, dragging_part = False, None
placed_correctly = {part: False for part in images}

font = pygame.font.Font(None, 74)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for part, rect in rects.items():
                if rect.collidepoint(event.pos):
                    dragging, dragging_part = True, part
                    break

        elif event.type == pygame.MOUSEBUTTONUP and dragging:
            if targets[dragging_part].colliderect(rects[dragging_part]):
                rects[dragging_part].topleft = targets[dragging_part].topleft
                placed_correctly[dragging_part] = True
            else:
                rects[dragging_part].topleft = initial_positions[dragging_part]
            dragging, dragging_part = False, None

        elif event.type == pygame.MOUSEMOTION and dragging:
            rects[dragging_part].move_ip(event.rel)

    window.fill(BACKGROUND)
    for target in targets.values():
        pygame.draw.rect(window, BLACK, target, 3)
    for part, img in images.items():
        window.blit(img, rects[part])

    if all(placed_correctly.values()):
        text = font.render("¡Wiiin!", True, GREEN)
        window.blit(text, (300, 250))
    pygame.display.update()
