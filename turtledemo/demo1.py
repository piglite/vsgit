import turtle
from turtle import Turtle
pen = Turtle()
pen.speed(0)
pen.left(60)
pen.width(6)
pen.color('green','purple')
pen.begin_fill()
for x in range(10):
    for y in range(2):
        pen.fd(60)
        pen.left(60)
        pen.fd(60)
        pen.left(120)
    pen.left(36)
pen.end_fill()
pen.width(5)
pen.color('aqua')
for x in range(10):
    for y in range(2):
        pen.fd(55)
        pen.left(60)
        pen.fd(55)
        pen.left(120)
    pen.left(36)
turtle.done()