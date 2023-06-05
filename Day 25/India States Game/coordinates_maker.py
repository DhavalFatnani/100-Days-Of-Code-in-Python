import turtle

import pandas as pd
from turtle import Screen

co_ordinates = []

screen = Screen()
screen.title("India States Game")
screen.setup(width=800, height=900, starty=20)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
#
# sdf = pd.read_csv("Indian_States.csv")
# states = sdf["States"]
# Final = pd.read_csv("co.csv")
# Final.insert(0, 'States', states)
# Final.to_csv("Indian_States.csv")

# df = pd.read_csv("out.csv")
# isf = pd.read_csv("India States-UTs.csv")
#
# df["States"] = isf["State"]
# x = df.assign()
# col = x.pop('States')
