from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
delay = 0.1
while is_game_on:
    screen.update()
    time.sleep(delay)
    snake.move()

    # Detect Collision between Snake and Food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
        delay -= 0.005

    # Detect Collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        delay = 0.1
        snake.reset()

    # Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            delay = 0.1
            snake.reset()


screen.exitonclick()
