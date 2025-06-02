# example 1
names = []
entry = []

for i in range(3):
    name = input("Enter a name: ").strip()
    entry.append(name)
    names.append(entry)

print(names)

# DEBUGGING
for i in entry:
    print(i,'',end='')
print()
for j in names:
    print(j,'',end='')
# conc, this works like nested loops
# each full entery list an inner loop
print('--------------------------------')
entry.append("SNEAKY")
print(names)
