import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("India States Game")
screen.setup(width=800, height=900, starty=20)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("Indian_States.csv")
all_states = df.States.to_list()

guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"Guess the States{len(guessed_states)}/{len(all_states)}",
                                    prompt="Enter Name of any State: ").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missingStates = pd.DataFrame(missing_states)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        record = df[df["States"] == answer_state]
        t.goto(int(record.x), int(record.y))
        t.write(f"{answer_state}", align="center", font=("Courier", 8, "bold"))

turtle.mainloop()
