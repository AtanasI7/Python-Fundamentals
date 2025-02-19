def validation(data):
    digits_counter = 0
    listed_data = list()
    checker_list = list()
    condition = False
    for i in data:
        listed_data.append(i)

    if not 6 <= len(data) <= 10:
        print('Password must be between 6 and 10 characters')

    for n in listed_data:
        if n.isdigit() or n.islower() or n.isupper():
            checker_list.append(n)
        else:
            condition = True

        if n.isdigit():
            digits_counter += 1

    if condition:
        print('Password must consist only of letters and digits')

    if digits_counter < 2:
        print('Password must have at least 2 digits')

    if listed_data == checker_list:
        if 6 <= len(data) <= 10:
            print('Password is valid')


password = input()
validation(password)