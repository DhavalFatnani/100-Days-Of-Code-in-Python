import random
import art as a
import data as d


# Select any two instagram handles from data, A and B
def select_handle():
    # A = d.data[random.randint(0, len(d.data) - 1)]
    A = random.choice(d.data)
    return A


# Compare the followers count of B against A, according to players input(Higher or lower)
def compare(handle_a, handle_b, inp):
    correct = False
    if inp == 'A':
        if handle_a['follower_count'] > handle_b['follower_count']:
            correct = True
        else:
            correct = False
    if inp == 'B':
        if handle_a['follower_count'] < handle_b['follower_count']:
            correct = True
        else:
            correct = False
    return correct


def display(h_a, h_b):
    print(f"Compare A: {h_a['name']}, a {h_a['description']}, from {h_a['country']}.")
    print(a.vs)
    print(f"Against B: {h_b['name']}, a {h_b['description']}, from {h_b['country']}.")
    x = input("Who has more followers? Type 'A' or 'B': ")
    return x


def game():
    Score = 0
    Handle_A = select_handle()
    Handle_B = select_handle()
    compare_input = display(Handle_A, Handle_B)
    while compare(Handle_A, Handle_B, compare_input):
        Score += 1
        print(f"You're right! Current score: {Score}.")
        Handle_A = Handle_B
        Handle_B = select_handle()
        compare_input = display(Handle_A, Handle_B)
        compare(Handle_A, Handle_B, compare_input)
    print(f"Sorry, that's wrong. Final score: {Score}")


# Start the game, ask the player to start the game
while True:
    print(a.logo)
    play = input("Do you want to play? Type 'y' or 'n': ")
    if play == 'y':
        game()
    else:
        break
