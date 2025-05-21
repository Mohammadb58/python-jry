# more loops till they click!
# this logic is what was missing from the 
# guessing game V2 that i stepped back from 

for i in range(0, 3):
    userNum = input("\nPlease enter you secret code: ").strip().lower()
    userNumBool = userNum.isdigit() 
    while userNumBool == False:
        print("\nInvaild input, I'll be nice and ignore this attempt 😀")
        userNum = input("\nPlease enter you secret code: ").strip().lower()
        userNumBool = userNum.isdigit()
    if userNum == '58':
        print("\nCorrect")
        break
    elif userNum != '58':
        if i == 0:
            print("\nNope, try again")
        elif i == 1:
            print("\nStill not it")
        elif i == 2:
            print("\nLast chance…")
    
if userNum == '58':
    print("\nFull Access\n")
        
else:
    print("\nAll attempts used.\n")