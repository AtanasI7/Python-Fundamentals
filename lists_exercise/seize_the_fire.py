level_of_fire = input().split('#')
water = int(input())
current_data = list()
current_effort = 0
total_effort = 0
total_fire = 0
condition = False
cells = list()

print('Cells:')

for i in level_of_fire:
    i = i.split(' ')

    if water <= int(i[2]):
        continue

    if 1 <= int(i[2]) <= 50 and i[0] == 'Low':
        water -= int(i[2])
        current_effort = int(i[2]) * 0.25
        water -= current_effort
        total_effort += current_effort
        total_fire += int(i[2])
        condition = True

    elif 51 <= int(i[2]) <= 80 and i[0] == 'Medium':
        water -= int(i[2])
        current_effort = int(i[2]) * 0.25
        water -= current_effort
        total_effort += current_effort
        total_fire += int(i[2])
        condition = True

    elif 81 <= int(i[2]) <= 125 and i[0] == 'High':
        water -= int(i[2])
        current_effort = int(i[2]) * 0.25
        water -= current_effort
        total_effort += current_effort
        total_fire += int(i[2])
        condition = True

    else:
        continue

    if condition:
        cells.append(i[2])

    condition = False
    current_effort = 0

for el in cells:
    print(f" - {el}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
