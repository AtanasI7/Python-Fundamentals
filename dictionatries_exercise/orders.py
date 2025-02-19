def orders():
    data = input()
    all_products_info = dict()

    while data != 'buy':
        # price_quantity_info = list()
        data = data.split(' ')
        product = data[0]
        price = float(data[1])
        quantity = int(data[2])

        if product not in all_products_info.keys():
            all_products_info[product] = [price, quantity]
            # price_quantity_info.append(price)
            # price_quantity_info.append(quantity)
            # all_products_info[product] = price_quantity_info

        elif product in all_products_info.keys():
            all_products_info[product] = [price, (quantity + all_products_info[product][1])]

        data = input()

    for key, value in all_products_info.items():
        total_price = value[0] * value[1]
        print(f"{key} -> {total_price:.2f}")


orders()
