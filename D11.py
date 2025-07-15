import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
my_cards=[]
comp_cards=[]
play=input("Do you wan to play a game of Blackjack? Type 'y' or 'n': ")
if play=='y':
    my_cards.extend(random.sample(cards,2))
    comp_cards.extend(random.sample(cards,2))
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card : {comp_cards[0]}")
    while True:
        next=input("Type 'y' to get another card, type 'n' to pass: ")
        if next=='y':
            my_cards.extend(random.sample(cards,1))
            if sum(my_cards)>21:
                print("Bust")
                print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")


