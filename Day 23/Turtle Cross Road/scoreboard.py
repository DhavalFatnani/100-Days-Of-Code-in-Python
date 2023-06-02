from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.display_scoreboard()

    def display_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 15, "bold"))

    def level_up(self):
        self.level += 1
        self.display_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align="center", font=("Courier", 40, "italic"))
