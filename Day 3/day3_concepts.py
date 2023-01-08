print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is you age?"))
    if age < 12:
        print("Please pay Rs.50")
    elif age <= 18:
        print("Please pay Rs.80")
    else:
        print("Please pay Rs.140")
else:
    print("Sorry, you have to grow taller before you can ride.")