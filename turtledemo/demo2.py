import turtle
from turtle import Turtle
pen = Turtle()
pen.speed(0)
turtle.colormode(255)
pen.getscreen().bgcolor('black')
pen.width(1)
pen.ht()
for y in range(10):
    pen.color(0,255-y*20,0+y*20)
    for x in range(8):
        pen.circle(y*2)
        pen.left(360/8)
for y in range(10):
    pen.color(0+y*20,0,255-y*20)
    for x in range(8):
        pen.circle(y*2+20)
        pen.left(360/8)
for y in range(10):
    pen.color(255-y*20,0+y*20,0)
    for x in range(8):
        pen.circle(y*2+40)
        pen.left(360/8)
for y in range(10):
    pen.color(0,255-y*20,0+y*20)
    for x in range(8):
        pen.circle(y*2+60)
        pen.left(360/8)

turtle.done()