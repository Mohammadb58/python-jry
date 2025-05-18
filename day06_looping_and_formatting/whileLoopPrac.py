# More while loop 

print("----------------------------------")

print("Time to find the secret word 🔎")

userWord1 = input("What do you think the secret word is: ")

userWord2 = userWord1.strip() 

userWord = userWord2.lower() 

while not userWord.lower() == "me":
    print("❌ No, but here is a hint (The word is near us)")
    userWord = input("What do you think the secret word is: ")
    
    print("❌ No, think closer")
    userWord = input("What do you think the secret word is: ")
    
    print("❌ No, they’re always with you... like right now")
    userWord = input("What do you think the secret word is: ")
    
    print("❌ No, The answer’s staring you in the mirror")
    userWord = input("What do you think the secret word is: ")
    
    print("❌ No, Ok the answer is you")
    userWord = input("What do you think the secret word is: ")
    
    print("❌ Seriously, the answer is 'me'")
    userWord = input("What do you think the secret word is: ")
   
print("✅ After all (you!) were the secret word")

print("----------------------------------")