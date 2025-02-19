def factorial(num):
    factor_num = 1
    if num == 0 or num == 1:
        return 1

    if num > 1:
        while num > 1:
            factor_num = num * factor_num
            num -= 1

    return factor_num



num1 = int(input())
num2 = int(input())
result = factorial(num1) / factorial(num2)
print(f'{result:.2f}')