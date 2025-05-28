# Keyword Filter

userSen = []
counter = 0
count = 0
while True:
    userInput = input("\nWhat is on your mind? like a journal or notes ('q' to Quit): ").strip().lower()
    if userInput == 'q' or userInput == 'quit':
        break
    userSen.append(userInput)

for sen in userSen:
    print(f'- {sen}')
    counter += 1
print(f"\nYou have entered {counter} total sentences")

userOption = input("\nWould you like to search any keyword: ").strip().lower()
if userOption == 'y' or userOption == 'yes':
    userWord = input("\nWhat is the word you would like to search: ").strip().lower()
    for word in userSen:
        #if userWord in word:
            # "he" matches "the"
            # which is a fix i need to do
            # print(f"= {word}")
            # count += 1
        #for subWord in word2:
            #if subWord == userWord:
                #print(f"- {subWord}")
                #count+=1
            #else:
                #continue
        word2 = word.split()
        if userWord in word2:
            print(f"- {word}")
        count += word2.count(userWord)
    
    print(f"\n'{userWord}' appeared {count} time/s\n")  

else:
    print("\nThanks, bye!\n")