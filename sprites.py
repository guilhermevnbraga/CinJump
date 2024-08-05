import pygame
import images 
# Definindo as cores de plataforma
cores_plataforma = {
    "verde": (0, 255, 0),
    "vermelho": (255, 0, 0),
    "azul": (0, 0, 255),
    "branco": (255, 255, 255),
    "cinza": (128, 128, 128),
    "dourado": (255, 215, 0),
    "ciano": (0, 255, 255),
    "roxo": (255, 0, 255),
    "cores totais": ["verde", "vermelho", "azul","verde", "vermelho", "azul","verde", "vermelho", "azul","azul","verde","verde","verde","azul","verde","azul","verde","verde","verde","verde","verde","branco"],
}
# IMAGENS
stefan= pygame.image.load('./images/stefan.png')
anjolina = pygame.image.load('./images/anjolina.png')
ricardo = pygame.image.load('./images/ricardo.png')
sergio = pygame.image.load('./images/sergio.png')
stefan_selecionar = pygame.transform.scale(stefan, (110, 210))
anjolina_selecionar = pygame.transform.scale(anjolina, (120, 220))
ricardo_selecionar = pygame.transform.scale(ricardo, (150, 250))
sergio_selecionar = pygame.transform.scale(sergio, (140, 240))
stefan_player = pygame.transform.scale(stefan, [40, 60])
anjolina_player = pygame.transform.scale(anjolina, [40,70])
ricardo_player = pygame.transform.scale(ricardo, [50,80])
sergio_player = pygame.transform.scale(sergio, [50,80])
imagem_moeda = pygame.image.load('./images/moeda.png')
imagem_diamante = pygame.image.load('./images/diamante.png')
imagem_vida = pygame.image.load('./images/coracao.png')
imagem_mola = pygame.image.load('./images/mola.png')
imagem_moeda = pygame.transform.scale(imagem_moeda, (20, 20))
imagem_diamante = pygame.transform.scale(imagem_diamante, (20, 20))
imagem_vida = pygame.transform.scale(imagem_vida, (20, 20))
imagem_mola = pygame.transform.scale(imagem_mola, (20, 20))
imagem_plataforma_normal = pygame.image.load('./images/normal.png')
imagem_plataforma_quebra = pygame.image.load('./images/quebra.png')
imagem_plataforma_quebra = pygame.transform.scale(imagem_plataforma_quebra, (100, 20))
imagem_plataforma_normal = pygame.transform.scale(imagem_plataforma_normal, (100, 20))
jogar = pygame.image.load("./images/botaojogar.png")
jogar = pygame.transform.scale(jogar, (150, 70))
sair = pygame.image.load("./images/botaosair.png")
sair = pygame.transform.scale(sair, (150, 70))
imagem_moeda_contador = pygame.transform.scale(imagem_moeda, (30, 30))
imagem_vida_contador = pygame.transform.scale(imagem_vida, (30, 30))
imagem_diamante_contador = pygame.transform.scale(imagem_diamante, (30, 30))
# EFEITOS SONOROS
pygame.mixer.init()
som_moeda= pygame.mixer.Sound('./sounds/coin.flac')
som_diamante= pygame.mixer.Sound('./sounds/diamante.ogg')
som_vida= pygame.mixer.Sound('./sounds/vida.flac')
som_mola= pygame.mixer.Sound('./sounds/mola.flac')
som_pulo= pygame.mixer.Sound('./sounds/pulo.wav')
plataforma_quebra = pygame.mixer.Sound('./sounds/plataforma_quebra.wav')
perdervida= pygame.mixer.Sound('./sounds/perdervida.mp3')