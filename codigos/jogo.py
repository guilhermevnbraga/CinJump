import pygame
from pygame.locals import *
from random import *
import sys
import pygame as pg
from codigos.sprites import *
from codigos.classes import *
from codigos.player import *
from codigos.game_logic import *

#aqui temos as variaveis que serão usadas no codigo
pontuacao_recorde = 0 # pontuação maxima atinigida no jogo que ficara salva e aparecera na tela de menu
LARGURA = 600#largura da tela
ALTURA = 800#altura da tela
FPS = 60#fps da tela colocamos 60 já que é o padrão
pygame.init()#começa o pygame
pygame.display.set_caption('Cin Jump')#nome do noso jogo
fonte = pygame.font.SysFont("Comic Sans MS", 20, True, True)#fonte usada no jogo
TELA = pygame.display.set_mode((LARGURA, ALTURA))#sdesenhar tela
clock = pygame.time.Clock()#clock do jogo

# variaveis globais usadas nas funçoes essas variaveis não são zeradas a cada loop do jogo mas modificadas
selecionou = False#caso vc já selecionou pela primeira vez um personagem
personagem_escolhido = ''#personagem atual 
pontuacao_recorde = 0#pontuação maxima atingida no jogo
parametros =[]#diferenciais de cada personagem

def recorde_def(pontuação):#aqui é onde vemos se a pontuação atingida no momento é maior que o recorde
    global pontuacao_recorde
    if pontuação > pontuacao_recorde:
        pontuacao_recorde = pontuação
    return pontuacao_recorde   
#def inicial que começa a musica do jogo e coloca na tela a imagem do menu
def comeco():
    global selecionou, personagem_escolhido
    pygame.mixer.music.load('./sounds/musica_fundo.wav')
    pygame.mixer.music.play(-1)
    menu_image = pygame.image.load("./images/menu.png")
    fundo = pygame.transform.scale(menu_image, (600, 800))
    fundo_ret = fundo.get_rect()
    fundo_ret = pygame.Rect(0, 0, 15, 15)
    TELA.blit(fundo, fundo_ret)
    menu()#chama a função menu
#função menu onde vc seleciona o que vai fazer, você pode jogar o jogo, mudar de personagem ou sair do jogo
def menu():
    global selecionou, personagem_escolhido
    while True:#aqui é o loop onde é selecionado qual o proximo passo do sistema
        #botões
        botao_jogar = Button(jogar, 290, 500)
        botao_sair = Button(sair, 290, 700)
        botao_selecionar = Button(personagem_seletor, 290, 600)
        #vê qual foi a opção selecionada
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:#jogador sai do jogo
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                #vê onde o jogador clicou na tela
                verifica_jogar = botao_jogar.clique(pygame.mouse.get_pos())
                verifica_sair = botao_sair.clique(pygame.mouse.get_pos())
                verifica_selecao = botao_selecionar.clique(pygame.mouse.get_pos())
                if verifica_sair:#nesse caso sai do jogo
                    pygame.quit()
                    sys.exit()
                if verifica_jogar and not selecionou:#caso nenhum personagem tenha sido selecionado mas o jogador coloque em começar o jogo o jogador é direcinado a tela de seleção de personagem
                    selecionar_personagem()#chama selecionar personagem
                elif verifica_jogar and selecionou:#caso ele vá apenas para começar o jogo ele vai para o main
                    main(personagem_escolhido)#chama o main com o sprite do personagem escolhido
                if verifica_selecao:#caso ele queira selecionar um personagem
                    selecionar_personagem()#chama selecionar personagem

        # mostrar o record atual na tela
        if pontuacao_recorde == 0:#enquanto a pontuação for 0
            recorde_mensagem = "Jogue a primeira vez para vermos seu melhor"
            fonte = pygame.font.SysFont("Comic Sans MS", 25, True, True)
        else:#assim que o jogador somar a primeira pontuação
            recorde_mensagem = f"RECORDE PESSOAL: {pontuacao_recorde}"
            fonte = pygame.font.SysFont("Comic Sans MS", 25, True, True)
        recorde_mensagem_surface = fonte.render(recorde_mensagem, True, (219, 30, 47))
        TELA.blit(recorde_mensagem_surface, (25, 25))#coloca a mensagem na tela
        
        #atualiza o botão
        botao_jogar.update(TELA)
        botao_sair.update(TELA)
        botao_selecionar.update(TELA)
        pygame.display.update()

