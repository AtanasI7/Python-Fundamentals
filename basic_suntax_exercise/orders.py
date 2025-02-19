num_of_orders = int(input())
whole_price = 0

for order_price in range(1, num_of_orders + 1):
    capsule_price = float(input())
    days = int(input())
    capsule_count = int(input())

    price = days * capsule_count * capsule_price
    print(f'The price for the coffee is: ${price:.2f}')
    whole_price += price


print(f'Total: ${whole_price:.2f}')

