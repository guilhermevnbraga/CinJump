import pygame
from sprites import *
class Jogador:
    def __init__(self, personagem, x, y):
        self.x = x
        self.y = y
        self.altura = 50
        self.tamanho = 40
        self.vel_y = 0
        self.image= personagem
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.x, self.y, self.tamanho, self.altura)
        self.cor = (254, 254, 0)
        self.colidiu = False
        self.dy = 0  # Adiciona o atributo dy aqui

    def desenhar(self, TELA):
        TELA.blit(self.image, self.rect)
    def movimentar(self, LARGURA, ALTURA, PLATAFORMAS, ITENS):
        self.scrollar = 0
        self.dx = 0
        self.dy = 0  # Inicializa dy aqui
        pontuacao = 0
        self.GRAVIDADE = 1
        self.scrollar_tamanho = 200
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.dx -= 10
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.dx += 10

        if self.vel_y < 20:
            self.vel_y += self.GRAVIDADE
        self.dy += self.vel_y

        # Lógica de movimentação lateral
        if self.rect.x + self.dx >= LARGURA:
            self.rect.x = 0
        elif self.rect.x + self.dx < 0:
            self.rect.x = LARGURA - self.tamanho

        if self.rect.bottom + self.dy > ALTURA:
            self.dy = 0
            self.vel_y = -20

        for plataformas in PLATAFORMAS:
            if plataformas.rect.colliderect(
                self.rect.x, self.rect.y + self.dy, self.tamanho, self.altura
            ):
                if self.rect.bottom < plataformas.rect.centery:
                    if self.vel_y >= 0:
                        som_pulo.play()
                        self.rect.bottom = plataformas.rect.top
                        self.dy = 0
                        self.vel_y = -25                  

        for item in ITENS:
            if item.mola and item.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.tamanho, self.altura):
                if self.rect.bottom < item.rect.centery:
                    if self.vel_y >= 0:
                        som_mola.play()
                        self.rect.bottom = item.rect.top
                        self.dy = 0
                        self.vel_y = -40

        if self.rect.top <= self.scrollar_tamanho and self.vel_y < 0:
            self.scrollar = -self.dy 
            pontuacao = -self.scrollar

        self.rect.x += self.dx
        self.rect.y += self.dy + self.scrollar
    
        return self.scrollar, pontuacao
