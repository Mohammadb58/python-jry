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
'''

for i in range(5, 0, -1):
    for j in range(5-i):
        print(" ", end="")
    for k in range(1, i+1):
        print(f"{k} ", end="")
    print()