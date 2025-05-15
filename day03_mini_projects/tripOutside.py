# How is the weather outside?
# there are still too many improvements to be made

print("The Weather Outside. Let's check if you should go outside.")

temp = float(input("What is the temp outside in Fahrenheit: "))

weather = input("Is is Sunny, Cloudy, Rainy, or Snowy: ")

if (temp < 20) and ((weather == "Sunny") or (weather == "Cloudy") or (weather == "Rainy") or (weather == "Snowy")):
    print("That is too cold. Enjoy the weather from the window.")
    
elif ((temp > 21 and temp < 34)) and ((weather == "Snowy") or (weather == "Rainy")):
    print("It is cold. Stay inside and make a cup hot chocolate.")
    
elif ((temp > 21) and (temp < 34)) and ((weather == "Sunny") or (weather == "Cloudy")):
    print("It is still cold but if you can handel it, open the window.")
    
elif ((temp > 35) and (temp < 44)) and ((weather == "Snowy") or (weather == "Rainy")):
    print("I'd recommend to stay inside.")

elif ((temp > 35) and (temp < 44)) and ((weather == "Sunny") or (weather == "Cloudy")):
    print("Cold but if you can handel it go for a walk")
    
elif ((temp > 45) and (temp < 54)) and ((weather == "Rainy") or (weather == "Snowy")):
    print("Only if you like the rain.")

elif ((temp > 45) and (temp < 54)) and ((weather == "Cloudy") or (weather == "Sunny")):
    print("Not too bad for a walk outside")
    
elif ((temp > 55) and (temp < 70)) and ((weather == "Cloudy") or (weather == "Sunny")):
    print("It perfect outside. Go for a walk.")
 
elif ((temp > 55) and (temp < 70)) and (weather == "Rainy"):
     print("Rainy but not too bad for a walk outside")

elif ((temp > 71) and (temp < 85)) and ((weather == "Sunny") or (weather == "Cloudy")):
    print("Too hot don't forget to apply sunscreen")

elif temp > 86:
    print("That is too hot stay inside")
    
else:
    print("Honestly it's hard to tell")