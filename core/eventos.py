import pygame
from entidades.lixo import gerar_lixo

def processar_eventos(game, eventos):
    for evento in eventos:
        if evento.type == pygame.QUIT:
            game.rodando = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if game.modo == "menu":
                if game.rect_start.collidepoint(evento.pos):
                    game.tocar_som("frente")
                    if not game.tutorial_visto:
                        game.modo = "tutorial"
                        game.tutorial_pagina = 0
                        game.tutorial_visto = True
                    else:
                        game.modo = "mapa"

                elif game.rect_opcoes.collidepoint(evento.pos):
                    game.tocar_som("frente")
                    game.modo = "opcoes"

            elif game.modo == "opcoes":
                if game.rect_som.collidepoint(evento.pos):
                    game.som_ativo = not game.som_ativo
                    game.atualizar_som()
                elif game.rect_voltar_menu.collidepoint(evento.pos):
                    game.tocar_som("voltar")
                    game.modo = "menu"

            elif game.modo == "tutorial":
                if evento.pos[0] < game.LARGURA // 2:
                    game.tutorial_pagina = max(0, game.tutorial_pagina - 1)
                    game.tocar_som("voltar")
                else:
                    game.tutorial_pagina += 1
                    game.tocar_som("frente")
                    if game.tutorial_pagina > 3:
                        game.modo = "mapa"

            elif game.modo == "mapa":
                for i, rect in enumerate(game.fase_rects):
                    if rect.collidepoint(evento.pos) and game.fases_desbloqueadas[i]:
                        game.tocar_som("ganhou")
                        game.fase_atual = i + 1
                        game.iniciar_fase(game.fase_atual)
                        game.modo = "jogo"
                if game.rect_voltar_menu.collidepoint(evento.pos):
                    game.tocar_som("voltar")
                    game.modo = "menu"

            elif game.modo == "jogo":
                if game.em_pausa:
                    if game.rect_pausado_continuar.collidepoint(evento.pos):
                        game.em_pausa = False
                elif game.menu_aberto:
                    if game.rect_menu_pause.collidepoint(evento.pos):
                        game.tocar_som("voltar")
                        game.em_pausa = True
                        game.menu_aberto = False
                    elif game.rect_menu_voltar.collidepoint(evento.pos):
                        game.tocar_som("voltar")
                        game.modo = "mapa"
                        game.menu_aberto = False
                elif game.rect_menu_jogo.collidepoint(evento.pos):
                    game.tocar_som("frente")
                    game.menu_aberto = True
                elif game.lixo_rect.collidepoint(evento.pos):
                    game.arrastando = True
                    game.offset_x = game.lixo_rect.x - evento.pos[0]
                    game.offset_y = game.lixo_rect.y - evento.pos[1]

        elif evento.type == pygame.MOUSEBUTTONUP:
            if game.modo == "jogo" and game.arrastando and not game.em_pausa:
                game.arrastando = False
                lixo_colocado = False
                for tipo, rect in game.lixeiras.items():
                    if rect.colliderect(game.lixo_rect):
                        lixo_colocado = True
                        if tipo == game.lixo_atual[1]:
                            game.pontuacao += 10
                            game.acertos += 1
                            game.brilho_lixeira = (rect.copy(), (0, 255, 0), 30)
                            game.tocar_som("acerto")
                        else:
                            game.pontuacao -= 5
                            game.erros += 1
                            game.brilho_lixeira = (rect.copy(), (255, 0, 0), 30)
                            game.tocar_som("erro")

                        game.lixos_restantes -= 1
                        if game.lixos_restantes > 0:
                            game.lixo_atual = gerar_lixo()
                            game.lixo_rect.x = 350
                            game.lixo_rect.y = 200
                        else:
                            acuracia = game.acertos / game.max_lixos
                            if acuracia >= 0.9 and game.fase_atual < game.total_fases:
                                game.fases_desbloqueadas[game.fase_atual] = True
                                game.tocar_som("ganhou")
                            else:
                                game.tocar_som("perdeu")
                            game.modo = "mapa"
                        break

                if not lixo_colocado:
                    game.lixo_rect.x = 350
                    game.lixo_rect.y = 200

        elif evento.type == pygame.MOUSEMOTION:
            if game.modo == "jogo" and game.arrastando and not game.em_pausa:
                game.lixo_rect.x = evento.pos[0] + game.offset_x
                game.lixo_rect.y = evento.pos[1] + game.offset_y