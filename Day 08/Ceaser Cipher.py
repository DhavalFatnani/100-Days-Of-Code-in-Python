alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(start_text, shift_amount, direction_of_conversion):
    end_text = ""
    if direction_of_conversion == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position >= 26:
                new_position -= 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction_of_conversion}d text is {end_text}")

from caesar_art import logo
print(logo)

restart = True
while restart:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        shift %= 26
        caesar(start_text=text, shift_amount=shift, direction_of_conversion=direction)
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
        if restart == 'no':
            print("GoodBye")
            restart = False