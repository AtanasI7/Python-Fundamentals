def version(numbers):
    numbers = int(''.join(numbers)) + 1
    print('.'.join(str(numbers)))


data = input().split('.')
version(data)