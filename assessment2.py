#Python Program for the purpose of the DevOps Assignment 2

assessment1, assessment2, assessment3 = eval(input("Enter the Assessment 1, Assessment 2, Assessment 3 Marks:"))

total_marks = (assessment1 * 20 + assessment2 * 40 + assessment3 *40)/100 

if total_marks > 85 and total_marks <= 100:
    print("HD")
elif total_marks > 75 and total_marks <=85:
    print("D")
elif total_marks > 65 and total_marks <=75:
    print("C")
elif total_marks >= 50 and total_marks <= 65:
    print("P")
else:
    print("F")
