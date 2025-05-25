'''
for i in range (1,4):
    for j in range(1,4):
        print(f" inner loop -{j}- ", end="")
    print(f" outer loop -{i}- ")
 
 
 
 
for i in range(1,4):
    print(i)
    for j in range(1,4):
        print(j, end="")
        
        
for i in range(1,4):
    print(f"Row {i}: ",end="")
    for j in range(1,4):
        print(f"{j} ", end="")
    print()
   


for i in range(1,6):
    for k in range(5-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(f"{j } ", end="")
    print()


for i in range(5, 0, -1):
    for j in range(5-i):
        print(" ", end="")
    for k in range(1, i+1):
        print(f"{k} ", end="")
    print()

    
for i in range(1,7):
    #if i % 2 == 0:
        #print(". ", end="")
    #else:
        #print("# ", end="")
    for j in range(1,7):
        if (j + i)%2 == 0:
            print("# ", end="")
        else:
            print(". ", end="")    
    print()

print('1 2 3 4 5')
print('2 4 6 8 10')
print('3 6 9 12 15')
print('4 8 12 16 20')
print('5 10 15 20 25')
print('-------------')

for i in range(1,6):
    for j in range(1,6):
        print(f"{j * i} ", end="")
    print() 

        
for i in range(1,10):
    if i<=5:
        for j in range(5-i):
            print(" ", end="")
        for k in range(1, i+1):
            print(f"{k} ", end="")
    else:
        for j in range(i-5):
            print(" ", end="")
        for k in range(1, 11-i):
            print(f"{k} ", end="")
    print()
    
for i in range(1,6):
    for j in range(10-2*i):
        print(" ", end="")
    for k in range(1, i+1):
        print(f" {k}  ", end="")
    print()
    '''
for i in range(1, 6):
    for j in range(10 - 2 * i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(f"{k:<3}", end="")
    print()
