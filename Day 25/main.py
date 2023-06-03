# with open("weather_data.csv") as weather_data:
#     data = weather_data.read()
#     data = data.split("\n")
# print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

df = pd.read_csv("weather_data.csv")
temperatures = list(df["temp"])
print(df)
print(temperatures)
