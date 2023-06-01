from turtle import Turtle, Screen

miku = Turtle()
screen = Screen()
speed = 10


def move_forward():
    miku.forward(speed)


def move_backward():
    miku.backward(speed)


def move_left():
    miku.lt(20)


def move_right():
    miku.rt(20)


def increase_speed():
    global speed
    speed += 10


def decrease_speed():
    global speed
    speed -= 10


def clear_all():
    screen.clear()
    miku.penup()
    miku.home()
    miku.pendown()


screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=move_left)
screen.onkey(key="D", fun=move_right)
screen.onkey(key="C", fun=clear_all)
screen.onkey(key="+", fun=increase_speed)
screen.onkey(key="-", fun=decrease_speed)
screen.exitonclick()
