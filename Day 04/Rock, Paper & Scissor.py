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
    your_choice = int(input("What do you choose> Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    if your_choice == 0 or your_choice == 1 or your_choice == 2:
        you_chose = moves[your_choice]
        print(f"Your Choice:\n{you_chose}")
        print(f"Computer chose:\n{computer_choice}\n")

        if (you_chose == rock and computer_choice == scissors) or (you_chose == scissors and computer_choice == paper) or (
                you_chose == paper and computer_choice == rock):
            print("You won")
        elif you_chose == computer_choice:
            print("TIED")
        else:
            print("You lose")
        break
    else:
        print("Invalid choice!")
        continue
