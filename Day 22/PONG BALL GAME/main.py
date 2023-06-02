from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

UPPER_WALL = (0, 280)
LOWER_WALL = (0, -280)

screen = Screen()
screen.title("PONG BALL")
screen.setup(width=800, height=600, starty=20)
screen.bgcolor("black")
screen.tracer(0)

paused = False
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = ScoreBoard()


screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with Upper or Lower Wall
    if ball.ycor() > UPPER_WALL[1] or ball.ycor() < LOWER_WALL[1]:
        ball.bounce_y()

    # Detect Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Ball Out of Bounds
    # Detect R Paddle Misses
    if ball.xcor() > 340:
        ball.reset_pos()
        score.l_scored()

    # Detect L Paddle Misses
    if ball.xcor() < -340:
        ball.reset_pos()
        score.r_scored()

screen.exitonclick()
