#Paint.py
#Carla Perez, Aranza Garcia
#Juego pintando, dibuja diferentes figuras de diferentes colores y tamaños 
from turtle import *
from freegames import vector
import math


def line(start, end):
    #Dibuja una linea del punto inicial hasta al final
    up()
    goto(start.x, start.y) #place where it starts
    down()
    goto(end.x, end.y) #place where it ends

def square(start, end):
    #Dibuja un cuadrado desde el punto de inicio hasta el punto final
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()
def Drawcircle(start, end):
    #Dibuja un circulo tomando en cuenta el punto inicial y final
    up()
    goto(start.x, start.y)
    down()
    Distance=abs(end-start)
    circle(Distance)

def rectangle(start, end):
    #Dibuja un rectángulo con los puntos iniciales y finales
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #arriba
    forward(2*end.x - start.x)
    #derecha
    right(90)
    forward(end.x - start.x)
    #base
    right(90)
    forward(2*end.x - start.x)
    #izquierda
    right(90)
    forward(end.x - start.x)

    end_fill()

    pass  # TODO

def triangle(start, end):
    #Dibuja un triangulo con los puntos iniciales y finales
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    # base
    forward(end.x - start.x) 
    left(120) #angulo del triangulo
    #lado 1
    forward(end.x - start.x) 
    left(120)
    #lado 2
    forward(end.x - start.x) 
    end_fill()
    pass  # TODO

def tap(x, y):
    #Guarda los puntos de inicio y los puntos finales
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    #Almacena los valores
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0) #dimensiones de la pantalla
onscreenclick(tap) 
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's') 
onkey(lambda: store('shape', drawcircle), 'c')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', Drawcircle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
