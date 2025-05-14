# Shopping Cart

item = input("What is the item you would like? ")

price = float(input("What is the price? "))

quantity = int(input("How many would you like? "))

total = price * quantity

print(f"You bought {quantity} {item}/s.")

print(f"You total before tax would be {total}$.")

tax = float(input("What is the tax in your state? "))

taxTotal = (total * tax) / 100

newTotal = taxTotal + total

print (f"Your new total with tax is {newTotal}$.")

discountCode = input("Do you have a discount code? yes/no? ")

if discountCode == "yes":
    dCode = float(input("How much is your discount code? "))
    
    if dCode >= 50:
        print (f" {dCode}% is a large discount. Please verify.")
        dCode = float(input("Please confirm it again? "))
        disTotal = newTotal * (dCode / 100)
    
        newDisTotal = newTotal - disTotal

        print(f"Sure here is your new discounted total is {newDisTotal}$.")
     
    
    else:
        disTotal = newTotal * (dCode / 100)
    
        newDisTotal = newTotal - disTotal

        print(f"Your new discounted total is {newDisTotal}$.")
else:
    print (f"No problem, you total after tax is {newTotal}$")