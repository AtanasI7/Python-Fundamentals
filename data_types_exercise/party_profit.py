group_size = int(input())
days = int(input())
gold = 0

for day in range(1, days + 1):
    gold += 50

    if day % 15 == 0:
        group_size += 5

    gold -= group_size * 2

    if day % 3 == 0:
        gold -= group_size * 3

    if day % 5 == 0:
        gold += group_size * 20

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        gold -= group_size * 2

coins_each = gold // group_size

print(f"{group_size} companions received {coins_each} coins each.")