from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter its color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []

x = -230
y = 100
_y = 30
miku = Turtle()
miku.penup()
miku.goto(x=230, y=150)
miku.seth(270)
miku.pendown()
miku.forward(275)
miku.hideturtle()

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y -= _y
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You're Correct! You Won, The Winning turtle is {winning_turtle}.")
            else:
                print(f"You're Wrong! You Lose, The Winning turtle is {winning_turtle}.")
        randomDistance = random.randint(0, 10)
        turtle.forward(randomDistance)

screen.exitonclick()
