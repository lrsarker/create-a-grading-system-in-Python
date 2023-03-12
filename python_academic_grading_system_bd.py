#Grading System
marks = float(input("Enter Marks: "))
letter_grade = 'F'
grade_point = 0

if marks >= 101:
    print("Enter valid Marks (Passing Number is 100 to 33)")
elif marks >= 80:
    letter_grade = 'A+'
    grade_point = 5
    print("Marks: ", marks)
    print("Grade Point: ", letter_grade)
    print("Latter Grade: ", grade_point)
elif marks >= 70:
    letter_grade = 'A'
    grade_point = 4
    print("Marks: ", marks)
    print("Grade Point: ", letter_grade)
    print("Latter Grade: ", grade_point)
elif marks >= 60:
    letter_grade = 'A-'
    grade_point = 3.5
    print("Marks: ", marks)
    print("Grade Point: ", letter_grade)
    print("Latter Grade: ", grade_point)
elif marks >= 50:
    letter_grade = 'B'
    grade_point = 2
elif marks >= 40:
    letter_grade = 'C'
    grade_point = 1
    print("Marks: ", marks)
    print("Grade Point: ", letter_grade)
    print("Latter Grade: ", grade_point)
elif marks >= 33:
    letter_grade = 'D'
    grade_point = 1
    print("Marks: ", marks)
    print("Grade Point: ", letter_grade)
    print("Latter Grade: ", grade_point)
elif marks <= 32:
    letter_grade = 'F'
    grade_point = 0
    print("Marks: ", marks)
    print("Grade Point: ", letter_grade)
    print("Latter Grade: ", grade_point)
else:
    print("Something went wrong, Try Again!")
    
