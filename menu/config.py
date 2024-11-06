import pygame

pygame.init()
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú Principal")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (200, 50, 50)
BG = (173, 216, 230)

fuente = pygame.font.Font(None, 36)
