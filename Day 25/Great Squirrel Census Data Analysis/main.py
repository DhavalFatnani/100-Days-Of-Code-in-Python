import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = df["Primary Fur Color"]
gray_squirrel_count = len(df[fur_color == "Gray"])
cinnamon_squirrel_count = len(df[fur_color == "Cinnamon"])
black_squirrel_count = len(df[fur_color == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

color_squirrel_count = pd.DataFrame(data_dict)
color_squirrel_count.to_csv("squirrel_count.csv")
