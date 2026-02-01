"""Memória, jogo de quebra-cabeça de pares.

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo.

Desafios:

1. Contar e imprimir quantos cliques ocorrem. --concluido
2. Reduzir o número de peças para um tabuleiro 4x4. --concluido
3. Detectar quando todas as peças forem reveladas.
4. Centralizar peças de um único dígito.
5. Usar letras em vez de números. --concluido
6. Identificar jogador em cada rodada. Qual o nome do jogador que vai iniciar um jogo?
7. Armazenar jogador e suas pontuações em arquivo. Ao final do jogo, armazenar em arquivo
o nome do jogador que jogou e sua respectiva pontuação na rodada. 
Deve ser armazenado a quantidade de cliques do jogador até resolver todo o tabuleiro.
8. Listar jogadores e suas pontuações. Exibir no terminal uma lista de todos os jogadores
que jogaram o jogo com suas respectivas pontuações.
"""

import turtle
import random
from freegames import path
from main import Score


carro = path('car.gif')
pecas = list(range(32)) * 2
estado = {'marca': None}
escondido = [True] * 64
toques = 0
game = {"state": False}
pecas_4_4 = list(range(8)) * 2
escondido_4_4 = [True] * 16
username = None
modo_de_jogo = None
dificuldade = None
p1 = None
configuracoes = {"username": None, "dificuldade": None, "p1": True, "p2": False}

t_username= turtle.Turtle()
mensagens_avisos = turtle.Turtle()
mensagens_avisos.hideturtle()
mensagens_avisos.teleport(0,-140)
mensagens_avisos.pencolor("red")

mudar_p1 = turtle.Turtle()
mudar_p1.teleport(-100,10)
mudar_p2 = turtle.Turtle()
mudar_p2.teleport(100,10)

mudar_facil = turtle.Turtle()
mudar_facil.teleport(-100,-40)
mudar_difi = turtle.Turtle()
mudar_difi.teleport(100,-40)
def letras(ind):
    letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    return letra[ind]
def quadrado_4(x, y):
    """Desenha um quadrado branco com contorno preto em (x, y)."""
    #TODO rescrever de forma que desenhe um quadrado a partir do ponto (x,y)
    # com 50 pixels de lado
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

