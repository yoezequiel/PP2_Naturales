import pygame
import random
from config import *

pygame.init()

font = pygame.font.SysFont(None, 40)

pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(name)

background_start = pygame.image.load(img_start)
sound_button = pygame.mixer.Sound(sound_button_dir)
check = pygame.mixer.Sound(check_sound)
win = pygame.mixer.Sound(win_sound)
pygame.mixer.music.load(background_sound_dir)
pygame.mixer.music.play(-1)

win_sound_played = False


def draw_button(button_hovered, button_clicked):
    if button_clicked:
        button_rect = pygame.Rect(
            (WIDTH // 2 - 224, HEIGHT // 3.2), (436 - 10, 101 - 10)
        )
    elif button_hovered:
        button_rect = pygame.Rect(
            (WIDTH // 2 - 224 - 5, HEIGHT // 3.2), (436 + 10, 101 + 10)
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


class Trash(pygame.sprite.Sprite):
    def __init__(self, trash_type):
        super().__init__()
        self.trash_type = trash_type
        self.image = pygame.transform.scale(trash_images[trash_type], (60, 70))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(0, HEIGHT - 30)
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

placed_correctly = {}

for i in range(trash_count):
    trash_type = random.choice(list(trash_images.keys()))
    trash = Trash(trash_type)
    all_sprites.add(trash)
    trash_group.add(trash)
    placed_correctly[trash] = False

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
    placed_correctly[new_trash] = False


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
                            selected_trash.kill()
                            placed_correctly[selected_trash] = True
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

    if all(placed_correctly.values()):
        pygame.mixer.music.stop()
        end = pygame.image.load(img_end)
        window.blit(end, (0, 0))
        if not win_sound_played:
            win.set_volume(0.1)
            win.play()
            win_sound_played = True
        pygame.display.update()

    pygame.display.flip()

pygame.quit()
