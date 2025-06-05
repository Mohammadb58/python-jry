# using lists as values this time

dictionary = {'Class 100' : [100, 50], 'Class 200' : [88, 77, 90], 'Class 300' : [77, 87, 93]}

dictionary['Class 100'].append(70)

for name, grades in dictionary.items():
    print(name, '', grades)
print()

total = 0 
count = 0
for grade in dictionary['Class 100']:
    total += grade
    count += 1
newTotal = total / count
print(f"Class 100 avr grade is {newTotal}")