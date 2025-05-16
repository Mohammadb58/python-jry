# validate user input 

print("Let's help you choose a username")

userName = input("Please enter your username, (1) must be no more then 12 characters long, (2) no spaces, and (3) no digits: ")

print(f"You choose {userName}")

# if else to check if the username is under or = to 12 chars
if len(userName) <= 12:
    userNameLenBool = True

else:
    userNameLenBool = False
    
# if else to check if there are any spaces
userNameCount = userName.count(" ")

if userNameCount <= 0:
    userNameSpaceBool = True

else:
    userNameSpaceBool = False
    
# if else to check if there any digits
userNameDigit = userName.count('0')
userNameDigit1 = userName.count('1')
userNameDigit2 = userName.count('2')
userNameDigit3 = userName.count('3')
userNameDigit4 = userName.count('4')
userNameDigit5 = userName.count('5')
userNameDigit6 = userName.count('6')
userNameDigit7 = userName.count('7')
userNameDigit8 = userName.count('8')
userNameDigit9 = userName.count('9')

if (userNameDigit <= 0) and (userNameDigit1 <= 0) and (userNameDigit2 <= 0) and (userNameDigit3 <= 0) and (userNameDigit4 <= 0) and (userNameDigit4 <= 0) and (userNameDigit5 <= 0) and (userNameDigit6 <= 0) and (userNameDigit7 <= 0) and (userNameDigit8 <= 0) and (userNameDigit9 <= 0):
    userNameDigitBool = True

else:
    userNameDigitBool = False 

if (userNameLenBool == True) and (userNameSpaceBool == True) and (userNameDigitBool == True):
    print(f"{userName} is vaild. Good choice.")
    
elif (userNameLenBool == False) and (userNameSpaceBool == True) and (userNameDigitBool == True):
    print("The username can't be more than 12 characters long")

elif (userNameLenBool == True) and (userNameSpaceBool == False) and (userNameDigitBool == True):
    print("The username can't have any spaces")

elif (userNameLenBool == True) and (userNameSpaceBool == True) and (userNameDigitBool == False):
    print("The username can't be have any digits")

elif (userNameLenBool == False) or  (userNameSpaceBool == False) or (userNameDigitBool == False):
    print("Invaild username. Please try another one.")
  
else:
    print("CHECK IF THIS EDGE CASE OCCURS")
    # Using a truth table i found three cases where this occurs 
    # However due to the last elif using 'or' rather than 'and'
    # the last else will never occur!