def finder():
    data = input()

    result = [data[i] + data[i + 1] for i in range(len(data)) if i == ':' and data[i + 1] != ' ']
    for n in result:
        print(n)

    for i in range(len(data)):
        if data[i] == ':':
            if data[i + 1] != ' ':
                emoji = f'{data[i]}{data[i + 1]}'
                print(emoji)


finder()

