import pygame
from pygame.locals import *
from random import *

# Definindo as cores de plataforma
cores_plataforma = {
    "verde": (0, 255, 0),
    "vermelho": (255, 0, 0),
    "azul": (0, 0, 255),
    "branco": (255, 255, 255),
    "cinza": (128, 128, 128),
    "dourado": (255, 215, 0),
    "ciano": (0, 255, 255),
    "roxo": (255, 0, 255),
    "cores totais": ["verde", "vermelho", "azul","verde", "vermelho", "azul","verde", "vermelho", "azul","verde","verde","verde","verde", "branco"],
}

# Classe Jogador
class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.altura = 20
        self.tamanho = 20
        self.vel_y = 0
        self.rect = pygame.Rect(self.x, self.y, self.tamanho, self.altura)
        self.cor = (254, 254, 0)
        self.colidiu = False
        self.dy = 0  # Adiciona o atributo dy aqui

    def desenhar(self, TELA):
        pygame.draw.rect(TELA, self.cor, self.rect)

    def movimentar(self, LARGURA, ALTURA, PLATAFORMAS, ITENS):
        self.scrollar = 0
        self.dx = 0
        self.dy = 0  # Inicializa dy aqui
        pontuacao = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.dx -= 20
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.dx += 20
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.dy -= 20

        if self.vel_y < 20:
            self.vel_y += GRAVIDADE
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
                        self.rect.bottom = plataformas.rect.top
                        self.dy = 0
                        self.vel_y = -25                  

        for item in ITENS:
            if item.mola and item.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.tamanho, self.altura):
                if self.rect.bottom < item.rect.centery:
                    if self.vel_y >= 0:
                        self.rect.bottom = item.rect.top
                        self.dy = 0
                        self.vel_y = -40

        if self.rect.top <= scrollar_tamanho and self.vel_y < 0:
            self.scrollar = -self.dy 
            pontuacao = -self.scrollar

        self.rect.x += self.dx
        self.rect.y += self.dy + self.scrollar
    
        return self.scrollar, pontuacao

class Plataforma:
    def __init__(self, X, Y, L, cor):
        self.X = X
        self.Y = Y
        self.L = L
        self.rect = pygame.Rect(self.X, self.Y, self.L, 20)
        self.velocidade = 2
        self.cor = cor
        self.velocida_condition = True if cor == cores_plataforma["azul"] else False
        self.vermelho = True if cor == cores_plataforma["vermelho"] else False

    def desenhar(self, TELA):
        pygame.draw.rect(TELA, self.cor, self.rect)

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
                return True

    def get_cor(self):
        return self.cor
    
    def scrollar_tela(self, scrollar):
        self.rect.y += scrollar
        
        if self.rect.y > ALTURA:
            return True
        return False


class Item:
    def __init__(self, plataforma, cor, i):
        self.X = plataforma.X + plataforma.L / 2 - 7.5
        self.Y = plataforma.Y - 15
        self.rect = pygame.Rect(self.X, self.Y, 15, 15)
        self.cor = cor
        self.mola = True if cor == cores_plataforma["branco"] else False
        item = randint(1, 200)
        self.moeda = (
            0
            if item <= 100 and i != 0
            else (
                1
                if 100 < item <= 170 and i != 0
                else 2 if 170 < item <= 190 and i != 0 else 3 if i != 0 else None
            )
        )

    def desenho(self, TELA):
        if self.mola:
            self.cor = (128, 128, 128)
            pygame.draw.rect(TELA, cores_plataforma["cinza"], self.rect)
        elif self.moeda == 1:
            self.cor = (255, 215, 0)
            pygame.draw.rect(TELA, cores_plataforma["dourado"], self.rect)
        elif self.moeda == 2:
            self.cor = (0, 255, 255)
            pygame.draw.rect(TELA, cores_plataforma["ciano"], self.rect)
        elif self.moeda == 3:
            self.cor = (255, 0, 255)
            pygame.draw.rect(TELA, cores_plataforma["roxo"], self.rect)

    def sumir_item(self, player, item):
        if player.rect.colliderect(item):
            return True

    def get_cor(self):
        return self.cor

    def scrollar_item(self, scrollar):
        self.rect.y += scrollar

        if self.rect.y > ALTURA:
            return True
        return False

# Funções

def gerar_plataformas(MAX_PLATAFORMAS):
    PLATAFORMAS = []
    for p in range(0, MAX_PLATAFORMAS):
        plataforma_aleatoria = choice(cores_plataforma["cores totais"])
        PLATAFORMAS.append(plataforma_aleatoria)
    return PLATAFORMAS

