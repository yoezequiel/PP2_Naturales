import pygame

pygame.init()
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú Principal")

BG = (177, 241, 97)
NEGRO = (0, 0, 0)

fuente = pygame.font.Font(None, 36)
