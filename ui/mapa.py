import pygame
from config import PRETO, BRANCO, CINZA, VERDE, CINZA_ESCURO

def desenhar_mapa(game):
    
    if game.img_fundo_mapa:
        game.TELA.blit(game.img_fundo_mapa, (0, 0))
    else:
        game.TELA.fill((210, 255, 210))
    
    game.TELA.blit(game.FONTE.render("", True, PRETO), (280, 50))

    for i, rect in enumerate(game.fase_rects):
        cor = VERDE if game.fases_desbloqueadas[i] else CINZA
        pygame.draw.rect(game.TELA, cor, rect)
        texto = game.FONTE.render(f"Fase {i+1}", True, BRANCO if game.fases_desbloqueadas[i] else PRETO)
        game.TELA.blit(texto, (rect.x + 10, rect.y + 30))

    pygame.draw.rect(game.TELA, CINZA_ESCURO, game.rect_voltar_menu)
    game.TELA.blit(game.FONTE.render("Voltar", True, BRANCO), (game.rect_voltar_menu.x + 10, game.rect_voltar_menu.y + 5))
