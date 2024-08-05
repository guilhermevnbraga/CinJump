import pygame
from random import *
from sprites import *
class Plataforma:
    def __init__(self, X, Y, L, cor):
        self.X = X
        self.Y = Y
        self.L = L
        self.rect = pygame.Rect(self.X, self.Y, self.L, 20)
        self.velocidade = randint(1,6)
        self.cor = cor
        self.velocida_condition = True if cor == cores_plataforma["azul"] else False
        self.vermelho = True if cor == cores_plataforma["vermelho"] else False

    def desenhar(self, TELA):
        if not self.vermelho:
            TELA.blit(imagem_plataforma_normal, self.rect)
        else:
            TELA.blit(imagem_plataforma_quebra, self.rect) 
    def mover_azul(self, LARGURA):
        if self.velocida_condition:
            self.X += self.velocidade
            self.rect.left = self.X
            if self.X > LARGURA - self.L or self.X < 0:
                self.velocidade *= -1

    def sumir_vermelho(self, R_PLAYER):
        # A comparação correta do movimento vertical do jogador
        if self.vermelho:
            if R_PLAYER.rect.bottom == self.rect.top and R_PLAYER.vel_y < 0 and R_PLAYER.dy == 0:
                plataforma_quebra.play()
                return True

    def get_cor(self):
        return self.cor
    
    def scrollar_tela(self, scrollar):
        self.rect.y += scrollar
        
        if self.rect.y > 780:
            return True
        return False


class Item:
    def __init__(self, plataforma, cor, i, pontuacao):
        self.X = plataforma.X + plataforma.L / 2 - 10
        self.Y = plataforma.Y - 20
        self.rect = pygame.Rect(self.X, self.Y, 20, 20)
        self.cor = cor
        self.mola = True if cor == cores_plataforma["branco"] else False
        item = randint(1, 200)
        self.moeda = (
            0
            if item <= 100 and i != 0
            else (
                1
                if 100 < item <= 170 and i != 0
                else 2 if 170 < item <= 190 and i != 0 else 3 if i != 0 and pontuacao < 15000 else None
            )
        )

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

    def sumir_item(self, player, item):
        if player.rect.colliderect(item):
            return True

    def get_cor(self):
        return self.cor

    def scrollar_item(self, scrollar):
        self.rect.y += scrollar

        if self.rect.y > 765:
            return True
        return False