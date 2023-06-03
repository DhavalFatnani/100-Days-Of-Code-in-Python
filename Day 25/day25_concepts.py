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

data_dict = df.to_dict()

# temperatures = list(df["temp"])
temperatures = df["temp"]
temp_list = temperatures.to_list()
# avg_temp = sum(temp_list) / len(temp_list)
avg_temp = temperatures.mean()
max_temp = temperatures.max()

# print(df)
# print(temperatures)
# print(data_dict)
# print(temp_list)
# print(avg_temp)
# print(max_temp)

# Get Data in Columns
conditions = df["condition"]
_conditions = df.condition

# Get Data in Rows
# print(df[df.day == "Monday"])

# Get Row having Max Temperature
# print(df[df.temp == df.temp.max()])

monday = df[df.day == "Monday"]
monday_temp_C = int(monday.temp)
# print(monday.condition)
# Temp from Celsius to Fahrenheit
monday_temp_F = (monday_temp_C * (9/5))+32
# print(monday_temp_F)

# Creating a DataFrame from Scratch
data_dikt = {
    "students": ["Dev", "Sahil", "Neil"],
    "scores": [56, 76, 64]
}

dff = pd.DataFrame(data_dikt)
# print(dff)
# dff.to_csv("new_data.csv")
