from turtle import Turtle

ALIGNMENT = "center"
STYLE = ("Courier", 60, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_display()

    def score_display(self):
        self.clear()
        self.goto(-80, 220)
        self.write(self.l_score, align=ALIGNMENT, font=STYLE)
        self.goto(80, 220)
        self.write(self.r_score, align=ALIGNMENT, font=STYLE)

    def l_scored(self):
        self.l_score += 1
        self.score_display()

    def r_scored(self):
        self.r_score += 1
        self.score_display()

