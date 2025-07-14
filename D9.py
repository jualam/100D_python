def find_highest_bidder(bidding_dict):
    highest_bid=0
    highest_bidder=""
    for key in bidding_dict:
        if bidding_dict[key]>highest_bid:
            highest_bid=bidding_dict[key]
            highest_bidder=key

    print(f"\nThe winner is {highest_bidder} with a bid of ${highest_bid}!")

print("Welcome to the secret auction program")
auction_dict={}
while True:
    name=input("What is your name: ")
    bid=int(input("Enter your bid: $"))
    auction_dict[name]=bid
    while True:
        multi_bidders=input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if multi_bidders=='yes':
            print("\n"*12)
            break
        elif multi_bidders=='no':
            break
        else:
            print("Select either 'yes' or 'no'")
    if multi_bidders=='no':
        find_highest_bidder(auction_dict)
        break


    

