def office_chairs(number):
    condition = True
    free_chairs = 0
    for i in range(1, number + 1):
        data = input().split(' ')
        chairs = data[0]
        people = int(data[1])
        if len(chairs) >= people:

            free_chairs += len(chairs) - people

        if len(chairs) < people:
            needed_chairs = people - len(chairs)
            print(f"{needed_chairs} more chairs needed in room {i}")
            condition = False

    if condition:
        print(f"Game On, {free_chairs} free chairs left")



lines = int(input())
office_chairs(lines)
