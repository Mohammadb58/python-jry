# While loop practice 

print("----------------------------------")

name = input("Please enter my name: ")

name2 = name.strip().lower()

print(f"{name2} <---")

while not name2 == "mohammad":
    print("❌ You can't spell my name!😔")
    name2 = input("Please enter my name: ")
    name2 = name2.strip().lower()

print(f"✅Yup, that is how u spell my name 'Mohammad' ☺️")

print("----------------------------------")