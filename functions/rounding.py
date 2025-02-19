def rounded(base_list):
    new_list = list()
    for n in base_list:
        n = float(n)

        new_list.append(round(n))

    return new_list


numbers = input().split(' ')
print(rounded(numbers))