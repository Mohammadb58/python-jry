list = [1,2,2,3,4,5]

print(list.count(6))

fruits = ['apple', 'orange', 'apple']

print(fruits.index('apple'))

fruits.insert(-100, 'ghost')

for fruit in fruits:
    print(fruit,"",end="")
    
x= fruits.sort()
print()
for fruit in fruits:
    print(fruit,"",end="")
    
print(x)


original = ['banana', 'apple', 'cherry']
copy = original.copy()

copy.sort()

print("Original:", original)
print("Copy:", copy)
