# The Odd-Even Pyramid Gauntlet

print("--------------------------------------------------------------------------\n")

print("🏺Welcome to The Odd-Even Pyramid Gauntlet🏺\n")

print("I'll ask you for a number then buld a pyramid.🐍\n")

userNumOrig = input("Please enter a number: ")

userNum = userNumOrig.strip()

userNumClean = userNum.isdigit()

if userNumClean == True:
    userNum = int(userNum)
    for i in range(1, userNum + 1):
        if i % 2 == 0:
            tot = i * ' @'
            print(f"{tot:^{userNum*2}}")
        elif i % 2 != 0:
            tot1 = i * ' *'
            print(f"{tot1:^{userNum*2}}")
else:
    print("❌Invaild option!❌\n")
    
print("--------------------------------------------------------------------------\n")
