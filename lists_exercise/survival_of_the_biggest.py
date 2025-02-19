numbers = input().split(' ')
copy_number = list(map(int, numbers))
special_number = int(input())

for n in range(special_number):
    current_element = min(copy_number)
    numbers.remove(str(current_element))
    copy_number.remove(current_element)

print(', '.join(numbers))