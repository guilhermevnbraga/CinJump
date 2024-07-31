import pygame
from pygame.locals import *
from random import *
import sys

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

    def desenhar(self, TELA):
        pygame.draw.rect(TELA, self.cor, self.rect)

    def movimentar(self, LARGURA, ALTURA, PLATAFORMAS,GRAVIDADE, scrollar_tamanho):
        self.scrollar = 0
        self.dx = 0
        self.dy = 0
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

        if self.rect.x + self.dx >= LARGURA:
            self.dx = -self.rect.x
        elif self.rect.x + self.dx <= 0:
            self.dx = LARGURA - 20
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
                        self.vel_y = -20

        if self.rect.top <= scrollar_tamanho and self.vel_y < 0:
            self.scrollar -= self.dy 
            pontuacao += self.scrollar if self.vel_y < 0 else 0

        self.rect.x += self.dx
        self.rect.y += self.dy + self.scrollar

        return self.scrollar, pontuacao

class plataforma:

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

    def sumir_vermelho(self,R_PLAYER):
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

class item:
    def __init__(self, X, Y, cor, i):
        self.X = X
        self.Y = Y
        self.rect = pygame.Rect(self.X + 42.5, self.Y - 15, 15, 15)
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
			#position0= x // position1= y


# FUNÇÕES


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
    P_Y = ALTURA - 30
    for i, p in enumerate(LISTA_PLATAFORMAS):
        P_L = 100
        P_X = randint(0, LARGURA - 110)
        cor = cores_plataforma["verde"] if i == 0 else cores_plataforma[p]
        plataform = plataforma(P_X, P_Y, P_L, cor)
        dados["plataforma"].append(plataform)
        if cor != cores_plataforma["azul"]:
            ite = item(P_X, P_Y, cor, i)
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


def render_mapa(plataformas, items, LARGURA, TELA,scrollar):

    for plataforma, itens, i in zip(plataformas, items, range(len(plataformas))):
        plataforma.mover_azul(LARGURA)
        itens.desenho(TELA)
        plataforma.desenhar(TELA)
        deletar = plataforma.scrollar_tela(scrollar)
        deletar2 = itens.scrollar_item(scrollar)
        if deletar:
            plataformas.pop(i)
        if deletar2:
            items.pop(i)


def menu():
	while True:
		jogar = pygame.image.load("jogar.png")
		jogar = pygame.transform.scale(jogar, (100, 60))
		botao_jogar= Button(jogar, 400, 500)
		
		sair = pygame.image.load("sair.png")
		sair = pygame.transform.scale(sair, (100, 60))
		botao_sair= Button(sair, 200, 200)

		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == pygame.MOUSEBUTTONDOWN:
				verifica_jogar= botao_jogar.clique(pygame.mouse.get_pos())
				verifica_sair= botao_sair.clique(pygame.mouse.get_pos())
				if verifica_sair== True:
					pygame.quit()
					sys.exit()
				if verifica_jogar== True:
					main()
					

		TELA.fill("black")

		botao_jogar.update()
		botao_sair.update()
		pygame.display.update()


# AREA DE TESTES RETIRAR QUANDO O CÓDIGO FOR FINALIZADO
LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
fonte = pygame.font.SysFont("arial", 20, True, True)
TELA = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

def main():
    
    moedas = 0
    vidas = 0
    diamantes = 0
    pontuacao = 0
    scrollar_tamanho = 100
    scrollar = 0

    MAX_PLATAFORMAS = 20

    plataformas = gerar_plataformas(MAX_PLATAFORMAS)
    dados = construir_mapa(plataformas, LARGURA, ALTURA)

    X_PLAYER = dados["plataforma"][0].rect.left + 40
    Y_PLAYER = dados["plataforma"][0].rect.top - 20
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

        # Colisão com as plataformas

        coletou = update_mapa(
            dados["plataforma"],
            dados["itens"],
            player,
        )
        if coletou == "moeda":
            moedas += 1
            pontuacao += 5
        elif coletou == "diamante":
            diamantes += 1
            pontuacao += 25
        elif coletou == "vida" and vidas < 1:
            vidas += 1

        render_mapa(dados["plataforma"], dados["itens"], LARGURA, TELA, scrollar)

        player.desenhar(TELA)
        scrollar, pontuacao_somar = player.movimentar(LARGURA, ALTURA, dados["plataforma"], GRAVIDADE, scrollar_tamanho)
        pontuacao += pontuacao_somar
        pontuacao_somar = 0

        TELA.blit(mensagem_format, (10, 10))
        TELA.blit(mensagem2_format, (10, 30))
        TELA.blit(mensagem3_format, (10, 50))
        TELA.blit(mensagem4_format, (10, 70))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


menu()
