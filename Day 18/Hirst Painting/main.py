from turtle import Turtle, Screen, colormode
import random
# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# extracted_colors = []
# for color in colors:
#     extracted_colors.append(tuple(color.rgb))
# print(extracted_colors)
colors_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
colormode(255)
miku = Turtle()
screen = Screen()
miku.penup()
miku.setpos(-280, -230)
_y = 50
y = -230
for i in range(10):
    for j in range(10):
        miku.dot(15, random.choice(colors_list))
        miku.fd(50)
        y = miku.ycor()
    miku.setpos(-280, y+_y)

screen.exitonclick()
