import pygame
import sys
from sprites import *

pontuacao_recorde = 0
LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
fonte = pygame.font.SysFont("Comic Sans MS", 20, True, True)
TELA = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()
class Button():
	def __init__(self, image, x_pos, y_pos):
		self.image = image #imagem do botao
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self): #blit poe uma imagem na tela
		TELA.blit(self.image, self.rect) #usa a posicao do rect para por a image na tela

	def clique(self, posicao): #confere se a posicao do mouse = posicao do botao
		if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom):
			return True
		else:
			return False	
 
def mensagem_gameover(pontuacao):
    if pontuacao <= 5000:
        mensagem = "Poderia ter sido melhor"
        x = 151
    elif pontuacao <= 10000:
        mensagem = "Não foi tão ruim, mas você pode melhorar!"
        x = 34
    elif pontuacao <= 20000:
        mensagem = "Bom trabalho! Continue assim!"
        x = 105
    elif pontuacao <= 30000:
        mensagem = "Excelente! Você está ficando bom nisso!"
        x = 56
    elif pontuacao <= 40000:
        mensagem = "Impressionante! Você está quase no topo!"
        x = 41
    elif pontuacao <= 50000:
        mensagem = "Fantástico! Quase um mestre do jogo!"
        x = 66
    elif pontuacao <= 60000:
        mensagem = "Incrível! Você é um jogador de elite!"
        x = 72
    elif pontuacao <= 70000:
        mensagem = "Fenomenal! Poucos chegam tão longe!"
        x = 60
    elif pontuacao <= 80000:
        mensagem = "Surpreendente! Você está entre os melhores!"
        x = 32
    elif pontuacao <= 90000:
        mensagem = "Magnífico! Sua habilidade é invejável!"
        x = 37
    elif pontuacao < 100000:
        mensagem = "Lendário! Você está no topo do mundo!"
        x = 47
    else:  # pontuacao >= 100000
        mensagem = "Divino! Você é uma lenda viva!"
        x = 113
    
    return mensagem, x