def repeater():
    data = input().split(' ')

    for i in data:
        print(i * len(i), end='')


repeater()