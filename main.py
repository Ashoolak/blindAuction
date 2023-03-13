from os import system, name


# define our clear function
def clear():
     _ = system('clear')


bids = {}
currentHigh = 0
winner = ""
repeat = False


repeat = input("Are there any bidders (Yes, No)? ").lower()
if repeat == "yes":
    clear()
    repeat = True
else:
    repeat = False


while repeat:
    name = input("What is you name: ")
    amount = int(input("What is your bid: "))
    bids[name] = amount
    repeat = input("Are there any bidders (Yes, No)? ").lower()
    if repeat == "yes":
        clear()
        repeat = True
    else:
        repeat = False


for bid in bids:
    if bids[bid] > currentHigh:
        currentHigh = bids[bid]
        winner = bid
if winner != "":
    print(f'the winner is {winner} with a bid of ${bids[winner]}')
else:
    print("No bids, the item was not sold!")