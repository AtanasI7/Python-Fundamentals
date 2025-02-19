def group_of_tens(numbers):
    new_data = sorted(numbers, key=lambda x: 10 < int(x) <= 20)
    print(new_data)





data = input().split(', ')
group_of_tens(data)