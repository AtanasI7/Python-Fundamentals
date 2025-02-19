item_price = input().split('|')
budget = float(input())
profit = 0
new_budget = 0
profit_list = list()
condition = False


for a in item_price:
    a = a.split('->')
    item = a[0]
    price = float(a[1])
    condition = False

    if price <= budget:
        if item == 'Clothes':
            if price <= 50:
                condition = True

        if item == 'Shoes':
            if price <= 35:
                condition = True

        if item == 'Accessories':
            if price <= 20.50:
                condition = True

    if condition:
        budget -= price
        new_price = price * 0.4 + price
        current_profit = new_price - price
        profit += current_profit
        new_budget += new_price
        profit_list.append(f'{new_price:.2f}')

budget += new_budget

print(' '.join(profit_list))
print(f'Profit: {profit:.2f}')
if budget >= 150:
    print(f"Hello, France!")

else:
    print('Not enough money.')