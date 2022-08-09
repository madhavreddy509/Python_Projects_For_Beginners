from turtle import *
import turtle
turt=turtle.Turtle()
import math
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("This is OWASP!")
t = turtle.Turtle()


def CAP(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.pensize(2)
    t.speed(10)


def circle(r, color):
    x_point = 0
    y_pont = -r
    CAP(x_point, y_pont)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def star(r, color):
    CAP(0, 0)
    t.pencolor(color)
    t.setheading(162)
    t.forward(r)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(math.cos(math.radians(18)) * 2 * r)  # 2cos18°*r
        t.right(144)
    t.end_fill()
    t.hideturtle()
circle(288, 'crimson')
circle(234, 'snow')
circle(174, 'crimson')
circle(114, 'blue')
star(114, 'snow')
