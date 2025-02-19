number = int(input())
word = input()
day_list = list()
new_list = list()

for i in range(number):
    current = input()
    day_list.append(current)
    if word in current:
        new_list.append(current)


print(day_list)
print(new_list)
