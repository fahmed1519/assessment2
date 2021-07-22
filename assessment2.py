#Python Program for the purpose of the DevOps Assignment 2

assessment1 = int(input("Enter the Assessment 1 Marks:"))
assessment2 = int(input("Enter the Assessment 2 Marks:"))
assessment3 = int(input("Enter the Assessment 3 Marks:"))

total_marks = (assessment1 * 20 + assessment2 * 40 + assessment3 *40)/100 

if total_marks > 90 and total_marks <= 100:
    print("HD")
elif total_marks > 70 and total_marks <=90:
    print("D")
elif total_marks > 60 and total_marks <=70:
    print("C")
elif total_marks >= 50 and total_marks <= 60:
    print("P")
else:
    print("F")
