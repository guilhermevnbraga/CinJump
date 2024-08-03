import pygame
from pygame.locals import *
from random import *
import sys
import pygame as pg

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
    "cores totais": ["verde", "vermelho", "azul","verde", "vermelho", "azul","verde", "vermelho", "azul","azul","verde","verde","verde","azul","verde","azul","verde","verde","verde","verde","verde","branco"],
}
# IMAGENS
stefan= pygame.image.load('stefan.png')

# EFEITOS SONOROS
pygame.mixer.init()
som_moeda= pygame.mixer.Sound('coin.flac')
som_diamante= pygame.mixer.Sound('diamante.ogg')
som_vida= pygame.mixer.Sound('vida.flac')
som_mola= pygame.mixer.Sound('mola.flac')
som_pulo= pygame.mixer.Sound('pulo.wav')
perdervida= pygame.mixer.Sound('perdervida.mp3')
# Classe Jogador
class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.altura = 50
        self.tamanho = 40
        self.vel_y = 0
        self.image= stefan
        self.image= pygame.transform.scale(self.image, [40,50])
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
            self.dx -= 15
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.dx += 15
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.dy -= 15

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
        
        if self.rect.y > 780:
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

        if self.rect.y > 765:
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
        P_X = randint(0, LARGURA - 180)
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
def atualizar_dificuldade(pontuacao):
    if 10000 <= pontuacao < 15000 and cores_plataforma['cores totais'][0] != 'vermelho':
        cores_plataforma['cores totais'][0] = 'vermelho'
    elif 15000 <= pontuacao < 20000 and cores_plataforma['cores totais'][2] != 'vermelho':
        cores_plataforma['cores totais'][2] = 'vermelho'
    elif 20000 <= pontuacao < 25000 and cores_plataforma['cores totais'][3] != 'vermelho':
        cores_plataforma['cores totais'][3] = 'vermelho'
    elif 25000 <= pontuacao < 30000:
        if cores_plataforma['cores totais'][5] != 'vermelho':
            cores_plataforma['cores totais'][5] = 'vermelho'
        if cores_plataforma['cores totais'][6] != 'vermelho':
            cores_plataforma['cores totais'][6] = 'vermelho'
    elif 30000 <= pontuacao < 40000 and cores_plataforma['cores totais'][11] != 'vermelho':
        cores_plataforma['cores totais'][11] = 'vermelho'
    elif pontuacao >= 40000 and cores_plataforma['cores totais'][0] != ['vermelho']:
        cores_plataforma['cores totais'] = ['vermelho',"azul", 'vermelho', 'azul',"azul", 'vermelho', 'vermelho', 'vermelho',"verde", 'vermelho', 'azul', 'vermelho', 'azul', ]


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
def comeco():
    pygame.mixer.music.load('musica_fundo.wav')
    pygame.mixer.music.play(-1)
    fundo= pygame.image.load('menu.png')
    fundo= pygame.transform.scale(fundo, [LARGURA,ALTURA])
    fundo_ret = fundo.get_rect()
    fundo_ret = pygame.Rect(0, 0, 15, 15)
    TELA.blit(fundo, fundo_ret)
    menu()

def menu():
	while True:
		jogar = pygame.image.load("botaojogar.png")
		jogar = pygame.transform.scale(jogar, (150, 70))
		botao_jogar= Button(jogar, 290, 500)
		
		sair = pygame.image.load("botaosair.png")
		sair = pygame.transform.scale(sair, (150, 70))
		botao_sair= Button(sair, 290, 600)
        
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
		
		botao_jogar.update()
		botao_sair.update()
		pygame.display.update()

# Area de testes

LARGURA = 600
ALTURA = 800
FPS = 60
pygame.init()
fonte = pygame.font.SysFont("arial", 20, True, True)
TELA = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()
def main():
    backgr= pygame.image.load('fundo.png')
    backgr= pygame.transform.scale(backgr, [LARGURA,ALTURA])
    backgr_ret = backgr.get_rect()
    backgr_ret = pygame.Rect(0, 0, 15, 15)
    moedas = 0
    vidas = 0
    diamantes = 0
    pontuacao = 0
    scrollar = 0
    MAX_PLATAFORMAS = 20  # Número máximo de plataformas simultâneas

    plataformas = gerar_plataformas(MAX_PLATAFORMAS)
    dados = construir_mapa(plataformas, LARGURA, ALTURA)
    rodar = True
    X_PLAYER = dados["plataforma"][0].rect.left + 30
    Y_PLAYER = dados["plataforma"][0].rect.top - 50
    player = Jogador(X_PLAYER, Y_PLAYER)
    gameover= False
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
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
                rodar = False

        TELA.blit(backgr, backgr_ret)
        player.desenhar(TELA)
        scrollar, pontuacao_somar = player.movimentar(LARGURA, ALTURA, dados["plataforma"], dados["itens"])
        pontuacao -= pontuacao_somar
        if player.rect.bottom >= 780 and not gameover:
            perdervida.play()
            if vidas >= 1:
                vidas -= 1
                player.vel_y = -50
            else:
                gameover = True
        if gameover:
            pygame.mixer.music.stop()
            player.GRAVIDADE=0
            imagem= pygame.image.load('gameover.png')
            imagem= pygame.transform.scale(imagem, [LARGURA,ALTURA])
            retangulo = imagem.get_rect()
            retangulo = pygame.Rect(0, 0, 15, 15)
            TELA.blit(imagem, retangulo)
            pygame.display.update()
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]: #clicar espaço para voltar ao menu
                comeco()
            if keys[pg.K_ESCAPE]: #clicar esc para sair
                pygame.quit()
                sys.exit()

        else:

            # Verifica e remove as plataformas que saem da tela
            render_mapa(dados["plataforma"], dados["itens"], LARGURA, TELA, scrollar)

            # Gera novas plataformas quando necessário
            while len(dados["plataforma"]) < MAX_PLATAFORMAS:
                nova_plataforma = choice(cores_plataforma["cores totais"])
                ultima_plataforma = dados["plataforma"][-1]

                # Posição X aleatória, mas dentro dos limites da tela
                P_X = randint(0, LARGURA - 180)
                
                # A nova plataforma será gerada a uma distância controlada da última
                P_Y = ultima_plataforma.rect.top - randint(100, 150)
                P_L = 100

                cor = cores_plataforma[nova_plataforma]
                nova_plat = Plataforma(P_X, P_Y, P_L, cor)
                dados["plataforma"].append(nova_plat)
                
                # Geração do item em cima da nova plataforma
                if cor != cores_plataforma["azul"]:
                    novo_item = Item(nova_plat, cor, len(dados["plataforma"]))
                    dados["itens"].append(novo_item)
            
            atualizar_dificuldade(pontuacao)
        
            coletou = update_mapa(dados["plataforma"], dados["itens"], player)
            if coletou == "moeda":
                moedas += 1
                som_moeda.play()
                pontuacao += 100
            elif coletou == "diamante":
                som_diamante.play()
                diamantes += 1
                pontuacao += 500
            elif coletou == "vida" and vidas < 3:
                som_vida.play()
                vidas += 1

            TELA.blit(mensagem_format, (10, 10))
            TELA.blit(mensagem2_format, (10, 30))
            TELA.blit(mensagem3_format, (10, 50))
            TELA.blit(mensagem4_format, (10, 70))
            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()

comeco()
