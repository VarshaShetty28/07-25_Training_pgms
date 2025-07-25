def CGPA(marks, no_subs):
    grade_points = []
    total = 0
    failed = False

    for mark in marks:
        if mark >= 90:
            grade_points.append(10)
        elif mark >= 80:
            grade_points.append(9)
        elif mark >= 70:
            grade_points.append(8)
        elif mark >= 60:
            grade_points.append(7)
        elif mark >= 50:
            grade_points.append(6)
        elif mark >= 40:
            grade_points.append(5)
        else:
            grade_points.append(0)
            failed = True

   
    for grade in grade_points:
        total += grade
    CGPA_Obtained = total / no_subs
    CGPA_Obtained = round(CGPA_Obtained, 2)


    if failed:
        print(f" You have failed in one or more subjects.")
    else:
        print(" You passed all subjects!")

    print(f"Your CGPA is: {CGPA_Obtained}")


print(" Your CGPA Calculator")
no_subs = int(input("Enter your total number of subjects: "))
marks = []

for i in range(no_subs):
    val = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(val)

print("Your marks:", marks)
CGPA(marks, no_subs)
