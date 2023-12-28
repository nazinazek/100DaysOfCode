import os
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)
print("Welcome to the secret auction program.")
auction = True
bidders = {}

while auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bit?: $"))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    max_bid = 0
    if other_bidders == "yes":
        os.system('cls||clear')
    if other_bidders == "no":
        for key in bidders:
            if bidders[key] > max_bid:
                max_bid = bidders[key]
        auction = False
    os.system('cls||clear')
    for key in bidders:
        if max_bid == bidders[key]:
            print(f"The winner is {key} with a bid of ${bidders[key]}.")
        