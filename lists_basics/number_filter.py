number = int(input())
even_list = list()
odd_list = list()
negative_list = list()
positive_list = list()

for i in range(number):
    current = int(input())

    if current % 2 == 0:
        even_list.append(current)
    else:
        odd_list.append(current)

    if current >= 0:
        positive_list.append(current)
    else:
        negative_list.append(current)

filter_word = input()

if filter_word == 'even':
    print(even_list)
if filter_word == 'odd':
    print(odd_list)
if filter_word == ' positive':
    print(positive_list)
if filter_word == ' negative':
    print(negative_list)

