import pygame
from config import PRETO, BRANCO, CINZA, CINZA_ESCURO

def desenhar_jogo(game):
    # tela de fundo 
    if game.img_fundo_jogo:
        game.TELA.blit(game.img_fundo_jogo, (0, 0))
    else:
        game.TELA.fill(BRANCO)
    
    
    
    #lixeiras
    
    for tipo, rect in game.lixeiras.items():
        img = game.img_lixeiras.get(tipo)
        if img:
            game.TELA.blit(img, (rect.x, rect.y))
        else:
            # fallback visual se imagem não carregar
            pygame.draw.rect(game.TELA, CINZA, rect)

    
    # brilho das lixeiras
    
    if game.brilho_lixeira:
        rect, cor, tempo = game.brilho_lixeira
        brilho_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        brilho_surface.fill((*cor, 100))
        game.TELA.blit(brilho_surface, (rect.x, rect.y))
        game.brilho_lixeira = (rect, cor, tempo - 1)
        if game.brilho_lixeira[2] <= 0:
            game.brilho_lixeira = None


    # lixo atual
    
    img_lixo = game.img_lixos.get(game.lixo_atual[0])
    if img_lixo:
        game.TELA.blit(img_lixo, (game.lixo_rect.x, game.lixo_rect.y))
    else:
        pygame.draw.rect(game.TELA, (200, 200, 255), game.lixo_rect)
        texto_lixo = game.FONTE.render(game.lixo_atual[0], True, PRETO)
        game.TELA.blit(texto_lixo, (game.lixo_rect.x + 10, game.lixo_rect.y + 10))


    # HUD
    
    texto_ponto = game.FONTE.render(f"Pontuação: {game.pontuacao}", True, PRETO)
    game.TELA.blit(texto_ponto, (500, 60))

    texto_fase = game.FONTE.render(f"Fase {game.fase_atual} - {game.lixos_restantes} restantes", True, PRETO)
    game.TELA.blit(texto_fase, (20, 60))


    # botao menu
    
    pygame.draw.rect(game.TELA, CINZA_ESCURO, game.rect_menu_jogo)
    game.TELA.blit(game.FONTE.render("Menu", True, BRANCO), (game.rect_menu_jogo.x + 25, game.rect_menu_jogo.y + 5))


    # pausado
    
    if game.em_pausa:
        titulo_pausa = game.FONTE_GRANDE.render("PAUSADO", True, PRETO)
        game.TELA.blit(titulo_pausa, (260, 190))
        pygame.draw.rect(game.TELA, CINZA_ESCURO, game.rect_pausado_continuar)
        game.TELA.blit(game.FONTE.render("Continuar", True, BRANCO), (game.rect_pausado_continuar.x + 30, game.rect_pausado_continuar.y + 15))

    # menu aberto
    elif game.menu_aberto:
        pygame.draw.rect(game.TELA, CINZA_ESCURO, game.rect_menu_pause)
        game.TELA.blit(game.FONTE.render("Pausar", True, BRANCO), (game.rect_menu_pause.x + 50, game.rect_menu_pause.y + 15))
        pygame.draw.rect(game.TELA, CINZA_ESCURO, game.rect_menu_voltar)
        game.TELA.blit(game.FONTE.render("Voltar Mapa", True, BRANCO), (game.rect_menu_voltar.x + 20, game.rect_menu_voltar.y + 15))
