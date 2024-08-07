# CIn Jump

## Desenvolvedores

Arthur Rocha Campos <arc></br>
Elisson Dias de Oliveira <edo></br>
Guilherme José da Silva <gjs></br>
Guilherme Vinícius Nigro Braga <gvnb></br>
Ruan Alexandre Ferreira da Silva <rafs2></br>
Vitor Lacerda <vll>

## Sobre o jogo

<ul>
	<li>Jogo criado como um projeto final da cadeira de Introdução à Programação do curso de Ciência da Computação da UFPE;</li>
	<li>Inspirado no clássico Doodle Jump, o jogo consiste em pular em plataformas verticais infinitas para conseguir a maior pontuação, só que com alguns elementos do Centro de Informática;</li>
	<li>
		É possível encontrar as seguintes mecânicas no jogo:
		<ul>
			<li>
				4 personagens selecionáveis, cada um diferentes mecânicas:
				<ul>
					<li>Stefan: Pulo mais alto;</li>
					<li>Anjolina: Pulo muito mais alto, porém com uma gravidade maior;</li>
					<li>Ricardo: Maior velocidade lateral;</li>
					<li>Sérgio: Gravidade menor.</li>
				</ul>
			</li>
			<li>
				3 coletáveis diferentes e que influenciam na jogabilidade:
				<ul>
					<li>Moedas: + 100 pontos;</li>
					<li>Diamantes: +500 pontos;</li>
					<li>Vidas: Faz com que o jogador sobreviva ao cair fora do mapa.</li>
				</ul>
			</li>
			<li>
				4 tipos de plataformas com diferentes funcionalidades:
				<ul>
					<li>Madeira normal: plataforma sem nenhuma especialidade;</li>
					<li>Madeira vermelha: Quebra após pular nela;</li>
					<li>Madeira com movimento: plataforma que se movimenta e que possui 6 níveis de velocidade;</li>
					<li>Madeira com mola: possui uma mola que aumenta a distância do pulo após o contato.</li>
				</ul>
			</li>
			<li>
				Pontuação recorde pessoal (funciona apenas com o jogo aberto);
			</li>
			<li>
				Mensagens de classificação dependendo da sua pontuação final ;
			</li>
			</li>
			<li>
				Níveis de dificuldade discretos que variam dependendo de sua pontuação atual.
			</li>
		</ul>
	</li>
</ul>

## Requisitos

<ul>
    <li>
        Algum local que rode python (Vscode ou Pycharm, por exemplo);
    </li>
    <li>
        Ter a biblioteca “pygame” instalada (preferencialmente, a última versão).
    </li>
</ul>

## Como jogar

<ul>
    <li>
        Baixe o repositório no seu PC;
    </li>
    <li>
        Abra o diretório x no seu compilador de preferência;
    </li>
    <li>
        Execute o arquivo “main.py”.
    </li>
</ul>

## Controles

<ul>
    <li>
        Setinhas para esquerda e direita ou A e D para movimentar o personagem para, respectivamente, esquerda ou direita;
    </li>
    <li>
        Cursor do mouse para selecionar os botões.
    </li>
</ul>

## Screenshots do Jogo:

### Tela Inicial

<img src="./images/home.jpeg"></img>

### Escolha de personagem

<img src="./images/chooseCharacter.jpeg"></img>

### Gameplay

<img src="./images/game1.jpeg"></img>

### Gameplay

<img src="./images/game2.jpeg"></img>

### Fim de jogo

<img src="./images/gameover.jpeg"></img>

## Arquitetura do Projeto:

<ul>
    <li>
        O modo como os arquivos e pastas foram organizados está listado acima, onde as setas representam a ordem import em que nós colocamos um arquivo dentro de outro;
    </li>
    <li>
        As pastas onde foram salvas as fotos e áudios utilizados no jogo são representados pelo balão “imagens e sons utilizados nos jogos” que no repositório correspondem às pastas imagens e pela pasta sounds;
    </li>
    <li>
        Os arquivos usados na imagem também estão inclusos em uma pasta com o nome códigos, sendo os arquivos:
        <ul>
            <li>
                “sprites.py” - Esse sendo o arquivo que transforma as imagens e sons mostrados no item anterior em variáveis e armazena seu valor, além de formatá-las para um formato específico;
            </li>
            <li>
                “classes.py” - Nesse arquivo é onde temos as definições das classes que serão usadas no jogo, sendo elas plataforma e itens, além da classe Button;
            </li>
            <li>
                “player.py” - É o arquivo onde criamos a classe do player que é o personagem jogável, ele é o responsável por interagir com as plataforma e itens, além dos controles do personagem;
            </li>
            <li>
                “game_logic.py” - É onde nós colocamos as funções que geram as plataformas e itens, incluindo também as funções que atualizam o mapa dependendo da interação do jogador com o mapa, além do funcionamento principal do jogo.;
            </li>
            <li>
                “jogo.py” - Aqui é onde a lógica central do jogo está, há variáveis globais que mantêm o estado do jogo entre os loops. As funções principais incluem o menu principal, a seleção de personagem e a tela de game over. A função principal, chamada “main()”, inicializa o jogo configurando o fundo, gerando plataformas e itens, posicionando o jogador, e iniciando o loop do jogo, em que são registrados os coletáveis, pontuação, além do funcionamento do jogo;
            </li>
            <li>
                “main.py” - Tem como função apenas chamar o arquivo “jogo.py” já que ele ficou muito grande, desse jeito o único arquivo que o jogador precisa abrir para rodar o jogo tem 5 linhas.
            </li>
        </ul>
    </li>
</ul>

## Ferramentas, bibliotecas e Frameworks

