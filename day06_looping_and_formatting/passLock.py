# Final while loop 

print("----------------------------------")

userPass1 = input("What do you think the password is: ")

userPass2 = userPass1.strip().lower()

attemptsCount = 1
if userPass2 == "league":
    userPassBool = True 
else:
    userPassBool = False
    
if attemptsCount <= 4:
    attemptsCountBool = True 
else:
    attemptsCountBool = False 

while (userPassBool == False) or (attemptsCountBool == False):
    if attemptsCount <= 4:
        if attemptsCount == 1:
            print("❌ Wrong, You got 3 attempts left")
            userPass2 = input("What do you think the password is: ")
            userPass2 = userPass2.strip().lower()
            attemptsCount += 1
        elif attemptsCount == 2:
            print("❌ Wrong, You got 2 attempts left")
            userPass2 = input("What do you think the password is: ")
            userPass2 = userPass2.strip().lower()
            attemptsCount += 1
        elif attemptsCount == 3:
            print("❌ Wrong, You got 1 attempt left")
            userPass2 = input("What do you think the password is: ")
            userPass2 = userPass2.strip().lower()
            attemptsCount += 1
        else:
            attemptsCountBool = False
    else:
        userPassBool = False

if (userPassBool == True) and (attemptsCountBool == True):
    print("X")
else:
    print("X")
print("✅ ACCESS")
