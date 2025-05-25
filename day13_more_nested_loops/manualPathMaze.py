# Manual Path Maze
row = int(input("Enter a row: "))
col = int(input("Enter a col: "))

for i in range(1,6):
    for j in range(1,6):
        if i == row and j == col:
            print("• ", end="")
        else:
            print(". ", end="")
    print()
    
userDir = input("\nEnter a move: up, down, left, right: ")

if userDir == 'right':
    for x in range(1,6):
        for y in range(1,6):
            if x == row and y == col + 1:
                print("• ", end="")
            else:
                print(". ", end="")
        print()
if userDir == 'left':
    for x in range(1,6):
        for y in range(1,6):
            if x == row and y == col - 1:
                print("• ", end="")
            else:
                print(". ", end="")
        print()
if userDir == 'up':
    for x in range(1,6):
        for y in range(1,6):
            if x == row -1 and y == col:
                print("• ", end="")
            else:
                print(". ", end="")
        print()
if userDir == 'down':
    for x in range(1,6):
        for y in range(1,6):
            if x == row+1 and y == col:
                print("• ", end="")
            else:
                print(". ", end="")
        print()