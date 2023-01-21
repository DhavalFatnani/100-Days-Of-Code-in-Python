# import random
#
# random_integer = random.randint(1,10)
# print(random_integer)
#
# random_float = random.random()
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your Love Score is {love_score}")

states_of_india = ["Gujarat", "Maharashtra", "Punjab","Kerala","Tamil Nadu", "Goa", "Madhya Pradesh", "Rajasthan"]
x = "Sikkim"
states_of_india.append(x)
states_of_india.extend(["Bihar","Andhra Pradesh", "Uttar Pradesh"])

print(states_of_india)

fruits = ["Strawberries" "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)