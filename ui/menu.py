import pygame
from config import VERDE, CINZA_ESCURO, PRETO, BRANCO

def desenhar_menu(game):
    #adicionando imagem
    if game.img_fundo_menu:
        game.TELA.blit(game.img_fundo_menu, (0, 0))
    else:
        game.TELA.fill((230, 230, 255))
        
     # titulo do jogo    
    titulo = game.FONTE.render("Coleta Seletiva", True, PRETO) # nome
    game.TELA.blit(titulo, (280, 100)) # tamanho do nome

    # botao start
    pygame.draw.rect(game.TELA, VERDE, game.rect_start)
    game.TELA.blit(game.FONTE.render("Start", True, PRETO), (game.rect_start.x + 60, game.rect_start.y + 15)) # dimensoes e posição 
    
    # botao opcoes
    pygame.draw.rect(game.TELA, CINZA_ESCURO, game.rect_opcoes)
    game.TELA.blit(game.FONTE.render("Opções", True, PRETO), (game.rect_opcoes.x + 45, game.rect_opcoes.y + 15)) # dimensoes e posição 
   