print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is you age?"))
    if age < 12:
        bill = 50
        print(f"Child tickets are Rs.{bill}")
    elif age <= 18:
        bill = 80
        print(f"Youth tickets are Rs.{bill}")
    elif 45 <= age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 140
        print(f"Adults tickets are Rs.{bill}")

    wants_photo = input("Do you want a photo taken? Y or N.")
    wants_photo = wants_photo.lower()
    if wants_photo == 'y':
        # Add 50rs. to the bill
        bill += 50

        print(f"Your final bill is rs.{bill}")
    else:
        print(f"Your final bill is rs.{bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
