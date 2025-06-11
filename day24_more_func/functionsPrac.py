# functions practice

# Task #1
# Greet the User
wordToNum = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "twenty-one": 21, "twenty two": 22, "twenty-three": 23, "twenty four": 24, "twenty-five": 25,
    "twenty-six": 26, "twenty-seven": 27, "twenty-eight": 28, "twenty-nine": 29, "thirty": 30
}

def greeting(name, age):
    print(f"Hello {name}!")
    print(f"You are {age} years old, happy bday!")

name = input("Please enter your name: ").strip().capitalize()
nameCheck = bool(name)
while nameCheck == False:
    print("Invaild name!")
    name = input("Please enter your name: ").strip().capitalize()
    nameCheck = bool(name)

age = input("Please enter your age: ")
if age not in wordToNum:
    ageCheckBool = age.isdigit()
    if ageCheckBool == True:
        age = int(age)
        while age <= 0:
            print("Invaild age!")
            age = int(input("Please enter your age: "))
    else:
        print("Invaild age!")
        
greeting(name, age)