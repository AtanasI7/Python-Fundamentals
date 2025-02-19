n_times = int(input())
check = 0

while check < n_times:
    text = input()
    check += 1

    if check > n_times:
        break

    if ',' in text:
        print(f'{text} is not pure!')

    elif '.' in text:
        print(f'{text} is not pure!')

    elif '_' in text:
        print(f'{text} is not pure!')

    else:
        print(f"{text} is pure.")