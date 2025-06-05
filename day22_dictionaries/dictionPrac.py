# More Dictionaries Practice

dictionarie = {'Mohammad' : 90, 'Ali' : 88, 'Malek' : 95}

for name in dictionarie.keys():
    print(name)
print()

for grade in dictionarie.values():
    print(grade)
print()

dictionarie.update({'Ali' : 70})

for name, grade in dictionarie.items():
    print(name, '', grade)
print()

dictionarie.update({'Abdullah' : '85'})

for name, grade in dictionarie.items():
    print(name, '', grade)
print()

dictionarie.pop('Abdullah')

for name, grade in dictionarie.items():
    print(name, '', grade)
print()