# Student Score Tracker
list = []
avrList = []
name = ''
totalScore = 0
counter = 0
highestScore = score
lowestScore = score
print("\nWlecome to the Student Score Tracker")

while True:
    subList = []
    name = input("\nPlease enter the name: ").strip().lower()
    if name == 'q' or name == 'quit':
        break
    subList.append(name)
    score = int(input("\nPlease enter the score: "))
    if score == 'q' or score == 'quit':
        break
    subList.append(score)
    list.append(subList)
            
print(f"\nThe length of your list is", len(list))
'''
for score in list:
    if list[1]:
        avrList.append(score)
    else:
        continue
'''

for student in list:
    avrList.append(student[1])
    
for score in avrList:
    totalScore += score
    counter += 1
total = totalScore / counter
print(f"\nThe avrage score of your list is {total:.2f}")

for score in avrList:
    highestScore = score
    lowestScore = score
    if score >= highestScore:
        highestScore = score
    elif score < lowestScore:
        lowestScore = score
    else:
        continue
print(f"\nThe highes score is {highestScore} and lowest was {lowestScore}")

for student in list:
    if student[1] == highestScore:
        print(f"The highes score was by {student[0]}")
    elif student[1] == lowestScore:
        print(f"The lowest score was by {student[0]}")
    else:
        continue
