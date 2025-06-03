# finding the largest number 

# ill try to find the largest num in this list
nums = [[-100, -50, -25, -12, -6, -3, -1],
        [0, 2, 400, 8, 16, 32],
        [],
        [100, 200]]
emptyListBool = False
for rows in nums:
    for num in rows:
        emptyListBool = True
        highestNum = num
        break

if emptyListBool == True:    
    for numList in nums: 
        for num in numList:
            if num > highestNum:
                highestNum = num
            else:
                continue
    print(f"The highest Num is --- {highestNum} ---")
else:
    print("\nThe list is empty!\n")
