import pygame
import sys

pygame.init()
pygame.joystick.init()  # Inicializa el sistema de joystick

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cuerpo Humano")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BACKGROUND = (51, 51, 51)

# Cargar imágenes
head = pygame.image.load("head.png")
body = pygame.image.load("body.png")
left_arm = pygame.image.load("left_arm.png")
right_arm = pygame.image.load("left_arm.png")
left_leg = pygame.image.load("leg.png")
right_leg = pygame.image.load("leg.png")

right_arm = pygame.transform.flip(left_arm, True, False)
left_leg = pygame.transform.flip(left_leg, True, False)

initial_positions = {
    "head": (50, 50),
    "body": (50, 150),
    "left_arm": (50, 250),
    "right_arm": (50, 350),
    "left_leg": (50, 450),
    "right_leg": (50, 550),
}

head_rect = head.get_rect(topleft=initial_positions["head"])
body_rect = body.get_rect(topleft=initial_positions["body"])
left_arm_rect = left_arm.get_rect(topleft=initial_positions["left_arm"])
right_arm_rect = right_arm.get_rect(topleft=initial_positions["right_arm"])
left_leg_rect = left_leg.get_rect(topleft=initial_positions["left_leg"])
right_leg_rect = right_leg.get_rect(topleft=initial_positions["right_leg"])

target_positions = {
    "head": (500, 85),
    "body": (500, 150),
    "left_arm": (467, 150),
    "right_arm": (565, 150),
    "left_leg": (500, 248),
    "right_leg": (533, 248),
}

head_target = pygame.Rect(target_positions["head"], head.get_size())
body_target = pygame.Rect(target_positions["body"], body.get_size())
left_arm_target = pygame.Rect(target_positions["left_arm"], left_arm.get_size())
right_arm_target = pygame.Rect(target_positions["right_arm"], right_arm.get_size())
left_leg_target = pygame.Rect(target_positions["left_leg"], left_leg.get_size())
right_leg_target = pygame.Rect(target_positions["right_leg"], right_leg.get_size())

targets = {
    "head": head_target,
    "body": body_target,
    "left_arm": left_arm_target,
    "right_arm": right_arm_target,
    "left_leg": left_leg_target,
    "right_leg": right_leg_target,
}

dragging = False
dragging_part = None

placed_correctly = {
    "head": False,
    "body": False,
    "left_arm": False,
    "right_arm": False,
    "left_leg": False,
    "right_leg": False,
}

font = pygame.font.Font(None, 74)
coord_font = pygame.font.Font(None, 36)

# Inicializar joystick
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Usando joystick: {joystick.get_name()}")
else:
    joystick = None
    print("No se detectó ningún joystick.")

joystick_speed = 5  # Velocidad de movimiento con el mando

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if head_rect.collidepoint(event.pos):
                dragging = True
                dragging_part = "head"
            elif body_rect.collidepoint(event.pos):
                dragging = True
                dragging_part = "body"
            elif left_arm_rect.collidepoint(event.pos):
                dragging = True
                dragging_part = "left_arm"
            elif right_arm_rect.collidepoint(event.pos):
                dragging = True
                dragging_part = "right_arm"
            elif left_leg_rect.collidepoint(event.pos):
                dragging = True
                dragging_part = "left_leg"
            elif right_leg_rect.collidepoint(event.pos):
                dragging = True
                dragging_part = "right_leg"

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                part_rect = eval(f"{dragging_part}_rect")
                if targets[dragging_part].colliderect(part_rect):
                    part_rect.topleft = targets[dragging_part].topleft
                    placed_correctly[dragging_part] = True
                else:
                    part_rect.topleft = initial_positions[dragging_part]
            dragging = False
            dragging_part = None

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                part_rect = eval(f"{dragging_part}_rect")
                part_rect.move_ip(event.rel)

    # Manejar el movimiento con el joystick
    if joystick:
        axis_x = joystick.get_axis(0)  # Eje X del stick izquierdo
        axis_y = joystick.get_axis(1)  # Eje Y del stick izquierdo

        if dragging:
            part_rect = eval(f"{dragging_part}_rect")
            part_rect.x += int(axis_x * joystick_speed)
            part_rect.y += int(axis_y * joystick_speed)

    window.fill(BACKGROUND)

    pygame.draw.rect(window, BLACK, head_target, 3)
    pygame.draw.rect(window, BLACK, body_target, 3)
    pygame.draw.rect(window, BLACK, left_arm_target, 3)
    pygame.draw.rect(window, BLACK, right_arm_target, 3)
    pygame.draw.rect(window, BLACK, left_leg_target, 3)
    pygame.draw.rect(window, BLACK, right_leg_target, 3)

    window.blit(head, head_rect)
    window.blit(body, body_rect)
    window.blit(left_arm, left_arm_rect)
    window.blit(right_arm, right_arm_rect)
    window.blit(left_leg, left_leg_rect)
    window.blit(right_leg, right_leg_rect)

    if all(placed_correctly.values()):
        text = font.render("¡Wiiin!", True, GREEN)
        window.blit(text, (300, 250))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    coord_text = coord_font.render(f"Coords: {mouse_x}, {mouse_y}", True, WHITE)
    coord_rect = coord_text.get_rect(bottomright=(width - 10, height - 10))
    window.blit(coord_text, coord_rect)

    pygame.display.update()
