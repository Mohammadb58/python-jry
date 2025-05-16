# practice string methods


fullName = "Mohammad Abu Rashed "

print(fullName)

lengthName = len(fullName)

print(lengthName)

firstOccur = fullName.find("M")

print(firstOccur)

lastOccur = fullName.rfind("m")

print(lastOccur)

letterCap = fullName.capitalize()

print(letterCap)

upperCase = fullName.upper()

print(upperCase)

lowerCase = fullName.lower()

print(lowerCase)

isItAllDigits = fullName.isdigit()

print(isItAllDigits)

# whitspace count so my string will cause a False flag
isItAllAlpha = fullName.isalpha()

print(isItAllAlpha)

count = fullName.count('m') # "m" == 'm' 

print(count)

#cap each word in the string
title = fullName.title()

print(title)

#removes leading and trailing whitespace
strip = fullName.strip()

print(strip)

replace = fullName.replace("m", "-")

print(replace)

replace2 = fullName.replace("M", "_")

print(replace2)

replace3 = fullName.replace("m", "-", 1)

print(replace3)


testCase = ""
testCaseTwo = "   "
testCaseThree = " >2> "

length = len(testCase)

print(len)

lenTwo = len(testCaseTwo)

print(lenTwo)

lenThree = len(testCaseThree)

print(f"{lenThree} look here") # next time organize it better

find = testCase.find("")

print(find)

find2 = testCase.find(" ")

print(find2)

find3 = testCaseTwo.find("")

print(find3)

find4 = testCaseTwo.find(" ")

print(find4)

find5 = testCaseTwo.rfind(" ")

print(find5)

find6 = testCase.upper()

print(find6) # returns nothing!

find7 = testCaseTwo.upper()

print(find7)

find8 = testCaseThree.upper()

print(find8)

find9 = testCase.lower()

print(find9) # returns nothing!

find10 = testCaseTwo.lower()

print(find10)

find11 = testCaseThree.lower()

print(find11)

find12 = testCase.isalpha()

print(find12)

find13 = testCaseTwo.isalpha()

print(find13)

find14 = testCaseThree.isalpha()

print(find14)

find15 = testCase.count(" ")

print(find15)

find15 = testCase.count("")

print(find15)

find16 = testCaseTwo.count(" ")

print(find16)

find17 = testCaseTwo.count("")

print(find17)

find18 = testCaseThree.count(" ")

print(find18)

find19 = testCaseThree.count("")

print(find19)

find18 = testCase.replace("", "-")

print(find18)

find19 = testCaseTwo.replace("", "-")

print(find19)

find20 = testCaseTwo.replace(" ", "-")

print(find20)

find21 = testCaseThree.replace(" ", "2")

print(find21)
