import os
# from replit import clear
from art import logo

print(logo)
another_user = 'yes'
dict = {}

def ToFindWinner (records):
    max= 0
    for bidder in records:
        if records[bidder] > max:
            max = records[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max}")
    

while another_user != 'no':
    name = input('What is your name? ')
    bid = int(input("What's your bid? $"))
    dict[name] = bid
    # if dict["name"] > max:
    #     max = dict["name"]
    #     participant = name
    os.system('cls')
    another_user = input("Are there any other bidders? 'yes' or no ").lower()
print(dict)

ToFindWinner(dict)
