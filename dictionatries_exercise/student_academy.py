def student_academy():
    number = int(input())
    student_grades = dict()


    for i in range(1, number + 1):
        name = input()
        grade = float(input())

        if name not in student_grades.keys():
            student_grades[name] = []
        student_grades[name].append(grade)

    for student, grades in student_grades.items():
        average_grade = sum(grades) / len(grades)
        if average_grade >= 4.5:
            print(f"{student} -> {average_grade:.2f}")


student_academy()