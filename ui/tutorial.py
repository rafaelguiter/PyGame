import pygame
from config import PRETO

"""
def desenhar_tutorial(game):
    cor = game.cores_tutorial[game.tutorial_pagina]
    game.TELA.fill(cor)
    texto = game.FONTE.render(f"Tutorial {game.tutorial_pagina + 1}/4", True, PRETO)
    game.TELA.blit(texto, (game.LARGURA // 2 - 80, game.ALTURA // 2 - 20))
    
    
    """
    
def desenhar_tutorial(game):
    if 0 <= game.tutorial_pagina < len(game.img_tutorial):
        imagem = game.img_tutorial[game.tutorial_pagina]
        if imagem:
            game.TELA.blit(imagem, (0, 0))
        else:
            game.TELA.fill((255, 255, 255))
    else:
        game.TELA.fill((255, 255, 255))

    texto = game.FONTE.render(f"Tutorial {game.tutorial_pagina + 1}/4", True, (0, 0, 0))
    game.TELA.blit(texto, (game.LARGURA // 2 - 80, 20))