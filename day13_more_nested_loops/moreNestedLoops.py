for rows in range(1,6):
    for cols in range(1,6):
        if (rows + cols) % 2 ==0:
            print("A ", end="")
        else:
            print("B ", end="")
    print()
print("-----------------------------")    
# does the same thing as above but shorter    
for rows in range(1,6):
    for cols in range(1,6):
        print("A ", end="") if (rows + cols) % 2 ==0  else print("B ", end="")
    print()
print("-----------------------------")    
    
