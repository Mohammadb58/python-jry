# 3x3 grid using nested lists

nums = [[1,2,3],[4,5,6],[]]

for numRow in nums:
    for num in numRow:
        print(num,'',end='')
    print()
print() 
#print(nums[-1][-1])
print(nums[-2][-1])