#aqui é a tela de seleção de personagem que pode ser um dos 4 professores, stephan, anjolina, sergio e ricardo 
def selecionar_personagem():
    global selecionou, personagem_escolhido, parametros
    #carrega a imagem da tela de seleção
    imagem_selecao = pygame.image.load("./images/selecao.png")
    fundo_selecao = pygame.transform.scale(imagem_selecao, (600, 800))    
    fundo_rect = fundo_selecao.get_rect()
    fundo_rect = pygame.Rect(0, 0, 15, 15)
    TELA.blit(fundo_selecao, fundo_rect)
    while True:
        #posiciona a imagem do personagem que vai ser selecionado como um botão 
        stefan_select = Button(stefan_selecionar, 70, 469)
        anjolina_select = Button(anjolina_selecionar, 222, 469)
        ricardo_select = Button(ricardo_selecionar, 377, 469)
        sergio_select = Button(sergio_selecionar, 533, 469)

        for event in pygame.event.get():#aqui vemos qual vai ser o proximo passo do jogador
            if event.type == pygame.QUIT:#caso o jogador feche o jogo
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:#caso onde o jogador seleciona o personagem nesse caso retorna que um personagem foi selecionado e o personagem que foi
                verificar_stefan = stefan_select.clique(pygame.mouse.get_pos())
                verificar_anjolina = anjolina_select.clique(pygame.mouse.get_pos())
                verificar_ricardo = ricardo_select.clique(pygame.mouse.get_pos())
                verificar_sergio = sergio_select.clique(pygame.mouse.get_pos())
                if verificar_stefan:#seleciona stephan como personagem
                    selecionou = True
                    personagem_escolhido = stefan_player
                    parametros =[-27, 1, 10]#diferenças dos personagens, pulo, gravidade, velocidade
                    main(personagem_escolhido)#no final chama o jogo com o sprite do personagem selecionado
                if verificar_anjolina:#seleciona anjolina
                    selecionou = True
                    personagem_escolhido = anjolina_player
                    parametros =[-40, 1.5, 10]#diferenças dos personagens, pulo, gravidade, velocidade
                    main(personagem_escolhido)#no final chama o jogo com o sprite do personagem selecionado
                if verificar_ricardo:#seleciona ricardo
                    selecionou = True
                    personagem_escolhido = ricardo_player
                    parametros =[-25, 1, 18]#diferenças dos personagens, pulo, gravidade, velocidade
                    main(personagem_escolhido)#no final chama o jogo com o sprite do personagem selecionado
                if verificar_sergio:#seleciona sergio
                    selecionou = True
                    personagem_escolhido = sergio_player
                    parametros =[-25, 0.8, 10]#diferenças dos personagens, pulo, gravidade, velocidade
                    main(personagem_escolhido)#no final chama o jogo com o sprite do personagem selecionado
        
        #manter o botão atualizado
        stefan_select.update(TELA)
        anjolina_select.update(TELA)
        ricardo_select.update(TELA)
        sergio_select.update(TELA)
        pygame.display.update()    

#função que cria a tela de game over
def game_over(pontuacao, player):
    #tela de game over qpara quando o jogador cai do mapa e não tem mais vida
    #para o player para ele ficar parado
    pygame.mixer.music.stop()#começa musica
    player.GRAVIDADE = 0
    #carrega a imagem do game over
    imagem = pygame.image.load('./images/gameover.png')
    imagem = pygame.transform.scale(imagem, [LARGURA, ALTURA])
    retangulo = imagem.get_rect()
    retangulo = pygame.Rect(0, 0, 15, 15)
    TELA.blit(imagem, retangulo)
    
    #vê qual a mensagem que vai aparecer dependendo da pontuação atingida
    mensagem, x = mensagem_gameover(pontuacao)
    pontuacao_mensagem = f'PONTUAÇÃO {pontuacao}'
    posicao = len(pontuacao_mensagem)*15#achar o x da pontuação
    posicao = (600 - posicao)/2
    fonte_grande = pygame.font.SysFont("Comic Sans MS", 25, True, True)
    mensagem_format = fonte_grande.render(mensagem, True, (219, 30, 47))
    pontuacao_format = fonte_grande.render(pontuacao_mensagem, True, (219, 30, 47))
    TELA.blit(pontuacao_format, (posicao, 30))
    TELA.blit(mensagem_format, (x, 80)) 
    
    pygame.display.update()
    #dependendo da tecla apertada vai para o comeco ou sai do jogo
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]: #clicar espaço para voltar ao menu
        comeco()
    if keys[pg.K_ESCAPE]: #clicar esc para sair
        pygame.quit()
        sys.exit()

#aqui é a fução que seleciona a mensagem que aparece na tela de gameover ela devolve a mensagem e a posição x da mensagem
def mensagem_gameover(pontuacao):
    if pontuacao <= 5000:
        mensagem = "Reprovado!"
        x = 250
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
#função que da a sensação de plataformas infinitas        
def plataforma_infinita(dados, MAX_PLATAFORMAS, espacamento, pontuacao):
    #ele vê se o toal de plataformas restantes é menor que a plataformas maximas caso seja menor ele precisa criar plataformas até que seja maior ou igual ao max_plataformas
    while len(dados["plataforma"]) < MAX_PLATAFORMAS:
        #nova_plataforma
        nova_plataforma = choice(cores_plataforma["cores totais"])
        ultima_plataforma = dados["plataforma"][-1]
        
        P_X = randint(10, LARGURA - 110)
        P_Y = ultima_plataforma.rect.top - randint(espacamento[0], espacamento[1])
        P_L = 100

        cor = cores_plataforma[nova_plataforma]
        nova_plat = Plataforma(P_X, P_Y, P_L, cor)
        dados["plataforma"].append(nova_plat)
        #caso a plataforma não se mova criamos o novo item que ficara nela 
        if cor != cores_plataforma["azul"]:
            novo_item = Item(nova_plat, cor, len(dados["plataforma"]), pontuacao)
            dados["itens"].append(novo_item)

