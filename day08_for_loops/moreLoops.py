# more loops 
#for loop #1
userNum = int(input("How many squares of numbers would you like: "))

for i in range(1, userNum + 1):
    print(i ** 2)

print("bye")

print("-------------------------------------------------------------\n")

# for loop #2
userStr1 = input("Please enter a string: ")
userStr = userStr1.strip().lower()
vowelCount = 0

for i in userStr:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowelCount += 1
        print(f"Here is the vowel: {i} and count is {vowelCount}")
    else:
        continue
print("bye")

print("-------------------------------------------------------------\n")       

# for loop #3

userMulNumO = input("What is the number you would like to see it * by: ")
userMulNum1 = userMulNumO.strip()
userMulNum = userMulNum1.isdigit()
print(f"DEBUG {userMulNum} <----------->")

if userMulNum == True:
    userMulNum1 = int(userMulNum1)
    for i in range(1, 11):
        result = i * userMulNum1
        print(f"{userMulNum1} x {i} = {result}");
else:
    print("Invaild choice")

userNumSuit = input("Please enter a number for the suitcase: ")

userNumClean = userNumSuit.strip()
userNumCleanDigit = userNumClean.isdigit()

if userNumCleanDigit == True:
    userNumClean = int(userNumClean)
    if userNumClean <= 100:
        for i in range(1, userNumClean + 1):
            total = i * '#'
            print(total)
    else:
        print("Too big of a number!")
else:
    print("invaild choice")