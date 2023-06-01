from turtle import Turtle

STYLE = ('Courier', 18, 'italic')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.scoreboard()
        self.hideturtle()

    def scoreboard(self):
        self.write(f"Score: {self.score}", font=STYLE, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER!", font=STYLE, align=ALIGNMENT)
