# Practicing Dictionary
dictionary = {'Mohammad' : 90,
              'Ali' : 88,
              'Malek' : 99} 

for name, grade in dictionary.items():
    print(name, '', grade)
print()   
# This will return the value of the given key
# 90 in this case
print(dictionary.get('Mohammad'))

print()

# this updated Mohammad's grade to 100
dictionary.update({'Mohammad' : 100})

for name, grade in dictionary.items():
    print(name, '', grade)

print()
# this adds a new key nd value    
dictionary.update({'NO ONE' : 100})

for name, grade in dictionary.items():
    print(name, '', grade)
print()

# this pops 'NO ONE" from the dictionary
dictionary.pop('NO ONE')

for name, grade in dictionary.items():
    print(name, '', grade)
print()

# this removes the most recent key and its value
# does not takr any args
dictionary.popitem()

for name, grade in dictionary.items():
    print(name, '', grade)
print()

print(dictionary.keys())
print()

print(dictionary.values())
print()

print(dictionary.items())
