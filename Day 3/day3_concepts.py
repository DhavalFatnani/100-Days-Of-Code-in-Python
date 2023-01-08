print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is you age?"))
    if age < 12:
        bill = 50
        print("Child tickets are Rs.50")
    elif age <= 18:
        bill = 80
        print("Youth tickets are Rs.80")
    else:
        bill = 140
        print("Adults tickets are Rs.140")

    wants_photo = input("Do you want a photo taken? Y or N.")
    wants_photo = wants_photo.lower()
    if wants_photo == 'y':
        #Add 50rs. to the bill
        bill += 50

        print(f"Your final bill is rs.{bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")