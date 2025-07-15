import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score==0:
        return "Lose, Dealer has Blackjack"
    elif u_score==0:
        return "Win, You have Blackjack"
    elif u_score>21:
        return "Lose, You went over"
    elif c_score>21:
        return "Win, Dealer went over"
    elif u_score>c_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      '------'                           |__/   
""")
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    # deal the initial two cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        #Calculate initial score
        user_score=calculate_score(user_cards)
        comp_score=calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score==0 or comp_score==0 or user_score>21:
            is_game_over=True
        else:
            next=input("Type 'y' to get another card or 'n' to stop: ")
            if next=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while comp_score!=0 and comp_score<17:
        computer_cards.append(deal_card())
        comp_score=calculate_score(computer_cards)

    print(f"Your final hand is {user_cards}. final score: {user_score}")
    print(f"Computer's final hand is {computer_cards}. final score: {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")=='y':
    print("\n"*15)
    play_game()
    