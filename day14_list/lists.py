names = ['mohammad', 'ali', 'adam']

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