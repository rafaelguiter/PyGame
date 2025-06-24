import pygame
from config import *
from entidades.lixo import gerar_lixo
from fases.fase import calcular_max_lixos
from utils.funcoes import carregar_som
from utils.funcoes import carregar_imagem # adicinando os sprites
from utils.funcoes import carregar_imagens_lixeiras # adicinando os sprites de lixeiras
from utils.funcoes import carregar_imagem_escalada # adicinando os sprites dos lixos
from core.eventos import processar_eventos

from ui.menu import desenhar_menu
from ui.tutorial import desenhar_tutorial
from ui.mapa import desenhar_mapa
from ui.jogo import desenhar_jogo
from ui.opcoes import desenhar_opcoes
from ui.fim_jogo import desenhar_fim_jogo

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.som_ativo = True 

        self.LARGURA = LARGURA
        self.ALTURA = ALTURA
        self.TELA = TELA
        self.FONTE = FONTE
        self.FONTE_GRANDE = FONTE_GRANDE

        self.clock = pygame.time.Clock()
        self.rodando = True

        self.modo = "menu"
        self.fase_atual = None
        self.total_fases = 5
        self.fases_desbloqueadas = [True] + [False] * (self.total_fases - 1)

        self.tutorial_pagina = 0
        self.tutorial_visto = False

        self.rect_start = pygame.Rect(300, 200, 200, 60)
        self.rect_opcoes = pygame.Rect(300, 300, 200, 60)
        self.rect_voltar_menu = pygame.Rect(20, 20, 120, 40)
        self.rect_menu_jogo = pygame.Rect(20, 10, 120, 40)
        self.rect_menu_pause = pygame.Rect(300, 200, 200, 60)
        self.rect_menu_voltar = pygame.Rect(300, 300, 200, 60)
        self.rect_pausado_continuar = pygame.Rect(300, 320, 200, 60)
        self.fase_rects = [pygame.Rect(100 + i * 130, 250, 100, 100) for i in range(self.total_fases)]
        self.rect_som = pygame.Rect(300, 400, 200, 60)
        self.rect_fim_jogo_continuar = pygame.Rect(300, 400, 200, 50)
        
        # Fundos das telas
        
        #fundo menu
        self.img_fundo_menu = carregar_imagem("fundo_inicial.png")
        if self.img_fundo_menu:
            self.img_fundo_menu = pygame.transform.scale(self.img_fundo_menu, (self.LARGURA, self.ALTURA))
    
        #fundo jogo
        self.img_fundo_jogo = carregar_imagem("playground.png")
        if self.img_fundo_jogo:
            self.img_fundo_jogo = pygame.transform.scale(self.img_fundo_jogo, (self.LARGURA, self.ALTURA))
            
        #fundo mapa    
        self.img_fundo_mapa = carregar_imagem("fundo_fases.png")
        if self.img_fundo_mapa:
            self.img_fundo_mapa = pygame.transform.scale(self.img_fundo_mapa, (self.LARGURA, self.ALTURA))
            
        #fundo opcoes
        self.img_fundo_opcoes = carregar_imagem("fundo_opcoes.jpg")
        if self.img_fundo_opcoes:
            self.img_fundo_opcoes = pygame.transform.scale(self.img_fundo_opcoes, (self.LARGURA, self.ALTURA))
        
        
        
        #imagens tutorial
        self.img_tutorial = [
        carregar_imagem_escalada("tutorial/tutorial_1.png", (self.LARGURA, self.ALTURA)),
        carregar_imagem_escalada("tutorial/tutorial_2.png", (self.LARGURA, self.ALTURA)),
        carregar_imagem_escalada("tutorial/tutorial_3.png", (self.LARGURA, self.ALTURA)),
        carregar_imagem_escalada("tutorial/tutorial_4.png", (self.LARGURA, self.ALTURA)),
        ]
        

        
        # Imagens das lixeiras
        
        tipos = ["plastico", "papel", "organico", "vidro", "metal"]
        tamanho_lixeira = (130, 150)  # tamanho desejado para a sprite

        self.img_lixeiras = {
        tipo: carregar_imagens_lixeiras(f"lixeira_{tipo}", tamanho_lixeira)
            for tipo in tipos
        }
        
        
        self.lixeiras = {
            "plastico": pygame.Rect(50, 430, 130, 150),
            "papel": pygame.Rect(190, 430, 130, 150),
            "organico": pygame.Rect(330, 430, 130, 150),
            "vidro": pygame.Rect(470, 430, 130, 150),
            "metal": pygame.Rect(610, 430, 130, 150),
        }
        
        
        # Imagens dos tipos de lixo
        tamanho_lixo = (100, 100) # tamanho do lixo
        
        self.img_lixos = {
        "Garrafa PET": carregar_imagem_escalada("lixos/garrafa_pet.png", tamanho_lixo),
        "Folha de papel": carregar_imagem_escalada("lixos/papel.png", tamanho_lixo),
        "Cascas de frutas": carregar_imagem_escalada("lixos/casca.png", tamanho_lixo),
        "Pote de vidro": carregar_imagem_escalada("lixos/vidro.png", tamanho_lixo),
        "Lata de refrigerante": carregar_imagem_escalada("lixos/lata_refrigerante.png", tamanho_lixo),
        }
        

        self.pontuacao = 0
        self.acertos = 0
        self.erros = 0
        self.max_lixos = 0
        self.lixos_restantes = 0

        self.lixo_atual = None
        self.lixo_rect = pygame.Rect(350, 200, 100, 100)
        self.arrastando = False
        self.offset_x = 0
        self.offset_y = 0
        self.brilho_lixeira = None

        self.em_pausa = False
        self.menu_aberto = False

        self.cores_tutorial = [(0, 255, 0), (255, 255, 0), (0, 150, 255), (255, 165, 0)]
        
        self.sons = {    
            "acerto": carregar_som("assets/sons/acerto.mp3"),
            "erro": carregar_som("assets/sons/erro.mp3"),
            "frente": carregar_som("assets/sons/frente.wav"),
            "voltar": carregar_som("assets/sons/tras.wav"),
            "perdeu": carregar_som("assets/sons/awww.mp3"),
            "ganhou": carregar_som("assets/sons/ganhoufase.mp3")
        }
        
        
        self.musica_tutorial = "assets/sons/tutorial.mp3"
        self.musica_fundo_jogo = "assets/sons/musica_fundo.mp3"

        self.musica_atual = None
        
    def iniciar_fase(self, fase):
        self.pontuacao = 0
        self.acertos = 0
        self.erros = 0
        self.max_lixos = calcular_max_lixos(fase)
        self.lixos_restantes = self.max_lixos
        self.lixo_atual = gerar_lixo()
        self.lixo_rect.x = 350
        self.lixo_rect.y = 200
        self.em_pausa = False
        self.menu_aberto = False
        
    def tocar_som(self, nome):
        if self.som_ativo and nome in self.sons:
            self.sons[nome].play()
            
    
    def atualizar_som(self):
        if not self.som_ativo:
            pygame.mixer.music.stop()
            self.musica_atual = None
            return

        musica_desejada = None

        if self.modo == "jogo":
            musica_desejada = self.musica_fundo_jogo
        elif self.modo == "tutorial":
            musica_desejada = self.musica_tutorial
        elif self.modo == "mapa":
            musica_desejada = self.musica_tutorial    
        else:
            pygame.mixer.music.stop()
            self.musica_atual = None
            return

        if self.musica_atual != musica_desejada:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(musica_desejada)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
            self.musica_atual = musica_desejada
    

    def executar(self):
        while self.rodando:
            self.TELA.fill(BRANCO)
            eventos = pygame.event.get()
            processar_eventos(self, eventos)
            self.atualizar_som()
            self.renderizar()
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

    def renderizar(self):
        
        self.atualizar_som() # inicializando musica
        
        if self.modo == "menu":
            desenhar_menu(self)
        elif self.modo == "tutorial":
            desenhar_tutorial(self)
        elif self.modo == "mapa":
            desenhar_mapa(self)
        elif self.modo == "jogo":
            desenhar_jogo(self)
        elif self.modo == "opcoes":
            desenhar_opcoes(self)
        elif self.modo == "fim_jogo":
            desenhar_fim_jogo(self)