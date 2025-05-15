# temperature conversion

print("Temperature Conversion")

tempOne = input("Would you like to convert from Fahrenheit or Celsius (F/C): ")

tempNumber = float(input(f"Please enter the temp in {tempOne}: "))

FahToCel = ((tempNumber - 32) * 5/9)

CelToFah = ((tempNumber * (9/5)) + 32)

if (tempOne == "F") or (tempOne == "f"):
    print(f"{tempNumber}{tempOne} to Celsius is {round(FahToCel, 3)}C.")

elif (tempOne == "C") or (tempOne == "C"):
    print(f"{tempNumber}{tempOne} to Fahrenheit is {round(CelToFah, 3)}F.")

else: 
    print("Invaild input")