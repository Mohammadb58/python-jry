# compound interest calc

print("-------------------------------------------------------------\n")
print("Welcome the the compound interest calculator 💵\n")
userOption = input("Press S to start or Q to quit: ")

# this loop will run on anything other than 'q'
# but ill keep it this way!
while not userOption.lower().strip() == 'q':
    principal = float(input("Initial amount you would like to invest: "))
    while principal <= 0:
        print("❌The principal can't be zero or under!")
        principal = float(input("Initial amount you would like to invest: "))
      
    interestRate = float(input("\nWhat is the Interest rate (as a %): "))
    while interestRate <= 0 or interestRate > 100:
        print("❌The interest rate can't be under zero or above 100!")
        interestRate = float(input("\nWhat is the Interest rate (as a %): "))
       
    nPerYear = float(input("\nNumber of times interest is added per year: "))
    while nPerYear <= 0 or nPerYear >= 13:
        print("❌The interest added per year must be between 1-12")
        nPerYear = float(input("\nNumber of times interest is added per year: "))

    years = float(input("\nHow many years: "))
    while years <= 0:
        print("❌The years can't be zero or under!")
        years = float(input("\nHow many years: "))

    interestRate2 = interestRate / 100

    finalAmount = principal*(1 + interestRate2 / nPerYear)**(years*nPerYear)
    print(f"\nYou then would have ${finalAmount:.2f}\n")
    userOption = input("Press S to start or Q to quit: ")


if userOption.lower().strip() == 'q':
    print("\n💵 Thank you 💵")

print("\n------------------------------------------------------------\n")