def calculator(num):
    result_even = 0
    result_odd = 0
    attempt = map(int, list(num))

    for i in attempt:
        if i % 2 == 0:
            result_even += i
        else:
            result_odd += i

    return result_odd, result_even


number = input()

print(f"Odd sum = {calculator(number)[0]}, Even sum = {calculator(number)[1]}")
