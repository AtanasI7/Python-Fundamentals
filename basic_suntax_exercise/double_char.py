word = input()
new_word = ''

while word != 'End':
    for i in word:
        print(i + i, end='')

    word = input()
    print()

