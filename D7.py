import random
word_list=["apple","monkey","donkey"]
word_to_guess=random.choice(word_list)
print(word_to_guess)
lives=6
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
placeholder=""
for letter in word_to_guess:
    placeholder += "_"
print(placeholder)
game_over=False
correct_letter=[]
while not game_over:
    guessed_letter=input("Guess a letter in lowercase: ")
    display=""
    for letters in word_to_guess:
        if guessed_letter==letters:
            display+=letters
            correct_letter.append(guessed_letter)
        elif letters in correct_letter:
            display+=letters
        else:
            display+="_"
    print(display)
    if guessed_letter not in word_to_guess:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose")

    if "_" not in display:
        game_over=True
        print("You win")

    print(f"Final stage {HANGMANPICS[6-lives]}")