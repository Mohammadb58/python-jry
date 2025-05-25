# Code Lock Grid Puzzle
# will fix it later when i learn lists
# i cant get to store each unlocked cell
rowCount = 1
colCount = 1
while True:    
    row = input("\nEnter row (0–5): ").strip()
    userRowBool = row.isdigit() 
    col = input("\nEnter col (0–5): ").strip()
    userColBool = row.isdigit()

    while userRowBool == False and userColBool == False:
        print("\nInvaild coordinates")
        row = input("\nEnter row (0–5): ").strip()
        userRowBool = row.isdigit() 
        col = input("\nEnter col (0–5): ").strip()
        userColBool = row.isdigit()

    print(f"\nDEBUG: -> {row} {col}")
    print()
    row = int(row)
    col = int(col)
    for i in range(1,6):
        for j in range(1,6):
            if i == row and j == col or rowCount == i and colCount == j:
                print("✅ ", end="")
                rowCount = row
                colCount = col
            else:
                print("🔒 ", end="")
        print()
    if i == "✅ " and j == "✅ ":
        break
    else:
        continue