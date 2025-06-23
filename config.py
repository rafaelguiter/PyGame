import pygame

LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Coleta Seletiva")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (150, 150, 150)
VERDE = (0, 200, 0)
CINZA_ESCURO = (100, 100, 100)

pygame.font.init()
FONTE = pygame.font.SysFont(None, 40)
FONTE_GRANDE = pygame.font.SysFont(None, 80)

FPS = 60