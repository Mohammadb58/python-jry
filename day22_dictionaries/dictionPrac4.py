# Deep Logic Play

capitals = {'France': 'Paris',
            'Japan' : 'Tokyo',
            'USA' : 'Washington'
}

userCountry = input("\nPlease enter a country: ").strip()
foundBool = False
for country, capital in capitals.items():
    if userCountry == country:
        print(f"The capital of {userCountry} is {capital}")
        foundBool = True
        break
    else:
        continue
if foundBool != True:
    print("\nCountry not found.")
