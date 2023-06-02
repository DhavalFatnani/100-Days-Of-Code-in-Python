from turtle import Turtle

STYLE = ('Courier', 18, 'italic')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.color("white")
        self.goto(-250, 250)
        self.pendown()
        self.forward(300)
        self.right(300)
        self.right(300)
        self.right(300)
        self.penup()
        self.goto(0, 270)
        self.scoreboard()
        self.hideturtle()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, HighScore: {self.highscore}", font=STYLE, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER!", font=STYLE, align=ALIGNMENT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.scoreboard()
