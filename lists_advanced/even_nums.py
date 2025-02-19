def even_numbers(numbers):
    position = list()
    for n in range(len(numbers)):
        if numbers[n] % 2 == 0:
            position.append(n)
    print(position)


data = list(map(int, input().split(', ')))
even_numbers(data)
