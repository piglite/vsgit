import turtle
from turtle import Turtle,TurtleScreen,Screen
pen = Turtle()
screen = turtle.getscreen()
screen.onkey(lambda:pen.fd(100),'Up')
screen.listen()
turtle.done()