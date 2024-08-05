import pygame
import sys
from sprites import *

pontuacao_recorde = 0
LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
pygame.display.set_caption('Cin Jump')
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
        mensagem = "Reprovado!"
        x = 200
    elif pontuacao <= 10000:
        mensagem = "Ficou na final..."
        x = 200
    elif pontuacao <= 20000:
        mensagem = "DOPE! Mas ainda dá para melhorar"
        x = 105
    elif pontuacao <= 30000:
        mensagem = "CRAZY! Continue pulando!"
        x = 140
    elif pontuacao <= 40000:
        mensagem = "BADASS! Tirou 10 em IP com essa pontuação"
        x = 25
    elif pontuacao <= 50000:
        mensagem = "APOCALYPTIC! Joga muito!"
        x = 140
    elif pontuacao <= 60000:
        mensagem = "SAVAGE! Você ultrapassou César!"
        x = 105
    elif pontuacao <= 70000:
        mensagem = "SICK SKILLS! VOA MULEKE!"
        x = 130
    elif pontuacao >= 70001 and pontuacao < 100000:
        mensagem = "SSSTYLISH! Já pode tirar o diploma!"
        x = 60
    elif pontuacao >= 100000:
        mensagem = "A quanto tempo você está aqui?"
        x = 105
    
    return mensagem, x