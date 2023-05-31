from turtle import Turtle, Screen, colormode
import random
import numpy as np

miku = Turtle()
screen = Screen()
colormode(255)


def random_direction():
    directions = [0, 90, 180, 270]
    randomDirection = random.choice(directions)
    return randomDirection


def random_color():
    randomColor = tuple(np.random.choice(range(255), size=3))
    return randomColor


for _ in range(500):
    miku.color(random_color())
    miku.pensize(15)
    miku.speed(0)
    miku.forward(30)
    miku.seth(random_direction())

screen.exitonclick()
