print("""> i hate dejav�s.
                 _           ___             _____________
          ,-----' |  ,    | <_'_`)         ,'             `.
          | //  : | /   (() :-)-||        /    Tsk, tsk!    \
          | //  : |  -  [:]  \-_/`    ___/  The accents are  \
          | //  : | \   \ \__/:_\     `.    on the "e" and    |
          `-----._|  `   \__// ( \|     |   the "a" and on    |
           _/___\_         //  | ||]    |   the "a" they're   |
     _____[_______]_[~~-_ (.L_/  ||      \   the other way   /
    [____________________]' `\_,/'/       \      around     /
      ||| /          |||  ,___,'./         `._____________,'
      ||| \          |||,'______|
      ||| /          /|| I==||
      ||| \       __/_||  __||__
  -----||-/------`-._/||-o--o---o---
    ~~~~~'

Ool""")

print("Welcome to the treasure island. Your mission is to find the treasure.")
print("You are standing at the entrance of a dark cave.")
step1=input("Left or Right: ")
if step1.lower()=="left":
    print("Swim or wait")
    step2=input("Swim or Wait: ")
    if step2.lower()=="wait":
        print("Which door")
        step3=input("Red or Blue or yellow or any other color: ")
        if step3.lower()=="blue":
            print("Eaten by mango beats, Game over!!!")
        elif step3.lower()=="red":
            print("Burned by ice, Game over!!!")
        elif step3.lower()=="yellow":
            print("Congrats. You've Won!!!")
        else:
            print("Game over!!!")
    else:
        print("Attacked by a trout, You're dead!")
else:
    print("You fell into a cave. Game over!!!")
