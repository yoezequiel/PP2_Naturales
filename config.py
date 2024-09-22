import pygame

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("El Bosque en Peligro")

RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load("assets/img/forest.png")

trash_images = {
    "plastico": pygame.image.load("assets/img/plastico.png"),
    "vidrio": pygame.image.load("assets/img/vidrio.png"),
    "papel": pygame.image.load("assets/img/papel.png"),
    "organico": pygame.image.load("assets/img/organico.png"),
}
recycle_bins = {
    "plastico": pygame.image.load("assets/img/contenedor_plastico.png"),
    "vidrio": pygame.image.load("assets/img/contenedor_vidrio.png"),
    "papel": pygame.image.load("assets/img/contenedor_papel.png"),
    "organico": pygame.image.load("assets/img/contenedor_organico.png"),
}
