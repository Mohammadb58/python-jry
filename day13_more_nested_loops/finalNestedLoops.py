size=10
for i in range(1,size+1):
    for j in range(1,size+1):
        if i == j:
            print('D ', end="")
        elif i+j == size+1:
            print('A ', end="")
        else:
            print('- ', end="")
    print()