#Python Program for the purpose of the DevOps Assignment 2

assessment1 = int(input("Enter the Assessment 1 Marks:"))
assessment2 = int(input("Enter the Assessment 2 Marks:"))
assessment3 = int(input("Enter the Assessment 3 Marks:"))

total_marks = (assessment1 * 20 + assessment2 * 40 + assessment3 *40)/100 

grade = "F"
if total_marks > 85 and total_marks <= 100:
    grade = "HD"
elif total_marks > 75 and total_marks <=85:
    grade = "D"
elif total_marks > 65 and total_marks <=75:
    grade = "C"
elif total_marks >= 50 and total_marks <= 65:
    grade = "P"
else:
    grade = "F"

print(grade)
