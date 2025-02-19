numbers = input()
example = list(numbers.split(' '))
inverted = list()

for i in example:
    if int(i) > 0:
        a = -abs(int(i))
        inverted.append(a)
    else:
        a = abs(int(i))
        inverted.append(a)

print(inverted)