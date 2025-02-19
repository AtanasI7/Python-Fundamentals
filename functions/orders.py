def order(product, quantity):

    if product == 'coffee':
        return 1.5 * quantity
    elif product == 'coke':
        return 1.4 * quantity
    elif product == 'water':
        return 1 * quantity
    elif product == 'snacks':
        return 2 * quantity


ordered = input()
number = int(input())
final_price = order(ordered, number)

print(f"{final_price:.2f}")