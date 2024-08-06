import pygame
from random import *
from codigos.sprites import *

#aqui nós temos as classes usadas no jogo

#aqui temos a classe do botão que sera usado na interface do jogo
class Button():
	def __init__(self, image, x_pos, y_pos):
		self.image = image #imagem do botao
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, TELA): #blit poe uma imagem na tela
		TELA.blit(self.image, self.rect) #usa a posicao do rect para por a imagem na tela

	def clique(self, posicao): #confere se a posicao do mouse = posicao do botao
		if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom):
			return True
		else:
			return False	

#aqui temos a classe da plataforma que pode ser normal, que se move e que quebra
class Plataforma:
    #aqui temos a informações que cada plataforma tem
    def __init__(self, X, Y, L, cor):
        #aqui temos as medidas da plataforma, posição X e Y, largura e altura
        self.X = X
        self.Y = Y
        self.L = L
        self.rect = pygame.Rect(self.X, self.Y, self.L, 20)
        #aqui temos as velocidades das plataforma que se movem que podendo ser entre 6 velocidades que são escolhidas aleatoriamente 
        self.velocidade = randint(1,6)
        self.cor = cor#aqui tem a cor dessa plataforma 
        #aqui eu tenho onde vejo se a plataforma era do tipo normal, que quebra ou que se move 
        self.velocida_condition = True if cor == cores_plataforma["azul"] else False#caso que se move
        self.vermelho = True if cor == cores_plataforma["vermelho"] else False#caso que ela quebra
    
    #aqui como o sprite da plataforma que quebra é diferente das normais e que se movem eu faço essa diferenciação 
    def desenhar(self, TELA):
        if not self.vermelho:
            TELA.blit(imagem_plataforma_normal, self.rect)
        else:
            TELA.blit(imagem_plataforma_quebra, self.rect) 
    
    #aqui é a logica em que a plataforma que se move tem sua posição alterada ela ocorre caso a condição velocidade_condition seja verdadeira
    def mover_azul(self, LARGURA):
        if self.velocida_condition:
            self.X += self.velocidade
            self.rect.left = self.X
            if self.X > LARGURA - self.L or self.X < 0:
                self.velocidade *= -1
    
    #aqui é a logica que fala se a plataforma é ou não para ser deletada após encostar
    def sumir_vermelho(self, R_PLAYER):
        # A comparação correta do movimento vertical do jogador
        if self.vermelho:
            if R_PLAYER.rect.bottom == self.rect.top and R_PLAYER.vel_y < 0 and R_PLAYER.dy == 0:
                plataforma_quebra.play()
                return True
    
    #aqui pegamos a cor da plataforma
    def get_cor(self):
        return self.cor
    
    #aqui é onde ocorre a movimentação das plataformas na posição Y que representa a movimentação da tela dando a sensação de scroll da tela
    def scrollar_tela(self, scrollar):
        self.rect.y += scrollar
        
        if self.rect.y > 780:
            return True
        return False

#aqui nós temos a classe do item que é moeda, diamante, vida e mola
class Item:
    #aqui temos os dados de cada item
    def __init__(self, plataforma, cor, i, pontuacao):
        #aqui nós temos a posição do item que vai ficar em cima da plataforma por isso recebe os valores da plataforma
        self.X = plataforma.X + plataforma.L / 2 - 10
        self.Y = plataforma.Y - 20
        self.rect = pygame.Rect(self.X, self.Y, 20, 20)
        
        #aqui pegamos a cor da plataforma e cas0o seja branca quer dizer que a plataforma vai ter a mola além da seleçãpo do item que é decidido gerando um numero aleatorio entre 0 e 200 e para o item ser gerado ele deve ser maior que 100
        self.cor = cor
        self.mola = True if cor == cores_plataforma["branco"] else False
        item = randint(1, 200)
        self.moeda = (
            0
            if item <= 100 and i != 0
            else (
                1#item mais comum a moeda
                if 100 < item <= 170 and i != 0
                else 2#item incomum diamante
                if 170 < item <= 190 and i != 0 
                else 3#item raro vida
                if i != 0 and pontuacao < 15000 else 
                None#caso de ser a primeira plataforma ( ela não tera nenhum item)
            )
        )
    
    #aqui é onde desenhamos o item mudando seu sprite dependo do item e mudo seu sprite
    def desenho(self, TELA):
        if self.mola:
            self.cor = (128, 128, 128)
            TELA.blit(imagem_mola, self.rect)
        elif self.moeda == 1:
            self.cor = (255, 215, 0)
            TELA.blit(imagem_moeda, self.rect)
        elif self.moeda == 2:
            self.cor = (0, 255, 255)
            TELA.blit(imagem_diamante, self.rect)
        elif self.moeda == 3:
            self.cor = (255, 0, 255)
            TELA.blit(imagem_vida, self.rect)
    
    #aqui é onde vemos a colisão do personagem com o item
    def sumir_item(self, player, item):
        if player.rect.colliderect(item):
            return True
    
    #aqui vemos a cor do item
    def get_cor(self):
        return self.cor
    
    #aqui movimentamos o item na tela na posição Y
    def scrollar_item(self, scrollar):
        self.rect.y += scrollar

        if self.rect.y > 765:
            return True
        return False