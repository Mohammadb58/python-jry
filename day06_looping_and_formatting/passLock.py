# Final while loop 

print("----------------------------------")

userPass1 = input("What do you think the password is: ")

userPass2 = userPass1.strip().lower()

attemptsCount = 1    
attemptsCountBool = True 
    

while not (userPass2 == "league") and (attemptsCountBool == True):
    #if attemptsCount <= 4:
    if attemptsCount == 1:
        print("❌ Wrong, You got 3 attempts left")
        userPass2 = input("What do you think the password is: ")
        userPass2 = userPass2.strip().lower()
        attemptsCount = 2
    elif attemptsCount == 2:
        print("❌ Wrong, You got 2 attempts left")
        userPass2 = input("What do you think the password is: ")
        userPass2 = userPass2.strip().lower()
        attemptsCount = 3
    elif attemptsCount == 3:
        print("❌ Wrong, You got 1 attempt left")
        userPass2 = input("What do you think the password is: ")
        userPass2 = userPass2.strip().lower()
        attemptsCount = 4
    elif attemptsCount >= 4:
        attemptsCountBool = False
        

if (userPass2 == "league") and (attemptsCountBool == True):
    print("✅ ACCESS")
else:
    print("❌ Access Denied ❌")
