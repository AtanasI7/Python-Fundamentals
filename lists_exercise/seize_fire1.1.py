fires_cells = input().split('#')
water = int(input())
effort = 0
total_fire = 0
condition = False
print("Cells:")

for current_fire in fires_cells:
    fire_info = current_fire.split(' = ')
    type_of_fire = fire_info[0]
    value_of_fire = int(fire_info[1])
    condition = False

    if type_of_fire == ' High':
        if 81 <= value_of_fire <= 125:
            condition = True

    if type_of_fire == ' Medium':
        if 51 <= value_of_fire <= 80:
            condition = True

    if type_of_fire == ' Low':
        if 1 <= value_of_fire <= 50:
            condition = True

    if condition:
        if water >= value_of_fire:
            water -= value_of_fire
            effort += value_of_fire * 0.25
            total_fire += value_of_fire
            print(f" - {value_of_fire}")


print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")