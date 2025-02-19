def students(data):
    pb = dict()
    fund = dict()
    adv = dict()

    while ':' in data:
        data = data.split(':')
        name = data[0]
        id = int(data[1])
        course = data[2]

        if course == 'programming basics':
            pb[name] = id

        elif course == 'fundamentals':
            fund[name] = id

        elif course == 'advanced':
            adv[name] = id

        data = input()

        if data == 'programming basics':
            for key in pb:
                print(f"{pb} - {pb[key]}")
                break

        elif data == 'fundamentals':
            for key in pb:
                print(f"{pb} - {pb[key]}")
                break

        elif data == 'advanced':
            for key in pb:
                print(f"{pb} - {pb[key]}")
                break


info = input()
students(info)

