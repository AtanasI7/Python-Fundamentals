numbers = input().split(' ')
abs_list = list()


def testing():

    for n in numbers:
        current_number = abs(float(n))
        abs_list.append(current_number)

    print(abs_list)

testing()
