import math

# calculating the area and circumference of a circle

calcType = input("Would you like to calculating the area or circumference of a circle? ")

if calcType == "circumference":
    radius = float(input("What is the radius of the circle? "))
    
    if radius >= 0:

        circumference = (2 * math.pi * radius)

        print (f"The circumference of the circle is {round(circumference, 2)}cm")
        
    else:
        print ("Invaild radius.")
    
elif calcType == "area":
    radius = float(input("What is the radius of the circle? "))
    
    if radius >= 0:

        #area = (math.pi * radius * radius)
        area = (math.pi * pow(radius, 2))

        print (f"The area of the circle is {round(area, 2)}cm^2")
        
    else:
        print ("Invaild radius.")

else:
    print ("Sorry, invaild input.")