import pygame
import os


# importar sons
def carregar_som(caminho):
    return pygame.mixer.Sound(caminho)

# importar imagens
def carregar_imagem(nome_arquivo):
    caminho = os.path.join("assets", "imagens", nome_arquivo)
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        return imagem
    except Exception as e:
        print(f"Erro ao carregar imagem '{nome_arquivo}': {e}")
        return None
      
# carregando sprites de lixeira
def carregar_imagens_lixeiras(nome_base, tamanho=None):
    extensoes = [".png", ".jpg", ".jpeg"]
    for ext in extensoes:
        caminho = f"assets/imagens/lixeiras/{nome_base}{ext}"
        if os.path.isfile(caminho):
            print(f"[✓] Carregado: {caminho}")
            imagem = pygame.image.load(caminho).convert_alpha()
            if tamanho:
                imagem = pygame.transform.scale(imagem, tamanho)
            return imagem
    print(f"[x] Falhou: {nome_base}")
    return None

# codigo funcional ate aqui kkkkk

def carregar_imagem_escalada(nome_arquivo, tamanho):
    caminho = os.path.join("assets", "imagens", nome_arquivo)
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        return pygame.transform.scale(imagem, tamanho)
    except Exception as e:
        print(f"[x] Erro ao carregar imagem: {nome_arquivo} -> {e}")
        return None