def minimum(num):
    print(f"The minimum number is {min(num)}")
    print(f"The maximum number is {max(num)}")
    print(f"The sum number is: {sum(num)}")



data = list(map(int, input().split(' ')))

minimum(data)


# minimum = lambda x: min(x), data
# maximum = lambda x: max(x), data
# summed = lambda x: sum(x), data
#
# print(minimum)
# print(maximum)
# print(summed)