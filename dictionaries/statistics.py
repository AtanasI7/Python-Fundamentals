def statistics(data):
    stats = dict()

    while data != 'statistics':
        data = data.split(':')
        food = data[0]
        quantity = int(data[1])
        if food in stats.keys():
            stats[food] += quantity
        else:
            stats[food] = quantity


        data = input()

    print('Products in stock:')
    for i in stats:
        print(f"- {i}: {stats[i]}")
    print(f"Total Products: {len(stats)}")
    print(f"Total Quantity: {sum(stats.values())}")

info = input()
statistics(info)

