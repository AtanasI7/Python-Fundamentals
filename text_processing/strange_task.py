def strange():
    data = input()
    number_list = list()
    letters_list = list()
    other_list = list()
    for i in data:
        if i.isdigit():
            number_list.append(i)
        elif i.isupper() or i.islower():
            letters_list.append(i)
        else:
            other_list.append(i)

    print(f"{''.join(number_list)}\n{''.join(letters_list)}\n{''.join(other_list)}")

strange()