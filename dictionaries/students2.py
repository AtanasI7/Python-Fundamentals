def students(data):
    courses = dict()

    while ':' in data:
        data = data.split(':')
        name = data[0]
        id = data[1]
        course = data[2]

        if course not in courses.keys():
            courses[course] = dict()

        courses[course][id] = name

        data = input()

    data = data.replace('_', ' ')

    for id in courses[data]:
        print(f"{courses[data][id]} - {id}")

info = input()
students(info)