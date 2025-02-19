decoration_quantity = int(input())
days_left = int(input())
budget = 0
spirit = 0
condition_5th_day = False


for day in range(1, days_left + 1):
    condition_5th_day = False

    if day % 11 == 0:
        decoration_quantity += 2

    if day % 2 == 0:
        spirit += 5
        budget += 2 * decoration_quantity

    if day % 3 == 0:
        spirit += 3 + 10
        budget += 5 * decoration_quantity + 3 * decoration_quantity
        condition_5th_day = True

    if day % 5 == 0:
        spirit += 17
        budget += 15 * decoration_quantity

        if condition_5th_day:
            spirit += 30

    if day % 10 == 0:
        spirit -= 20
        budget += 23

        if day == days_left:
            spirit -= 30


print(f'Total cost: {budget}')
print(f'Total spirit: {spirit}')
