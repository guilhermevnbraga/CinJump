import pygame
from pygame.locals import *
from random import *
import sys
import pygame as pg
from sprites import *
from menu import *
from plataforms_itens import *
from player import *
from game_logic import *
def recorde_def(pontuação):
    global pontuacao_recorde
    if pontuação>pontuacao_recorde:
        pontuacao_recorde=pontuação
    return pontuacao_recorde   
def comeco():
    pygame.mixer.music.load('./sounds/musica_fundo.wav')
    pygame.mixer.music.play(-1)
    menu_image = pygame.image.load("./images/menu.png")
    fundo = pygame.transform.scale(menu_image, (600,800))
    fundo_ret = fundo.get_rect()
    fundo_ret = pygame.Rect(0, 0, 15, 15)
    TELA.blit(fundo, fundo_ret)
    menu()

def menu():
    while True:
        botao_jogar = Button(jogar, 290, 500)
        botao_sair = Button(sair, 290, 600)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                verifica_jogar = botao_jogar.clique(pygame.mouse.get_pos())
                verifica_sair = botao_sair.clique(pygame.mouse.get_pos())
                if verifica_sair == True:
                    pygame.quit()
                    sys.exit()
                if verifica_jogar == True:
                    main()

        # Exibição do recorde na tela
        if(pontuacao_recorde==0):
            recorde_mensagem = f"Jogue a primeira vez para vermos seu melhor"
            fonte = pygame.font.SysFont("Comic Sans MS", 25, True, True)
        else:
            recorde_mensagem = f"RECORDE PESSOAL: {pontuacao_recorde}"
            fonte = pygame.font.SysFont("Comic Sans MS", 25, True, True)
        recorde_mensagem_surface = fonte.render(recorde_mensagem, True, (219, 30, 47))
        TELA.blit(recorde_mensagem_surface, (25, 25))

        botao_jogar.update()
        botao_sair.update()
        pygame.display.update()	
def main():
    backgr = pygame.image.load('./images/fundo.png')
    backgr= pygame.transform.scale(backgr, [LARGURA,ALTURA])
    backgr_ret = backgr.get_rect()
    backgr_ret = pygame.Rect(0, 0, 15, 15)
    moedas = 0
    vidas = 0
    diamantes = 0
    scrollar = 0
    MAX_PLATAFORMAS = 20 
    espaçamento = [100,150]
    pontuacao = 0
    plataformas = gerar_plataformas(MAX_PLATAFORMAS)
    dados = construir_mapa(plataformas, LARGURA, ALTURA)
    rodar = True
    X_PLAYER = dados["plataforma"][0].rect.left + 30
    Y_PLAYER = dados["plataforma"][0].rect.top - 50
    player = Jogador(X_PLAYER, Y_PLAYER)
    gameover= False
    while rodar:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
                pygame.quit()
                sys.exit()

        TELA.blit(backgr, backgr_ret)


        player.desenhar(TELA)
        scrollar, pontuacao_somar = player.movimentar(LARGURA, ALTURA, dados["plataforma"], dados["itens"])
        pontuacao -= pontuacao_somar
        pontuacao_recorde = recorde_def(pontuacao)
        if player.rect.bottom >= 780 and not gameover:
            perdervida.play()
            if vidas >= 1:
                vidas -= 1
                player.vel_y = -50
            else:
                player.rect.y = 1000
                gameover = True
        if gameover:

            pygame.mixer.music.stop()
            player.GRAVIDADE=0
            imagem= pygame.image.load('./images/gameover.png')
            imagem= pygame.transform.scale(imagem, [LARGURA,ALTURA])
            retangulo = imagem.get_rect()
            retangulo = pygame.Rect(0, 0, 15, 15)
            TELA.blit(imagem, retangulo)

            
            mensagem, x = mensagem_gameover(pontuacao)
            pontuacao_mensagem = f'PONTUAÇÃO {pontuacao}'
            fonte_grande = pygame.font.SysFont("Comic Sans MS", 25, True, True)
            mensagem_format = fonte_grande.render(mensagem, True, (219, 30, 47))
            pontuacao_format = fonte_grande.render(pontuacao_mensagem, True, (219, 30, 47))
            TELA.blit(pontuacao_format, (180, 30))
            TELA.blit(mensagem_format, (x, 80)) 
           
            pygame.display.update()
            
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]: #clicar espaço para voltar ao menu
                comeco()
            if keys[pg.K_ESCAPE]: #clicar esc para sair
                pygame.quit()
                sys.exit()

        else:

            
            render_mapa(dados["plataforma"], dados["itens"], LARGURA, TELA, scrollar)

            
            while len(dados["plataforma"]) < MAX_PLATAFORMAS:
                nova_plataforma = choice(cores_plataforma["cores totais"])
                ultima_plataforma = dados["plataforma"][-1]

               
                P_X = randint(10, LARGURA - 110)
                
                
                P_Y = ultima_plataforma.rect.top - randint(espaçamento[0], espaçamento[1])
                P_L = 100

                cor = cores_plataforma[nova_plataforma]
                nova_plat = Plataforma(P_X, P_Y, P_L, cor)
                dados["plataforma"].append(nova_plat)
                
                
                if cor != cores_plataforma["azul"]:
                    novo_item = Item(nova_plat, cor, len(dados["plataforma"]),pontuacao)
                    dados["itens"].append(novo_item)
            
            espaçamento1 = atualizar_dificuldade(pontuacao)
            if espaçamento1 is not None:
                espaçamento = espaçamento1
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
            TELA.blit(imagem_moeda_contador, (10, 10))
            mensagem_format = fonte.render(f"x {moedas}", True, (254, 225, 86))
            TELA.blit(mensagem_format, (50, 10))

            # Exibe a imagem da vida e a quantidade coletada
            TELA.blit(imagem_vida_contador, (10, 50))
            mensagem2_format = fonte.render(f"x {vidas}", True, (203, 56, 51))
            TELA.blit(mensagem2_format, (50, 50))

            # Exibe a imagem do diamante e a quantidade coletada
            TELA.blit(imagem_diamante_contador, (10, 90))
            mensagem3_format = fonte.render(f"x {diamantes}", True, (90, 203, 255))
            TELA.blit(mensagem3_format, (50, 90))
            fonte2 = pygame.font.SysFont("Comic Sans MS", 30, True, True)
            
            mensagem4_format = fonte2.render(f"{pontuacao}", True, (128, 0, 0))
            TELA.blit(mensagem4_format, (12, 130))
            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()

comeco()