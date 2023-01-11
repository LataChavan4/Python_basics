from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to secret auction programm.")
other_bidder = True
bids = {}
# def bid_dict(bidder, amount):
#   bids[bidder] = amount
while other_bidder:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids[name] = bid
  bidder = input("Are there any other bidders? Type 'yes'or 'no'.\n")
  if bidder == "yes":
    clear()
  if bidder == "no":
    other_bidder = False

Highest_bid = 0
for bidder in bids:
  if bids[bidder] > Highest_bid:
    Highest_bid = bids[bidder]
winner = bidder

print(f"The winner is {winner} with highest bid of ${Highest_bid}")