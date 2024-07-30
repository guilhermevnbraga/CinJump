import pygame
from pygame.locals import *
from random import *

# O CODIGO DEVERÁ SOFRER ALTERAÇÕES APÓS DECIDIR OS SPRITES

cores_plataforma = {
    "verde": (0, 255, 0),
    "vermelho": (255, 0, 0),
    "azul": (0, 0, 255),
    "branco": (255, 255, 255),
    "cinza": (128, 128, 128),
    "dourado": (255, 215, 0),
    "ciano": (0, 255, 255),
    "roxo": (255, 0, 255),
    "cores totais": ["verde", "vermelho", "azul", "branco"],
}

# CLASSE


class plataforma:

    def __init__(self, X, Y, L, cor, i):
        self.X = X
        self.Y = Y
        self.L = L
        self.velocidade = 2
        self.cor = cor
        self.velocida_condition = True if cor == cores_plataforma["azul"] else False
        self.vermelho = True if cor == cores_plataforma["vermelho"] else False

    def desenhar(self, TELA):
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


class item:
    def __init__(self, X, Y, cor, i):
        self.X = X
        self.Y = Y
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
            return pygame.draw.rect(
                TELA, cores_plataforma["cinza"], (self.X + 42.5, self.Y - 15, 15, 15)
            )
        elif self.moeda == 1:
            self.cor = (255, 215, 0)
            return pygame.draw.rect(
                TELA, cores_plataforma["dourado"], (self.X + 42.5, self.Y - 15, 15, 15)
            )
        elif self.moeda == 2:
            self.cor = (0, 255, 255)
            return pygame.draw.rect(
                TELA, cores_plataforma["ciano"], (self.X + 42.5, self.Y - 15, 15, 15)
            )
        elif self.moeda == 3:
            self.cor = (255, 0, 255)
            return pygame.draw.rect(
                TELA, cores_plataforma["roxo"], (self.X + 42.5, self.Y - 15, 15, 15)
            )

    def sumir_item(self, player, item):
        if player.colliderect(item):
            return True

    def get_cor(self):
        return self.cor


# FUNÇÕES


def gerar_plataformas(MAX_PLATAFORMAS):
    PLATAFORMAS = []
    for p in range(0, MAX_PLATAFORMAS):
        plataforma_aleatoria = choice(cores_plataforma["cores totais"])
        PLATAFORMAS.append(plataforma_aleatoria)
    return PLATAFORMAS


def construir_mapa(LISTA_PLATAFORMAS, LARGURA, TELA, ALTURA):
    dados = {
        "plataforma": [],
        "plataforma posicao": [],
        "itens": [],
        "itens posicao": [],
    }
    P_Y = ALTURA - 30
    for i, p in enumerate(LISTA_PLATAFORMAS):
        P_L = 100
        P_X = randint(0, LARGURA - 110)
        cor = cores_plataforma["verde"] if i == 0 else cores_plataforma[p]
        plataform = plataforma(P_X, P_Y, P_L, cor, i)
        plataform_cor = plataform.desenhar(TELA)
        dados["plataforma"].append(plataform)
        dados["plataforma posicao"].append(plataform_cor)
        if cor != cores_plataforma["azul"]:
            ite = item(P_X, P_Y, cor, i)
            ite_aux = ite.desenho(TELA)
            dados["itens"].append(ite)
            dados["itens posicao"].append(ite_aux)
        P_Y -= 30 + randint(30, 150)
    return dados


def update_mapa(plataformas, plataformas_aux, itens, itens_aux, R_PLAYER):
    for plataforma, plataforma_aux, i in zip(
        plataformas, plataformas_aux, range(len(plataformas_aux))
    ):
        if plataforma.get_cor() == cores_plataforma[
            "vermelho"
        ] and plataforma.sumir_vermelho(R_PLAYER, plataforma_aux):
            plataformas_aux.pop(i)
            plataformas.pop(i)

    for item, item_aux, i in zip(itens, itens_aux, range(len(itens_aux))):
        if item.get_cor() != cores_plataforma["cinza"] and item_aux is not None:
            if item.sumir_item(R_PLAYER, item_aux):
                itens_aux.pop(i)
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


def render_mapa(plataformas, items, LARGURA, TELA):
    plataformas_aux = []

    for plataforma, itens in zip(plataformas, items):
        plataforma.mover_azul(LARGURA)
        plataformas_aux.append(plataforma.desenhar(TELA))
        itens.desenho(TELA)

    return plataformas_aux


# AREA DE TESTES RETIRAR QUANDO O CÓDIGO FOR FINALIZADO

moedas = 0
vidas = 0
diamantes = 0
pontuacao = 0

LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
fonte = pygame.font.SysFont("arial", 20, True, True)
TELA = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

MAX_PLATAFORMAS = 20

plataformas = gerar_plataformas(MAX_PLATAFORMAS)
dados = construir_mapa(plataformas, LARGURA, TELA, ALTURA)

PLAYER = (254, 254, 0)
X_PLAYER = dados["plataforma posicao"][0][0] + 40
Y_PLAYER = dados["plataforma posicao"][0][1] - 20
VELOCIDADE_PLAYER = -20
BOTTOM_HEIGHT = 1
GRAVIDADE = 2
rodar = True
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

    R_PLAYER = pygame.draw.rect(TELA, PLAYER, (X_PLAYER, Y_PLAYER, 20, 20))

    # Objeto de colisão com a parte inferior do player
    BOTTOM_RECT = pygame.Rect(
        R_PLAYER.left,
        R_PLAYER.bottom - BOTTOM_HEIGHT + 20,
        R_PLAYER.width,
        BOTTOM_HEIGHT,
    )

    # Velocidade do player
    Y_PLAYER += VELOCIDADE_PLAYER

    # Gravidade
    if VELOCIDADE_PLAYER < 20:
        VELOCIDADE_PLAYER += GRAVIDADE

    # Fazer o player ir pro outro lado da tela
    if X_PLAYER >= LARGURA:
        X_PLAYER = 0
    elif X_PLAYER <= 0:
        X_PLAYER = LARGURA - 20

    if Y_PLAYER >= ALTURA - 20:
        Y_PLAYER = ALTURA - 20

    # Movimentação principal
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        X_PLAYER = X_PLAYER - 20
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        X_PLAYER = X_PLAYER + 20
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        VELOCIDADE_PLAYER = -20

    # Colisão com as plataformas
    if (
        BOTTOM_RECT.collidelistall(dados["plataforma posicao"])
        and VELOCIDADE_PLAYER >= 0
    ):
        VELOCIDADE_PLAYER = -30

    coletou = update_mapa(
        dados["plataforma"],
        dados["plataforma posicao"],
        dados["itens"],
        dados["itens posicao"],
        BOTTOM_RECT,
    )
    if coletou == "moeda":
        moedas += 1
        pontuacao += 5
    elif coletou == "diamante":
        diamantes += 1
        pontuacao += 25
    elif coletou == "vida" and vidas < 1:
        vidas += 1

    dados["plataforma posicao"] = render_mapa(
        dados["plataforma"], dados["itens"], LARGURA, TELA
    )

    TELA.blit(mensagem_format, (10, 10))
    TELA.blit(mensagem2_format, (10, 30))
    TELA.blit(mensagem3_format, (10, 50))
    TELA.blit(mensagem4_format, (10, 70))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
