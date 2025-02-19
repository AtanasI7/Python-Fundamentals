def students(data):
    courses = dict()

    while ':' in data:
        (name, id, course) = data.split(':')

        if course not in courses:
            courses[course] = dict()

        courses[course][id] = name

        data = input()

    data = data.replace('_', ' ')

    for i in courses[data]:
        print(f"{courses[data][i]} - {i}")


info = input()
students(info)