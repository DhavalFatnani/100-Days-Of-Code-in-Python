###################### SCOPE ######################

# friends = 1
#
# def increase_friends():
#     friends = 2
#     print(f"friends inside function: {friends}")
#
# increase_friends()
# print(f"friends outside function: {friends}")

"""
LOCAL SCOPE
"""

def drink_soda():
    soda_level = "drinking"
    print(f"soda level: {soda_level}")

drink_soda()
#print(f"soda level: {soda_level}")


"""
GLOBAL SCOPE
"""
soda_status = "not drinking"
def drink_soda():
    soda_level = "drinking"
    print(f"soda level: {soda_status}")

drink_soda()
print(f"soda level: {soda_status}")

"""
In Python, there is no block scope.
i.e local scope is determined by functions, not by if,else,while,for kind of statements.
So, if I declare a variable inside a function, it is local to that function. And if I declare a variable outside a function, it is global.
If I declare a variable inside a loop or a conditional statement, In python, it is still global.
"""

game_level = 3

enemies = ["Skeleton", "Zombie", "Goblin"]
for _ in range(len(enemies)):
    if game_level < 5:
        new_enemy = enemies[0]

print(new_enemy)

# MODIFYING GLOBAL SCOPE VARIABLES

enemy = 1
def increase_enemies():
    print(f"enemies inside function: {enemy}")
    return enemy + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# GLOBAL CONSTANTS

PI = 3.14159265
URL = "https://www.google.com"
TWITTER = "https://twitter.com"
