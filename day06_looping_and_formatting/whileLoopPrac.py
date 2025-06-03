# More while loop 

print("----------------------------------")

print("\nTime to find the secret word 🔎")

counter = 0

userWord1 = input("\nWhat do you think the secret word is: ")

userWord2 = userWord1.strip() 

userWord = userWord2.lower() 

while userWord.lower() != "me":
    if counter == 0:
        print("\n❌ No, but here is a hint (The word is near us)")
        userWord = input("\nWhat do you think the secret word is: ")
        counter += 1
    
    elif counter == 1:
        print("\n❌ No, think closer")
        userWord = input("\nWhat do you think the secret word is: ")
        counter += 1
    
    elif counter == 2:
        print("\n❌ No, they’re always with you... like right now")
        userWord = input("\nWhat do you think the secret word is: ")
        counter += 1
    
    elif counter == 3:
        print("\n❌ No, The answer’s staring you in the mirror")
        userWord = input("\nWhat do you think the secret word is: ")
        counter += 1
    
    elif counter == 4:
        print("\n❌ No, Ok the answer is you")
        userWord = input("\nWhat do you think the secret word is: ")
        counter += 1
    
    else:
        print("\n❌ Seriously, the answer is 'me'")
        userWord = input("\nWhat do you think the secret word is: ")
   
print("\n✅ After all (you!) were the secret word")

print("----------------------------------")