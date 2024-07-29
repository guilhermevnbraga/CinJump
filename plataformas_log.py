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

############################################################################################
import pygame
from random import *

# O CODIGO DEVERÁ SOFRER ALTERAÇÕES APÓS DECIDIR OS SPRITES 

cores_plataforma = {'verde': (0,255,0),
                    'vermelho': (255,0,0),
                    'azul': (0,0,255),
                    'cores totais': ['verde', 'vermelho', 'azul']}
#CLASSE 

class plataforma:
    
    def __init__(self, X, Y, L):
        self.X = X
        self.Y = Y
        self.L = L

    def desenhar(self,COR,TELA):
        pygame.draw.rect(TELA, COR, (self.X, self.Y, self.L, 30))


# FUNÇÕES

def gerar_plataformas(MAX_PLATAFORMAS):
    PLATAFORMAS = []
    for p in range (0,MAX_PLATAFORMAS):
        plataforma_aleatoria = choice(cores_plataforma['cores totais'])   
        PLATAFORMAS.append(plataforma_aleatoria)
    return PLATAFORMAS

def construir_mapa(LISTA_PLATAFORMAS,LARGURA,TELA):
    MULTIPLICADOR = 0
    for i,p in enumerate(LISTA_PLATAFORMAS):
        P_L = 100
        P_X = randint(0, LARGURA-110)
        if i ==0:
            P_Y = 10
        else:    
            P_Y = 160 + MULTIPLICADOR
            MULTIPLICADOR +=  150
        cor = cores_plataforma[p]
        platform = plataforma(P_X,P_Y,P_L)
        platform.desenhar(cor,TELA)
        

# AREA DE TESTES RETIRAR QUANDO O CÓDIGO FOR FINALIZADO
LARGURA = 600
ALTURA = 800

pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))

MAX_PLATAFORMAS = int(ALTURA/100)

plataformas = gerar_plataformas(MAX_PLATAFORMAS)
construir_mapa(plataformas, LARGURA, TELA)
rodar = True
while rodar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False
        

    pygame.display.update()
pygame.quit()


####################################################################################
#plataforma azul se move
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
        plataforma.mover_azul(LARGURA)  # Atualiza a posição das plataformas
        plataforma.desenhar(TELA)  # Desenha as plataformas na nova posição
    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()


#############################################################################################################################
#plataforma vermelha sumir implementada

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

def construir_mapa(LISTA_PLATAFORMAS,LARGURA,TELA):
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
LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

MAX_PLATAFORMAS = 20

plataformas = gerar_plataformas(MAX_PLATAFORMAS)
plataformas,plataformas_aux = construir_mapa(plataformas, LARGURA, TELA)
rodar = True
while rodar:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False
    
    TELA.fill((0, 0, 0))    
    
    if pygame.key.get_pressed()[K_a]:
        X_PLAYER = X_PLAYER - 20
    if pygame.key.get_pressed()[K_d]:
        X_PLAYER = X_PLAYER + 20
    if pygame.key.get_pressed()[K_w]:
        Y_PLAYER = Y_PLAYER - 20
    if pygame.key.get_pressed()[K_s]:
        Y_PLAYER = Y_PLAYER + 20
    
    R_PLAYER = pygame.draw.rect(TELA, PLAYER, (X_PLAYER, Y_PLAYER, 20, 20))
    
    
    
    for plataforma,i in zip(plataformas,range(len(plataformas))):
        for platform,i_aux in zip(plataformas_aux,range(len(plataformas_aux))):
            if plataforma.get_cor() == cores_plataforma['vermelho'] and i == i_aux:
                if plataforma.sumir_vermelho(R_PLAYER, platform):
                    plataformas_aux.pop(i_aux)
                    plataformas.pop(i)
        plataforma.mover_azul(LARGURA) 
        plataforma.desenhar(TELA)  

    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

################################################################################
#codigo guilherme atualizado
import pygame
from pygame.locals import *
from random import *

