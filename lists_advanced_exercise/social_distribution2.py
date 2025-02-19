def social_distribution(numbers, min_wealth):
    numbers = list(map(int, numbers))
    condition = True

    for i in range(0, len(numbers)):
        max_num = max(numbers)
        current_num = numbers[i]
        if current_num < min_wealth:
            difference = min_wealth - current_num
            current_num += difference
            max_num -= difference
            numbers[i] = current_num

            for n in range(0, len(numbers)):
                if numbers[n] > max_num:
                    numbers[n] = max_num
                    break

        if min_wealth > max_num:
            print('No equal distribution possible')
            condition = False
            break
        # current_num += 5
        # numbers[i] = current_num
    if condition:
        print(numbers)

population = input().split(', ')
wealth = int(input())
social_distribution(population, wealth)

