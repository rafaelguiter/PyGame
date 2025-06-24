import pygame
from config import *

def desenhar_fim_jogo(game):
    """Desenha a tela de fim de jogo com a pontuação do jogador"""
    
    # Fundo escuro semi-transparente
    superficie_escura = pygame.Surface((game.LARGURA, game.ALTURA))
    superficie_escura.set_alpha(128)
    superficie_escura.fill(PRETO)
    game.TELA.blit(superficie_escura, (0, 0))
    
    # Retângulo principal da tela de fim de jogo
    rect_principal = pygame.Rect(115, 150, 570, 350)
    pygame.draw.rect(game.TELA, BRANCO, rect_principal)
    pygame.draw.rect(game.TELA, PRETO, rect_principal, 3)
    
    # Título
    titulo = game.FONTE_GRANDE.render("FASE CONCLUÍDA!", True, PRETO)
    titulo_rect = titulo.get_rect(center=(game.LARGURA // 2, 200))
    game.TELA.blit(titulo, titulo_rect)
    
    # Informações da pontuação
    y_pos = 280
    
    # Pontuação total
    texto_pontuacao = game.FONTE.render(f"Pontuação Total: {game.pontuacao}", True, PRETO)
    texto_rect = texto_pontuacao.get_rect(center=(game.LARGURA // 2, y_pos))
    game.TELA.blit(texto_pontuacao, texto_rect)
    y_pos += 40
    
    # Acertos
    texto_acertos = game.FONTE.render(f"Acertos: {game.acertos}/{game.max_lixos}", True, VERDE)
    texto_rect = texto_acertos.get_rect(center=(game.LARGURA // 2, y_pos))
    game.TELA.blit(texto_acertos, texto_rect)
    y_pos += 40
    
    # Erros
    texto_erros = game.FONTE.render(f"Erros: {game.erros}", True, (255, 0, 0))
    texto_rect = texto_erros.get_rect(center=(game.LARGURA // 2, y_pos))
    game.TELA.blit(texto_erros, texto_rect)
    y_pos += 40
    
    # Acurácia
    acuracia = (game.acertos / game.max_lixos) * 100
    texto_acuracia = game.FONTE.render(f"Acurácia: {acuracia:.1f}%", True, PRETO)
    texto_rect = texto_acuracia.get_rect(center=(game.LARGURA // 2, y_pos))
    game.TELA.blit(texto_acuracia, texto_rect)
    y_pos += 60
    
    # Mensagem baseada no desempenho
    if acuracia >= 90:
        mensagem = "Parabéns! Você passou para a próxima fase!"
        cor_mensagem = VERDE
    else:
        mensagem = "Continue praticando! Tente novamente."
        cor_mensagem = (255, 165, 0)  # Laranja
    
    texto_mensagem = game.FONTE.render(mensagem, True, cor_mensagem)
    texto_rect = texto_mensagem.get_rect(center=(game.LARGURA // 2, y_pos))
    game.TELA.blit(texto_mensagem, texto_rect)
    y_pos += 60
    
    # Botão para continuar
    rect_continuar = pygame.Rect(300, y_pos, 200, 50)
    pygame.draw.rect(game.TELA, CINZA_ESCURO, rect_continuar)
    pygame.draw.rect(game.TELA, PRETO, rect_continuar, 2)
    
    texto_continuar = game.FONTE.render("Continuar", True, BRANCO)
    texto_rect = texto_continuar.get_rect(center=rect_continuar.center)
    game.TELA.blit(texto_continuar, texto_rect)
    
    # Armazenar o retângulo do botão para uso nos eventos
    game.rect_fim_jogo_continuar = rect_continuar 