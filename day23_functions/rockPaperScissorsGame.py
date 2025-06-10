# rock, paper, scissors game
import random

print("\nWelcome to the rock, paper, scissors game.")

game = ['rock', 'paper', 'scissors']

programChoice = random.choice(game)

while True:
    userChoice = input("\nWhat is your pick (rock, paper, scissors): ")
    if userChoice.lower().strip() == programChoice:
        print(f"\nIt's a TIE the program choose {programChoice}")
        break
    elif userChoice.lower().strip() == 'rock' and programChoice == 'paper':
        print(f"\nYou LOOSE ✊ the program choose {programChoice}")
        break
    elif userChoice.lower().strip() == 'rock' and programChoice == 'scissors':
        print(f"\nYou WIN ✊ the program choose {programChoice}") 
        break
    elif userChoice.lower().strip() == 'paper' and programChoice == 'rock':
        print(f"\nYou WIN 📄 the program choose {programChoice}")
        break        
    elif userChoice.lower().strip() == 'paper' and programChoice == 'scissors':
        print(f"\nYou LOOSE 📄 the program choose {programChoice}")
        break
    elif userChoice.lower().strip() == 'scissors' and programChoice == 'paper':
        print(f"\nYou WIN ✂️ the program choose {programChoice}")
        break
    elif userChoice.lower().strip() == 'scissors' and programChoice == 'rock':
        print(f"\nYou LOOSE ✂️ the program choose {programChoice}")
        break
    else:
        print('\nInvaild choice')
        continue