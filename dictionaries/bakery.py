def bakery(data):
    vakery = dict()

    for i in range(0, len(data), 2):
        food = data[i]
        quantity = int(data[i + 1])

        vakery[food] = quantity

    print(vakery)


info = input().split(' ')
bakery(info)