def construir_mapa(LISTA_PLATAFORMAS, LARGURA, ALTURA):
    dados = {
        "plataforma": [],
        "itens": [],
    }
    P_Y = ALTURA - 60
    for i, p in enumerate(LISTA_PLATAFORMAS):
        P_L = 100
        P_X = randint(0, LARGURA - 110)
        cor = cores_plataforma["verde"] if i == 0 else cores_plataforma[p]
        plataform = Plataforma(P_X, P_Y, P_L, cor)
        dados["plataforma"].append(plataform)
        if cor != cores_plataforma["azul"]:
            ite = Item(plataform, cor, i)
            dados["itens"].append(ite)
        P_Y -= 30 + randint(30, 150)
    return dados

def update_mapa(plataformas, itens, R_PLAYER):
    for plataforma, i in zip(plataformas, range(len(plataformas))):
        if plataforma.get_cor() == cores_plataforma[
            "vermelho"
        ] and plataforma.sumir_vermelho(R_PLAYER):
            plataformas.pop(i)

    for item, i in zip(itens, range(len(itens))):
        if item.get_cor() != cores_plataforma["cinza"] and item is not None:
            if item.sumir_item(R_PLAYER, item):
                itens.pop(i)
                return (
                    "moeda"
                    if item.get_cor() == cores_plataforma["dourado"]
                    else (
                        "diamante"
                        if item.get_cor() == cores_plataforma["ciano"]
                        else (
                            "vida"
                            if item.get_cor() == cores_plataforma["roxo"]
                            else False
                        )
                    )
                )
    return False

def render_mapa(plataformas, items, LARGURA, TELA, scrollar):
    # Itera de trás para frente para evitar problemas ao remover itens
    for i in range(len(plataformas) - 1, -1, -1):
        plataforma = plataformas[i]

        # Verifica se o índice atual existe em ambas as listas
        if i < len(items):
            item = items[i]
            deletar_item = item.scrollar_item(scrollar)
            if deletar_item:
                items.pop(i)
            else:
                item.desenho(TELA)

        # Movimenta e desenha a plataforma
        plataforma.mover_azul(LARGURA)
        deletar_plataforma = plataforma.scrollar_tela(scrollar)
        if deletar_plataforma:
            plataformas.pop(i)
        else:
            plataforma.desenhar(TELA)

# Area de testes
moedas = 0
vidas = 1
diamantes = 0
pontuacao = 0
scrollar_tamanho = 200
scrollar = 0

LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
fonte = pygame.font.SysFont("arial", 20, True, True)
TELA = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

MAX_PLATAFORMAS = 10

plataformas = gerar_plataformas(MAX_PLATAFORMAS)
dados = construir_mapa(plataformas, LARGURA, ALTURA)

X_PLAYER = dados["plataforma"][0].rect.left + 40
Y_PLAYER = dados["plataforma"][0].rect.top - 20
VELOCIDADE_PLAYER = -20
GRAVIDADE = 1
rodar = True
player = Jogador(X_PLAYER, Y_PLAYER)

while rodar:
    mensagem = f"Moedas: {moedas}"
    mensagem2 = f"Vidas: {vidas}"
    mensagem3 = f"Diamantes: {diamantes}"
    mensagem4 = f"Pontuação TOTAL!!: {pontuacao}"
    mensagem_format = fonte.render(mensagem, True, (255, 255, 255))
    mensagem2_format = fonte.render(mensagem2, True, (255, 255, 255))
    mensagem3_format = fonte.render(mensagem3, True, (255, 255, 255))
    mensagem4_format = fonte.render(mensagem4, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False
        if pygame.key.get_pressed()[K_ESCAPE]:
            rodar = False
    
    TELA.fill((0, 0, 0))
    player.desenhar(TELA)
    scrollar, pontuacao_somar = player.movimentar(LARGURA, ALTURA, dados["plataforma"], dados["itens"])
    pontuacao += pontuacao_somar
    
    if player.rect.top >= 750:
        if vidas == 1:
            vidas -= 1
            player.vel_y = -50
        else:
            rodar = False

    pygame.draw.line(TELA, (255,255,255), (0, scrollar_tamanho), (LARGURA, scrollar_tamanho), 1)
    coletou = update_mapa(dados["plataforma"], dados["itens"], player)
    if coletou == "moeda":
        moedas += 1
        pontuacao += 5
    elif coletou == "diamante":
        diamantes += 1
        pontuacao += 25
    elif coletou == "vida" and vidas < 3:
        vidas += 1

    render_mapa(dados["plataforma"], dados["itens"], LARGURA, TELA, scrollar)
    
    TELA.blit(mensagem_format, (10, 10))
    TELA.blit(mensagem2_format, (10, 30))
    TELA.blit(mensagem3_format, (10, 50))
    TELA.blit(mensagem4_format, (10, 70))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
