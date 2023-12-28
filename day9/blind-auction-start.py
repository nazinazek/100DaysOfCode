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
    winner = ""
    if other_bidders == "yes":
        os.system('cls||clear')
    if other_bidders == "no":
        os.system('cls||clear')
        for key in bidders:
            if bidders[key] > max_bid:
                max_bid = bidders[key]
                winner = key
        auction = False
        print(f"The winner is {winner} with a bid of ${max_bid}.")
    
    
        