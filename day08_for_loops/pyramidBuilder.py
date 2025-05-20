# more loops 
userNumPyr = input("Please enter a number for the pyramid: ")

userNumClean = userNumPyr.strip()
userNumCleanDigit = userNumClean.isdigit()

if userNumCleanDigit == True:
    userNumClean = int(userNumClean)
    for i in range(1, userNumClean + 1, 2):
        total = i * '*' 
        print(f"{total:^{userNumClean}}")
    
else:
    print("Invaild")