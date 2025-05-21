userNum = int(input("Please enter a number: "))

for i in range(1, userNum + 1):
    if userNum % i == 0:
        print(i)
    else:
        continue