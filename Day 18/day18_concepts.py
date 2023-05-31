from turtle import Turtle as T, Screen as S, colormode
import numpy as np

miko = T()
# jayo = Turtle()
screen = S()
miko.shape("turtle")
# jayo.shape("turtle")
# miko.fd(100)
# jayo.setheading(180)
# jayo.fd(100)
# print(miko.distance(jayo))

# CHALLENGE 1 - Draw a SQUARE
"""WAY 1"""
# miko.fd(100)
# miko.lt(90)
# miko.fd(100)
# miko.lt(90)
# miko.fd(100)
# miko.lt(90)
# miko.fd(100)
# miko.lt(90)
"""WAY 2"""
# for _ in range(0, 4):
#     miko.fd(100)
#     miko.lt(90)

# Challenge 2 - Draw a Dashed Line
# for _ in range(15):
#     miko.fd(10)
#     miko.penup()
#     miko.fd(10)
#     miko.pendown()

# Challenge 3 - Draw a Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon and Decagon
side = 100
shape = 3
colormode(255)
for _ in range(8):
    random_color = tuple(np.random.choice(range(255), size=3))
    miko.color(random_color)
    angle = 360 / shape
    for n in range(shape):
        miko.fd(side)
        miko.left(angle)
    shape += 1

screen.exitonclick()
