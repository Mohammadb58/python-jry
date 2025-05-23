# The Pyramid Arena

print("\nThe Pyramid Arena 📜")

userHeight = input("\nPlease enter the Pyramid height: ").strip()
userHeightBool = userHeight.isdigit()
while userHeightBool == False:
    print("\n❌ Invaild number")
    userHeight = input("\nPlease enter the Pyramid height: ").strip()
    userHeightBool = userHeight.isdigit()
userHeight = int(userHeight)

userOriginalSymbol = input("\nPlease enter a pattern symbol (*, @, #, etc.): ").strip()
# just to make it look clean while printing
userSymbol = " " + userOriginalSymbol

userDirection = input("\nPlease enter a direction normal or inverted (N/I): ").strip().lower()
while userDirection != 'i' and userDirection != 'n' and userDirection != 'normal' and userDirection != 'inverted':
    print("\n❌ Invaild direction")
    userDirection = input("\nPlease enter a direction normal or inverted (N/I): ").strip().lower()

userMode = input("\nPlease enter the row mode (odd, even, or all): ").strip().lower()
while userMode != 'odd' and userMode != 'even' and userMode != 'all':
    print("\n❌ Invaild row mode")
    userMode = input("\nPlease enter the row mode (odd, even, or all): ").strip().lower()
      
print(f"{userHeight}-{userSymbol}-{userDirection}-{userMode}")

for i in range(1, userHeight + 1):
    if (userDirection == 'n' or userDirection == 'normal') and (userMode == 'all'):
       total = i * userSymbol
       print(f"{total:^{userHeight*2}}")
    elif (userDirection == 'n' or userDirection == 'normal') and (userMode == 'even'):
        if i % 2 == 0:
            total = i * userSymbol
            print(f"{total:^{userHeight*2}}")

    elif (userDirection == 'n' or userDirection == 'normal') and (userMode == 'odd'):
        if i % 2 != 0:
            total = i * userSymbol
            print(f"{total:^{userHeight*2}}")
    else:
        break
for j in range(userHeight, 0, -1):
    if (userDirection == 'i' or userDirection == 'inverted') and (userMode == 'all'):
       total = j * userSymbol
       print(f"{total:^{userHeight*2}}")
    elif (userDirection == 'i' or userDirection == 'inverted') and (userMode == 'even'):
        if j % 2 == 0:
            total = j * userSymbol
            print(f"{total:^{userHeight*2}}")
    elif (userDirection == 'i' or userDirection == 'inverted') and (userMode == 'odd'):
        if j % 2 != 0:
            total = j * userSymbol
            print(f"{total:^{userHeight*2}}")
    else:
        break