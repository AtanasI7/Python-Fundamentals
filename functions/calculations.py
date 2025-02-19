def calculations(operator, a, b):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a // b
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


command = input()
first_num = int(input())
second_num = int(input())


print(calculations(command, first_num, second_num))