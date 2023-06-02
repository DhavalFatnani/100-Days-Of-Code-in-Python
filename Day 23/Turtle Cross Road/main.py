from turtle import Screen
from player import Player
from car_manager import Cars
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600, starty=20)
screen.tracer(0)

player = Player()
cars = Cars()
score = Score()

screen.listen()
screen.onkeypress(fun=player.move, key="space")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # Detect Collision between Player and Any Car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            is_game_on = False
            score.game_over()

    # On Successful Crossing
    if player.is_at_finishline():
        player.start()
        cars.level_up()
        score.level_up()

screen.exitonclick()
