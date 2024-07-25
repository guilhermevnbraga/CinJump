import pygame
from random import *

# O CODIGO DEVERÁ SOFRER ALTERAÇÕES APÓS DECIDIR OS SPRITES 

#CLASSE

class plataforma:
    
    def __init__(self, X, Y, LARGURA):
        self.X = X
        self.Y = Y
        self.LARGURA = LARGURA

    def desenhar(self,COR,TELA):
        pygame.draw.rect(TELA, COR, (self.X, self.Y, self.LARGURA, 30))


# FUNÇÕES

def gerar_plataformas(MAX_PLATAFORMAS):
    PLATAFORMAS = []
    for p in range (randint(1,MAX_PLATAFORMAS)):
        GERAR_PLATAFORMA = randint(0,3)
        if GERAR_PLATAFORMA == 0:
            PLATAFORMAS.append('verde')
        elif GERAR_PLATAFORMA == 1:
            PLATAFORMAS.append('vermelho')
        elif GERAR_PLATAFORMA == 2:
            PLATAFORMAS.append('verde')
        elif GERAR_PLATAFORMA == 3:
            PLATAFORMAS.append('azul')
    return PLATAFORMAS

def construir_mapa(LISTA_PLATAFORMAS,LARGURA,TELA):
    MULTIPLICADOR = 0
    for p in LISTA_PLATAFORMAS:
        P_L = randint(60,120)
        P_X = randint(0, LARGURA-30)
        P_Y = MULTIPLICADOR*randint(120,150)
        MULTIPLICADOR +=  1
        if p == 'vermelho':
            platform = plataforma(P_X,P_Y,P_L)
            platform.desenhar((255,0,0),TELA)
        elif p == 'verde':
            platform = plataforma(P_X,P_Y,P_L)
            platform.desenhar((0,255,0),TELA)
        elif p == 'azul':
            platform = plataforma(P_X,P_Y,P_L)  
            platform.desenhar((0,0,255),TELA)  

# AREA DE TESTES RETIRAR QUANDO O CÓDIGO FOR FINALIZADO
LARGURA = 580
ALTURA = 780

pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))

MAX_PLATAFORMAS = 10

plataformas = gerar_plataformas(MAX_PLATAFORMAS)
construir_mapa(plataformas, LARGURA, TELA)
rodar = True
while rodar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False


    pygame.display.update()
pygame.quit()