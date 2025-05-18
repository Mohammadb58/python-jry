# Number lock mini game

print("------------------------------------------------\n")
print("💀 Challenge: The Number Lock\n")

print("You will be guessing a 3 digit code") 
print("I'll tell you if your guess is higher or lower\n") 

userNum = input("What is your guess: ")
userNumBool = False
while not (userNum == 517) and (userNumBool == False):
    if userNum.isdigit():
        userNum = int(userNum)
        if 0 <= userNum <= 999:
            if userNum > 517:
                print(f"🤔 Too high. Think of a number less that {userNum}\n")
                userNum = input("What is your guess: ")
                userNumDigit = userNum.isdigit
        
            elif userNum < 517:
                print(f"🙃 Too low. Think of a number greater that {userNum}\n")
        
                userNum = input("What is your guess: ")
                userNumDigit = userNum.isdigit()
            
            else:
                userNumBool = True
                
        elif (userNum < 0) or (userNum > 999):
            print("Invalid guess! Must be a 3-digit number\n")
            userNum = input("What is your guess: ")
    else:
        print("Invalid guess! Must be a 3-digit number\n")
        userNum = input("What is your guess: ")
    
print("\n✅ Corecct 517 is the right answer")
print("\n------------------------------------------------")