import random

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images=[rock,paper,scissors]
choice=int(input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
comp_choice=random.randint(0,2)
print(f"You choose {game_images[choice]}")
print(f"Computer choose {game_images[comp_choice]}")
if choice==0:
    if comp_choice==0:
        print("both players selected rock, it's a tie!")
    elif comp_choice==1:
        print("Computer choose paper, paper covers rock, you lose!")
    else:
        print("Computer choose scissors, rock smashes scissors, you win!")

elif choice==1:
    if comp_choice==0:
        print("Computer choose rock, paper covers rock, you win!")
    elif comp_choice==1:
        print("both players selected paper, it's a tie!")
    else:
        print("Computer choose scissors, scissors cuts paper, you lose!")

else:
    if comp_choice==0:
        print("Computer choose rock, rock smashes scissors, you lose!")
    elif comp_choice==1:
        print("Computer choose paper, scissors cuts paper, you win!")
    else:
        print("both players selected scissors, it's a tie!")