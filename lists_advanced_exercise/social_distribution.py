def social_distribution(numbers, wealth):
    numbers = list(map(int, numbers))
    reprocessed_numbers = list()
    max_number = max(numbers)

    for i in range(0, len(numbers)):
        current_num = numbers[i]
        if current_num < wealth:
            if max_number > wealth:
                difference = wealth - current_num
                max_number -= difference
                current_num += difference
                max_number -= max(numbers) - difference
                reprocessed_numbers.append(current_num)




            else:
                print(f"No equal distribution possible")
                break

    print(reprocessed_numbers)


population = input().split(', ')
min_wealth = int(input())

social_distribution(population, min_wealth)

