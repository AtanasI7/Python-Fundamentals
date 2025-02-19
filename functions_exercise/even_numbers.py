def even_nums(numbers):
    only_evens = list()
    for i in numbers:
        if i % 2 == 0:
            only_evens.append(i)
    return only_evens


data = map(int, input().split(' '))


print(even_nums(data))


# result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(' ')))))
#
# print(result)