names = ['mohammad', 'ali', 'adam', 'ali']

for name in names:
    print(name, "- ", end="")
print()

print("-----------------------------")

print(('mohammad') in names or ('malek') in names)
# returns TRUE in this case 

print("-----------------------------")

print('malek' in names)
# returns FALSE in this case

print("-----------------------------")


names[0] = 'malek'
for name in names:
    print(name, "- ", end="")
print()
print("-----------------------------")

names.append('MK')
for name in names:
    print(name, "- ", end="")
print()

print("-----------------------------")

names.remove('ali')
for name in names:
    print(name, "- ", end="")
print()

print("-----------------------------")

names.insert(10, 'MK')
for name in names:
    print(name, "- ", end="")
print()

print("-----------------------------")

names.reverse()
for name in names:
    print(name, "- ", end="")
print()

print("-----------------------------")

names.clear()
for name in names:
    print(name, "- ", end="")
print()

print("-----------------------------")

# this wont run becuase the list is clear 
print(names.index("malek"))

print("-----------------------------")

print(names.count("ali"))

print("-----------------------------")
