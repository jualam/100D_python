from data import data
import random
import os

def compare(option1,option2):
    if option1['follower_count']>option2['follower_count']:
        return 'a'
    else:
        return 'b'
first_round=True
win_count=0
a, b = random.sample(data, 2)
print("""__  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/ """)

while True:
    os.system('cls' if os.name == 'nt' else 'clear') 
    if not first_round:
        print(f"Current score: {win_count}")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    choice= input("Who has more followers? Type 'A' or 'B': " ).lower()
    answer=compare(a,b)
    if choice==answer:
        win_count+=1
        print(f"You're right! Current score: {win_count}")
        first_round=False
        a=b
        b=random.choice(data)
        while b==a:
            b=random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {win_count}")
        break