users = []
usernames = []
userages = []
for i in range (0,3):
    userInput = input("Enter a name: ")
    userInput2 = input("Enter their age: ")
    users.append([userInput, userInput2])
     
for user in users:
    print(user, '', end='')
