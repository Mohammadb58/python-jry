# While loop practice 

print("----------------------------------")

name1 = input("Please enter my name: ")

name2 = name1.strip()
name = name2.lower()

while not name.lower() == "mohammad":
    print("❌ You can't spell my name!😔")
    name = input("Please enter my name: ")

print(f"✅Yup, that is how u spell my name {name.upper()} ☺️")

print("----------------------------------")