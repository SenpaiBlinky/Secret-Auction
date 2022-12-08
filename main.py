from judge_hammer import logo
import os

print(logo)

auctioneer = {}
repeat = True

# PLAYER SELECTION
while repeat == True:

    name = input("What is your name?")
    bid = int(input("What is your bid?"))

    auctioneer[name] = bid

    next_participant = input("Is there another participant? 'Y' or 'N' ")
    if next_participant == "N":
        repeat = False
    else:
        os.system('cls')
        
# VICTORY CHOOSER
highest_bid = 0
highest_bidder = ""

for name in auctioneer:
    
    if auctioneer[name] > highest_bid:
        highest_bid = auctioneer[name]
        highest_bidder = name
        
print(f"Highest bidder is {highest_bidder} with a bid of {highest_bid}, congrats")
        