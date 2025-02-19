numbers = int(input())
positive_list = list()
negative_list = list()
negative_sum = 0


for i in range(1, numbers + 1):
    current_num = int(input())
    if current_num > 0:
        positive_list.append(current_num)

    elif current_num < 0:
        negative_list.append(current_num)
        negative_sum += current_num

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {negative_sum}")


