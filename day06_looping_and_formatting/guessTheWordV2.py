# V2 of my old version that didn't work  

print("----------------------------------")

print("Time to find the secret word 🔎")

userWord = input("What do you think the secret word is: ")

userWord2 = userWord.strip().lower()
guessCounter = 1

while not userWord2 == "me":
    if guessCounter == 1:
        print("❌ No, but here is a hint (The word is near us)")
        userWord2 = input("What do you think the secret word is: ")
        userWord2 = userWord2.strip().lower()
        guessCounter = 2
    elif guessCounter == 2:
        print("❌ No, think closer")
        userWord2 = input("What do you think the secret word is: ")
        userWord2 = userWord2.strip().lower()
        guessCounter = 3
    elif guessCounter == 3:
        print("❌ No, they’re always with you... like right now")
        userWord2 = input("What do you think the secret word is: ")
        userWord2 = userWord2.strip().lower()
        guessCounter = 4
    elif guessCounter == 4:
        print("❌ No, The answer’s staring you in the mirror")
        userWord2 = input("What do you think the secret word is: ")
        userWord2 = userWord2.strip().lower()
        guessCounter = 5
    elif guessCounter == 5:
        print("❌ No, Ok the answer is you")
        userWord2 = input("What do you think the secret word is: ")
        userWord2 = userWord2.strip().lower()
        guessCounter = 6
    else:
        print("❌ Seriously, the answer is 'me'")
        userWord2 = input("What do you think the secret word is: ")
        userWord2 = userWord2.strip().lower()
        
print("✅ After all (you!) were the secret word")

print("----------------------------------")