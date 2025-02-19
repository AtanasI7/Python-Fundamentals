def even_check(nums):
    if nums % 2 == 0:
        return  True
    else:
        return False

data = map(int, input().split(' '))
result = list(filter(even_check, data))

print(result)