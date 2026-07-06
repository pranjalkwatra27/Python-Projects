Bid = {}

def find_highest_bidder(bidding):
    winner=""
    amount=0
    for i in bidding:
        bidders=bidding[i]
        if bidding[i]>amount:
            amount=bidding[i]
            winner=i
    print(f"The winner is {winner} with amount {amount}")

Flag=True
while Flag==True:
    name = input("What is your name?")
    price = float(input("What is your price?"))
    Bid[name] = price
    should_continue = input("Any other Bidders?Yes/No").lower()
    if should_continue == "no":
        Flag = False
        find_highest_bidder(Bid)

    elif should_continue == "yes":
        print("\n" * 20)














