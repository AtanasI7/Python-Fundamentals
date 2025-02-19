def stock(data, needed_items):
    stocked = dict()

    for key in range(0, len(data), 2):
        food = data[key]
        value = int(data[key + 1])
        stocked[food] = value

    for i in needed_items:
        if i in stocked.keys():
            print(f"We have {stocked[i]} of {i} left")
        else:
            print(f"Sorry, we don't have {i}")

info = input().split(' ')
searching_products = input().split(' ')
stock(info, searching_products)

