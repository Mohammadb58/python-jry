# Weight Converter

print("Weight Converter")

userOption = input("Would you like to convert from (lb/kg): ")

userNumber = float(input("How much would you like to convert: "))

lbToKg = userNumber * 0.453592

kgToLb = userNumber * 2.20462


if (userOption == "lb") or (userOption == "LB"):    
    print(f"{userNumber}lb to kg is {round(lbToKg, 2)}.")
    
elif (userOption == "kg") or (userOption == "KG"):    
    print(f"{userNumber}kg to lb is {round(kgToLb, 2)}.")

else:
    print("Invaild input")
    userOption2 = input("Would you like to convert again (Yes/No): ")
    
    if (userOption2 == "Yes") or (userOption2 == "yes"):
        
        userOptionTwo = input("Would you like to convert from (lb/kg): ")
        userNumberTwo = float(input("How much would you like to convert: "))
        lbToKg2 = userNumberTwo * 0.453592

        kgToLb2 = userNumberTwo * 2.20462
        
        if (userOptionTwo == "lb") or (userOptionTwo == "LB"):    
            print(f"{userNumberTwo}lb to kg is {round(lbToKg2, 2)}.")
    
        elif (userOptionTwo == "kg") or (userOptionTwo == "KG"):    
            print(f"{userNumberTwo}kg to lb is {round(kgToLb2, 2)}.")
    
    elif (userOption2 == "No") or (userOption2 == "no"):
        print("No problem")
        
    else:
        print("Invaild input")
    
print("Have a good day.")