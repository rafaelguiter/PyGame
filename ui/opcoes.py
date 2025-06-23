import pygame
from config import PRETO, CINZA_ESCURO, BRANCO

def desenhar_opcoes(game):
     # tela de fundo 
    if game.img_fundo_opcoes:
        game.TELA.blit(game.img_fundo_opcoes, (0, 0))
    else:
        game.TELA.fill((240, 240, 240))

    titulo = game.FONTE_GRANDE.render("Opções", True, PRETO)
    game.TELA.blit(titulo, (game.LARGURA // 2 - titulo.get_width() // 2, 100))

    # Botão de som
    cor_botao_som = (100, 200, 100) if game.som_ativo else (200, 100, 100)
    game.rect_som = pygame.Rect(game.LARGURA // 2 - 100, 250, 200, 60)
    pygame.draw.rect(game.TELA, cor_botao_som, game.rect_som)
    texto_som = "Som: ON" if game.som_ativo else "Som: OFF"
    game.TELA.blit(game.FONTE.render(texto_som, True, PRETO), (game.rect_som.x + 50, game.rect_som.y + 15))

    # Botão de voltar
    game.rect_voltar_menu = pygame.Rect(20, 20, 120, 40)
    pygame.draw.rect(game.TELA, CINZA_ESCURO, game.rect_voltar_menu)
    texto_voltar = game.FONTE.render("Voltar", True, BRANCO)
    game.TELA.blit(texto_voltar, (game.rect_voltar_menu.x + 10, game.rect_voltar_menu.y + 5))