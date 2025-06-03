# Shopping Cart: Advanced Edition
total = 0
total2 = 0
items = []
prices = []

print("\n---------------------------------------------")

print("\nWelcome to the Shopping Cart program")

while True:
    userItem = input("\nEnter item name ('q' to Quit): ").strip()
    if userItem == 'q':
        break
    userPrice = input("\nEnter its price ('q' to Quit): ").strip()
    if userPrice == 'q':
        break
    userPrice = int(userPrice)
    items.append(userItem)
    prices.append(userPrice)

for price in prices:
    total += price
print(f"\n- Your list has {len(items)} items.")
print(f"\n- The total price is {total}$.")
print()
for item in items:
    print('-',item)
    
userRm = input("\nWould you like to delete anything in the list (Y/N): ").lower()
if userRm == 'y':
    userRmItem = input("\nWhat item would you like to remove: ")
    indx = items.index(userRmItem)
    prices.pop(indx)
    items.remove(userRmItem)
    for price in prices:
        total2 += price
    print(f"\n- Your list has {len(items)} items.")
    print(f"\n- The total price is {total2}$.")
    print()
    for item in items:
        print('-',item)
else:
    print("\nNo problem, Thanks")
    
userCheck = input("\nWould you like to check if anything was repeated (Y/N): ").lower()
if userCheck == 'y':
    userCheckItem = input("\nWhat item would u like to check: ")
    print(f"\nYour list has {items.count(userCheckItem)} {userCheckItem}\n")
else:
    print("\nNo problem, Thanks\n")
