from turtle import Turtle, Screen, colormode
from random import randint

miku = Turtle()
screen = Screen()
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    randomColor = [r, g, b]
    randomColor = tuple(randomColor)
    return randomColor


miku.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        miku.color(random_color())
        miku.circle(100)
        miku.seth(miku.heading() + size_of_gap)


draw_spirograph(10)
screen.exitonclick()
