def values(data):
    data = data.split(', ')
    ascii_dict = dict()

    for i in data:
        ascii_dict[i] = ord(i)

    print(ascii_dict)


info = input()
values(info)