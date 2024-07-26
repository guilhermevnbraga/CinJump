import pygame
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
        if cor ==cores_plataforma['azul']: 
            self.velocida_condition =True 
        else:
            self.velocida_condition = False
        

    def desenhar(self,TELA):
        pygame.draw.rect(TELA, self.cor, (self.X, self.Y, self.L, 20))
        
    def mover_azul(self, LARGURA):
        if self.velocida_condition:
            self.X += self.velocidade
            if self.X > LARGURA - self.L or self.X < 0:
                self.velocidade *= -1


# FUNÇÕES

def gerar_plataformas(MAX_PLATAFORMAS):
    PLATAFORMAS = []
    for p in range (0,MAX_PLATAFORMAS):
        plataforma_aleatoria = choice(cores_plataforma['cores totais'])   
        PLATAFORMAS.append(plataforma_aleatoria)
    return PLATAFORMAS

def construir_mapa(LISTA_PLATAFORMAS,LARGURA,TELA):
    MULTIPLICADOR = 0
    plataformas =[]
    P_Y = ALTURA -30
    for i,p in enumerate(LISTA_PLATAFORMAS):
        P_L = 100
        P_X = randint(0, LARGURA-110)
        cor = cores_plataforma[p]
        platform = plataforma(P_X,P_Y,P_L, cor)
        plataformas.append(platform)
        platform.desenhar(TELA)
        print(plataformas)
        P_Y -= 30 + randint(30, 150)
    return plataformas    
        

# AREA DE TESTES RETIRAR QUANDO O CÓDIGO FOR FINALIZADO
LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

MAX_PLATAFORMAS = 20

plataformas = gerar_plataformas(MAX_PLATAFORMAS)
plataformas = construir_mapa(plataformas, LARGURA, TELA)
rodar = True
while rodar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False
    TELA.fill((0, 0, 0))    
    for plataforma in plataformas:
        plataforma.mover_azul(LARGURA) 
        plataforma.desenhar(TELA)  
    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()