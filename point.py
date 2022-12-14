import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor('black')

Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')

rotate = 360

def drawCircles(t, size):  # type: ignore
    for _ in range(10):
        t.circle(size)
        size = size - 4

def drawSpecial(t, size, repeat):  # type: ignore
    for _ in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(Albert, 100, 10)

Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
rotate = 90

def drawCircles(t, size):  # type: ignore
    for _ in range(4):
        t.circle(size)
        size = size - 10

def drawSpecial(t, size, repeat):  # type: ignore
    for _ in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(Steve, 100, 10)

Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
rotate = 80

def drawCircles(t, size):  # type: ignore
    for _ in range(4):
        t.circle(size)
        size = size - 5

def drawSpecial(t, size, repeat):  # type: ignore
    for _ in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(Barry, 100, 10)

Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
rotate = 90

def drawCircles(t, size):  # type: ignore
    for _ in range(4):
        t.circle(size)
        size = size - 19

def drawSpecial(t, size, repeat):  # type: ignore
    for _ in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(Terry, 100, 10)

Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate = 90

def drawCircles(t, size):
    for _ in range(4):
        t.circle(size)
        size = size - 20

def drawSpecial(t, size, repeat):
    for _ in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(Will, 100, 10)

turtle.getscreen()._root.mainloop( )  # type: ignore  