# mini python calc

print("Welcome to mini python calculator")

numberOne = float(input("Please enter your first number: "))

operator = input("Please enter your operator: ")

numberTwo = float(input("Please enter your second number: "))

if operator == "+":
    total = numberOne + numberTwo
    print(f"Answer: {round(total, 2)}")
    isVaild = True
elif operator == "-":
    total = numberOne - numberTwo
    print(f"Answer: {round(total, 2)}")
    isVaild = True
elif operator == "*":
    total = numberOne * numberTwo
    print(f"Answer: {round(total, 2)}")
    isVaild = True
elif operator == "/":
    total = numberOne / numberTwo
    print(f"Answer: {round(total, 2)}")
    isVaild = True
elif operator == "%":
    total = numberOne % numberTwo
    print(f"Answer: {round(total, 2)}")
    isVaild = True  
else:
    print("Invaild operator")
    isVaild = False

    
if isVaild == True:
    playAgain = input("Would you like to calculate again (Yes/No): ")
    
elif isVaild == False:
    playAgain = False


if (playAgain == "Yes") or (playAgain == "yes"):

    numberThree = float(input("Please enter your first number: "))

    operatorTwo = input("Please enter your operator: ")

    numberFour = float(input("Please enter your second number: "))

    if operatorTwo == "+":
        total2 = numberThree + numberFour
        print(f"Answer: {round(total2, 2)}")
    elif operatorTwo == "-":
        total2 = numberThree - numberFour
        print(f"Answer: {round(total2, 2)}")
    elif operatorTwo == "*":
        total2 = numberThree * numberFour
        print(f"Answer: {round(total2, 2)}")
    elif operatorTwo == "/":
        total2 = numberThree / numberFour
        print(f"Answer: {round(total2, 2)}")
    elif operatorTwo == "%":
        total2 = numberThree % numberFour
        print(f"Answer: {round(total2, 2)}")
    elif operator == "":
        print("Invaild operator")
        isVaild = False   
    else:
        print("Invaild operator")
        
else:
    print("Thanks")
    
print("Have a good day.")