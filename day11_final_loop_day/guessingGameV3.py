# : 🎮 The Guessing Game V3
import time 
import random
import datetime

print("\nWelcome to The Guessing Game V3 🎮\n")

time.sleep(4)
print("\nYou will be guessing a number between 1 and 100")

time.sleep(4)
print("\nBe smart about it you only have 6 attempts")

userAttCount = 0
correctGuess = False

userOption = input("\nPlease enter any key to Start or 'q' to Quit: ").strip().lower()

startTime = time.time()
while userOption != 'q' and userOption != 'quit':
    randomInt = random.randint(1, 100)
    #Sprint(randomInt)
    for attempt in range(6):
        time.sleep(2)
        userGuess = input("\nWhat is your guess🤔: ").strip()
        userGuessBool = userGuess.isdigit()
        # I won't count invaild attempts
        while userGuessBool == False:
            print("\nInvaild guess")
            userGuess = input("\nWhat is your guess🤔: ").strip()
            userGuessBool = userGuess.isdigit()
        # when we reach here "userGuessBool" will be True
        userGuess = int(userGuess)
        if userGuess != randomInt:
            userAttCount += 1
            if userGuess > randomInt:
                print("\n❌ Wrong, Too HIGH ⬆")  
            else:
                print("\n❌ Wrong, Too LOW ⬇️")
        # break out the for loop if user guess is right
        elif userGuess == randomInt:
            correctGuess = True
            print("\n🔥 CORRECT!")
            break  
    if correctGuess == True:
        print("\nThanks")
        userOption = input("\nPlease enter any key to restart or 'q' to Quit: ").strip().lower()        
    else:
        print("\nSorry You lost all you attempts")
        userOption = input("\nPlease enter any key to restart or 'q' to Quit: ").strip().lower()
endTime = time.time()
time = endTime - startTime
if userAttCount > 0:
    print(f"\nIt took you {userAttCount} attempts and {time:.2f} seconds to finish the game.")
else:
    print("\nBYE!\n")