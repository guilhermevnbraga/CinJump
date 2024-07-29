import pygame
from pygame.locals import *
from random import *

# O CODIGO DEVERÁ SOFRER ALTERAÇÕES APÓS DECIDIR OS SPRITES 

cores_plataforma = {'verde': (0,255,0),
                    'vermelho': (255,0,0),
                    'azul': (0,0,255),
                    'cores totais': ['verde', 'vermelho', 'azul']}

#CLASSE 

class plataforma:
    
    def __init__(self, X, Y, L, cor):
        self.X = X
        self.Y = Y
        self.L = L
        self.velocidade = randint(1,4)
        self.cor = cor
        if cor == cores_plataforma['azul']: 
            self.velocida_condition = True 
        else:
            self.velocida_condition = False
        if cor == cores_plataforma['vermelho']:
            self.vermelho = True
        else:
            self.vermelho = False

    def desenhar(self,TELA):
        return pygame.draw.rect(TELA, self.cor, (self.X, self.Y, self.L, 20))
        
    def mover_azul(self, LARGURA):
        if self.velocida_condition:
            self.X += self.velocidade
            if self.X > LARGURA - self.L or self.X < 0:
                self.velocidade *= -1

    def sumir_vermelho(self, player, plataforma):
        if self.vermelho:
            if player.colliderect(plataforma):
                return True

    def get_cor(self):
        return self.cor



# FUNÇÕES

def gerar_plataformas(MAX_PLATAFORMAS):
    PLATAFORMAS = []
    for p in range (0,MAX_PLATAFORMAS):
        plataforma_aleatoria = choice(cores_plataforma['cores totais'])   
        PLATAFORMAS.append(plataforma_aleatoria)
    return PLATAFORMAS

def construir_mapa(LISTA_PLATAFORMAS, LARGURA,TELA):
    plataformas =[]
    plataformas_aux = []
    P_Y = ALTURA -30
    for i,p in enumerate(LISTA_PLATAFORMAS):
        P_L = 100
        P_X = randint(0, LARGURA-110)
        cor = cores_plataforma[p]
        if cor == (255,0,0):
            plataforma_vermelha = plataforma(P_X,P_Y,P_L, cor)
            vermelho = plataforma_vermelha.desenhar(TELA)
            plataformas.append(plataforma_vermelha)
            plataformas_aux.append(vermelho)
        elif cor == (0,255,0):
            plataforma_verde = plataforma(P_X,P_Y,P_L, cor)
            verde = plataforma_verde.desenhar(TELA)
            plataformas.append(plataforma_verde)
            plataformas_aux.append(verde)
        else:
            plataforma_azul = plataforma(P_X,P_Y,P_L, cor)
            azul = plataforma_azul.desenhar(TELA)
            plataformas.append(plataforma_azul)  
            plataformas_aux.append(azul)          
        P_Y -= 30 + randint(30, 150)
    return plataformas, plataformas_aux  
        

# AREA DE TESTES RETIRAR QUANDO O CÓDIGO FOR FINALIZADO

PLAYER = (254,254,0)
X_PLAYER = 300
Y_PLAYER = 750
VELOCIDADE_PLAYER = -20
BOTTOM_HEIGHT = 1
GRAVIDADE = 1
LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

MAX_PLATAFORMAS = 20

plataformas = gerar_plataformas(MAX_PLATAFORMAS)
plataformas, plataformas_aux = construir_mapa(plataformas, LARGURA, TELA)
rodar = True
while rodar:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False
    
    TELA.fill((0, 0, 0))    
    
    R_PLAYER = pygame.draw.rect(TELA, PLAYER, (X_PLAYER, Y_PLAYER, 20, 20))

    # Objeto de colisão com a parte inferior do player
    BOTTOM_RECT = pygame.Rect(R_PLAYER.left, R_PLAYER.bottom - BOTTOM_HEIGHT, R_PLAYER.width, BOTTOM_HEIGHT)

    # Velocidade do player
    Y_PLAYER += VELOCIDADE_PLAYER

    # Gravidade
    if VELOCIDADE_PLAYER < 10:
        VELOCIDADE_PLAYER += GRAVIDADE

    # Fazer o player ir pro outro lado da tela
    if (X_PLAYER >= LARGURA):
        X_PLAYER = 0
    elif (X_PLAYER <= 0):
        X_PLAYER = LARGURA - 20

    # Movimentação principal
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        X_PLAYER = X_PLAYER - 20
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        X_PLAYER = X_PLAYER + 20
    
    # Colisão com as plataformas
    if BOTTOM_RECT.collidelistall(plataformas_aux):
        VELOCIDADE_PLAYER = -20
    
    
    for plataforma, i in zip(plataformas, range(len(plataformas))):
        for platform, i_aux in zip(plataformas_aux, range(len(plataformas_aux))):
            if plataforma.get_cor() == cores_plataforma['vermelho'] and i == i_aux:
                if plataforma.sumir_vermelho(BOTTOM_RECT, platform):
                    print(plataforma.X, plataforma.Y)
                    print(R_PLAYER.x, R_PLAYER.y)
                    plataformas_aux.pop(i_aux)
                    plataformas.pop(i)
        plataforma.mover_azul(LARGURA) 
        plataforma.desenhar(TELA)  

    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
