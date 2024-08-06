import pygame
from codigos.sprites import *
#aqui temos a clase do jogador
class Jogador:
    #o def initial é para dar ao jogador seu parametros como posição e tamanho além do sprite que ele ira receber
    
    def __init__(self, personagem, x, y, parametros):
        #posição do jogador na tela
        self.x = x
        self.y = y
        #medidas do jogador e sprite usado
        self.altura = 60
        self.tamanho = 40
        self.image= personagem
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.x, self.y, self.tamanho, self.altura)
        #variáveis usadas na movimentação do personagem
        self.vel_y = 0
        self.colidiu = False
        self.dy = 0  # Adiciona o atributo dy aqui
        #parametros que vem dependendo do personagem selecionado
        self.pulo = parametros[0]
        self.GRAVIDADE = parametros[1]
        self.movimento_lateral =parametros[2]

    #aqui é onde o player é desenhado

    def desenhar(self, TELA):
        TELA.blit(self.image, self.rect)

    #aqui é realmente a logica por trás do jogador onde vemos a movimentação que são os pulos junto com a movimentação lateral e a colisão com plataformas e itens

    def movimentar(self, LARGURA, ALTURA, PLATAFORMAS, ITENS):
        self.scrollar = 0 #aqui é onde temos a variavel responsavél por fazer a sensação do mapa estar se movimentando
        self.dx = 0
        self.dy = 0  # Inicializa dy aqui
        pontuacao = 0
        self.scrollar_tamanho = 200

        #aqui nós vemos se o jogador vai ir para a esquerda ou direita alterando o self.dx
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.dx -= self.movimento_lateral
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.dx += self.movimento_lateral
        #aqui nós temos a logica do pulo 
        if self.vel_y < 20:
            self.vel_y += self.GRAVIDADE
        self.dy += self.vel_y

        # Lógica de movimentação lateral para quando o player sai dos limites da tela
        if self.rect.x + self.dx >= LARGURA:
            self.rect.x = 0
        elif self.rect.x + self.dx < 0:
            self.rect.x = LARGURA - self.tamanho
        
        #aqui nós vemos se o player colidiu com a plataforma caso tenha colidido ele salta 
        for plataformas in PLATAFORMAS:
            if plataformas.rect.colliderect(
                self.rect.x, self.rect.y + self.dy, self.tamanho, self.altura
            ):
                if self.rect.bottom < plataformas.rect.centery:
                    if self.vel_y >= 0:
                        som_pulo.play()
                        self.rect.bottom = plataformas.rect.top
                        self.dy = 0
                        self.vel_y = self.pulo                 
        
        #aqui vemos a colisão com a mola que faz com que o player dê um salto mais alto
        for item in ITENS:
            if item.mola and item.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.tamanho, self.altura):
                if self.rect.bottom < item.rect.centery:
                    if self.vel_y >= 0:
                        som_mola.play()
                        self.rect.bottom = item.rect.top
                        self.dy = 0
                        self.vel_y = self.pulo*2
        
        #aqui é onde fazemos a movimentação da tela caso o player vá muito para cima dando a sensação de que o mapa esta relamente decendo e também se baseia nesse número para dar a pontuação que o jogador esta fazendo
        if self.rect.top <= self.scrollar_tamanho and self.vel_y < 0:
            self.scrollar = -self.dy 
            pontuacao = -self.scrollar
            pontuacao = int(pontuacao)
        
        #aqui atualizamos a posição do personagem no final de tudo
        self.rect.x += self.dx
        self.rect.y += self.dy + self.scrollar
    
        return self.scrollar, pontuacao #retornamos a pontuação que o player fez e o quanto o mapa se movimentou
