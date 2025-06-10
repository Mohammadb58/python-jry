# rock, paper, scissors game
import random

print("\nWelcome to the rock, paper, scissors game.")

game = ['rock', 'paper', 'scissors']

playing = True
while playing:
    programChoice = random.choice(game)
    while True:
        userChoice = input("\nWhat is your pick (rock, paper, scissors): ")
        if userChoice.strip().lower() not in game:
            print('\nInvaild choice')
            continue 
        if userChoice.lower().strip() == programChoice:
            print(f"\nIt's a TIE the program choose {programChoice}")
            break
        elif userChoice.lower().strip() == 'rock' and programChoice == 'scissors':
            print(f"\nYou WIN ✊ the program choose {programChoice}") 
            break
        elif userChoice.lower().strip() == 'paper' and programChoice == 'rock':
            print(f"\nYou WIN 📄 the program choose {programChoice}")
            break        
        elif userChoice.lower().strip() == 'scissors' and programChoice == 'paper':
            print(f"\nYou WIN ✂️ the program choose {programChoice}")
            break
        else:
            print(f"\nYou LOOSE the program choose {programChoice}")
            break
    playAg = input("\nWould you like to play again (Y/N): ").strip().lower()
    if playAg == 'yes' or playAg == 'y':
        playing = True
    else:
        playing = False
    
print("\nThanks for playing\n")