#função principal onde rodamos o jogo
def main(personagem):
    #carrega a imagem de fundo
    backgr = pygame.image.load('./images/fundo.png')
    backgr = pygame.transform.scale(backgr, [LARGURA, ALTURA])
    backgr_ret = backgr.get_rect()
    backgr_ret = pygame.Rect(0, 0, 15, 15)
    #itens coletados na rodada e pontuação atingida (inicialmente)
    moedas = 0
    vidas = 0
    diamantes = 0
    pontuacao = 0
    #construir as primeiras plataformas
    MAX_PLATAFORMAS = 20 
    espacamento = [100, 150]
    plataformas = gerar_plataformas(MAX_PLATAFORMAS)
    dados = construir_mapa(plataformas, LARGURA, ALTURA)
    scrollar = 0
    rodar = True
    #posição inicial do jogador para ficar em cima da primeira plataforma
    X_PLAYER = dados["plataforma"][0].rect.left + 30
    Y_PLAYER = dados["plataforma"][0].rect.top - 60
    player = Jogador(personagem, X_PLAYER, Y_PLAYER, parametros)#cria o player com o sprite selecionado
    gameover = False#caso de derrota no jogo abra a tela de game over
    while rodar:
        #vê se o jogador quer sair do jogo
        for event in pygame.event.get():#se a tecla selecionada for esc ou der quit no jogo, o jogo fecha
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[K_g]:#caso a tecla selecionada seja (g) o jogo vai para a tela de game over para o caso do jogador querer sair do jogo sem fechar ele
                gameover = True
                player.rect.y = 1000
        TELA.blit(backgr, backgr_ret)#carrega a imagem de fundo

        player.desenhar(TELA)#desenha o player na tela
        scrollar, pontuacao_somar = player.movimentar(LARGURA, ALTURA, dados["plataforma"], dados["itens"])#vê a pontuação e o quanto a tela deve descer para dar a sensação de movimento de tela
        pontuacao -= pontuacao_somar#como a pontução chega negativa tem que subtrair da pontuação
        recorde_def(pontuacao)#Vê se a pontuação é recorde

        #aqui vê se o jogador chegou no fim da tela significando que ele morreu ou perdeu uma vida
        if player.rect.bottom >= 780 and not gameover:#o not game over é para garantir que o jogo não fique tocando diversas vezes o som de perder vida
            perdervida.play()
            if vidas >= 1:#caso que o player tenha uma vida
                vidas -= 1#diminui a vida
                player.vel_y = -60#o jogador da um pulo para cima do jogo para dar chance ao player
            else:#caso que ele não tenha nenhuma vida
                player.rect.y = 1000#coloca a posição do player de forma que ele não interaje com o jogo
                gameover = True#a função gameover é chamada
        
        if gameover:#caso o player tenha morrido chama a função game over
            game_over(pontuacao, player)

        else:
            render_mapa(dados["plataforma"], dados["itens"], LARGURA, TELA, scrollar)#renderiza o mapa

            plataforma_infinita(dados, MAX_PLATAFORMAS, espacamento, pontuacao)#cria novas plataformas caso nescessario
            
            espacamento1 = atualizar_dificuldade(pontuacao)#atualiza o novo espaçamento da tela baseado na dificuldade
            if espacamento1 is not None:
                espacamento = espacamento1#atualiza o espaçamento
            coletou = update_mapa(dados["plataforma"], dados["itens"], player)#vÊ se algum item foi coletado
            if coletou == "moeda":#caso coletou moeda
                moedas += 1
                som_moeda.play()
                pontuacao += 100
            elif coletou == "diamante":#caso coletou diamante
                som_diamante.play()
                diamantes += 1
                pontuacao += 500
            elif coletou == "vida" and vidas < 3:#caso coletou vida sendo que no maximo o jogador tem três vidas
                som_vida.play()
                vidas += 1

            # mostrar os itens coletados e a pontuação no canto superior esquerdo da tela
            TELA.blit(imagem_moeda_contador, (10, 10))
            mensagem_format = fonte.render(f"x {moedas}", True, (254, 225, 86))
            TELA.blit(mensagem_format, (50, 10))

            TELA.blit(imagem_vida_contador, (10, 90))
            mensagem2_format = fonte.render(f"x {vidas}", True, (203, 56, 51))
            TELA.blit(mensagem2_format, (50, 90))

            TELA.blit(imagem_diamante_contador, (10, 50))
            mensagem3_format = fonte.render(f"x {diamantes}", True, (90, 203, 255))
            TELA.blit(mensagem3_format, (50, 50))
            fonte2 = pygame.font.SysFont("Comic Sans MS", 30, True, True)
            
            mensagem4_format = fonte2.render(f"{pontuacao}", True, (128, 0, 0))
            TELA.blit(mensagem4_format, (12, 130))
            pygame.display.update()#da update no jogo
            clock.tick(FPS)

    pygame.quit()#caso acabe o jogo

comeco()#chamar a função comeco
