# Loops haven't clicked yet

while True:
    userOrigNum = input("\nPlease enter you guess (press q to quit): ")

    userCleanNum = userOrigNum.strip().lower()
    userNumBool = userCleanNum.isdigit()
    
    if userNumBool == True:
        userCleanNum = int(userCleanNum)
        for i in range (0, userCleanNum + 1):
            if i % 2 == 0:
                print(i)
            #else:
                #continue
        
    elif userCleanNum == 'q' or userCleanNum == 'quit':
        print("\nThanks for playing.")
        break
       
    else:
        print("\nPlease try a vaild input")