# O CODIGO DEVERÁ SOFRER ALTERAÇÕES APÓS DECIDIR OS SPRITES 

cores_plataforma = {'verde': (0,255,0),
                    'vermelho': (255,0,0),
                    'azul': (0,0,255),
                    'branco': (255,255,255),
                    'cinza':(128,128,128),
                    'amarelo':(255,215,0),
                    'cores totais': ['verde', 'vermelho', 'azul', 'branco']}

#CLASSE 

class plataforma:
    
    def __init__(self, X, Y, L, cor, i):
        self.X = X
        self.Y = Y
        self.L = L
        self.velocidade = randint(1,4)
        self.cor = cor
        self.velocida_condition = True if cor == cores_plataforma['azul'] else False
        self.vermelho =True if cor == cores_plataforma['vermelho'] else False
        #parte do item
        self.mola = True if cor == cores_plataforma['branco'] else False
        item = randint(1, 100)
        self.moeda =True if item < 50 and i !=0 else False
        

    def desenhar(self,TELA):
        return pygame.draw.rect(TELA, self.cor, (self.X, self.Y, self.L, 20))
    #parte de colocar o item
    def item(self,TELA):
        if self.mola:
            return pygame.draw.rect(TELA, cores_plataforma['cinza'], (self.X + 42.5, self.Y - 15, 15, 15))
        elif self.moeda:
            return pygame.draw.rect(TELA, cores_plataforma['amarelo'], (self.X + 42.5, self.Y - 15, 15, 15))
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

def construir_mapa(LISTA_PLATAFORMAS,LARGURA,TELA):
    plataformas =[]
    plataformas_aux = []
    P_Y = ALTURA -30
    for i,p in enumerate(LISTA_PLATAFORMAS):
        P_L = 100
        P_X = randint(0, LARGURA-110)
        if i == 0:
            cor = cores_plataforma['verde']
        else:
            cor = cores_plataforma[p]
        plataform = plataforma(P_X,P_Y,P_L, cor,i)
        plataform_cor = plataform.desenhar(TELA)
        plataformas.append(plataform)
        plataformas_aux.append(plataform_cor)
        print(plataformas_aux)
        P_Y -= 30 + randint(30, 150)
    return plataformas, plataformas_aux  
        

# AREA DE TESTES RETIRAR QUANDO O CÓDIGO FOR FINALIZADO

LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

MAX_PLATAFORMAS = 20

plataformas = gerar_plataformas(MAX_PLATAFORMAS)
plataformas,plataformas_aux = construir_mapa(plataformas, LARGURA, TELA)

PLAYER = (254,254,0)
X_PLAYER = plataformas_aux[0][0] + 40
Y_PLAYER = plataformas_aux[0][1] - 20
rodar = True
while rodar:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False
        if pygame.key.get_pressed()[K_ESCAPE]:
            rodar = False    
    
    TELA.fill((0, 0, 0))    
    
    if pygame.key.get_pressed()[K_a]:
        X_PLAYER = X_PLAYER - 10
    if pygame.key.get_pressed()[K_d]:
        X_PLAYER = X_PLAYER + 10
    if pygame.key.get_pressed()[K_w]:
        Y_PLAYER = Y_PLAYER - 10
    if pygame.key.get_pressed()[K_s]:
        Y_PLAYER = Y_PLAYER + 10
    
    R_PLAYER = pygame.draw.rect(TELA, PLAYER, (X_PLAYER, Y_PLAYER, 20, 20))
    
    
    
    for plataforma,plataforma_aux,i in zip(plataformas,plataformas_aux,range(len(plataformas))):
        if plataforma.get_cor() == cores_plataforma['vermelho']:
            if plataforma.sumir_vermelho(R_PLAYER, plataforma_aux):
                plataformas_aux.pop(i)
                plataformas.pop(i)
        plataforma.mover_azul(LARGURA) 
        plataforma.desenhar(TELA)  
        plataforma.item(TELA)

    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
