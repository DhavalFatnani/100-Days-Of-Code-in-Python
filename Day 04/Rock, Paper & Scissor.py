import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]
computer_choice = random.choice(moves)
while True:
    choice = int(input("What do you choose> Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    if choice == 0 or choice == 1 or choice == 2:
        chose = moves[choice]
        print(f"Your Choice:\n{chose}")
        print(f"Computer chose:\n{computer_choice}\n")

        if (chose == rock and computer_choice == scissors) or (chose == scissors and computer_choice == paper) or (
                chose == paper and computer_choice == rock):
            print("You won")
        elif chose == computer_choice:
            print("TIED")
        else:
            print("You lose")
        break
    else:
        print("Invalid choice!")
        continue