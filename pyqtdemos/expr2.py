import turtle
from turtle import Turtle
from random import randint
from time import sleep
from threading import Thread

turtle.colormode(255)
pens = []
cs = ['yellow','pink','cyan','violet','maroon','orange']
for x in range(6):
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pens.append(pen)
    pen.color(cs[x])
    pen.up()
    pen.goto(0,100)
    pen.down()
    pen.left(x*60)

while True:
    for x in range(6):
        pen = pens[x]
        pen.begin_fill()
        pen.fd(100)
        pen.left(90)
        pen.circle(100,60)
        pen.goto(0,100)
        pen.end_fill()
        pen.right(90)
    for x in range(6):
        pen.left(1)
    sleep(0.1)

turtle.done()
