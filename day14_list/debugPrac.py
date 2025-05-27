# more list practice
nums = ['1','2','3','4','5','6','7','8','9']
#nums = []

# this pops the index 
#nums.pop(1)
nums.pop(1)

for num in nums:
    print(num, "", end="")
    

nums = []

nums.remove('1')
for num in nums:
    print(num, "", end="")

nums = ['2']

print(nums.index('1'))
for num in nums:
    print(num, "", end="")
    

nums = [1,2,'6',4,5]

nums.sort()
for num in nums:
    print(num, "", end="")
 
 
alphs = ['@','b','d','@']

alphs.sort()
for alph in alphs:
    print(alph, "", end="")
    

nums = [1,2,3,4,5]

nums.insert(100, 0)
for num in nums:
    print(num, "", end="")

nums = []

nums.reverse()
for num in nums:
    print(num, "", end="")
    

nums1 = [1,2,3,4,5]
#nums1.pop(1)
nums2 = nums1.copy()
nums1.pop(1)
for i in nums1:
    print(i,"",end="")
print()
#nums2.pop(1)
#nums2.remove(1)
for j in nums2:
    print(j,"",end="")
   