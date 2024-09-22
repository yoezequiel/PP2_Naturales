import pygame
import random
from config import *

pygame.init()

font = pygame.font.SysFont(None, 40)


class Trash(pygame.sprite.Sprite):
    def __init__(self, trash_type):
        super().__init__()
        self.trash_type = trash_type
        self.image = pygame.transform.scale(trash_images[trash_type], (50, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.y = random.randint(0, HEIGHT - 20)
        self.selected = False

    def update(self, pos):
        if self.selected:
            self.rect.center = pos


class RecycleBin(pygame.sprite.Sprite):
    def __init__(self, bin_type, x, y):
        super().__init__()
        self.bin_type = bin_type
        self.image = pygame.transform.scale(recycle_bins[bin_type], (60, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


all_sprites = pygame.sprite.Group()
trash_group = pygame.sprite.Group()

for i in range(5):
    trash_type = random.choice(list(trash_images.keys()))
    trash = Trash(trash_type)
    all_sprites.add(trash)
    trash_group.add(trash)

recycle_bins_group = pygame.sprite.Group()
bin_positions = [(10, 10), (740, 10), (10, 510), (740, 510)]
bin_types = list(recycle_bins.keys())

for i, bin_type in enumerate(bin_types):
    recycle_bin = RecycleBin(bin_type, bin_positions[i][0], bin_positions[i][1])
    all_sprites.add(recycle_bin)
    recycle_bins_group.add(recycle_bin)

selected_trash = None
error_message = None
message_timer = 0


def create_new_trash():
    trash_type = random.choice(list(trash_images.keys()))
    new_trash = Trash(trash_type)
    all_sprites.add(new_trash)
    trash_group.add(new_trash)


running = True
while running:
    clock.tick(FPS)

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected_trash is None:
                for trash in trash_group:
                    if trash.rect.collidepoint(mouse_pos):
                        trash.selected = True
                        selected_trash = trash
                        break
            else:
                for bin in recycle_bins_group:
                    if bin.rect.collidepoint(mouse_pos):
                        if selected_trash.trash_type == bin.bin_type:
                            print("¡Reciclaje exitoso!")
                            selected_trash.kill()
                            selected_trash = None
                        else:
                            error_message = "¡Contenedor incorrecto!"
                            message_timer = 60
                            create_new_trash()
                        break

    all_sprites.update(mouse_pos)

    screen.blit(background, (0, 0))

    for sprite in all_sprites:
        if sprite != selected_trash:
            screen.blit(sprite.image, sprite.rect)

    if selected_trash:
        screen.blit(selected_trash.image, selected_trash.rect)

    if error_message and message_timer > 0:
        error_text = font.render(error_message, True, RED)
        screen.blit(
            error_text, (WIDTH // 2 - error_text.get_width() // 2, HEIGHT // 2 - 20)
        )
        message_timer -= 1
    else:
        error_message = None

    pygame.display.flip()

pygame.quit()