<ul>
        <li>
            As seguintes ferramentas foram utilizadas:
            <ul>
                <li>
                    Vscode: Principal IDE utilizada no desenvolvimento;
                </li>
                <li>
                    Canvas: Utilizado para criar as imagens das diferentes telas do jogo;
                </li>
                <li>
                    Whatsapp: Principal canal de comunicação da equipe;
                </li>
                <li>
                    Discord: Canal de comunicação para falar com os monitores responsáveis do projeto ;
                </li>
                <li>
                    Playlist de vídeos “Pygame - Jumpy” do canal do youtube “Coding With Russ”, vídeos que ajudaram a programar nosso jogo, com ideias e soluções para algumas funcionalidades do jogo.
                </li>
            </ul>
        </li>
        <li>
            As seguintes bibliotecas foram utilizadas:
            <ul>
                <li>
                    Pygame como biblioteca principal para a construção do jogo e suas funcionalidades, como a movimentação, a posição das plataformas, colisão entre plataformas, entre outros aspectos, além do design do jogo, com a possibilidade de carregar imagens para cada elemento do jogo;
                </li>
                <li>
                    Sys para fechar o jogo de maneira correta com a função “sys.exit()”;
                </li>
                <li>
                    Biblioteca Random para dar uma aleatoriedade no jogo, como a geração aleatória dos tipos de plataformas, o espaçamento entre as plataformas subsequentes e a geração dos tipos de itens.
                </li>
            </ul>
        </li>
</ul>

## Divisão de Trabalho

<ul>
    <li>
        Inicialmente, possuía um plano fixo para a divisão de trabalho, entretanto, ao decorrer do projeto, as funções de cada integrante não foram fixas com o decorrer do projeto e acabou que cada integrante ficou responsável por algo a mais. 
    </li>
    <li>
        Aqui está o que cada integrante acabou realizando:
        <ul>
            <li>
                Guilherme Braga:
                <ul>
                    <li>Criação inicial da movimentação do personagem</li>
                </ul>
            </li>
            <li>
                Elisson Oliveira e Guilherme José:
                <ul>
                    <li>
                        Funcionalidade geral do jogo, como classes, loop principal, geração de mapa, etc.
                    </li>
                    <li>
                        Organização do código após junção das partes
                    </li>
                </ul>
            </li>
            <li>
                Arthur Rocha e Vitor Lacerda:
                <ul>
                    <li>
                        Design, como seleção de sprites, imagens e sons do jogo
                    </li>
                    <li>
                        Transição de telas entre o jogo
                    </li>
                </ul>
            </li>
            <li>
                Ruan Alexandre:
                <ul>
                    <li>
                        Criação de slides e do relatório do github
                    </li>
                    <li>
                        Conselhos e revisão na parte de movimentação do personagem em conjunto com Guilherme Braga
                    </li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        Todos revisaram os slides e a descrição do git antes de publica-lá
    </li>
    <li>
        Todos participaram diretamente ou indiretamente dos ajustes e correções de bugs
    </li>
</ul>

## Conceitos utilizados

<ul>
    <li>
        Listas:
        <ul>
            <li>
                Utilizado para armazenar plataformas e itens do mapa.
            </li>
        </ul>
    </li>
    <li>
        Dicionários:
        <ul>
            <li>
                Utilizado para armazenar informações, como tuplas e listas.
            </li>
        </ul>
    </li>
    <li>
        Condicionais:
        <ul>
            <li>
                Utilizado para diversas situações, como a seleção de personagens, armazenar os coletáveis, etc.
            </li>
        </ul>
    </li>
    <li>
        Laços de repetição:
        <ul>
            <li>
                Utilizado “for”s para acessar conteúdos das listas e dicionários, além do “while” para o loop do jogo.
            </li>
        </ul>
    </li>
    <li>
        Funções:
        <ul>
            <li>
                Facilitar sequências de códigos que são reutilizados ou passar para outras telas.
            </li>
        </ul>
    </li>
    <li>
        Classes:
        <ul>
            <li>
                Orientação de objetos, como a movimentação, funcionalidades das plataformas, itens e botões.
            </li>
        </ul>
    </li>
</ul>

## Desafios e Erros

### Pergunta 1

    “Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?”

### Resposta:

    A geração das plataformas, quando chegava na metade/final do limite determinado da lista de plataformas,
    as plataformas subsequentes ficavam mais espaçadas do que o normal e que os itens não estavam sendo
    gerados corretamente em cima da plataforma, ficando espalhado pelo mapa. Após pedir ajuda dos monitores e
    ninguém apresentar uma solução plausível até que em certo momento Arthur se lembrou de ter retirado uma
    parte do código de uma função para colocá-lo dentro do loop principal, tentamos isso e deu certo, não
    sabemos o exato motivo do porque, mas funcionou.

### Pergunta 2

    Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?

### Resposta:

    Resolver bugs foi definitivamente o maior desafio, devido a nossa inexperiência com o pygame entender
    onde exatamente havia os erros foi mais complicado que quando mexemos com python normal, para lidar com
    isso bastou estudar mais sobre a linguagem, pedir ajuda aos monitores, conversar entre si e revisar o
    código juntos.

### Pergunta 3

    “Quais as lições aprendidas durante o projeto?”

### Resposta:

    Aprendemos a mexer com o pygame, que pode funcionar como uma base para aprender outras linguagens de
    desenvolvimento de jogos, aprendemos a trabalhar em um projeto em equipe, dividir tarefas entre si, se
    ajudar. Tudo isso nos dá experiência para o futuro no mercado de trabalho e em projetos pessoais de
    python e pygame.
