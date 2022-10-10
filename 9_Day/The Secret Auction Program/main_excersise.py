import os
from art import logo

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bide_amount = bidding_record[bidder]
        if bide_amount > highest_bid:
            highest_bid = bide_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
    
print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        print("Clearing screen...")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Invalid input. Please try again.")
        os.system('cls' if os.name == 'nt' else 'clear')
    