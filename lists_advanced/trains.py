def train(number, data):
    num_wagons = list()
    command = data[0]
    for i in range(1, number + 1):
        num_wagons.append(0)

    while command != 'End':
        if command == 'add':
            people = int(data[1])
            num_wagons[-1] += people

        elif command == 'insert':
            index = int(data[1])
            people = int(data[2])
            num_wagons[index] += people

        elif command == 'leave':
            index = int(data[1])
            people = int(data[2])
            num_wagons[index] -= people

        data = input().split(' ')
        command = data[0]
    print(num_wagons)


wagons = int(input())
information = input().split(' ')
train(wagons, information)

