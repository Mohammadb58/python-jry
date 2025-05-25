'''
for rows in range(1,6):
    for cols in range(1,6):
        if (rows + cols) % 2 ==0:
            print("A ", end="")
        else:
            print("B ", end="")
    print()
print("-----------------------------")    
# does the same thing as above but shorter    
for rows in range(1,6):
    for cols in range(1,6):
        print("A ", end="") if (rows + cols) % 2 ==0  else print("B ", end="")
    print()
print("-----------------------------")    

counter = 1   
for i in range(1,6):
    for j in range(counter,counter+5):
        #print(j,"",end="")
        # This did not work because the counter
        # starts at 1 so it print 5 O's then it
        # then it starts at 6 so it prints 5 E's
        # but what we wanted was each num aka 'j'
        #print("O ", end="") if counter %2 != 0 else print("E ", end="")
        print("O ", end="") if j %2 != 0 else print("E ", end="")
    print()
    counter+=5
print("-----------------------------")    
'''
size=10
for i in range(1,size+1):
    for j in range(1,size+1):
        if i == 1 or i == size:
            print("* ", end="")
        else:
            if j==1 or j==size:
                print("* ", end="")
            else:
                print("  ",end="")
    print()