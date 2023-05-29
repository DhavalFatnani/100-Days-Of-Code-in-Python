"""
Password Generator Project
Eazy Level - Order not randomised:
e.g. 4 letter, 2 symbol, 2 number = JduE&!91

Hard Level - Order of characters randomised:
e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
check_eazy = ['e', 'h']
check = input("Which do you want? Enter 'E' for Eazy and 'H' for Hard! ").lower()
password = ""
chars = []

if check == check_eazy[0]:
    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    for letter in range(0, nr_letters):
        random_letter = str(random.choice(letters))
        password += str(random_letter)
        chars.append(random_letter)

    for symbol in range(0, nr_symbols):
        random_symbol = random.choice(symbols)
        password += str(random_symbol)
        chars.append(random_symbol)

    for number in range(0, nr_numbers):
        random_number = random.choice(numbers)
        password += str(random_number)
        chars.append(random_number)
else:
    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    for letter in range(0, nr_letters):
        random_letter = random.choice(letters)
        chars.append(random_letter)

    for symbol in range(0, nr_symbols):
        random_symbol = random.choice(symbols)
        chars.append(random_symbol)

    for number in range(0, nr_numbers):
        random_number = random.choice(numbers)
        chars.append(random_number)

    updated_password = ""
    characters = random.sample(chars, len(chars))
    for character in characters:
        updated_password += character
    password = updated_password

print(f"Here is your password: {password}")
