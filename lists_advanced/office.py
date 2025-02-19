def office(numbers, factor):
    happy_workers = 0
    sad_workers = 0
    numbers = list(map(factor, numbers))
    average = sum(numbers) // len(numbers)
    text = ''

    for n in numbers:
        if n >= average:
            happy_workers += 1
        else:
            sad_workers += 1

    if happy_workers < sad_workers:
        print(f"Score: {happy_workers}/{sad_workers}. Employees are not happy!")
    else:
        print(f"Score: {happy_workers}/{sad_workers}. Employees are happy!")


data = list(map(int, input().split(' ')))
command = int(input())

office(data, command)

