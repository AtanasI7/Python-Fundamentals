def office(numbers, multiplicator):
    average = sum(numbers) / len(numbers)
    happy_employees = list(filter(lambda n: n >= average, numbers))

    if len(happy_employees) >= len(numbers) / 2:
        print(f"Score: {len(happy_employees)}/{len(numbers)}. Employees are happy!")
    else:
        print(f"Score: {len(happy_employees)}/{len(numbers)}. Employees are not happy!")


employees = list(map(int, input().split(' ')))
factor = int(input())
office(employees, factor)