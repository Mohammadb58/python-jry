# : 🎮 The Guessing Game V2
import time 
import random

print("\nWlecome to The Guessing Game V2 🎮\n")

#time.sleep(4)
print("You will be guessing a number between 1 and 100\n")

#time.sleep(4)
print("Be smart about you only have 6 attempts\n")

randomInt = random.randint(1, 100)
randomInt2 = int(randomInt)
print(randomInt)
userAttCount = 0

while True:
    #time.sleep(2)
    userOriginalGuess = input("\nWhat is your guess🤔: ")
    userGuess = userOriginalGuess.strip()
    
    userGuessBool = userGuess.isdigit()
    if userGuessBool == True:
        #if userAttCount < 6: 
        userGuess = int(userGuess)
            #userAttCount += 1
        for i in range(6):
            if userGuess != randomInt2:
                if userGuess > randomInt2:
                    print("\n❌ Wrong, Too HIGH")  
                else:
                    print("\n❌ Wrong, Too LOW")
                continue
            else:
                print("\n🔥 CORRECT!")
                
        
        else:
            print("\nSorry You lost all you attempts")
            break
    else:
        print("\n❌Invaild input please try again❌") 

print(f"DEBUG <---> {userGuess}")