# for looops

#userOption = int(input("How many stars do you want? "))

#for x in range(0, userOption):
#    print("*")

userNum = int(input("What number are toy thinking of: "))

for counter in range(1, userNum + 1): # I added 1 to make it inclusive
    print(f"{counter}--> counter") 
    print(f"{userNum}--> userNum") 
    if counter % 2 == 0:
        print(f"{counter} is even")
    else:
        print(f"{counter} is odd")