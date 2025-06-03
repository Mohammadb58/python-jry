#Student Score Tracker V2
students = [] # main list with names and grades
numOfStudents = 0
overallTotal = 0
noneEmptyListBool = False
print('\n-----------------------------------------------------')
print("\nWlecome to the Student Score Tracker")

while True:
    name = input("\nPlease enter a Student name ('q' to quit): ").strip()
    if name.lower() == 'q':
        break
    else:
        grade = input("\nPlease enter their grade: ").strip()
        gradeDigBool = grade.isdigit()
        if gradeDigBool == True:
            students.append([name, grade])
        else:
            print("\nInvaild")
            break

for student in students:
    noneEmptyListBool = True
    highestGrade = int(student[1])
    lowestGrade = int(student[1])
    break
if noneEmptyListBool == True:
    for student in students:
        overallTotal += int(student[1])
    print(overallTotal)
    total = overallTotal / len(students)
    print(f"\n- Your list has {len(students)} student/s.")
    print(f"\n- The average grade in your list is {total:.2f}.")
    
    for student in students:
        if int(student[1]) >= highestGrade:
            highestGrade = int(student[1])
        elif int(student[1]) <= lowestGrade:
            lowestGrade = int(student[1])
        else:
            continue
    print(f"\nThe highest grade is {highestGrade}")
    print(f"\nThe lowest grade is {lowestGrade}")
    for student in students:
        print('\n',student)
else:
    print("\nSorry please try vaild inputs\n")
    
    
# NOTES:
    #Allow users input after invaild input
    #What if there are 2,3.. Top Grades