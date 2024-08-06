import pygame
# Definindo as cores de plataforma
cores_plataforma = {
    "verde": (0, 255, 0),#plataforma normal
    "vermelho": (255, 0, 0),#platafrma que quebra
    "azul": (0, 0, 255),#plataforma que se move
    "branco": (255, 255, 255),#plataforma que tem o item mola
    "cinza": (128, 128, 128),#cor do item mola
    "dourado": (255, 215, 0),#cor da moeda
    "ciano": (0, 255, 255),#cor do diamante
    "roxo": (255, 0, 255),#cor da vida
    "cores totais": ["verde", "vermelho", "azul","verde", "vermelho", "azul","verde", "vermelho", "azul","azul","verde","verde","verde","azul","verde","azul","verde","verde","verde","verde","verde","branco"],
    #a chave cores_totais é a lista que usamos para selecionar a plataforma aleatoriamente já que usamos o choice para pegar uma nova cor para a plataforma e também mudaremos essa lista com o passar do código já que a dificuldade vai almentar gradualmente 
}
# IMAGENS
#imagens dos jogadores
stefan= pygame.image.load('./images/stefan.png')
anjolina = pygame.image.load('./images/anjolina.png')
ricardo = pygame.image.load('./images/ricardo.png')
sergio = pygame.image.load('./images/sergio.png')
#imagens que ficam na tela de seleção
stefan_selecionar = pygame.transform.scale(stefan, (110, 210))
anjolina_selecionar = pygame.transform.scale(anjolina, (110, 210))
ricardo_selecionar = pygame.transform.scale(ricardo, (110, 210))
sergio_selecionar = pygame.transform.scale(sergio, (110, 210))
#imagens que seão usadas no jogo
stefan_player = pygame.transform.scale(stefan, [40, 60])
anjolina_player = pygame.transform.scale(anjolina, [40, 60])
ricardo_player = pygame.transform.scale(ricardo, [40, 60])
sergio_player = pygame.transform.scale(sergio, [40, 60])
#imagem dos itens
imagem_moeda = pygame.image.load('./images/moeda.png')
imagem_diamante = pygame.image.load('./images/diamante.png')
imagem_vida = pygame.image.load('./images/coracao.png')
imagem_mola = pygame.image.load('./images/mola.png')
#imagens que serão usadas dentro do jogo
imagem_moeda = pygame.transform.scale(imagem_moeda, (21, 21))
imagem_diamante = pygame.transform.scale(imagem_diamante, (20, 20))
imagem_vida = pygame.transform.scale(imagem_vida, (20, 20))
imagem_mola = pygame.transform.scale(imagem_mola, (20, 20))
#imagens usado no contador de itens coletados
imagem_moeda_contador = pygame.transform.scale(imagem_moeda, (30, 30))
imagem_vida_contador = pygame.transform.scale(imagem_vida, (30, 30))
imagem_diamante_contador = pygame.transform.scale(imagem_diamante, (30, 30))
#imagem plataforma normal
imagem_plataforma_normal = pygame.image.load('./images/normal.png')
imagem_plataforma_quebra = pygame.image.load('./images/quebra.png')
#imagem da plataforma usada no jogo
imagem_plataforma_quebra = pygame.transform.scale(imagem_plataforma_quebra, (100, 20))
imagem_plataforma_normal = pygame.transform.scale(imagem_plataforma_normal, (100, 20))
#imagem botões
jogar = pygame.image.load("./images/botaojogar.png")
sair = pygame.image.load("./images/botaosair.png")
personagem_seletor = pygame.image.load("./images/personagem.png")
#imagens dos botões que serão usados no menu
jogar = pygame.transform.scale(jogar, (150, 70))
sair = pygame.transform.scale(sair, (150, 70))
personagem_seletor = pygame.transform.scale(personagem_seletor, (150, 70))


# EFEITOS SONOROS

pygame.mixer.init()
som_moeda= pygame.mixer.Sound('./sounds/coin.flac')
som_diamante= pygame.mixer.Sound('./sounds/diamante.ogg')
som_vida= pygame.mixer.Sound('./sounds/vida.flac')
som_mola= pygame.mixer.Sound('./sounds/mola.flac')
som_pulo= pygame.mixer.Sound('./sounds/pulo.wav')
plataforma_quebra = pygame.mixer.Sound('./sounds/plataforma_quebra.wav')
perdervida= pygame.mixer.Sound('./sounds/perdervida.mp3')