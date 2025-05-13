# if else & typecasting

#P1 
carCondition = False 


if carCondition:
    print ("The car is in good condition")
else:
    print ("The car is in bad condition")
    
    
#P2
phoneCharge = 100
 
if phoneCharge >= 100:
    print ("Fully charged")
else:
    print ("Needs charge")


#P3 
temp = 60

if temp > 90:
    print ("Its too HOT")
else:
    print ("Its nice outside") 
    
# Typecasting

firstName = "Mohammad"
age = 20
gpa = 3.2
#isStudent = 1
isStudent = True

age = float(age)

firstName = bool(firstName)

print (firstName)
print (age)
