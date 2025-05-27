# List Tracker

names = []

userinput = ''
print("\nWlecome to the List Tracker")

while userinput != 'stop':    
    userinput = input("\nPlease enter a name ('stop' to quit): ").strip().lower()
    
    names.append(userinput)
print("\nYour list has", end="")
names.remove('stop')
for name in names:
    print(", ", name, end="")

userinput2 = input("\nWould u like to see many times “e.g. Ali” appears in the list (Y/N)? ").strip().lower()

if userinput2 == 'y':
    userName = input("\nWhat is the name you would like to check? ").strip().lower()
    print(f"{userName} appeared ", end="")
    print(names.count(userName), "time/s")
else:
    print("\nBye")
    