"""
Secret Auction Program
"""
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidders = []
import os
from time import sleep
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def evaluate():
    winner = ''
    highest_bid = 0
    for bidder in bidders:
        bid_amount = bidder['bid']
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder['name']
    print(f'The winner is {winner} with a bid of Rs.{highest_bid}')

while True:
    Name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    _bidder = {
        "name": Name,
        "bid": bid
    }
    more_bidder = input("Are there any other bidders? Type 'yes' or 'no' ")
    bidders.append(_bidder)
    if more_bidder == "yes":
        sleep(2)
        clear()
        continue
    elif more_bidder == "no":
        sleep(2)
        clear()
        evaluate()
        break
    else:
        print("Invalid input")
        break