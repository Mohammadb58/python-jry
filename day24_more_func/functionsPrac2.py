# functions practice

# Task #2
# Odd or Even Checker

def numCheck(num):
    if num % 2 == 0:
        print("\nEVEN\n")
    else:
        print("\nODD\n")
        
num = input("\nPlease enter a num: ")
numBool = num.isdigit()
while numBool == False:
    num = input("\nPlease enter a num: ")
    numBool = num.isdigit()
num = int(num)
numCheck(num)