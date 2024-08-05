import pygame
import sys
from sprites import *
from plataforms_itens import *
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
        P_X = randint(10, LARGURA - 110)
        cor = cores_plataforma["verde"] if i == 0 else cores_plataforma[p]
        plataform = Plataforma(P_X, P_Y, P_L, cor)
        dados["plataforma"].append(plataform)
        if cor != cores_plataforma["azul"]:
            ite = Item(plataform, cor, i, 0)
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
def atualizar_dificuldade(pontuacao):
    if 10000 <= pontuacao < 15000 and cores_plataforma['cores totais'][0] != 'vermelho':
        cores_plataforma['cores totais'][0] = 'vermelho'
        return [130,160]
    elif 15000 <= pontuacao < 20000 and cores_plataforma['cores totais'][2] != 'vermelho':
        cores_plataforma['cores totais'][2] = 'vermelho'
        return [150,170]
    elif 20000 <= pontuacao < 25000 and cores_plataforma['cores totais'][3] != 'vermelho':
        cores_plataforma['cores totais'][3] = 'vermelho'
        return [170,190]
    elif 25000 <= pontuacao < 30000:
        if cores_plataforma['cores totais'][5] != 'vermelho':
            cores_plataforma['cores totais'][5] = 'vermelho'
        if cores_plataforma['cores totais'][6] != 'vermelho':
            cores_plataforma['cores totais'][6] = 'vermelho'
        return [190,200]
    elif 30000 <= pontuacao < 40000 and cores_plataforma['cores totais'][11] != 'vermelho':
        cores_plataforma['cores totais'][11] = 'vermelho'
        return [200,230]
    elif pontuacao >= 40000 and cores_plataforma['cores totais'][0] != ['vermelho']:
        cores_plataforma['cores totais'] = ['vermelho',"azul", 'vermelho', 'azul',"azul", 'vermelho', 'vermelho', 'vermelho',"verde", 'vermelho', 'azul', 'vermelho', 'azul', ]
        return [230,260]
