'''
# split practice 
userList = 'm o h a m m a d'
print(userList.split(' '))

userInput = input("Enter what ever on your mind: ")

print(userInput.split())

userInput = input("Enter what ever on your mind: ")

print(userInput.split(' '))


# bool testing (typecast)

bool1 = True

print(type(bool1))

bool2 = False

print(type(bool2))

bool3 = 0

print(type(bool3))

bool4 = 1

print(type(bool4))

bool5 = ' '

print(type(bool5))

bool = 1
print(bool)

bool = 11
print(bool)


print(bool(''))
print(bool('False'))
# the bool is ONLY checking if there is anything here
print(bool('falsee'))
print(bool(1))
print(bool({False}))
print(bool([]))


# for loops practice 

for i in range(1,11):
    print(i, '', end='')
print() 

# it wont run w/o the -1 step
for j in range(10,0,-1):
    print(j, '', end='')

print() 
for k in range(0,21,2):
    print(k,'',end='')

print() 
for l in range(0,21,200):
    print(l,'',end='')

print() 
for m in range(0,21,-200):
    print(m,'',end='')
    
print() 
for n in range():
    print(n,'',end='')
'''

# ,count() practice/review

name = 'mohammad a'
print(name.count(' '))
print(name.count(''))
print(name.count('m'))
# int not allowed
#print(name.count(1))
print('-----------------------')
#num = 123456789
num = '123456789'
print(num.count(' '))
print(num.count(''))
print(num.count('4'))

print('-----------------------')
listA = ['moe', 'ali', 'mk']
print(listA.count(' '))
print(listA.count(''))
print(listA.count('ali'))
print(listA)
