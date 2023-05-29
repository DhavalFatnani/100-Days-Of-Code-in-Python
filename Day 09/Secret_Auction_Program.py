"""
Secret Auction Program
"""

import os

# from time import sleep

logo = '''
                         ___________
                         \\         /
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


def clr():
    return os.system('cls')


def find_winner(all_bidders):
    winner = ''
    highest_bid = 0
    for bidder in all_bidders:
        bid_amount = bidder['bid']
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder['name']
    print(f'The winner is {winner} with a bid of Rs.{highest_bid}')


while True:
    Name = input("What is your name?: ")
    bid = int(input("What is your bid?: Rs. "))
    _bidder = {
        "name": Name,
        "bid": bid
    }
    more_bidder = input("Are there any other bidders? Type 'yes' or 'no' ")
    bidders.append(_bidder)
    if more_bidder == "yes":
        clr()
        continue
    elif more_bidder == "no":
        clr()
        find_winner(bidders)
        break
    else:
        print("Invalid input")
        break
