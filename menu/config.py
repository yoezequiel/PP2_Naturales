import pygame

pygame.init()
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú Principal")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (200, 50, 50)
BG = (173, 216, 230)

COLOR_FONDO = (40, 40, 40)
COLOR_BORDES = (255, 255, 255)
COLOR_SELECCION = (0, 102, 204)
COLOR_TEXTO = (255, 255, 255)
COLOR_ERROR = (255, 0, 0)
COLOR_BOTON = (100, 100, 100)
COLOR_BOTON_SEL = (150, 150, 150)
COLOR_BOTON_TEXTO = (255, 255, 255)