def quadrado(x,y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()



def indice(x, y):
    """Converte coordenadas (x, y) no índice da peça."""
    coluna = int((x + 200) // 100)
    linha = int((y + 200) // 100)
    if 0 <= coluna < 4 and 0 <= linha < 4:
        return linha * 4 + coluna
    return None

def indice_4(x,y):
    return int((x + 200) //50 + ((y + 200) // 50) * 8)

def coordenadas_4(contador):
    """Converte o índice da peça em coordenadas (x, y)."""
    return (contador % 4) * 100 - 200 , (contador // 4) * 100 - 200

def coordenadas(contador):
    return (contador % 8 ) * 50 -200, (contador //8) * 50 -200
def toque(x, y):
    """Atualiza a marcação e as peças escondidas com base no clique."""
    posicao = indice(x, y) if configuracoes["dificuldade"]=="facil" else indice_4(x,y)
    marca = estado['marca']
    global toques
    toques+=1
    print(toques)
    if (marca is None or marca == posicao or (pecas[marca] != pecas[posicao] if configuracoes["dificuldade"]=="dificil" else pecas_4_4[marca] != pecas_4_4[posicao])):
        estado['marca'] = posicao
    else:
        if configuracoes["dificuldade"]=="dificil":
            escondido[posicao] = False
            escondido[marca] = False
            estado['marca'] = None
        else:
            escondido_4_4[posicao] = False
            escondido_4_4[marca] = False
            estado['marca'] = None

# def digitar_username(x,y):
#     global username
#     username = turtle.textinput("Username", "Digite seu username: ")
#     if username=="":
#         username= None


def init():
    global username
    # turtle.up()
    # turtle.goto(0,80)
    # turtle.write("Bem vindo ao\njogo da memoria", font=('Arial', 18, 'normal'), align="Center")
    # turtle.teleport(0,40)
    # turtle.write("Digite seu username:", font=('Arial', 14, 'normal'), align="Center")
    # turtle.teleport(0,30)
    # turtle.showturtle()
    # turtle.onclick(digitar_username)
    turtle.clear()
    turtle.up()
    turtle.goto(0, 120)
    turtle.write("JOGO DA MEMÓRIA", align="center", font=("Arial", 22, "bold"))

    turtle.goto(0, 80)
    turtle.write("Clique para digitar seu username", align="center", font=("Arial", 14, "normal"))
    turtle.goto(0, 60)
    
    t_username.teleport(0,60)
    t_username.write(f"[ {configuracoes['username'] if configuracoes["username"]!=None else ""} ]", align="center", font=("Arial", 14, "bold"))
    t_username.onclick(digitar_username)
    turtle.goto(0, 40)
    turtle.showturtle()
    turtle.onclick(digitar_username)
    if configuracoes["username"] is not None:
        teste_de_validcao = Score("test.json")
        if teste_de_validcao.existe_usuario(configuracoes["username"]):
            mensagens_avisos.clear()
            mensagens_avisos.write("Ja existe um usuario com esse nome!", font=('Arial', 14, 'normal'), align="Center")
            t_username.clear()
            configuracoes["username"] = None
            turtle.update()

    turtle.goto(-100, 10)
    turtle.write("1 Jogador", align="center", font=("Arial", 14, "normal"))
    turtle.showturtle()
    mudar_p1.onclick(mudar_modo_de_jogador_p1)
    turtle.goto(100, 10)

    turtle.write("2 Jogadores", align="center", font=("Arial", 14, "normal"))
    mudar_p2.onclick(mudar_modo_de_jogador_p2)
    turtle.goto(-100, -40)
    turtle.write("Fácil", align="center", font=("Arial", 14, "normal"))
    mudar_facil.onclick(mudar_difi_facil)
    turtle.goto(100, -40)
    turtle.write("Difícil", align="center", font=("Arial", 14, "normal"))
    mudar_difi.onclick(mudar_difi_difi)

    turtle.goto(0, -90)
    turtle.write("INICIAR JOGO", align="center", font=("Arial", 16, "bold"))
    turtle.onclick(init_game)
    # Associação dos cliques
    # turtle.onclick(digitar_username, 1)


def digitar_username(x,y):
    configuracoes["username"] = turtle.textinput("Username", "Digite seu username: ")
    turtle.clear()
    turtle.update()
    t_username.clear()
    if configuracoes["username"]=="":
        configuracoes["username"] = None
    else:
        t_username.clear()


def init_game(x,y):
    if configuracoes["username"] and configuracoes["dificuldade"]!=None:
        game["state"] = True
        turtle.onscreenclick(toque)
    else:
        mensagens_avisos.clear()
        mensagens_avisos.write("complete todas as configuraçoes", font=('Arial', 14, 'normal'), align="Center")
        turtle.update()

def mudar_modo_de_jogador_p1(x,y):
    configuracoes["p2"] = False
    print("Modo de jogo alterado para \033[0;34m1 player\033[m")
    return

def mudar_modo_de_jogador_p2(x,y):
    configuracoes["p2"] = True
    print("Modo de jogo alterado para \033[0;33m2 players\033[m")
    return

def mudar_difi_facil(x,y):
    configuracoes["dificuldade"] = "facil"
    print("Dificuldade alterada para \033[0;32mfacil\033[m")
    return
def mudar_difi_difi(x,y):
    configuracoes["dificuldade"] = "dificil"
    print("Dificuldade alterada para \033[0;31mdificil\033[m")
    return
def desenhar():
    """Desenha a imagem e as peças."""
    global game
    if game['state']:
        for n in turtle.turtles():
            n.clear()
            n.hideturtle()
        turtle.clear()
        turtle.goto(0, 0)
        turtle.shape(carro)
        turtle.stamp()
        global toques
        if configuracoes["dificuldade"]=="facil":
            for contador in range(16):
                if escondido_4_4[contador]:
                    x, y = coordenadas_4(contador)
                    quadrado_4(x, y)
        else:
            for contador in range(64):
                if escondido[contador]:
                    x, y = coordenadas(contador)
                    quadrado(x, y)
        marca = estado['marca']
        if marca is not None and (escondido[marca] if configuracoes["dificuldade"]=="dificil" else escondido_4_4[marca]):
            x, y = coordenadas(marca) if configuracoes["dificuldade"]=="dificil" else coordenadas_4(marca)
            turtle.up()
            turtle.goto(x + 2, y)
            turtle.color('black')
            turtle.write(letras(pecas_4_4[marca]) if configuracoes["dificuldade"]=="facil" else pecas[marca], font=('Arial', 30, 'normal'))
        turtle.update()
        turtle.ontimer(desenhar, 100)
    else:
        init()
        turtle.update()
        turtle.ontimer(desenhar, 100)

def game_over():
    turtle.clear()
    turtle.goto(-60,0)
    p1 = Score("test.json")
    p1.add_user({"nome": username, "score": toques})
    turtle.write("Acabou", font=('Arial', 30, 'normal'))
random.shuffle(pecas)

turtle.setup(420, 420, 370, 0)
turtle.addshape(carro)
turtle.hideturtle()
turtle.tracer(False)

# TODO associar o clique do mouse à função toque
"""
Toque associado ao fim da função init apos o ususario digitar o username para não houver
bugs de contagem e mostrar peças antes do tabuleiro
"""
# turtle.onscreenclick(toque)
desenhar()
turtle.mainloop()