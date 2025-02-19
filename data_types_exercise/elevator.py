person_num = int(input())
capacity_num = int(input())

if capacity_num > person_num:
    print(1)

elif person_num // capacity_num > 0:
    full_courses = int(person_num / capacity_num)

    if person_num % capacity_num < person_num and person_num % capacity_num != 0:
        full_courses += 1

    print(full_courses)
