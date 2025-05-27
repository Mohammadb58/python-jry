nums = [1,2,3,[4,5,6],7,8,9]

for num in nums:
    print(num, "", end="")
    
    
numsCopy = nums.copy()

nums[3].remove(4)

print()
for numCopy in nums:
    print(numCopy, "", end="")
    
print()

for num in nums:
    print(num, "", end="")