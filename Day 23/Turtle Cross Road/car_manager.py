from turtle import Turtle, colormode
import random
import numpy as np

colormode(255)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(tuple(np.random.choice(range(255), size=3)))
            new_car.goto(300, random.randint(-200, 200))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        print(self.car_speed)
