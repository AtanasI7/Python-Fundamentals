numbers = input().split(', ')
zero_counter = 0
zero_to_back_list = list()

for n in numbers:
    n = int(n)
    if n != 0:
        zero_to_back_list.append(n)
    else:
        zero_counter += 1

for i in range(1, zero_counter + 1):
    zero_to_back_list.append(0)

print(zero_to_back_list)