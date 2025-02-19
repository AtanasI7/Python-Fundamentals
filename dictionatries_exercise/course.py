def learning_courses():
    data = input()
    study_course = dict()
    condition = False

    while True:

        if data == 'end':
            condition = True
            break

        data = data.split(' : ')
        course = data[0]
        student_name = data[1]

        if course not in study_course.keys():
            study_course[course] = []
        study_course[course].append(student_name)

        data = input()

    if condition:
        for key, value in study_course.items():
            print(f"{key}: {len(value)}")
            for i in value:
                print(f"-- {i}")


learning_courses()
