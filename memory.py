"""Memória, jogo de quebra-cabeça de pares.

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo.

Desafios:

1. Contar e imprimir quantos cliques ocorrem.
2. Reduzir o número de peças para um tabuleiro 4x4.
3. Detectar quando todas as peças forem reveladas.
4. Centralizar peças de um único dígito.
5. Usar letras em vez de números.
6. Identificar jogador em cada rodada. Qual o nome do jogador que vai iniciar um jogo?
7. Armazenar jogador e suas pontuações em arquivo. Ao final do jogo, armazenar em arquivo
o nome do jogador que jogou e sua respectiva pontuação na rodada. 
Deve ser armazenado a quantidade de cliques do jogador até resolver todo o tabuleiro.
8. Listar jogadores e suas pontuações. Exibir no terminal uma lista de todos os jogadores
que jogaram o jogo com suas respectivas pontuações.
"""

import turtle
import random
from time import sleep
from freegames import path
from main import Score


carro = path('car.gif')
pecas = list(range(8)) * 2
estado = {'marca': None}
escondido = [True] * 16
toques = 0
game = {"state": False}
pecas_4_4 = list(range(8)) * 2
escondido_4_4 = [True] * 16
username = ""
def letras(ind):
    letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    return letra[ind]
def quadrado(x, y):
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

def quadrado_4(x,y):
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

def coordenadas(contador):
    """Converte o índice da peça em coordenadas (x, y)."""
    return (contador % 4) * 100 - 200 , (contador // 4) * 100 - 200

def toque(x, y):
    """Atualiza a marcação e as peças escondidas com base no clique."""
    posicao = indice(x, y)
    marca = estado['marca']
    global toques
    toques+=1
    print(toques)
    if marca is None or marca == posicao or pecas[marca] != pecas[posicao]:
        estado['marca'] = posicao
    else:
        escondido[posicao] = False
        escondido[marca] = False
        estado['marca'] = None

def digitar_username(x,y):
    global username
    username = turtle.textinput("Username", "Digite seu username: ")
    if username=="":
        username= None


def init():
    # global username
    # turtle.up()
    # turtle.goto(0,80)
    # turtle.write("Bem vindo ao\njogo da memoria", font=('Arial', 18, 'normal'), align="Center")
    # turtle.teleport(0,40)
    # turtle.write("Digite seu username:", font=('Arial', 14, 'normal'), align="Center")
    # turtle.teleport(0,30)
    # turtle.showturtle()
    # turtle.onclick(digitar_username)
    # if username is not None:
    #     teste_de_validcao = Score("test.json")
    #     if not teste_de_validcao.existe_usuario(username):
    #         game['state'] = True
    #         turtle.update()
    #         turtle.hideturtle()
    #         turtle.onscreenclick(toque)
    #         return
    #     else:
    #         turtle.teleport(0,20)
    #         turtle.pencolor("red")
    #         turtle.write("Ja existe um usuario com esse nome!", font=('Arial', 14, 'normal'), align="Center")
    #         turtle.teleport(0,10)
    #         turtle.pencolor("black")
    turtle.clear()
    turtle.up()
    turtle.goto(0, 120)
    turtle.write("JOGO DA MEMÓRIA", align="center", font=("Arial", 22, "bold"))

    turtle.goto(0, 80)
    turtle.write("Clique para digitar seu username", align="center", font=("Arial", 14, "normal"))
    turtle.goto(0, 60)
    turtle.write("[ USERNAME ]", align="center", font=("Arial", 14, "bold"))

    turtle.goto(-100, 10)
    turtle.write("1 Jogador", align="center", font=("Arial", 14, "normal"))

    turtle.goto(100, 10)
    turtle.write("2 Jogadores", align="center", font=("Arial", 14, "normal"))

    turtle.goto(-100, -40)
    turtle.write("Fácil", align="center", font=("Arial", 14, "normal"))

    turtle.goto(100, -40)
    turtle.write("Difícil", align="center", font=("Arial", 14, "normal"))

    turtle.goto(0, -90)
    turtle.write("INICIAR JOGO", align="center", font=("Arial", 16, "bold"))

    # Associação dos cliques
    turtle.onclick(digitar_username, 1)
def desenhar():
    """Desenha a imagem e as peças."""
    global game
    if game['state']:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.shape(carro)
        turtle.stamp()
        global toques
        for contador in range(16):
            if escondido[contador]:
                x, y = coordenadas(contador)
                quadrado(x, y)
        if toques>=12:
            return game_over()
        marca = estado['marca']
        if marca is not None and escondido[marca]:
            x, y = coordenadas(marca)
            turtle.up()
            turtle.goto(x + 2, y)
            turtle.color('black')
            turtle.write(letras(pecas[marca]), font=('Arial', 30, 'normal'))
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