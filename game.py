from turtle import *
import random

tilesx = [-150, -100, -50, 0, 50, 100, 150]
tilesy = [-150, -100, -50, 0, 50, 100, 150]


player = {'ix': 3, 'iy': 1}

state = {
    'score': 0,
    'posicaox': tilesx[player['ix']],
    'posicaoy': tilesy[player['iy']]
}


setup(width=400, height=400)
tracer(False)



turtle_player = Turtle()
turtle_player.shape("square")
turtle_player.color("black")
turtle_player.penup()
turtle_player.speed(0)
turtle_player.goto(state['posicaox'], state['posicaoy'])


def move(direcao):
    if direcao == 'direita' and player['ix'] < len(tilesx) - 1:
        player['ix'] += 1
    elif direcao == 'esquerda' and player['ix'] > 0:
        player['ix'] -= 1
    elif direcao == 'cima' and player['iy'] < len(tilesy) - 1:
        player['iy'] += 1
    elif direcao == 'baixo' and player['iy'] > 0:
        player['iy'] -= 1

    state['posicaox'] = tilesx[player['ix']]
    state['posicaoy'] = tilesy[player['iy']]

    turtle_player.goto(state['posicaox'], state['posicaoy'])
    update()


listen()
onkeypress(lambda: move('direita'), 'Right')
onkeypress(lambda: move('esquerda'), 'Left')
onkeypress(lambda: move('cima'), 'Up')
onkeypress(lambda: move('baixo'), 'Down')



NUM_INIMIGOS = 6
inimigos = []

for _ in range(NUM_INIMIGOS):
    t = Turtle()
    t.shape("square")
    t.color("red")
    t.penup()
    t.speed(0)

    inimigos.append({
        'turtle': t,
        'ix': random.randint(0, len(tilesx) - 1),
        'iy': len(tilesy) - 1
    })


def reload():
    for inimigo in inimigos:
        inimigo['iy'] -= 1

        if inimigo['iy'] < 0:
            inimigo['iy'] = len(tilesy) - 1
            inimigo['ix'] = random.randint(0, len(tilesx) - 1)
            state['score'] += 1

        x = tilesx[inimigo['ix']]
        y = tilesy[inimigo['iy']]
        inimigo['turtle'].goto(x, y)

        # evento do game over
        if inimigo['ix'] == player['ix'] and inimigo['iy'] == player['iy']:
            game_over()
            return

    update()
    ontimer(reload, 250)


def game_over():
    clear()
    penup()
    goto(0, 0)
    color("green")
    write("GAME OVER", align="center", font=("Arial", 24, "bold"))


reload()
done()