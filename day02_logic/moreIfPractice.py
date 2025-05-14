# Movie ticket system

age = int(input("Welcome to AMC, What is your age: "))

if age <= 0:
    print ("Please try again")
    ticketPrice = 0
    
elif age < 5:
    print ("You get a free ticket!")
    ticketPrice = 0
    
elif age >= 5 and age <= 12:
    print ("Your total would be 5$")
    ticketPrice = 5
    
elif age >= 13 and age <= 17:
    print ("Your total would be 7$")
    ticketPrice = 7

elif age >= 18 and age <= 64:
    print ("Your total would be 10$")
    ticketPrice = 10

elif age >= 65:
    print ("Your total would be 7$")
    ticketPrice = 7

else:
    print ("This edge case may never occur!")
    
popCorn = input ("Would you like a popcorn or a drink with that (Yes/No): ")

if (popCorn == "Yes") or (popCorn == "yes"):
    print ("That would be 3$ more.")
    popCost= 3
    
elif (popCorn == "No") or (popCorn == "no"):
    print ("No problem, have a nice day.")
    popCost = 0

else:
    print ("Have a good day!")
    
rec = input("Would you like to know the total break down (Yes/No): ")

if (rec == "Yes") or (rec == "yes"):
    tax = (((popCost + ticketPrice) * 10.75) / 100)
    total = popCost + ticketPrice + tax
    print (f"Your total is {round(total, 2)}$, which includes the ticket price: {ticketPrice}$, and Add-ons: {popCost}$.")
    
elif (rec == "No") or (rec == "no"):
    print ("No problem, have a nice day.")

else:
    print ("Have a good day!")