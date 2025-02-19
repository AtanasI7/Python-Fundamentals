num_lines = int(input())
tank_capacity = 0

for i in range(1, num_lines + 1):
    liters = int(input())

    if tank_capacity + liters <= 255:
        tank_capacity += liters

    else:
        print("Insufficient capacity!")



print(tank_capacity)