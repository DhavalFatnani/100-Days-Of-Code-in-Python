from turtle import Turtle, Screen
from prettytable import PrettyTable

chunnu = Turtle()
print(chunnu)
chunnu.shape("turtle")
chunnu.color("red")
chunnu.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
