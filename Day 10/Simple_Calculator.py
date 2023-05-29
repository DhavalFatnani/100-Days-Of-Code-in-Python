logo = """
 _____________________
|  _________________  |
| | CAL Cizzzzz   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ `.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ `.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# ADD FUNCTION
def add(_n1, _n2):
    return _n1 + _n2


# Subtract Function
def subtract(_n1, _n2):
    return _n1 - _n2


# Multiply Function
def multiply(_n1, _n2):
    return _n1 * _n2


# Divide Function
def divide(_n1, _n2):
    return _n1 / _n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    continue_program = True
    n1 = float(input("Enter the first number: "))
    for symbol in operators:
        print(symbol)

    while continue_program:
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number: "))
        calculate = operators[operation]
        answer = calculate(n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")
        inp = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if inp == "y":
            n1 = answer
            continue_program = True
            for symbol in operators:
                print(symbol)
        elif inp == "n":
            import os
            os.system("cls")
            continue_program = False
            calculator()
        else:
            inp = input("Invalid input. Try again!: ")
            if inp == 'y':
                continue_program = True
                n1 = answer
            elif inp == 'n':
                continue_program = False
                calculator()
            else:
                print("Nahi Sudhroge!")
                continue_program = False


calculator()
