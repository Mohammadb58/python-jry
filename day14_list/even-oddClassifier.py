# Even-Odd Classifier 
userInput = ''
evenList = []
oddList = []
nums = []
print("\nWelcome to the Even-Odd Classifier")
while True:
    userInput = input("\nPlease enter a vaild number over 0 ('Done' to quit): ").strip().lower()
    if userInput == 'done':
        break
    userInputBool = userInput.isdigit()
    while userInputBool == False and userInput != 'done':
        print("\nInvaild number")
        userInput = input("\nPlease enter a vaild number over 0 'Done' to quit): ").strip().lower()
        userInputBool = userInput.isdigit()
    if userInput == 'done':
        break
    nums.append(userInput)
print("\nYour list has ", end="")
for num in nums:
    print(num, "", end="")
print("\nYour list has", len(nums), "num/s.")
for num in nums:
    num = int(num)
    if num % 2 == 0:
        evenList.append(num)
    else:
        oddList.append(num)
print("\nYour list has", len(evenList), "even num/s.")
print("\nYour list has", len(oddList), "odd num/s.\n")