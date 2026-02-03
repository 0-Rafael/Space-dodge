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
3. Detectar quando todas as peças forem reveladas. --concluido
4. Centralizar peças de um único dígito. --concluido
5. Usar letras em vez de números. --concluido
6. Identificar jogador em cada rodada. Qual o nome do jogador que vai iniciar um jogo? --concluido
7. Armazenar jogador e suas pontuações em arquivo. Ao final do jogo, armazenar em arquivo
o nome do jogador que jogou e sua respectiva pontuação na rodada. --concluido
Deve ser armazenado a quantidade de cliques do jogador até resolver todo o tabuleiro. --concluido
8. Listar jogadores e suas pontuações. Exibir no terminal uma lista de todos os jogadores
que jogaram o jogo com suas respectivas pontuações. --conluido
"""

import turtle
import random
from freegames import path
from main import Score

cont = 2;
carro = path('car.gif')
pecas = list(range(32)) * 2
estado = {'marca': None, 'segunda': False, "bloqueado": False}
escondido = [True] * 64
toques = 0
game = {"state": False}
pecas_4_4 = list(range(8)) * 2
escondido_4_4 = [True] * 16
username = None
modo_de_jogo = None
dificuldade = None
p1 = None
configuracoes = {"username": None, "dificuldade": None, "p1": True, "p2": False, "usernamep2": None}

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

jogadores = {"p1": {
    "score":0,
    "toques": 0,
    "nome": configuracoes["username"]
},
    "p2": {
        "score": 0,
        "toques": 0,
        "nome": configuracoes["usernamep2"]
    }
}
jogador_atual = "p1"

score = Score("test.json")
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
    global toques, jogador_atual
    if estado["bloqueado"]:
        """Evitar clique durante a transição"""
        return
    posicao = indice(x, y) if configuracoes["dificuldade"]=="facil" else indice_4(x,y)
    marca = estado['marca']
    toques+=1
    jogadores[jogador_atual]["toques"]+=1
    if posicao==estado["marca"]:
        return
    if marca is None:
        estado["marca"] = posicao
        return
    estado["segunda"] = posicao
    if configuracoes["dificuldade"]=="facil":
        acerto = pecas_4_4[estado["segunda"]]==pecas_4_4[marca]
    else:
        acerto = pecas[estado["segunda"]]==pecas[marca]
    if acerto:
        if configuracoes["dificuldade"] == "facil":
            escondido_4_4[estado["segunda"]] = False
            escondido_4_4[marca] = False
        else:
            escondido[estado["segunda"]] = False
            escondido[marca] = False
        estado["marca"]=None
        estado["segunda"] = None
        jogadores[jogador_atual]["toques"]+=1
    else:
        if configuracoes["p2"]:
            estado["bloqueado"] = True
            turtle.ontimer(mostrar_pecas_devagar, 700)
            if jogador_atual=="p1":
                jogador_atual="p2"
            else:
                jogador_atual="p1"
        else:
            estado["bloqueado"] = True
            turtle.ontimer(mostrar_pecas_devagar, 700)

def mostrar_pecas_devagar():
    """Função utilizada para fazer delay para que a segunda peça possa ser mostrada"""
    estado["marca"] = None
    estado["segunda"] = None
    estado["bloqueado"] = False

def init():
    global username
    turtle.clear()
    turtle.up()
    turtle.goto(0, 120)
    turtle.write("JOGO DA MEMÓRIA", align="center", font=("Arial", 22, "bold"))

    turtle.goto(0, 80)
    turtle.write("Clique para digitar seu username", align="center", font=("Arial", 14, "normal"))
    turtle.goto(0, 60)
    
    t_username.teleport(0,60)

    """Verificação para diferença na aparencia do username"""
    if configuracoes["p2"]==False:
        t_username.clear()
        t_username.write(f"[ {configuracoes['username'] if configuracoes["username"]!=None else ""} ]", align="center", font=("Arial", 14, "bold"))
    else:
        t_username.clear()
        t_username.write(f"[ {configuracoes['username'] if configuracoes["username"]!=None else "" } | {configuracoes['usernamep2'] if configuracoes['usernamep2']!= None else ""} ]", align="center", font=("Arial", 14, "bold"))
    t_username.onclick(digitar_username)
    turtle.goto(0, 40)
    turtle.showturtle()
    turtle.onclick(digitar_username)

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


def digitar_username(x,y):
    configuracoes["username"] = turtle.textinput("Username", "Digite seu username: ")
    turtle.clear()
    turtle.update()
    t_username.clear()
    if configuracoes["username"]=="":
        configuracoes["username"] = None
    else:
        jogadores["p1"]["nome"] = configuracoes["username"]
        t_username.clear()
    if configuracoes["dificuldade"]==None:
        if configuracoes["p2"]:
            if configuracoes["username"]==configuracoes["usernamep2"]:
                mensagens_avisos.clear()
                mensagens_avisos.write(
                "Players não podem ter o mesmo nome",
                font=('Arial', 14, 'normal'),
                align="Center"
                )
                configuracoes["username"]= None
                return
        if score.existe_nome(configuracoes["username"]):
            mensagens_avisos.clear()
            mensagens_avisos.write(
                "Já existe um usuário com esse nome!",
                font=('Arial', 14, 'normal'),
                align="Center"
            )
            configuracoes["username"] = None
            return
                
        else:
            mensagens_avisos.clear()
    else:
        mensagens_avisos.clear()
        validar_usuario_completo("username")
def validar_usuario_completo(player):
    if configuracoes[player] is None:
        return

    if score.existe_usuario(
        configuracoes[player],
        configuracoes["dificuldade"]
    ):
        mensagens_avisos.clear()
        mensagens_avisos.write(
            "Usuário já jogou nessa dificuldade!",
            font=('Arial', 14, 'normal'),
            align="Center"
        )
        configuracoes[player]= None
        t_username.clear()
def digitar_username_p2():
    configuracoes["usernamep2"] = turtle.textinput("Username", "Digite o username do Player 2: ")
    turtle.clear()
    turtle.update()
    t_username.clear()
    if configuracoes["usernamep2"]=="":
        configuracoes["usernamep2"] = None
    else:
        jogadores["p2"]["nome"] = configuracoes["usernamep2"]
        t_username.clear()
    if configuracoes["dificuldade"]==None:
        if configuracoes["username"]==configuracoes["usernamep2"]:
            mensagens_avisos.clear()
            mensagens_avisos.write(
            "Players não podem ter o mesmo nome",
            font=('Arial', 14, 'normal'),
            align="Center"
            )
            configuracoes["usernamep2"]= None
            return
        if score.existe_nome(configuracoes["usernamep2"]):
            mensagens_avisos.clear()
            mensagens_avisos.write(
                "Já existe um usuário com esse nome!",
                font=('Arial', 14, 'normal'),
                align="Center"
            )
            configuracoes["usernamep2"] = None
            return
        else:
            mensagens_avisos.clear()
    else:
        mensagens_avisos.clear()
        validar_usuario_completo("usernamep2")
    

def init_game(x,y):
    global estado,toques,jogador_atual
    estado = {"marca": None, "segunda": None, "bloqueado": False}
    toques = 0
    jogador_atual = "p1"
    if not configuracoes["p2"]:
        if configuracoes["username"] and configuracoes["dificuldade"]!=None:
            game["state"] = True
            turtle.onscreenclick(None)
            turtle.onscreenclick(toque)
        else:
            mensagens_avisos.clear()
            mensagens_avisos.write("complete todas as configuraçoes", font=('Arial', 14, 'normal'), align="Center")
            turtle.update()
    else:
        if configuracoes["username"] and configuracoes["dificuldade"]!=None and configuracoes["usernamep2"]:
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
    digitar_username_p2()
    return

def mudar_difi_facil(x,y):
    configuracoes["dificuldade"] = "facil"
    validar_usuario_completo("username")
    validar_usuario_completo("usernamep2")
    print("Dificuldade alterada para \033[0;32mfacil\033[m")
    return
def mudar_difi_difi(x,y):
    configuracoes["dificuldade"] = "dificil"
    validar_usuario_completo("username")
    validar_usuario_completo("usernamep2")
    print("Dificuldade alterada para \033[0;31mdificil\033[m")
    return


def desenhar():
    def playercolor(player):
        return 'blue' if player == "p1" else 'red'

    global game
    if game['state']:
        for n in turtle.turtles():
            n.clear()
            n.hideturtle()
        turtle.clear()
        turtle.goto(0, 0)
        turtle.shape(carro)
        turtle.stamp()

        # Desenha os quadrados escondidos (tampas)
        if configuracoes["dificuldade"] == "facil":
            for contador in range(16):
                if escondido_4_4[contador]:
                    x, y = coordenadas_4(contador)
                    quadrado_4(x, y)
        else:
            for contador in range(64):
                if escondido[contador]:
                    x, y = coordenadas(contador)
                    quadrado(x, y)  # Nota: mantive (x, y) padrão aqui

        # Desenha o conteúdo das peças reveladas
        for clique in ["marca", "segunda"]:
            pos = estado[clique]
            if pos is not None:
                if configuracoes["dificuldade"] == "facil":
                    if escondido_4_4[pos]:
                        x, y = coordenadas_4(pos)
                        turtle.up()
                        # Quadrado 4x4 tem 100px. Metade = 50.
                        # Y + 25 ajusta a altura da fonte para ficar visualmente no meio
                        turtle.goto(x + 50, y + 25)
                        turtle.write(letras(pecas_4_4[pos]), align="center", font=('Arial', 40, 'bold'))
                else:
                    if escondido[pos]:
                        x, y = coordenadas(pos)
                        turtle.up()
                        # Quadrado 8x8 tem 50px. Metade = 25.
                        # Y + 10 ajusta a base da fonte para não ficar colada no chão
                        turtle.goto(x + 25, y + 10)
                        turtle.write(pecas[pos], align="center", font=('Arial', 20, 'bold'))

        # Verifica fim de jogo
        if (configuracoes["dificuldade"] == "facil" and not any(escondido_4_4)) or (
                configuracoes["dificuldade"] != "facil" and not any(escondido)):
            game["state"] = False
            game_over()
            return

        # Mostra de quem é a vez
        if configuracoes["p2"]:
            msg = turtle.Turtle()
            msg.up()
            msg.goto(0, 170)
            msg.color(playercolor(jogador_atual))
            msg.write(f"Vez de: {jogadores[jogador_atual]['nome']}", align="center", font=("Arial", 14, "bold"))

        turtle.update()
        turtle.ontimer(desenhar, 100)
    else:
        init()
        turtle.update()
        turtle.ontimer(desenhar, 100)

def game_over():
    turtle.clear()
    turtle.goto(-120,50)
    if not configuracoes["p2"]:
        score.add_user({"nome": configuracoes["username"], "score": jogadores["p1"]["toques"], "dificuldade": configuracoes["dificuldade"]})
    else:
        score.add_user({"nome": configuracoes["username"], "score": jogadores["p1"]["toques"], "dificuldade": configuracoes["dificuldade"]})
        score.add_user({"nome": configuracoes["usernamep2"], "score": jogadores["p2"]["toques"], "dificuldade": configuracoes["dificuldade"]})
    turtle.write("FIM DE JOGO", font=('Arial', 30, 'normal'))
    ranking = turtle.Turtle()
    ranking.teleport(-160,-50)
    ranking.showturtle()
    ranking.write("ver o ranking", font=('Arial', 16, 'normal'))
    mudar_p1.teleport(-100,20)
    if not configuracoes["p2"]:
        mudar_p1.write(f"Score - {jogadores['p1']["nome"]}: {jogadores['p1']["toques"]} toques", font=('Arial', 12, 'normal'))
    else:
        mudar_p1.write(f"Score - {jogadores['p1']["nome"]}: {jogadores['p1']["toques"]} toques\nScore - {jogadores['p2']["nome"]}: {jogadores['p2']["toques"]} toques", font=('Arial', 12, 'normal'))
    ranking.onclick(ver_ranking)
    mensagens_avisos.showturtle()
    mensagens_avisos.teleport(40,-50)
    mensagens_avisos.pencolor("black")
    mensagens_avisos.write("ver sua posição", font=('Arial', 16, 'normal'))
    mensagens_avisos.onclick(mostrar_posicao)
    turtle.update()
    turtle.ontimer(game_over, 100)
def ver_ranking(x,y):
    score.mostra_scores()

def mostrar_posicao(x,y):
    if not configuracoes["p2"]:
        score.mostra_posicao(configuracoes["username"], jogadores["p1"]["toques"], configuracoes["dificuldade"])
    else:
        score.mostra_posicao(configuracoes["username"], jogadores["p1"]["toques"], configuracoes["dificuldade"])
        score.mostra_posicao(configuracoes["usernamep2"], jogadores["p2"]["toques"], configuracoes["dificuldade"])
random.shuffle(pecas)
random.shuffle(pecas_4_4)
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