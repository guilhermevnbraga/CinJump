from codigos.sprites import *
from codigos.classes import *

#aqui é a lista onde geramos as plataformas aleatoriamente ela gera novas plataformas dependendo do valor que receber
def gerar_plataformas(MAX_PLATAFORMAS):
    PLATAFORMAS = []
    for p in range(0, MAX_PLATAFORMAS):
        plataforma_aleatoria = choice(cores_plataforma["cores totais"])
        PLATAFORMAS.append(plataforma_aleatoria)
    return PLATAFORMAS

#aqui é onde contruimos o mapa pegando a lista gerada acima criando duas novas lista que armazenam as informações do itens de plataformas informações como posição na tela, cor e medidas
def construir_mapa(LISTA_PLATAFORMAS, LARGURA, ALTURA):
    dados = {
        "plataforma": [],
        "itens": [],
    }
    P_Y = ALTURA - 60#aqui temos a altura inicial 
    for i, cor_lista in enumerate(LISTA_PLATAFORMAS):#loop para ver a cor das plataforma
        P_L = 100 #a largura é fixa
        P_X = randint(10, LARGURA - 110)#o x é aleatorio no intervalo de 10 a 690 para a plataforma não escapar da tela e não ser gereda no canto da tela
        cor = cores_plataforma["verde"] if i == 0 else cores_plataforma[cor_lista]#a primeira plataforma é verde
        plataform = Plataforma(P_X, P_Y, P_L, cor)
        dados["plataforma"].append(plataform)#aqui colocamos a plataforma na lista
        if cor != cores_plataforma["azul"]:#aqui o item não aparece na plataforma que se move apenas nas que ficam paradas
            ite = Item(plataform, cor, i, 0)
            dados["itens"].append(ite)
        P_Y -= 30 + randint(30, 150)#aqui eu mudo o y para ela ser gerada acima da plataforma anterior para depois ser movimentada
    return dados

# aqui é a função onde ocorre a mudança do mapa para atualizara colisão com itens para coletar e plataformas para sumir 
def update_mapa(plataformas, itens, R_PLAYER):
    #aqui vemos se a plataforma é vermelha e houve colião se houve nós removemos ela da lista
    for plataforma, i in zip(plataformas, range(len(plataformas))):
        if plataforma.get_cor() == cores_plataforma[
            "vermelho"
        ] and plataforma.sumir_vermelho(R_PLAYER):
            plataformas.pop(i)

    #aqui é onde vemos a colisão com itens onde vemos se o item não é mola, se não for mola o item é coletado ou seja le eé retirado da lista
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

#aqui é onde realmente desenhamos o mapa 
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

#aqui é onde atualizamos a dificuldade do jogo onde com o passar do tempo cada vez mais plataformas que quebram são criadas e a distancia das plataformas almenta com o passar do tempo
def atualizar_dificuldade(pontuacao):
    #o modo que alteramos a quantidade de plataformas que quebram é mudando a lista com as cores totais de plataforma presentes no dicionario do arquivo sprites
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
    elif 30000 <= pontuacao < 50000 and cores_plataforma['cores totais'][11] != 'vermelho':
        cores_plataforma['cores totais'][11] = 'vermelho'
        return [200,230]
    elif pontuacao >= 50000 and cores_plataforma['cores totais'][0] != ['vermelho']:#aqui é onde o jogo chega na dificuldade máxima 
        cores_plataforma['cores totais'] = ['vermelho',"azul", 'vermelho', 'azul',"azul", 'vermelho', 'vermelho', 'vermelho',"verde", 'vermelho', 'azul', 'vermelho', 'azul', ]
        return [230,260]
