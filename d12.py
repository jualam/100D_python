import random

def guess_number(random_number,attempts):
    number_of_guesses=0
    while attempts>0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        number_of_guesses+=1
        if guess==random_number:
            print(f"Congratulations, you have guessed the number in {number_of_guesses} attempts!")
            break
        elif guess>random_number:
            print("Too high!")
        else:
            print("Too low!")
        attempts-=1
        if attempts>0:
            print("Guess Again!")
    if attempts==0:
        print("You have run out of attempts. The number was "+str(random_number))

while True:
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")
    while True:
        difficulty=input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            attempts=10
            break
        elif difficulty == 'hard':
            attempts=5
            break
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")
    number=random.randint(1,100)   
    guess_number(number,attempts)

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing. Goodbye! 👋")
        break
    else:
        print("\n"*15)




